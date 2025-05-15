#Write a program that accepts a string of numbers, separated by commas, from the console, 
# producing a list and a tuple containing every number.
user_input = input('Enter a string of numbers (e.g.: 34,25,67): ')
handle = user_input.split(",")
tuple_input = tuple(handle)
print(handle)
print(tuple_input)