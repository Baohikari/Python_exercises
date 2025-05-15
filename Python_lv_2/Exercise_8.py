# Write a program that accepts a sentence as input and counts the number of letters and digits in the sentence. 
# Suppose the following input is given to the program: hello world! 123

# Then the output will be:

# Number of letters: 10
# Number of digits: 3
user_input = input('Please enter a string: ')
words=[]
numbers=[]
letter_count = 0
digit_count = 0
for item in user_input.split(' '):
    if item.isdigit() ==  True:
        numbers.append(item)
    else: 
        words.append(item)

for word in ''.join(words):
    if word.isalpha():
        letter_count += 1

for digit in ''.join(numbers):
    if digit.isdigit():
        digit_count += 1

print(f'Amount of letters: {letter_count}')
print(f'Amount of digit: {digit_count}')