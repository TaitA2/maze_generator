from graphics import Line, Point


# create cell class used for dividing maze into blocks
class Cell():
    
    # constructor
    def __init__(self, x1, x2, y1, y2, win=None):
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
        # initalise a visited data member to False
        self.visited = False

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
        
        else:
            # create a line between top left and bottom left
            wall_line = Line(top_left, bottom_left)
            self._win.draw_line(wall_line, "#d9d9d9")

        # if cell has top wall
        if self.has_top_wall:
            # create a line between top left and top right
            wall_line = Line(top_left, top_right)
            self._win.draw_line(wall_line, "black")
        
        # if cell has top wall
        else:
            # create a line between top left and top right
            wall_line = Line(top_left, top_right)
            self._win.draw_line(wall_line, "#d9d9d9")

        # if cell has bottom wall
        if self.has_bottom_wall:
            # create a line between bottom left and bottom right 
            wall_line = Line(bottom_left, bottom_right)
            self._win.draw_line(wall_line, "black")
        
        # if cell has bottom wall
        else:
            # create a line between bottom left and bottom right 
            wall_line = Line(bottom_left, bottom_right)
            self._win.draw_line(wall_line, "#d9d9d9")

        # if cell has right wall
        if self.has_right_wall:
            # create a line between top right and bottom left 
            wall_line = Line(top_right, bottom_right)
            self._win.draw_line(wall_line, "black")
       
        # if cell has right wall
        else:
            # create a line between top right and bottom left 
            wall_line = Line(top_right, bottom_right)
            self._win.draw_line(wall_line, "#d9d9d9")
    
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
