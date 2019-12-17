class Point(object):
    def __init__(self, name, x, y):
        self._x = x
        self._y = y
        self._name = name

    def distance(self, obj):
        dist = ((self._x - obj._x) ** 2 + (self._y - obj._y) ** 2) ** 0.5
        print('{}与{}的距离为{}'.format(self._name, obj._name, dist))
        return dist


x1 = Point('x1', 0, 0)
x2 = Point('x2', 2.5, 0)
x2.distance(x1)
