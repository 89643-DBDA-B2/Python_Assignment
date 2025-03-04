dict1 = {'key_1': 200, 'key 2': 300}


result =0
for value in dict1 :
    print(f"value : {value} type : {type(value)}")
    result = result + dict1[value]

print(f"The sum of values is {result}")