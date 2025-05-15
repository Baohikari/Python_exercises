#For a certain integer n, write a program to create a dictionary containing (i, i*i) as integers from 1 to n (including 1 and n) 
# and then print this dictionary.
square_dic = {}
user_input = int(input('Enter a natural number: '))
def dictionary_of_squares(user_input):
    for i in range (1, user_input + 1):
        square_dic.update(
            {i: i*i}
        )

dictionary_of_squares(user_input)
print(square_dic)