people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print(f"A : The number of students are {len(people.keys())}")

print("-*-" * 10)

people['Lisa'] = 'Red'

print(f"The updated color of lisa is {people['Lisa']}")

print("-*-" * 10)


people.pop('Jenny')

print(f"Jenny is removed {people}")

print("-*-" * 10)


list_name = list(people.keys())
list_name.sort()
sorted_dictionary = {}


for value in list_name :
    sorted_dictionary[value] = people[value]

print(f"The sorted dictionary is {sorted_dictionary}")