# import tkinter library
from tkinter import Tk, BOTH, Canvas

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

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()