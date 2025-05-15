# Write a program that accepts as input 4-digit binary strings, separated by commas, 
# and checks whether they are divisible by 5. Then, the numbers divisible by 5 are separated into commas.
user_input = input("Please enter some binary strings (seperated by ,): ")

binary_number = [number for number in user_input.split(',')]

result=[]

for number_to_cal in binary_number:
    if int(number_to_cal, 2) % 5 == 0:
        result.append(number_to_cal)

print(','.join(result))