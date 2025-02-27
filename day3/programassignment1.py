length = int(input("Write length  of rectangle: "))
print(f"Length: {length}  Length: {type(length)}")
width = int(input("Write width of rectangle: "))
print(f"Width : {width} Width: {type(width)}")

Area = length * width
perimeter = (length +width)*2

print("Area of rectangle is: ",Area)
print(f"Perimeter of rectangle is:{perimeter} ")