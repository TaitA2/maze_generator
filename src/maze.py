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
        # randomly break walls in the maze
        self._break_walls_r(0, 0)
        # reset cells visited status
        self._reset_cells_visited()

    def _create_cells(self):
        # initalise list of cell lists
        self._cells = []
        # fiterate over rows
        for i in range(self.num_cols):
            # temporary list of cells created
            cells = []
            # set x coords based on iteration and maze's x coords
            x1 = self.x1 + (self.cell_size_x * i)
            x2 = x1 + self.cell_size_x
            # iterate over columns
            for j in range(self.num_rows):
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
        self._animate()
        # infinte loop
        while True:
            # TODO
            to_visit = []
            # i, j tuples for each neighboring cell
            try:
                above = self._cells[i - 1][j]
                if above.visited == False and i > 0:                        
                    to_visit.append(("left", i - 1, j))
            except IndexError:
                pass

            try:
                below = self._cells[i + 1][j]
                if below.visited == False and i < self.num_cols:                        
                    to_visit.append(("right", i + 1, j))
            except IndexError:
                pass

            try:
                left = self._cells [i][j - 1]
                if left.visited == False and j > 0:                        
                    to_visit.append(("above", i, j - 1))
            except IndexError:
                pass

            try:
                right = self._cells[i][j + 1]
                if right.visited == False and j < self.num_rows:                        
                    to_visit.append(("below", i, j + 1))
            except IndexError:
                pass
            
            # if zero possible directions 
            if to_visit == []:
                current.draw()
                return
            
            direction = random.randrange(len(to_visit))
            target_cell = to_visit[direction]
            target_i = target_cell[1]
            target_j = target_cell[2]
            target = self._cells[target_i][target_j]            
                
            if target_cell[0] == "above":
                current.has_top_wall = False
                target.has_bottom_wall = False

            if target_cell[0] == "below":
                current.has_bottom_wall = False
                target.has_top_wall = False

            if target_cell[0] == "left":
                current.has_left_wall = False
                target.has_right_wall = False

            if target_cell[0] == "right":
                current.has_right_wall = False
                target.has_left_wall = False
            
            
            self._break_walls_r(target_i, target_j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        # set current var to corresponding cell 
        current = self._cells[i][j]
        # list of tuples for directions containing direction name and indices
        directions = [("left", i - 1, j), ("right", i + 1, j), ("above", i, j - 1), ("below", i, j + 1)]
        # call the animate method
        self._animate()
        # set current cell's visited status to True
        current.visited = True
        # return True if current cell is the end cell
        if current == self._cells[-1][-1]:
            return True
        # iterate over each possible direction
        for direction in directions:
            target_i = direction[1]
            target_j = direction[2]
            try:
                target_cell = self._cells[target_i][target_j]
            except IndexError:
                pass
            available = False

            if direction[0] == "above" and target_i >= 0 and not target_cell.visited and not target_cell.has_bottom_wall and not current.has_top_wall:
                    available = True
            if direction[0] == "below" and target_i <= self.num_cols and not target_cell.visited and not target_cell.has_top_wall and not current.has_bottom_wall:
                    available = True
            if direction[0] == "left" and target_j >= 0 and not target_cell.visited and not target_cell.has_right_wall and not current.has_left_wall:
                    available = True
            if direction[0] == "right" and target_j <= self.num_rows and not target_cell.visited and not target_cell.has_left_wall and not current.has_right_wall:
                    available = True

            if available:
                current.draw_move(target_cell)
                r = self._solve_r(target_i, target_j)
                if r:
                    return True
                else:
                    current.draw_move(target_cell, undo=True)
        return False

