from graphics import *


def Intersection(p1, p2, p3, p4):
    st = time.time()
    win = GraphWin('Intersection Algo', 600, 480)
    point1 = Point(p1[0], p1[1])
    point2 = Point(p2[0], p2[1])
    l1 = Line(point1, point2)
    l1.draw(win)
    point3 = Point(p3[0], p3[1])
    point4 = Point(p4[0], p4[1])
    l2 = Line(point3, point4)
    l2.draw(win)
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1*p1[0] + b1*p1[1]
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2*p3[0] + b2*p3[1]
    determinant = a1*b2 - a2*b1
    if (determinant == 0):
        print("Lines are parallel!")
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
        fpoint = Point(x, y)
        Circle(fpoint, 3).draw(win)
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    win.getMouse()
    win.close()


def putpixel(win, x, y):
    pt = Point(x, y)
    pt.draw(win)


def main():
    x1 = int(input("Enter Start X1: "))
    y1 = int(input("Enter Start Y1: "))
    x2 = int(input("Enter End X2: "))
    y2 = int(input("Enter End Y2: "))
    x3 = int(input("Enter Start X3: "))
    y3 = int(input("Enter Start Y3: "))
    x4 = int(input("Enter End X4: "))
    y4 = int(input("Enter End Y4: "))
    Intersection((x1, y1), (x2, y2), (x3, y3), (x4, y4))


if __name__ == "__main__":
    main()
