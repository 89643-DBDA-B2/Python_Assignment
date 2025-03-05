# Create a class 'Student' with rollno, studentName, course ,dictionary of marks(subjectName -marks [5]).
# Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data
# E. accept records of 5 students and Print it


list_of_students = []
class Student :
    def __init__(self ,rollno, studentName, course , marks) :
        self.__rollno = rollno
        self.__course = course
        self.__studentName = studentName
        self.__marks = marks

    def setter(self ,rollno, studentName, course , marks) :
        self.__rollno = rollno
        self.__course = course
        self.__studentName = studentName
        self.__marks = marks

    def printing(self):
        print(self.__dict__)

while True :
    
    choice = int(input(""" Enter Choice
                1. Enter Student details
                2. exit
          """))
    
    if choice == 1 :
        print("""
            Enter rollno , studentName , course , marks 
              
              in that order
""")
        rollno = int(input())
        studentName = input()
        course = input()
        marks = int(input())

        student = Student(rollno,studentName,course,marks)
        list_of_students.append(student.__dict__)
        
    else :
        break

print(f"The list of student is {list_of_students}")


    
