
---

# 🧩 PathFinder AI: Visual DFS Solver

### *Real-time Maze Exploration & Pathfinding using Depth-First Search*

---

## ⚡ Project Overview

**PathFinder AI** is a dynamic simulation that demonstrates how an agent explores an unknown environment to find a target. By implementing a **Depth-First Search (DFS)** algorithm with a stack-based approach, the agent navigates through a grid filled with obstacles, making real-time decisions and visualizing its progress graphically.

---

## 🚀 Key Intelligent Features

| Feature | Description | Implementation |
| --- | --- | --- |
| **Dynamic Obstacle Generation** | Randomized barriers are placed to challenge the agent. | `random.sample` |
| **Real-time Visualization** | Frame-by-frame rendering of the exploration process. | `matplotlib.pyplot` |
| **Path Memory** | The agent keeps track of its current path and visited states. | `Stack (LIFO) & Sets` |
| **Score System** | Evaluates the efficiency of the exploration based on moves. | `Scoring Logic` |

---

## 🛠 Technical Deep-Dive

* **State Space:** The grid is modeled as a 1D array converted to 2D coordinates using `divmod`.
* **Search Strategy:** Uses a **Stack** to backtrack when it hits a dead end or an obstacle.
* **Environment Rendering:** Uses `plt.imshow` to represent:
* **Obstacles:** Black blocks
* **Path:** Blue trail
* **Agent:** Red indicator
* **Goal:** Target destination



---

## 🕹 Operation Guide

### 📂 1. Dependencies

Ensure you have the visualization library installed:

```bash
pip install matplotlib numpy

```

### ⚙️ 2. Execution

```bash
python "DFS SEARCH.py"

```

### 🧪 3. Configuration

Upon launch, the engine will prompt for:

* **Grid Dimensions:** Rows and Columns.
* **Obstacle Density:** Number of obstacles to generate.

---

## 📊 Logic Flow

1. **Initialize:** Generate grid and place the target at the bottom-right.
2. **Explore:** Agent moves in 4 directions (North, South, East, West).
3. **Backtrack:** If no valid moves are left, the agent pops from the stack to return to the last junction.
4. **Target Found:** Display final path, total moves, and cumulative score.

---

## 👨‍💻 Developed By

**Kian Barkhordari**

**حالا برویم سراغ کد؟ می‌خواهی آن را هم کاملاً انگلیسی و حرفه‌ای (Clean Code) کنم؟**
