L1 =[1,2,3]
T1 =4,5,6
L1plusT1 = []

L1plusT1.extend(L1)
L1plusT1.extend(T1)

print(f"the combined list is {L1plusT1}")

L1plusT1 = list(map(lambda n : str(n), L1plusT1))

print(f"The final list is {L1plusT1} and its type of first element is {type(L1plusT1[0])}")
