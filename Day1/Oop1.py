class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"Point({self._x}, {self._y})"

    def __str__(self):
        return f"Point object with x = {self._x}, y = {self._y}"

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)

def main():
    p1 = Point(5, 10)
    p2 = Point(5, 10)
    p3 = p1 + p2
    print(p3)
    if p1 == p2:
        print("They are equal")
    else:
        print("They are not equal")
    print(repr(p1))
    print(str(p1))





if __name__ == '__main__':
    main()
