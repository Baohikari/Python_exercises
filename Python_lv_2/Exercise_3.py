# Write a program that accepts a string of words from the user, separated by commas, 
# and prints those words in alphabetical order, separated by commas.
# Suppose the input is: without,hello,bag,world, then the output will be: bag,hello,without,world.
user_input = input('Please input a string: ')
splitted_string = user_input.split(',')

splitted_string.sort()
print(','.join(splitted_string))
