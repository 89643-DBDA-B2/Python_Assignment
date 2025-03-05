# Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
# def init (self,a,b,r):
# self.a = a
# self.b = b
# self.r = r
# A:- Define a Area() method of the class which calculates the area of the circle.
# B:- Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

PI=3.14

class Circle :
    def __init__(self,x,y,r) :
        self.__x=x
        self.__y=y
        self.__r=r

    def Area (self) :
        return PI * self.__r * self.__r
    
    def Perimeter(self) :
        return 2 * PI * self.__r


circle1 = Circle(10,20,30)

# print(f"We can access it {circle1.x} and {circle1.y}")

print(f"The area and perimeter is {circle1.Area()} {circle1.Perimeter()}")