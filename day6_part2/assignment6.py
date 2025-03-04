List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]

new_dic = {}

for val in List1 :
    if new_dic.get(val) == None :
        new_dic[val] = 1
    else :
        new_dic[val] = new_dic[val] +1

print(new_dic)