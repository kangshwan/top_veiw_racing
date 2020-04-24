import sys

class Point:    
    """2D Point class"""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y))

    def __ne__(self, other):
        return ((self.x != other.x) or (self.y != other.y))
   
class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn = Point(), w=0, h=0):
        """ Initialize rectangle at Point posn, with width w, height h """
        try:
            self.position = posn
            if w == 0 and h == 0:
                raise Exception
            self.width = w
            self.height = h
        except:
            print("width and height is not defined! check again.")

    def __str__(self):
        return  "({0}, {1}, {2})".format(
            self.position, self.width, self.height)
    
    def __repr__(self):
        return  "Rectangle({0}, {1}, {2})".format(
            repr(self.position), self.width, self.height)
    
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.position.x += dx
        self.position.y += dy
    
    def area(self):
        return self.width*self.height
    

    def flip(self):
        self.height, self.width = self.width, self.height

    def __iter__(self):
        return iter([self.position, Point(self.position.x+self.width, self.position.y ), Point(self.position.y, self.height), Point(self.position.x+self.width, self.position.y+self.height)])


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

if __name__ == '__main__':
    point_list = [Point(2,4),Point(3,4), Point(2,3), Point(), Point(0,4), Point(4,0)]

    r = Rectangle(Point(100, 50), 10, 5)
    for i in r:
        print(i)