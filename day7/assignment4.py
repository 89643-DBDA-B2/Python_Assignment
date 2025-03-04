Str1="Python83737@#8496"

numstr = "1,2,3,4,5,6,7,8,9,0"
sum=0
for char in Str1 :
    if char in numstr :
        sum = sum + int(char)

print(f"The sum is {sum} and average is {sum/len(numstr)}")
