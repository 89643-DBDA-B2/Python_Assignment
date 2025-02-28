numbers = 10,20,30,40
numbers2 = 10,20,30,40,50,60,70,80,90
#print(f"this is a tuple {numbers} and its data type is {type(numbers)}")

def function1() :
    n1,n2,n3,n4 = numbers
    print(f"sucessfully unpaked for equal assignement {numbers}")

#function1()

def function2() :
    # n1,n2,n3,n4,n5 = numbers
    # print(f" this is not enough assignment runtime error {numbers}")

     n1,n2,n3 = numbers
     print(f"this is too many values error {numbers}")

#function2()

#rest of values operator *
def function3() :
    n1,n2,*n3 = numbers2
    print(f"for n1,n2,*n3 n1 ={n1} n2 ={n2} n3={n3}")

    n1,*n2,n3 = numbers2
    print(f"for n1,*n2,n3 n1 ={n1} n2 ={n2} n3={n3}")  

    *n1,n2,n3 = numbers2
    print(f"for *n1,n2,n3 n1 ={n1} n2 ={n2} n3={n3}") 

#function3()     

def demofun():
    print(f"inside demo function")

def function4(param):
    print(f"inside function4 with param = {param} and param type {param}")
    param()

#print(f"dummy_function = {demofun}, type = {type(demofun)}")

#function4(demofun)

def squarenum() :
    numbers3 = 10,20,30,40,50,60,70,80,90,100

    for number in numbers3 :
        print(f"number is {number} and square is {number*number}")

#squarenum()

def squarenum2() :
    numbers3 = 10,20,30,40,50,60,70,80,90,100
    square = []

    for number in numbers3 :
        square.append(number**2)

    print(f"The new squared list is {square}")    


#squarenum2()

def logic(param) :
    return param** 2

def squarenum3() :
    numbers3 = 10,20,30,40,50,60,70,80,90,100
    square = [] 

    square = list(map(logic,numbers3))
    print(f"The new squared list is {square}")  

#squarenum3()  

def squarenum4() :
    numbers3 = 10,20,30,40,50,60,70,80,90,100
    square = [] 

    square = list(map(lambda n:n*n,numbers3))
    print(f"The new squared list is {square}") 

#squarenum4()


def function3():
    # list of numbers
    numbers = [10, 2, 4, 7, 8, 90, 23, 34, 67, 45]

    # lambda to check if the number is even
    is_even = lambda n: n % 2 == 0
    #even_numbers = list(map(is_even, numbers))  this will return list of true and false
    even_numbers = list(filter(is_even, numbers))  # this will return list of even numbers
    print(f"numbers = {numbers}")
    print(f"even_numbers = {even_numbers}")
