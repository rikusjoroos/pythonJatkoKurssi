class Point:
    counter = 0
    def __init__(self, x, y):
        self._x = x
        self._y = y

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
    print(Point.getter_count())
    p1 = Point(1.2, 1.4)
    print(Point.getter_count())
    p1.x
    print(Point.getter_count())
    p1.y
    print(Point.getter_count())
    p2 = Point(2, 3)
    print(Point.getter_count())
    p2.x
    print(Point.getter_count())
    

