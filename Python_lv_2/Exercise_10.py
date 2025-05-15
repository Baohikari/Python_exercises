# Write a program to calculate the value of a+aa+aaa+aaaa where a is the number entered by the user.
# Suppose a is entered as 1 then the output will be: 1234
user_input = input('Please enter a number: ')

n1 = int( "%s" % user_input )
n2 = int( "%s%s" % (user_input,user_input) )
n3 = int( "%s%s%s" % (user_input,user_input,user_input) )
n4 = int( "%s%s%s%s" % (user_input,user_input,user_input,user_input) )

print ("Tổng cần tính là: ",n1+n2+n3+n4)