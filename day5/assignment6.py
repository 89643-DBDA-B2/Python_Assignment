words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']

result = tuple(filter(lambda n : len(n)>5,words))

print(f"the charachter with more than 5 letters are {result}")
