inp = "The quick "

inp = inp.replace(" ","")
inp = inp.lower()
print(f"string is {inp} and data type {type(inp)}")

lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

flag = True

for char in lst :
    if char not in inp:
        print(char)
        flag = False
        break

if(flag == True):
    print("The string is palindrome")
else:
    print("It is not")