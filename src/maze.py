from cell import Cell
import time
import random

# class for 2D list of cells
class Maze():
    
    # constructor
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        # initalise data members
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        # call _create_cells() method
        self._create_cells()
        # break entrance and exit walls
        self._break_entrance_and_exit()
        if seed:
            self.seed = random.seed(seed)

    def _create_cells(self):
        # initalise list of cell lists
        self._cells = []
        # fiterate over rows
        for i in range(self.num_cols):
            # temporary list of cells created
            cells = []
            # set y coords based on iteration and maze's y coords
            y1 = self.y1 + (self.cell_size_y * i)
            y2 = y1 + self.cell_size_y
            # iterate over columns
            for j in range(self.num_rows):
                # set x coords based on iteration and maze's x coords
                x1 = self.x1 + (self.cell_size_x * j)
                x2 = x1 + self.cell_size_x
                # add new Cell object with above args and add to temporary list
                cells.append(Cell(x1, x2, y1, y2, self.win))
            # add temporary list to matrix
            self._cells.append(cells)

        # call draw cell method on each sell in matrix
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
    
    # method for drawing each cell in self._cells matrix
    def _draw_cell(self, i, j):
        # assign indexed cell to var
        cell = self._cells[i][j]
        # if conditional to allow unit testing
        if self.win:
        # call Cell's draw function
            cell.draw()
            # call maze's _animate() method
            self._animate()
    
    # method to visualise algorithm in real time
    def _animate(self):
        # call window's redraw method
        self.win.redraw()
        # wait short time for eyes to keep up
        time.sleep(0.025)

    # method to remove maze's entrance and exit walls
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    # recursive method to break cell walls
    def _break_walls_r(self, i, j):
        # mark current cell as visited
        current = self._cells[i][j]
        current.visited = True
        # infinte loop
        while True:
            # TODO
            return 