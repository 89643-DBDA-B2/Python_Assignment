original = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
final_list = []

for value in original :
    if  value % 19 == 0 or value % 13 == 0  :
        final_list.append(value)


print(f"The final list is {final_list}")

    
