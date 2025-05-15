#Python has many built-in functions, if you don't know how to use it, you can read the documentation online or find some books. 
# But Python also has built-in function documentation for every built-in function in Python. 
# The requirement of this assignment is to write a program to print documentation about 
# some built-in Python functions such as abs(), int(), input() and add documentation for the function you define yourself.
print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)
# Code by Quantrimang.com
def square(num):
 '''Trả lại giá trị bình phương của số được nhập vào.

 Số nhập vào phải là số nguyên.
 '''
 return num ** 2

print (square.__doc__)