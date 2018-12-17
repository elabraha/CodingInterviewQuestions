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

# Recursive solution to sudoku solver

rowsCheck = [set(range(1, 10)) for i in range(9)]
columnsCheck = [set(range(1, 10)) for i in range(9)]
sectionsCheck = [ [set(range(1, 10)) for i in range(grid.get_section())] for j in range(grid.get_section())]

def placed_value_remove(grid, row, col, size):
        val = grid.get_value_by_location(row, col)
        rowsCheck[row].remove(val)
        columnsCheck[col].remove(val)
        sectionsCheck[row // grid.get_section()][col // grid.get_section()].remove(val)

def check_possibilities(grid, row, col, size):
    val = grid.get_val

def find_cell_with_possibibities_remaining_1_or_2(grid, size):
    for i in range(size):
        for j in range(size):
            if  

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
        return True
    else:
        print("can not solve this sudoku")
        return False

# I decided to do this iteritivly too because I wanted to see if I really
# understood this.

def solve_grid(grid):
    size = grid.get_size()
    curr_row = 0
    curr_col = 0
    stack = list()
    # find the next empty spot
    curr_row, curr_col = find_next_empty(grid, size, curr_row, curr_col)
    # start value for checking values 1 through 9 in the first empty cell
    start = 1
    # enter while loop on condition that there are still empty spots.
    while curr_row != -1 and curr_col != -1:
        # make an assignment
        valid = False
        # checking values from start (normally 1 when not backtracking) through 9
        for value in range(start, 10):
            # if a valid placement was made
            valid = valid_placement(grid, curr_row, curr_col, value, size)
            if valid:
                # make the assignment and append to the stack
                grid.set_value_by_location(curr_row, curr_col, value)
                stack.append((curr_row, curr_col))
                # find the next empty spot
                curr_row, curr_col = find_next_empty(grid, size, curr_row, curr_col)
                # start the cell value range at 1 a because ...
                start = 1
                # ... now we break out of this for loop after we got the next
                # empty cell and we must start checking th values starting at
                # 1 again since we aren't inbacktracking.
                break
        if not valid:
            # no valid assignment was found for current cell so we enter this
            # if statement and then check if the current cell is the first cell.
            if curr_row == 0 and curr_col == 0:
                # if it is than no solution can be found.
                # this is never true. if valid a solution will will always be found.
                print("there is no solution to this puzzle.")
                return False
            # if the current cell is not the first one than the backtracking
            # starts pop the last cell that was assigned off of the stack and
            # make it the current cell
            curr_row, curr_col = stack.pop()
            # the start value is now set to the last value of the most recent
            # valid assigned cell
            start = grid.get_value_by_location(curr_row, curr_col) + 1
            # then set the that cell back to unassigned (AKA zero).
            grid.set_value_by_location(curr_row, curr_col, 0)
    return True

def check_solution(grid):
    # I wrote this to check if a solution was valid.
    # I wrote it for a code fights challenge before this.
    # this is why there is inconsistant style and I dont use
    # the methods I already wrote for checking. I just wanted to
    # show this other method of checking subdivisions.
    # ex: the integer division symbol "//"
    # I made this way more complicated than I needed to for a regular sudoku
    # board. I used a list of dictionaries to make lookup for each value o(1).
    columnsCheck = []
    rowsCheck = []
    subsect = []
    size = grid.get_size()
    sub_size = grid.get_section()
    # set up empty arrays to store the entire subsection or row or
    # column for checking validity in place.
    for i in range(sub_size):
        subsect.append([])
        for j in range(sub_size):
            subsect[i].append({})
    # subsection 2D array (3x3 for sudoku usually)
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
                # I use integer division which rounds down so when I divide
                # the row and column numbers it divides the numbers into
                # subsections depending on the size of the grid and subsections.
                # (in sudoku it's 81 cells and 9 subsections)

                # check if the value is in the subsection 2D array (3x3 for sudoku usually)
                elif val in subsect[i//sub_size][j//sub_size]:
                    # if it is it goes into this if statement and returns false
                    return False
                else:
                    # I could put anything in the dictionary it is
                    # supposed to just act as a hash set so the 1 is
                    # a placeholder just to know that the value is a key
                    # in the dictionaty
                    columnsCheck[j][val] = 1
                    rowsCheck[i][val] = 1
                    subsect[i//sub_size][j//sub_size][val] = 1
    return True