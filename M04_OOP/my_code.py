import math


class Point:
    counter = 0
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @staticmethod
    def closest(p_list):
        ranges = []
        for i in range (len(p_list)):
            x = abs(p_list[i].x)
            y = abs(p_list[i].y)
            measure = math.sqrt(x*x+y*y)
            ranges.append(measure)
        return min(ranges)

    @staticmethod
    def getter_count():
        return Point.counter

    @property
    def x(self):
        Point.counter = Point.counter + 1
        return self._x
    
    @x.setter
    def x(self, v):
        self._x = v
    
    @property
    def y(self):
        Point.counter = Point.counter + 1
        return self._y
    
    @y.setter
    def y(self, v):
        self._y = v
    
#Write test software under this if
if __name__ == "__main__":
    p1 = Point(2, 2)
    p2 = Point(3,3)
    p3 = Point(1,1)
    
    p_list = [p1,p2, p3]
    Point.closest(p_list)
    
    print(Point.closest(p_list))
