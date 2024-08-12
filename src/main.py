from graphics import Window
from maze import Maze

# main function
def main():

    # create window object
    win = Window(810, 610)

    # create Maze object
    num_rows = 12
    num_cols = 18
    cell_size_x = 20
    cell_size_y = 20
    maze = Maze(10, 10, num_rows, num_cols, cell_size_x, cell_size_y, win)

    # solve the maze
    maze.solve()

    # display window
    win.wait_for_close()

# call main()
if __name__ == "__main__":
    main()