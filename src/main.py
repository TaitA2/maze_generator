from graphics import Window
from maze import Maze

# main function
def main():

    # create window object
    win = Window(1810, 1610)

    # create Maze object
    num_rows = 5
    num_cols = 10
    maze = Maze(10, 10, num_rows, num_cols, 20, 20, win)

    # solve the maze
    maze.solve()

    # display window
    win.wait_for_close()

# call main()
if __name__ == "__main__":
    main()