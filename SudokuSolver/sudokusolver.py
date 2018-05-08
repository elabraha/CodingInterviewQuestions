# Solver using backtracking algorthm
# I had some help from geeks for geeks on this problem but not too much
# Links: https://www.geeksforgeeks.org/backtracking-set-7-suduku/

from sudokugrid import Grid
from solve import solve_grid_recursively, check_solution, solve_grid

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

    # first grid solve
    print("Grid 1:\n")
    grid = Grid()
    grid.assign_grid(arr)
    print("Unsolved: ")
    grid.print_grid()
    print("\nSolved: ")
    solve_grid_recursively(grid)
    grid.print_grid()
    print('\n')
    if check_solution(grid):
        print("Valid Solution!")
    else:
        print("Solution is not Valid!")

    # test 2:
    arr2 = [[0,1,9,6,0,0,3,4,2],
            [8,5,3,2,7,4,9,0,1],
            [2,0,6,0,3,0,5,7,8],
            [0,8,0,0,2,0,6,9,0],
            [0,7,4,5,9,1,8,2,3],
            [9,0,0,7,0,6,0,1,5],
            [5,9,1,8,4,0,2,3,0],
            [4,2,7,0,0,5,1,0,9],
            [0,0,8,9,1,0,7,5,4]]

    # arr2 = [[3,0,6,5,0,8,4,0,0],
    #         [5,2,0,0,0,0,0,0,0],
    #         [0,8,7,0,0,0,0,3,1],
    #         [0,0,3,0,1,0,0,8,0],
    #         [9,0,0,8,6,3,0,0,5],
    #         [0,5,0,0,9,0,6,0,0],
    #         [1,3,0,0,0,0,2,5,0],
    #         [0,0,0,0,0,0,0,7,4],
    #         [0,0,5,2,0,6,3,0,0]]

    # second grid solve
    print("\nGrid 2:\n")
    grid2 = Grid()
    grid2.assign_grid(arr2)
    print("Unsolved: ")
    grid2.print_grid()
    solve_grid(grid2)
    print("\nSolved: ")
    grid2.print_grid()
    print('\n')
    if check_solution(grid2):
        print("Valid Solution!")
    else:
        print("Solution is not Valid!")


if __name__ == "__main__":
    main()