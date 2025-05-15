#Exercise 2: Write a program that can calculate the factorial of a given number. 
#The result is printed as a string on one line, separated by commas. For example, 
#if the given number is 8, the output should be 40320.

#Solution 1: Use 'for' loop
result = 1
user_input = int(input('Enter an input: '))
for numbers in range(1, user_input + 1):
    result = result * numbers
print(result)

#Solution 2: Use recursion
def factor(n):
    if n == 0:
        return 1
    return n * factor(n - 1)
sol2 = factor(user_input)
print(sol2)