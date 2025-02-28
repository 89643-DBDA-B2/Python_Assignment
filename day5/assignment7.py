numbers = [5, 12, 3, 18, 9, 20,22,21]

greater_than_10 = tuple(filter(lambda n : n>10 , numbers))

print(f"The numbers greater than 10 are {greater_than_10}")