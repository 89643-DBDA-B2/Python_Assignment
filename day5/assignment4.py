numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_number = list(filter(lambda n : n%2 != 0 , numbers))

odd_number_square = list(map(lambda n:n*n,odd_number))

sum=0

for number in odd_number_square :
    sum = sum +number

print(f"The sum is {sum}")