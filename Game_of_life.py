import random
import time

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        # Initialize the grid with random live (1) and dead (0) cells
        return [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]

    def print_grid(self):
        for row in self.grid:
            print("".join(["█" if cell else " " for cell in row]))
        print("\n" + "-" * self.cols)

    def count_live_neighbors(self, row, col):
        # Count the number of live neighbors around the given cell
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r = (row + i) % self.rows
                c = (col + j) % self.cols
                live_neighbors += self.grid[r][c]
        return live_neighbors

    def next_generation(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)

                if self.grid[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0  # Cell dies
                    else:
                        new_grid[r][c] = 1  # Cell stays alive
                else:
                    if live_neighbors == 3:
                        new_grid[r][c] = 1  # Cell becomes alive

        self.grid = new_grid

    def run_simulation(self, generations):
        for _ in range(generations):
            self.print_grid()
            self.next_generation()
            time.sleep(1)


if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    generations = int(input("Enter the number of generations to simulate: "))

    game = GameOfLife(rows, cols)
    game.run_simulation(generations)
