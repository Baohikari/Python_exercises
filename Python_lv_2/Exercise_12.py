# Write a program to calculate the actual amount of a bank account based on the transaction log entered from the console.
# The log format is shown as follows:
# D 100
# W 200
# Example:
# D 300
# D 300
# W 200
# D 100
# Output will be 500
result = 0
while True:
    user_input = input()
    command = user_input.split(' ')
    if command[0] == 'D':
        result += int(command[1])
    if command[0] == 'W':
        result -= int(command[1])
    if not user_input:
        break

print(result)