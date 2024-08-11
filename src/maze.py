from cell import Cell
import time

# class for 2D list of cells
class Maze():
    
    # constructor
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
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

    def _create_cells(self):
        # initalise list of cell lists
        self._cells = []
        # fiterate over rows
        for i in range(self.num_rows):
            # temporary list of cells created
            cells = []
            # set x coords based on iteration and maze's x coords
            x1 = self.x1 + (self.cell_size_x * i)
            x2 = x1 + self.cell_size_x
            # iterate over columns
            for j in range(self.num_cols):
                # set y coords based on iteration and maze's y coords
                y1 = self.y1 + (self.cell_size_y * j)
                y2 = y1 + self.cell_size_y
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
