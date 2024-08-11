from graphics import Window
from maze import Maze

# main function
def main():

    # create window object
    win = Window(810, 610)

    # create Maze object
    maze = Maze(10, 10, 18, 12, 20, 20, win)

    # display window
    win.wait_for_close()

# call main()
if __name__ == "__main__":
    main()