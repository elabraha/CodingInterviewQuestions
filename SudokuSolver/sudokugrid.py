""" Sudoku grid class module """
class Grid:

    """ Sudoku grid initializer """
    def __init__(self, size=9, section_size=3):
        self.__size = size
        self.__section = section_size
        # create empty 2d array for grid.
        self.__grid = [[0 for x in range(self.__size)]for y in range(self.__size)]

    """ Print grid """
    def print_grid(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(self.__grid[i][j], end=' ')
            print('', end='\n')

    """ Assign grid from a 2D array """
    def assign_grid(self, assignedgrid):
        self.__grid = assignedgrid

    """ Set the value in a cell by specifying the row and column of the cell """
    def set_value_by_location(self, row, col, value):
        self.__grid[row][col] = value

    """ Get the value in a cell by specifying the row and column of the cell """
    def get_value_by_location(self, row, col):
        return self.__grid[row][col]

    """ Get the size of the grid """
    def get_size(self):
        return self.__size

    """ Get the size of the subsections of the grid """
    def get_section(self):
        return self.__section
