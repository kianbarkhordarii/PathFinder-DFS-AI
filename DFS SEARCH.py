import numpy as np
import random
import matplotlib.pyplot as plt
class PathFinderAI:
    """
    An AI agent that uses Depth-First Search (DFS) to navigate through 
    a maze with dynamic obstacles, visualized using Matplotlib.
    """
    def __init__(self, rows, cols, obstacle_count):
        self.rows = rows
        self.cols = cols
        self.target = (rows * cols) - 1
        self.obstacles = self._generate_obstacles(obstacle_count)
        self.move_vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)] # N, S, W, E
        self.visited = {0}
        self.stack = [(0, [])] # (current_state, untried_moves)
        self.path = [0]
        self.score_map = {0: 0}
        self.total_steps = 0

    def _generate_obstacles(self, count):
        """Randomly places obstacles in the grid, excluding the target."""
        all_positions = list(range(self.rows * self.cols))
        all_positions.remove(self.target)
        all_positions.remove(0) # Start point
        return set(random.sample(all_positions, count))

    def _get_next_state(self, current_state, move_idx):
        """Calculates the coordinates of the next state based on movement."""
        r, c = divmod(current_state, self.cols)
        dr, dc = self.move_vectors[move_idx]
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < self.rows and 0 <= nc < self.cols:
            return nr * self.cols + nc
        return current_state

    def visualize(self, current_state):
        """Renders the maze, obstacles, agent path, and target."""
        grid = np.zeros((self.rows, self.cols))
        
        # Mark Obstacles
        for obs in self.obstacles:
            grid[divmod(obs, self.cols)] = -1
        
        # Mark Path
        for p in self.path:
            grid[divmod(p, self.cols)] = 0.5
            
        # Mark Agent and Target
        grid[divmod(current_state, self.cols)] = 0.8
        grid[divmod(self.target, self.cols)] = 1.0

        plt.imshow(grid, cmap='nipy_spectral', interpolation='nearest')
        plt.title(f"DFS Exploration | Steps: {self.total_steps}")
        plt.axis('off')
        plt.pause(0.1)
        plt.clf()

    def solve(self):
        """Executes the DFS algorithm to find the target."""
        print(f"🔍 PathFinder AI: Exploration started on {self.rows}x{self.cols} grid...")
        
        plt.figure(figsize=(8, 6))

        while self.stack:
            curr_node, moves_left = self.stack[-1]
            self.visualize(curr_node)

            if curr_node == self.target:
                print("🎯 Target Reached!")
                self._final_report()
                break

            if not moves_left:
                moves_left = list(range(len(self.move_vectors)))
                random.shuffle(moves_left)

            found_next = False
            while moves_left:
                move_idx = moves_left.pop()
                next_node = self._get_next_state(curr_node, move_idx)

                if (next_node not in self.obstacles and 
                    next_node not in self.visited and 
                    next_node != curr_node):
                    
                    self.stack[-1] = (curr_node, moves_left)
                    self.stack.append((next_node, []))
                    self.visited.add(next_node)
                    self.path.append(next_node)
                    self.score_map[next_node] = self.score_map[curr_node] + 10
                    self.total_steps += 1
                    found_next = True
                    break
            
            if not found_next:
                # Backtracking logic
                self.stack.pop()
                if self.path: self.path.pop()

        plt.show()

    def _final_report(self):
        print("-" * 30)
        print(f"Path: {self.path}")
        print(f"Total Moves: {self.total_steps}")
        print(f"Final Efficiency Score: {sum(self.score_map.values())}")
        print("-" * 30)

if __name__ == "__main__":
    r = int(input("Enter Rows: "))
    c = int(input("Enter Cols: "))
    o = int(input("Enter Obstacles Count: "))
    
    ai_solver = PathFinderAI(r, c, o)
    ai_solver.solve()