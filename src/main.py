from graphics import Window
from maze import Maze

# main function
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

# call main()
if __name__ == "__main__":
    main()