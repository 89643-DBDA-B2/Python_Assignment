input = "Step on no pets"

input = input.replace(" ", "")
output = ""


output = input[::-1]

print(output)
input = input.lower
print(input)

if(input == output):
    print(f"This string is a palindrome")
