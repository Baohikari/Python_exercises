# Write a program that accepts a string of words separated by spaces as input, removes duplicates, 
# sorts them alphabetically, and prints them.
#Suppose the input is: hello world and practice makes perfect and hello world again
#Then the output is: again and hello makes perfect practice world
user_input = input('Please enter your string: ')

handle_word = [word for word in user_input.split(' ')]
print(' '.join(sorted(set(handle_word))))
