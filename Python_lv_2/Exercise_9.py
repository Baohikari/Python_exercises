# Write a program that accepts a sentence as input and counts uppercase and lowercase letters.

# Suppose the input is: Network Administration

# Then the output is:

Uppercase: 3
Lowercase: 8
user_input = input('Please enter a string: ')

count = {
    'Uppercase' : 0,
    'Lowercase': 0
}

for item in user_input:
    if item.isupper():
        count['Uppercase'] += 1
    if item.islower(): 
        count['Lowercase'] += 1

print(f"Amount of uppercase letters: {count['Uppercase']}")
print(f"Amount of lowercase letters: {count['Lowercase']}")