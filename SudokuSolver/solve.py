def check_column(grid, col, value, size):
    # check if the value is not in th column
    for row in range(size):
        if grid.get_value_by_location(row, col) == value:
            return False
    return True

def check_row(grid, row, value, size):
    # check ig the value is not in the row
    for col in range(size):
        if grid.get_value_by_location(row, col) == value:
            return False
    return True

def check_square(grid, row, col, value, size):
    # check if none of that same value are in this cell's block
    block = grid.get_section()
    y = row - (row % block)
    x = col - (col % block)
    for i in range(y, y + block):
        for j in range(x, x + block):
            if grid.get_value_by_location(i, j) == value:
                return False
    return True

def valid_placement(grid, row, col, value, size):
    # check if all the conditions are met for a valid placement in sudoku
    if (check_column(grid, col, value, size) and
            check_row(grid, row, value, size) and
            check_square(grid, row, col, value, size)):
        return True
    return False

def find_next_empty(grid, size, row, col):
    for r in range(row, size):
        for c in range(col, size):
            if grid.get_value_by_location(row, col) == 0:
                return (row, col)
    # I wasn't sure if the rows and columns backtrace through
    # the stack to the last valid placement.
    for i in range(size):
        for j in range(size):
            if grid.get_value_by_location(i, j) == 0:
                return (i, j)
    # return if there are no empty cells
    return (-1, -1)

# recursive solution

def recursive_solve_helper(grid, size, row=0, col=0):
    row, col = find_next_empty(grid, size, row, col)
    # if there are no empty cells left
    if row == -1 and col == -1:
            return True
    for value in range(1,10):
        if valid_placement(grid, row, col, value, size):
            # set the value
            grid.set_value_by_location(row, col, value)
            # if the recursive call returns true. then return true
            if recursive_solve_helper(grid, size, row, col):
                    return True
            # undo the current cell if it failed.
            grid.set_value_by_location(row, col, 0)
    return False

def solve_grid_recursively(grid):
    size = grid.get_size()
    if recursive_solve_helper(grid, size):
        return
    else:
        print("can not solve this sudoku")
        return

# I decided to do this iteritivly too because I wanted to see if I really
# understood this. I also have a recursive implementation

# still has an infinite loop fix later or take out

def solve_grid(grid):
    size = grid.get_size()
    curr_row = 0
    curr_col = 0
    stack = list()
    # find the next empty spot
    curr_row, curr_col = find_next_empty(grid, size, curr_row, curr_col)
    # enter while loop on condition that there are still empty spots.
    while curr_row != -1 and curr_col != -1:
        # make an assignment
        valid = False
        for value in range(1, 10):
            # if a valid placement was made
            valid = valid_placement(grid, curr_row, curr_col, value, size)
            if valid:
                # make the assignment and append to the stack
                grid.set_value_by_location(curr_row, curr_col, value)
                stack.append((curr_row, curr_col))
                break
        if not valid:
            print("trigger backtrace")
            rm_row, rm_col = stack.pop()
            grid.set_value_by_location(rm_row, rm_col, 0)
            curr_col = rm_col
            curr_row = rm_row
        # find the next empty spot
        # print(curr_col, curr_row)
        curr_row, curr_col = find_next_empty(grid, size, curr_row, curr_col)

def check_solution(grid):
    # I wrote this to check if a solution was valid.
    # I wrote it for a code fights challenge before this.
    # this is why there is inconsistant style.
    # ex: the integer division symbol "//"

    columnsCheck = []
    rowsCheck = []
    subsect = []
    size = grid.get_size()
    sub_size = grid.get_section()
    # set up empty arrrays to store the entire subsection or row or
    # column for checking validity in place.
    for i in range(sub_size):
        subsect.append([])
        for j in range(sub_size):
            subsect[i].append({})

    for i in range(grid.get_size()):
        rowsCheck.append({})
        columnsCheck.append({})
    # check every cell in the grid
    for i in range(size):
        for j in range(size):
            # if it is not  empty
            val = grid.get_value_by_location(i, j)
            if val != 0:
                # check column
                if val in columnsCheck[j]:
                    return False
                # check row
                elif val in rowsCheck[i]:
                    return False
                # check sub divide/section
                elif val in subsect[i//sub_size][j//sub_size]:
                    return False
                else:
                    columnsCheck[j][val] = i
                    rowsCheck[i][val] = j
                    subsect[i//sub_size][j//sub_size][val] = 1
    return True