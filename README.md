# 🧩 Sliding Puzzle Solver using AI Search Algorithms

An interactive **3×3 Sliding Puzzle (8-Puzzle)** game built with **Python** and **Streamlit** that demonstrates how different **Artificial Intelligence search algorithms** solve the puzzle.

The application allows users to shuffle the puzzle, choose a search algorithm, and watch the solution being animated step-by-step.

---

## 📖 Overview

The Sliding Puzzle is a classic Artificial Intelligence problem where the objective is to arrange the numbered tiles in the correct order by sliding them into the empty space.

This project demonstrates three fundamental AI search algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- A* Search (A-Star)

The application provides a simple graphical interface where users can:

- Shuffle the puzzle
- Select a solving algorithm
- Visualize the solving process
- Track the number of moves
- Monitor elapsed solving time

---

## 🚀 Features

- 🎮 Interactive 3×3 Sliding Puzzle
- 🔀 Random puzzle generation
- 🧠 Multiple AI search algorithms
  - Breadth First Search (BFS)
  - Depth First Search (DFS)
  - A* Search using Manhattan Distance heuristic
- 🎨 Smooth animated tile movement
- 📊 Move counter
- ⏱️ Timer
- 💻 Clean Streamlit interface
- 🖼️ Colorful tile visualization using Pillow

---

# Algorithms Used

## 1. Breadth First Search (BFS)

BFS explores every state level-by-level.

### Advantages

- Always finds the shortest solution
- Complete search algorithm

### Disadvantages

- High memory consumption
- Slow for complex puzzles

Time Complexity:

```
O(b^d)
```

Space Complexity:

```
O(b^d)
```

where

- b = branching factor
- d = solution depth

---

## 2. Depth First Search (DFS)

DFS explores one path completely before backtracking.

### Advantages

- Low memory usage
- Fast for shallow solutions

### Disadvantages

- Does not always find the shortest solution
- May get trapped in deep search trees

Time Complexity

```
O(b^m)
```

Space Complexity

```
O(bm)
```

where

- b = branching factor
- m = maximum search depth

---

## 3. A* Search

A* is an informed search algorithm that combines:

- Cost from start node (g)
- Heuristic estimate to goal (h)

Evaluation Function:

```
f(n) = g(n) + h(n)
```

This project uses the **Manhattan Distance** heuristic.

Advantages:

- Optimal
- Complete
- Much faster than BFS
- Explores fewer states

Time Complexity

```
Depends on heuristic
```

Space Complexity

```
Exponential in worst case
```

---

# Manhattan Distance Heuristic

The Manhattan Distance calculates how far every tile is from its correct position.

Formula:

```
|x1 - x2| + |y1 - y2|
```

The total heuristic value is the sum of all tile distances.

---

# Technologies Used

- Python 3
- Streamlit
- Pillow (PIL)
- Queue
- Priority Queue
- Random
- Time

---

# Project Structure

```
Sliding-Puzzle/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── home.png
    ├── shuffle.png
    └── solving.png
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/sliding-puzzle.git
```

Go inside the project

```bash
cd sliding-puzzle
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Requirements

```
streamlit
Pillow
```

Install manually

```bash
pip install streamlit pillow
```

---

# How to Use

### Step 1

Launch the application.

---

### Step 2

Click **Shuffle** to generate a randomized puzzle.

---

### Step 3

Choose one of the available algorithms:

- BFS
- DFS
- A*

---

### Step 4

Click **Solve**.

---

### Step 5

Watch the puzzle solve itself with smooth tile animations.

---

# User Interface

The application displays:

- Puzzle board
- Algorithm selector
- Shuffle button
- Solve button
- Move counter
- Timer
- Animated solution

---

# Example Goal State

```
1 2 3
4 5 6
7 8 _
```

where **_** represents the empty tile.

---

# Future Improvements

- 4×4 (15 Puzzle) support
- Greedy Best First Search
- Uniform Cost Search
- Iterative Deepening DFS
- IDA* Algorithm
- Puzzle solvability checker
- Manual tile movement
- Hint system
- Performance comparison graph
- Search tree visualization
- Dark mode UI
- Difficulty levels
- Mobile responsive interface

---

# Learning Outcomes

This project helps understand:

- State Space Search
- Artificial Intelligence Search Algorithms
- Heuristic Search
- Graph Traversal
- Streamlit Application Development
- Python Data Structures
- Animation in Streamlit
- Problem Solving using AI

---

# Screenshots

Add screenshots inside the **screenshots** folder.

Example:

```
screenshots/
│
├── home.png
├── shuffle.png
└── solving.png
```

---

# Author

**Revaan J.R.**

B.Tech Artificial Intelligence and Data Science

---

# License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!
