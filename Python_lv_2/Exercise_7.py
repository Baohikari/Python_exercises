# Write a program to find all numbers between 1000 and 3000 (both inclusive) such that all the digits in the number are even. 
# Print the found numbers in a comma-separated string, on a single line.
numbers = []
for number in range(1000, 3001):
    if number % 2 == 0:
        numbers.append(number)

print(','.join(str(number) for number in numbers))