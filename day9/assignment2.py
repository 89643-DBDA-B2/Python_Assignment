# 2.
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle. 
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with a  attribute and another Volume() method to calculate the volume of the Parallelepiped.

class Rectangle :

    def __init__(self,length,width):
        self._length = length
        self._width = width

    def Perimeter(self):
        return 2*(self.length + self.width)

    def Area(self):
        return self.length * self*width

    def display(self)
        print(f"The values are length : {self.length} width : {self.width} perimeter : {self.perimeter()} area : {self.area{}} ")

class Parallelepiped(Rectangle) :
    def __init__(self,length,width,is_parallelepiped)
        Rectangle.__init__(self,length,width)
        self.__is_parallelepiped = is_parallelepiped

    def volume(self):
        print(f"Inside parallelepiped method to calculate volume")
        #write volume logic here