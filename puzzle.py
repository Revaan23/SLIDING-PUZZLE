import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import time, random
from queue import Queue, PriorityQueue

# ----------------- Puzzle Definitions -----------------
GOAL = ((1,2,3),(4,5,6),(7,8,0))

def board_to_tuple(b): return tuple(tuple(r) for r in b)
def tuple_to_board(t): return [list(r) for r in t]

def find_zero(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0:
                return (i,j)
    return None

def valid_moves(pos):
    i,j = pos
    moves = []
    if i>0: moves.append((-1,0))
    if i<2: moves.append((1,0))
    if j>0: moves.append((0,-1))
    if j<2: moves.append((0,1))
    return moves

def swap_copy(b, p1, p2):
    nb = [row[:] for row in b]
    i1,j1 = p1; i2,j2 = p2
    nb[i1][j1], nb[i2][j2] = nb[i2][j2], nb[i1][j1]
    return nb

def manhattan(b):
    d = 0
    for i in range(3):
        for j in range(3):
            v = b[i][j]
            if v == 0: continue
            gi, gj = divmod(v-1,3)
            d += abs(gi-i)+abs(gj-j)
    return d

# ----------------- Solvers -----------------
def bfs_solver(start):
    start_t = board_to_tuple(start)
    q = Queue(); q.put(start_t)
    parent = {start_t: None}
    while not q.empty():
        cur = q.get()
        if cur == GOAL: break
        cur_b = tuple_to_board(cur)
        z = find_zero(cur_b)
        for d in valid_moves(z):
            nz = (z[0]+d[0], z[1]+d[1])
            nb = swap_copy(cur_b, z, nz)
            nb_t = board_to_tuple(nb)
            if nb_t not in parent:
                parent[nb_t] = cur
                q.put(nb_t)
    if GOAL not in parent: return []
    path=[]
    node=GOAL
    while node!=start_t:
        path.append(node)
        node=parent[node]
    path.reverse()
    return [tuple_to_board(t) for t in path]

def dfs_solver(start,max_depth=40):
    start_t = board_to_tuple(start)
    stack=[start_t]
    parent={start_t:None}
    depth={start_t:0}
    while stack:
        cur_t=stack.pop()
        if cur_t==GOAL: break
        if depth[cur_t]>=max_depth: continue
        cur=tuple_to_board(cur_t)
        z=find_zero(cur)
        for d in valid_moves(z):
            nz=(z[0]+d[0], z[1]+d[1])
            nb=swap_copy(cur,z,nz)
            nb_t=board_to_tuple(nb)
            if nb_t not in parent:
                parent[nb_t]=cur_t
                depth[nb_t]=depth[cur_t]+1
                stack.append(nb_t)
    if GOAL not in parent: return []
    path=[]
    node=GOAL
    while node!=start_t:
        path.append(node)
        node=parent[node]
    path.reverse()
    return [tuple_to_board(t) for t in path]

def a_star_solver(start):
    start_t = board_to_tuple(start)
    openq = PriorityQueue()
    openq.put((manhattan(start),0,start_t))
    parent = {start_t: None}
    gscore = {start_t: 0}
    while not openq.empty():
        _,g,cur_t = openq.get()
        if cur_t == GOAL: break
        cur=tuple_to_board(cur_t)
        z=find_zero(cur)
        for d in valid_moves(z):
            nz=(z[0]+d[0], z[1]+d[1])
            nb=swap_copy(cur,z,nz)
            nb_t=board_to_tuple(nb)
            ng = g+1
            if nb_t not in gscore or ng<gscore[nb_t]:
                gscore[nb_t]=ng
                f=ng+manhattan(nb)
                openq.put((f,ng,nb_t))
                parent[nb_t]=cur_t
    if GOAL not in parent: return []
    path=[]
    node=GOAL
    while node!=start_t:
        path.append(node)
        node=parent[node]
    path.reverse()
    return [tuple_to_board(t) for t in path]

# ----------------- Streamlit UI -----------------
CELL = 120
GRID_PAD = 16
ANIM_DELAY = 0.25  # adjust until it feels like local
TILE_COLORS = ["#FFB3BA","#FFDFBA","#FFFFBA","#BAFFC9","#BAE1FF","#E6BAFF","#FFD6A5","#BDE0FE"]

def draw_board(board, highlight=None):
    """Draw the board with optional moving tile highlight"""
    img = Image.new("RGB", (CELL*3+GRID_PAD*2, CELL*3+GRID_PAD*2), "#fafafa")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    for r in range(3):
        for c in range(3):
            v = board[r][c]
            x0 = GRID_PAD + c*CELL
            y0 = GRID_PAD + r*CELL
            color = TILE_COLORS[(v-1)%len(TILE_COLORS)] if v!=0 else "#fafafa"
            if highlight and (r,c)==highlight:
                color = "#FF6347"  # moving tile
            if v != 0:
                draw.rectangle([x0+12, y0+12, x0+CELL-12, y0+CELL-12],
                               fill=color, outline="#555", width=2)
                bbox = draw.textbbox((0,0), str(v), font=font)
                w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
                draw.text((x0+CELL/2-w/2, y0+CELL/2-h/2), str(v), fill="#222", font=font)
    return img

# ----------------- Session State -----------------
if "board" not in st.session_state: st.session_state.board = [list(r) for r in GOAL]
if "moves" not in st.session_state: st.session_state.moves = 0
if "start_time" not in st.session_state: st.session_state.start_time = time.time()

st.title("🧩 Sliding Puzzle Game (3x3)")

# ----------------- Controls -----------------
col1, col2 = st.columns([1,3])
with col1:
    algo = st.selectbox("Algorithm", ["BFS","DFS","A*"])
    if st.button("Shuffle"):
        b = [list(r) for r in GOAL]
        for _ in range(40):
            z = find_zero(b)
            mv = random.choice(valid_moves(z))
            nz = (z[0]+mv[0], z[1]+mv[1])
            b = swap_copy(b, z, nz)
        st.session_state.board = b
        st.session_state.moves = 0
        st.session_state.start_time = time.time()

    solve_btn = st.button("Solve")

with col2:
    board_placeholder = st.empty()
    info_placeholder = st.empty()
    elapsed = int(time.time()-st.session_state.start_time)
    board_placeholder.image(draw_board(st.session_state.board), use_container_width=True)
    info_placeholder.markdown(f"### Moves: {st.session_state.moves} | Time: {elapsed//60:02d}:{elapsed%60:02d}")

# ----------------- Animate solution -----------------
def animate_move(prev, next_board):
    """Animate moving tile"""
    moved_tile = None
    for r in range(3):
        for c in range(3):
            if prev[r][c] != 0 and prev[r][c] != next_board[r][c]:
                moved_tile = (r,c)
    board_placeholder.image(draw_board(prev, highlight=moved_tile), use_container_width=True)
    time.sleep(ANIM_DELAY)

if solve_btn:
    start = [r[:] for r in st.session_state.board]
    if algo=="BFS": path=bfs_solver(start)
    elif algo=="DFS": path=dfs_solver(start)
    else: path=a_star_solver(start)

    if path:
        for step, b in enumerate(path,1):
            prev_board = [r[:] for r in st.session_state.board]
            animate_move(prev_board, b)
            st.session_state.board = b
            st.session_state.moves = step
            elapsed = int(time.time()-st.session_state.start_time)
            board_placeholder.image(draw_board(b), use_container_width=True)
            info_placeholder.markdown(f"### Moves: {step} | Time: {elapsed//60:02d}:{elapsed%60:02d}")
        st.success(f"🎉 Puzzle solved in {len(path)} moves!")
    else:
        st.warning("⚠ No solution found.")
