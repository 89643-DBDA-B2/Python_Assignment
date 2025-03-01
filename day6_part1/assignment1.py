input = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

list1 =[] #strings
list2 = [] #numbers
final_lst = []

for lst in input :
    list1.append(lst[0])
    list2.append(lst[1])

list2.sort()

print(f"The seperate list are {list1} and {list2}")

for element in list2:
    for checklst in input:
        if checklst[1] == element :
            final_lst.append(checklst)


print(f"The final sorted list is {final_lst}")