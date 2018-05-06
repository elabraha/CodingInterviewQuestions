def check_column(grid, col, value, size):
    for row in range(size):
        if grid.get_value_by_location(row, col) == value:
            return False
    return True

def check_row(grid, row, value, size):
    for col in range(size):
        if grid.get_value_by_location(row, col) == value:
            return False
    return True
def check_square(grid, row, col, value, size):
    block = grid.get_section()
    y = row - (row % block)
    x = col - (col % block)
    for i in range(y, y + block):      
        for j in range(x, x + block):
            if grid.get_value_by_location(i, j) == value:
                return False
    return True

def valid_placement(grid, row, col, value, size):
    if not check_column(grid, col, value, size):
        return False
    if not check_row(grid, row, value, size):
        return False
    if not check_square(grid, row, col, value, size):
        return False
    return True
def search():
    size = grid.get_size()
    for i in range(size):
        for j in range(size):
            pass
def solve_grid(grid):
    print(valid_placement(grid, 5, 8, 8, 9))
    print(valid_placement(grid, 3, 8, 8, 9))
    print(valid_placement(grid, 0, 7, 8, 9))
    print(valid_placement(grid, 8, 8, 8, 9))