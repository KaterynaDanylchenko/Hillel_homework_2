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
    _begin = None
    _end = None

    @property  # getter
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property  # getter
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self):
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle:
    _point1 = None
    _point2 = None
    _point3 = None

    @property  # getter
    def point1(self):
        return self._point1

    @point1.setter
    def point1(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point1 = value

    @property  # getter
    def point2(self):
        return self._point2

    @point2.setter
    def point2(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point2 = value

    @property  # getter
    def point3(self):
        return self._point3

    @point3.setter
    def point3(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point3 = value

    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    @property
    def total_area(self):
        """This function takes point values when initializing triangle
            and calculates the area of the triangle using Heron's formula(perimetr divided by2)"""
        line1 = Line(self.point1, self.point2)
        line2 = Line(self.point2, self.point3)
        line3 = Line(self.point3, self.point1)
        AB = line1.length
        BC = line2.length
        CD = line3.length
        P = AB + BC + CD
        return (P*(P-AB)*(P-BC)*(P-CD))**0.5


point1 = Point(0, 5)
point2 = Point(4, 9)
point3 = Point(0, -4)
line = Line(point1, point3)

trig = Triangle(point1, point2, point3)

s = trig.total_area
print(s)



