# Solver using backtracking algorthm
# I had some help from geeks for geeks on this problem but not too much
# Links: https://www.geeksforgeeks.org/backtracking-set-7-suduku/

from sudokugrid import Grid
from solve import solve_grid_recursively, check_solution, solve_grid

# I will ad a method for taking in user input at some point.
# I havent decided how exactly I want users to enter data.
# batch file? indivodually? both?

def main():
    # testing solution in main

    # test 1:
    # arr = [[3,0,6,5,0,8,4,0,0],
    #        [5,2,0,0,0,0,0,0,0],
    #        [0,8,7,0,0,0,0,3,1],
    #        [0,0,3,0,1,0,0,8,0],
    #        [9,0,0,8,6,3,0,0,5],
    #        [0,5,0,0,9,0,6,0,0],
    #        [1,3,0,0,0,0,2,5,0],
    #        [0,0,0,0,0,0,0,7,4],
    #        [0,0,5,2,0,6,3,0,0]]
    arr = [[4, 0, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 9, 8],
            [3, 0, 0, 0, 8, 2, 4, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 8, 0],
            [9, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 6, 7, 0],
            [0, 5, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 9, 0, 7],
            [6, 4, 0, 3, 0, 0, 0, 0, 0]]
    # arr = [[0,1,9,6,0,0,3,0,0],
    #         [0,5,0,2,7,4,0,0,1],
    #         [2,0,6,0,3,0,5,7,0],
    #         [0,8,0,0,2,0,6,9,0],
    #         [0,7,4,5,0,1,8,0,3],
    #         [9,0,0,7,0,6,0,0,5],
    #         [5,9,0,8,4,0,2,3,0],
    #         [4,0,7,0,0,5,1,0,9],
    #         [0,0,8,9,1,0,7,0,0]]

    # first grid solve
    print("Grid 1:\n")
    grid = Grid()
    grid.assign_grid(arr)
    print("Unsolved: ")
    grid.print_grid()
    print()
    if check_solution(grid):
        print("This unfinished or finished grid is a valid grid.")
    else:
        print("This unfinished or finished grid is not a valid grid.")
    print("\nSolved: ")
    if solve_grid_recursively(grid):
        grid.print_grid()
        print('\n')
        if check_solution(grid):
            print("Valid Solution!")
        else:
            print("Solution is not Valid!")

    # test 2:
    # arr2 = [[0,1,9,6,0,0,3,0,0],
    #         [0,5,0,2,7,4,0,0,1],
    #         [2,0,6,0,3,0,5,7,0],
    #         [0,8,0,0,2,0,6,9,0],
    #         [0,7,4,5,0,1,8,0,3],
    #         [9,0,0,7,0,6,0,0,5],
    #         [5,9,0,8,4,0,2,3,0],
    #         [4,0,7,0,0,5,1,0,9],
    #         [0,0,8,9,1,0,7,0,0]]

    arr2 = [[3,0,6,5,0,8,4,0,0],
            [5,2,0,0,0,0,0,0,0],
            [0,8,7,0,0,0,0,3,1],
            [0,0,3,0,1,0,0,8,0],
            [9,0,0,8,6,3,0,0,5],
            [0,5,0,0,9,0,6,0,0],
            [1,3,0,0,0,0,2,5,0],
            [0,0,0,0,0,0,0,7,4],
            [0,0,5,2,0,6,3,0,0]]

    # second grid solve
    print("\nGrid 2:\n")
    grid2 = Grid()
    grid2.assign_grid(arr2)
    print("Unsolved: ")
    grid2.print_grid()
    print()
    if check_solution(grid2):
        print("This unfinished or finished grid is a valid grid.")
    else:
        print("This unfinished or finished grid is not a valid grid.")
    if solve_grid(grid2):
        print("\nSolved: ")
        grid2.print_grid()
        print('\n')
        if check_solution(grid2):
            print("Valid Solution!")
        else:
            print("Solution is not Valid!")


if __name__ == "__main__":
    main()