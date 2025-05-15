# Write a program with 2 digits, X, Y that receives values ​​from input and creates a 2-dimensional array.
# The element value in the ith row and jth column of the array must be i*j.
# Note: i=0,1,...,X-1; j=0,1,...,Y-1.
# For example: The input X, Y value is 3.5, the output is: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4 , 6, 8]]
user_x = int(input("Please enter a number X: "))
user_y = int(input("Please enter a number Y: "))

multilist = []
for row in range(user_x):
    row_list = []
    for col in range(user_y):
        row_list.append(0)
    multilist.append(row_list)

for row in range(user_x):
    for col in range(user_y):
        multilist[row][col]= row*col

print (multilist)