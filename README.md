# 🧩 Sliding Puzzle Solver using AI Search Algorithms

An interactive **3×3 Sliding Puzzle (8-Puzzle)** game built with **Python** and **Streamlit** that demonstrates how classic **Artificial Intelligence search algorithms** solve the puzzle efficiently.

The application allows users to shuffle the puzzle, choose a search algorithm, and watch the puzzle being solved with smooth animations while tracking the number of moves and elapsed time.

---

## 🌐 Live Demo

🚀 **Try the application online**

**https://sliding-puzzle-udrtuvmvvu9beckxtm3j4p.streamlit.app/**

---

# 📖 Overview

The Sliding Puzzle (8-Puzzle) is one of the most popular search problems in Artificial Intelligence.

The objective is to rearrange the numbered tiles into the correct order by sliding them into the empty space.

This project demonstrates how different AI search algorithms explore the puzzle's state space to reach the goal state.

---

# ✨ Features

- 🎮 Interactive 3×3 Sliding Puzzle
- 🔀 Random puzzle shuffling
- 🧠 Three AI search algorithms
  - Breadth First Search (BFS)
  - Depth First Search (DFS)
  - A* Search
- 📊 Move Counter
- ⏱️ Live Timer
- 🎨 Animated puzzle solving
- 🖼️ Colorful tile interface
- ⚡ Fast Streamlit-based web application

---

# 🤖 Algorithms Implemented

## Breadth First Search (BFS)

Breadth First Search explores every possible state level by level.

### Advantages

- Guarantees the shortest solution
- Complete search algorithm

### Disadvantages

- High memory consumption
- Slow for larger search spaces

**Time Complexity**

```
O(b^d)
```

**Space Complexity**

```
O(b^d)
```

---

## Depth First Search (DFS)

Depth First Search explores one branch completely before backtracking.

### Advantages

- Low memory usage
- Simple implementation

### Disadvantages

- May not find the shortest path
- Can get trapped in deep branches

**Time Complexity**

```
O(b^m)
```

**Space Complexity**

```
O(bm)
```

---

## A* Search Algorithm

A* is an informed search algorithm that combines:

- Cost from the start node
- Estimated cost to the goal

Evaluation Function

```
f(n) = g(n) + h(n)
```

where

- **g(n)** = Cost from the start node
- **h(n)** = Manhattan Distance heuristic

### Advantages

- Optimal
- Complete
- Faster than BFS
- Explores fewer states

---

# 📐 Manhattan Distance Heuristic

The Manhattan Distance measures how far each tile is from its correct position.

Formula

```
|x₁ − x₂| + |y₁ − y₂|
```

The heuristic value is the total Manhattan distance of all tiles.

---

# 🛠️ Technologies Used

- Python 3
- Streamlit
- Pillow (PIL)
- Queue
- Priority Queue
- Time
- Random

---

# 📂 Project Structure

```
Sliding-Puzzle/
│
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
└── screenshots/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/sliding-puzzle.git
```

Navigate to the project folder

```bash
cd sliding-puzzle
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

The application will open at

```
http://localhost:8501
```

---

# 📦 Requirements

```
streamlit==1.50.0
Pillow==11.2.1
streamlit-drawable-canvas
```

---

# 🎮 How to Use

### Step 1

Launch the application.

### Step 2

Click **Shuffle** to generate a random puzzle.

### Step 3

Choose one of the algorithms:

- BFS
- DFS
- A*

### Step 4

Click **Solve**.

### Step 5

Watch the puzzle solve itself step-by-step with animation.

---

# 🎯 Goal State

```
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 |   |
+---+---+---+
```

---

# 📊 Project Highlights

✅ Interactive AI Puzzle Solver

✅ Real-time Move Counter

✅ Live Timer

✅ Animated Solution Visualization

✅ Three AI Search Algorithms

✅ Manhattan Distance Heuristic

✅ Streamlit Web Interface

---

# 🚀 Future Enhancements

- 4×4 (15 Puzzle)
- Greedy Best First Search
- Uniform Cost Search
- Iterative Deepening DFS
- IDA* Algorithm
- Puzzle Solvability Checker
- Manual Tile Movement
- Hint System
- Difficulty Levels
- Performance Comparison Charts
- Search Tree Visualization
- Dark Mode
- Responsive Mobile Interface

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Artificial Intelligence
- State Space Search
- Graph Search Algorithms
- Heuristic Search
- Breadth First Search
- Depth First Search
- A* Search
- Manhattan Distance
- Streamlit Web Development
- Python Programming

---

# 📸 Screenshots

Add screenshots of your application inside the **screenshots/** folder.

Example:

```
screenshots/
├── home.png
├── shuffle.png
├── solving.png
└── solved.png
```

---

# 👨‍💻 Author

**Revaan J.R.**

**B.Tech – Artificial Intelligence and Data Science**

---

# ⭐ Live Application

🔗 **https://sliding-puzzle-udrtuvmvvu9beckxtm3j4p.streamlit.app/**

---

# 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ If you enjoyed this project, please consider giving it a **Star ⭐** on GitHub!
