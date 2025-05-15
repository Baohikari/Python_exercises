# Use a list to filter odd numbers from the list entered by the user.
# Suppose the input is: 1,2,3,4,5,6,7,8,9 then the output should be: 1,3,5,7,9
user_input = input('Please input number (seperated by ,): ')
result = [str_number for str_number in user_input.split(',') if int(str_number) % 2 != 0]
print(','.join(str(number) for number in result))