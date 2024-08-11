# import tkinter library
from tkinter import Tk, BOTH, Canvas
import time

# create Window class for pop up
class Window():

    # constructor
    def __init__(self, width, height):
        # set height and width
        self.width = width
        self.height = height
        # create root widget
        self.root = Tk()
        # set root tile
        self.root.title("A Mazing Program")
        # create canvas widget
        self.canvas = Canvas()
        # pack canvas so it can be drawn
        self.canvas.pack()
        # True if window is running 
        self.running = False
        # run self.close method when window is deleted
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    # method to draw a line on the window
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    
    # method for redrawing all graphics in the window
    def redraw(self):
        # update the root widget
        self.root.update_idletasks()
        self.root.update()
    
    # method for callling redraw() constantly while the window is running
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    # method to set running to False when window is closed
    def close(self):
        self.running = False

# create point class for creating lines
class Point():

    # constructor to set x and y coords of point
    def __init__(self, x, y):
        self.x = x
        self.y = y

# create line class to join points
class Line():

    # constructor
    def __init__(self, point1, point2):
        # save 2 points to be connected
        self.point1 = point1
        self.point2 = point2
    
    # method to draw a line between 2 points on provided canvas using provided fill color
    def draw(self, canvas, fill_color):
        # extract coords from points
        x1 = self.point1.x
        y1 = self.point1.y
        x2 = self.point2.x
        y2 = self.point2.y
        # call canvas' create line method using provided args
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)


# create cell class for dividing maze 
class Cell():
    
    # constructor
    def __init__(self, x1, x2, y1, y2, win):
        # set all 4 walls to True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # set coords of cell
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        # set the window the cell is in
        self._win = win

    # method to draw walls of cell
    def draw(self):
        # create 4 corner points from coords
        top_left = Point(self._x1, self._y1)
        bottom_left = Point(self._x1, self._y2)
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)

        # if cell has left wall
        if self.has_left_wall:
            # create a line between top left and bottom left
            wall_line = Line(top_left, bottom_left)
            self._win.draw_line(wall_line, "black")

        # if cell has top wall
        if self.has_top_wall:
            # create a line between top left and top right
            wall_line = Line(top_left, top_right)
            self._win.draw_line(wall_line, "black")

        # if cell has bottom wall
        if self.has_bottom_wall:
            # create a line between bottom left and bottom right 
            wall_line = Line(bottom_left, bottom_right)
            self._win.draw_line(wall_line, "black")

        # if cell has right wall
        if self.has_right_wall:
            # create a line between top right and bottom left 
            wall_line = Line(top_right, bottom_right)
            self._win.draw_line(wall_line, "black")
    
    # method to draw a line connect the center of 2 cells
    def draw_move(self, to_cell, undo=False):
        # set fill color 
        fill_color = "red"
        if undo:
            fill_color = "gray"
        # get center coords of cells
        from_x = (self._x1 + self._x2) / 2
        from_y = (self._y1 + self._y2) / 2
        to_x = (to_cell._x1 + to_cell._x2) / 2
        to_y = (to_cell._y1 + to_cell._y2) / 2
        # create center points from coords
        from_center = Point(from_x, from_y)
        to_center = Point(to_x, to_y)
        connecting_line = Line(from_center, to_center)
        self._win.draw_line(connecting_line, fill_color)


# class for 2D list of cells
class Maze():
    
    # constructor
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
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



def main():
    # create window object
    win = Window(810, 610)

    # # # create points
    # point1 = Point(100, 100)
    # point2 = Point(300, 100)

    # # create line from points
    # line = Line(point1, point2)

    # # draw line in red on window
    # win.draw_line(line, "red")

    # create cells
    cell1 = Cell(10, 30, 10, 30, win)
    cell2 = Cell(30, 50, 10, 30, win)
    cell3 = Cell(50, 70, 10, 30, win)

    # draw cells
    # cell1.draw()
    # cell2.draw()

    # draw connection between cells
    # cell1.draw_move(cell2)

    # create Maze object
    maze = Maze(10, 10, 18, 12, 20, 20, win)
    # create window
    win.wait_for_close()

if __name__ == "__main__":
    main()