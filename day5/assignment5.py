list1 = [1, 2, 3, 4, 5,9,98]
list2 = 5, 4, 3, 2, 1,6

combined = list(map(lambda a,b : a+b , list1,list2))

print(f"The combined list is {combined}")