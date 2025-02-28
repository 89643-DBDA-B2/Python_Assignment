mylist = ['41','DROND','Sunbeam', '13','ZARA']

final = []

for value in mylist :
    if value.isdigit() :
        print(value *3)
    else :
        print(f"{value}#")