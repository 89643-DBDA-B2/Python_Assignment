words = ["python", "functional", "programming", "is", "powerful"]
length_list =[]

def finding_length() :
    global length_list
    length_list = list(map(lambda n : len(n),words))
    #print(f"the length list is {length_list} and the data type of first element is {type(length_list[0])}")

finding_length()
print(f"{length_list}")
max_value = max(length_list)

print(f"The max string is {words[length_list.index(max_value,0)]}")