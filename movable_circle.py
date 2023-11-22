"""
Author name: Jeremiah E. Ochepo
last Edited: 2/15/2020 (7PM)
Discription:Movable circle GUI

"""
from graphics import *


def main():
    win = GraphWin('Click on a diagonal point', 200, 200, autoflush=False)

    # Progrsm Status Message
    msg = Text(Point(100.0, 20.0), 'Shapes')
    msg.setFace('helvetica')
    msg.setStyle('bold')
    msg.setSize(12)
    msg.draw(win)

    def shape_method():
        shape = Circle(Point(100, 100), 50)
        shape.setOutline('black')
        shape.setFill('red')
        shape.draw(win)

        # Loop
        for i in range(10):
            pt = win.getMouse()
            c = shape.getCenter()
            dx = pt.getX() - c.getX()
            dy = pt.getY() - c.getY()

            shape.move(dx, dy)

        win.close()

    shape_method()


main()
