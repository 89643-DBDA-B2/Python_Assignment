List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]

new_dict = {
    "Even": [], 
    "Odd": [], 
}

for num in List1:
    if num % 2 == 0:
        new_dict["Even"].append(num)
    else:
        new_dict["Odd"].append(num)

print(new_dict)
