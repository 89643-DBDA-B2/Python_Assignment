# Design a system where a Library manages multiple Books, and each Book has an ID, title, and author.
# Functionalities:
# Add a Book to the library.
# Display all Books in the library.
# Exit the system when done.

list_of_books = []
class Books :
    def __init__(self ,ID, title, author ) :
        self.__ID = ID
        self.__title = title
        self.__author = author

    def adding(self):
        list_of_books.append(self.__dict__)

while True :
    
    choice = int(input(""" Enter Choice
                1. Enter book details
                2. exit
          """))
    
    if choice == 1 :
        print("""
            Enter ID , title , author 
            in that order
""")
        ID = int(input())
        title = input()
        author = input()

        book = Books(ID, title, author)
        book.adding()
        
    else :
        break

print(f"The list of student is {list_of_books}")
