# Solver using backtracking algorthm
# I had some help from geeks for geeks on this problem but not too much
# Links: https://www.geeksforgeeks.org/backtracking-set-7-suduku/

from sudokugrid import Grid
from solve import solve_grid

def main():
    # my code here
    arr=[[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]

    grid = Grid()
    grid.assign_grid(arr)
    grid.print_grid()
    solve_grid(grid)

if __name__ == "__main__":
    main()