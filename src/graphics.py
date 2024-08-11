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
