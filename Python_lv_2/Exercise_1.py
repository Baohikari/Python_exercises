#Write a program and print the value according to the given formula: Q = √([(2 * C * D)/H]) 
# (in words: Q is equal to the square root of [(2 multiplied by C multiplied by D) divided by H] . 
# With the fixed value of C being 50, H being 30. D is a customizable range of values, entered from the user interface, 
# the values ​​of D are separated by commas.
#For example: Suppose the input string of D is 100,150,180, the output will be 18,22,24.
import math
d  = input('Enter a string of number (e.g.: 23,26,81): ')
def calculate_q(d, c = 50, h = 30):
    result_list = []
    d = d.split(',')
    for num in d:
        result = math.floor(math.sqrt((2 * c * h) / int(num)))
        result_list.append(result)
    return result_list

list_of_results = calculate_q(d)
str_result = ','.join(map(str, list_of_results))
print(str_result)

