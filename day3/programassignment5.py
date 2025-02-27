def max_of_three(a,b,c):
    """this is a function to find the maximum of three numbers"""
    if a >b and a>c:
        print("the max is a=",a)
    elif b>a and b>c:
        print(f"b is max b={b}")
    else:
        print("the max is c ={c}")

a=input("enter first number: ")
b=input("enter second number: ")
c=input("enter third number: ")

max_of_three(a=c,b=b,c=a)