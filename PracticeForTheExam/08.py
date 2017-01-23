'''
Created on Nov 23, 2016

@author: User1
'''


class Shape:
    def __init__(self, color):
        # print("building a shape")
        self.__color = color

    def setColor(self, newcolor):
        self.__color = newcolor

    def getColor(self):
        return self.__color

    def area(self):
        return 0

    def __str__(self):
        return "a " + self.__color + " shape"


class Rectangle(Shape):
    def __init__(self, width, height, color):
        Shape.__init__(self, color)
        # print("building a rectange")
        self.__width = width
        self.__height = height

    def getWidth(self, neww):
        return self.__width

    def getHeight(self, newh):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "a " + self.getColor() + " rectangle"


class Square(Rectangle):
    def __init__(self, side, color):
        # print("building a square")
        Rectangle.__init__(self, side, side, color)

    def getSide(self):
        return self.__width

    def __str__(self):
        return "a " + self.getColor() + " square"


class Ellipse(Shape):
    def __init__(self, major, minor, color):
        Shape.__init__(self, color)
        # print("building an ellipse")
        self.__major = major
        self.__minor = minor

    def getMajor(self):
        return self.__major

    def getMinor(self):
        return self.__minor

    def area(self):
        return 3.14 * self.__minor * self.__major

    def __str__(self):
        return "a " + self.getColor() + " ellipse"


class Circle(Ellipse):
    def __init__(self, radius, color):
        Ellipse.__init__(self, radius, radius, color)
        # print("building a circle")

    def getRadius(self):
        return self.getMajor()

    def area(self):
        return 3.14 * self.getRadius() ** 2

    def __str__(self):
        return "a " + self.getColor() + " circle"


shape = Shape("red")
print(str(shape) + ", area is = " + str(shape.area()))

"""
    The rectangle 'is a' shape
"""
rectangle = Rectangle(5, 2, "blue")
print(str(rectangle) + ", area is = " + str(rectangle.area()))

"""
    The square 'is a' particular rectangle
"""
square = Square(3, "green")
print(str(square) + ", area is =" + str(square.area()))

ellipse = Ellipse(10, 6, "pink")
print(str(ellipse) + ", area is =" + str(ellipse.area()))

"""
    The circle 'is a' particular ellipse
"""
circle = Circle(8, "magenta")
print(str(circle) + ", area is =" + str(circle.area()))



