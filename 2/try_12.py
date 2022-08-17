class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


class Line:
    begin = None
    end = None

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self):
        # print('in length_getter')
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle(Point, Line):
    point1 = None
    point2 = None
    point3 = None


    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        line1 = Line(p1, p2)
        line2 = Line(p2, p3)
        line3 = Line(p3, p1)
        AB = line1.length
        BC = line2.length
        CD = line3.length
        return AB, BC, CD

    @property
    def total_area(self, AB, BC, CD):
        return (self.AB + self.BC + self.CD) / 2


point1 = Point(0, 3)
point2 = Point(4, 0)
point3 = Point(0, -4)

# line1 = Line(point1, point2)
# line2 = Line(point2, point3)
# line3 = Line(point3, point1)

# print(line1.length)
# print(line2.length)
# print(line3.length)

# area = (line1.length + line2.length + line3.length) / 2
# print(area)
area = Triangle(point1, point2, point3)
print(area.total_area)
