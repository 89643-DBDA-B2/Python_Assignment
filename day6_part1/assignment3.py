num = [2,3,4,5,2,6,3,2]

final_list = []

for nu in num :
    if nu not in final_list :
        final_list.append(nu)

print(f"the final list is {final_list}")