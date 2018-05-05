def check_column(grid, col, value, size):
    for row in range(size):
        if grid.get_value_by_location(r, col) == value:
            return False
    return True

def check_row(grid, row, value, size):
    for col in range(size):
        if grid.get_value_by_location(row, c) == value:
            return False
    return True
def check_square(grid, row, col, value, size):
    unit = grid.get_section()
    x = row / unit
    y = col / unit
    for i in range(unit):

def valid_placement(grid, row, col, value, size):
    if()
def search():
    size = grid.get_size()
    for i in range(size):
        for j in range(size):

def solve_grid(grid):
    