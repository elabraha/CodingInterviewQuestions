class Grid:

    def __init__(self):
        self.size = 9
        self.grid = [[0 for x in range(9)]for y in range(9)] # create empty 2d array for grid.

    def print_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.grid[i][j], end=' ')
            print('', end='\n')

    def assign_grid(self, assignedGrid):
        self.grid = assignedGrid

    def set_value_by_location(self, row, col, value):
        self.grid[row][col] = value

    def get_value_by_location(self, row, col):
        return self.grid[row][col]

    def get_size(self):
        return self.size