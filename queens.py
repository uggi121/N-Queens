import random
import timeit

"""
To run, simply execute this file from the command line and enter the value of n when prompted.
The heuristic is pretty fast till N = 20, after which a discernible slowdown is evident.
"""

class Position:
    # Class that maintains information about a position, along with a direction of movement.
    def __init__(self, i, j, i_dir, j_dir):
        self.i = i
        self.j = j
        self.i_dir = i_dir
        self.j_dir = j_dir
        
    def move(self):
        # Move the position by one step using the direction vector provided.
        self.i += self.i_dir
        self.j += self.j_dir
        
    def make_cell(self):
        # Make a cell using the current position.
        return (self.i, self.j)

def get_cell_set(n):
    # Generate all cell values for a given number of rows and columns.
    return [(i, j) for i in range(n) for j in range(n)]
    
def remove_position_from_cell_set(position, cell_set):
    # Remove the given position from the set of positions/cells, if it exists.
    cell_to_remove = position.make_cell()
    if cell_to_remove in cell_set:
        cell_set.remove(position.make_cell())
    position.move()
    
def remove_horizontal_cells(cell_set, cell, n):
    # Remove cells on the same row as the given cell.
    position = Position(cell[0], 0, 0, 1)
    
    while position.j < n:
        remove_position_from_cell_set(position, cell_set)
        
def remove_vertical_cells(cell_set, cell, n):
    # Remove cells on the same column as the given cell.
    position = Position(0, cell[1], 1, 0)
    
    while position.i < n:
        remove_position_from_cell_set(position, cell_set)
        
def remove_diagonal_cells(cell_set, cell, n):
    # Remove cells on the same diagonal as the given cell.
    top_left_origin_shift = min(cell)
    position = Position(cell[0] - top_left_origin_shift, cell[1] - top_left_origin_shift, 1, 1)
    
    while position.i < n and position.j < n:
        remove_position_from_cell_set(position, cell_set)
        
    bottom_left_origin_shift = min(n - 1 - cell[0], cell[1])
    position = Position(cell[0] + bottom_left_origin_shift, cell[1] - bottom_left_origin_shift, -1, 1)
    
    while position.i >= 0 and position.j < n:
        remove_position_from_cell_set(position, cell_set)
    
def remove_attacking_cells(cell_set, cell, n):
    # Remove cells which can be attacked by a queen placed at the given cell.
    remove_horizontal_cells(cell_set, cell, n)
    remove_vertical_cells(cell_set, cell, n)
    remove_diagonal_cells(cell_set, cell, n)    
    
def generate_queen_positions(cell_set, n):
    positions = []
    
    while cell_set:
        cell = random.choice(cell_set)
        remove_attacking_cells(cell_set, cell, n)
        positions.append(cell)
        
    return positions

def run_heuristics(n):
    if n <= 0:
        return None
        
    cell_set = get_cell_set(n)
    positions = generate_queen_positions(cell_set, n)
    if len(positions) < n:
        return None
        
    return positions
    
def create_board(n):
    return [['.' for _ in range(n)] for _ in range(n)]
    
def place_queens(board, positions):
    for position in positions:
        i, j = position[0], position[1]
        board[i][j] = 'Q'
    
def print_board(positions):
    
    if not positions:
        print("Invalid input")
    
    n = len(positions)
    board = create_board(n)
    place_queens(board, positions)
    for row in board:
        print(row)
    print("\n")
    
def run_heuristics_till_answer():
    n = int(input("Please enter the number of rows and columns.\n"))
    
    if n in [2,3]:
        print("N =", n, "does not have a valid solution.")
        return
    
    positions = run_heuristics(n)
    while not positions:
        positions = run_heuristics(n)

    print_board(positions)
    
def main():
    run_heuristics_till_answer()
    
if __name__ == "__main__":
    main()
