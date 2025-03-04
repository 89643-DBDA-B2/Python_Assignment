input = "this is fun"

vowels = ['a','e','i','o','u']

new_str = ''

for char in input :
    if char not in vowels :
        str = char + 'o' + char 
        new_str = new_str + str

print(new_str)