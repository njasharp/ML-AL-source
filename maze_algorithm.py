import random

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.neighbors = []

    def add_neighbor(self, cell):
        self.neighbors.append(cell)

def generate_maze(rows, cols):
    maze = [[Cell(row, col) for col in range(cols)] for row in range(rows)]

    # Add neighbors for each cell
    for row in range(rows):
        for col in range(cols):
            cell = maze[row][col]
            if row > 0:
                cell.add_neighbor(maze[row - 1][col])
            if row < rows - 1:
                cell.add_neighbor(maze[row + 1][col])
            if col > 0:
                cell.add_neighbor(maze[row][col - 1])
            if col < cols - 1:
                cell.add_neighbor(maze[row][col + 1])

    stack = []
    start_cell = maze[0][0]
    start_cell.visited = True
    stack.append(start_cell)

    while stack:
        current_cell = stack[-1]
        unvisited_neighbors = [neighbor for neighbor in current_cell.neighbors if not neighbor.visited]

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            next_cell.visited = True
            stack.append(next_cell)
        else:
            stack.pop()

    return maze

def print_maze(maze):
    for row in maze:
        row_str = ""
        for cell in row:
            if cell.visited:
                row_str += "* "
            else:
                row_str += "# "
        print(row_str)

def remove_from_list(maze):
    # Code to remove cells from the list goes here
    pass

if __name__ == "__main__":
    rows = 10
    cols = 10
    maze = generate_maze(rows, cols)
    print_maze(maze)
    remove_from_list(maze)