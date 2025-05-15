# Write a program that accepts a string as input, converts the lines to uppercase and prints them on the screen.

lines=[]
while True:
    user_input = input('Please enter string (enter z if you are done): ')
    if user_input == 'z':
        break
    else:
        lines.append(user_input.upper())

for item in lines:
    print(item)