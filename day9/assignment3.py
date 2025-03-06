# 3.
# Create a class product having (pid and manufacture_location) as private fields,Create another class as Book 
#having (name, number_of_pages,author,price) as private fields. 
#Specify _init(), getters, setters, __str_() , print_data() Use correct OOP feature to implement this scenario.
# a) display the details of the product and book
# b) check if book price is 0 or negative then price is not valid otherwise print valid price.

class Product :
    def __init__(self,pid,man_loc):
        print("Inside product initializer")
        self.__pid = pid
        self.__man_loc = man_loc

    def getting(self):
        return str(self.__man_loc,self.__pid)

    def __str__(self):
        return self.getting()
    
class Book(Product) :
    def __init__(self,pid,man_loc,name, number_of_pages,author,price):
        print("Inside Book initializer")
        Product.__init__(self,pid,man_loc)
        self.__name = name
        self.__number_of_pages = number_of_pages
        self.__author = author
        if price > 0:
            self.__price  = price
        else :
            print("The price is not valid")

    def getting(self):
        return str(Product.getting(self), self.__price,self.__author,self.__number_of_pages,self.__name
)
    def __str__(self):
        return self.getting()

book1 = Book(89,"pune","xyz",54,"gdusouf",98)

print(f"{book1}")
