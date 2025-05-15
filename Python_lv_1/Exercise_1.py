#Write a program to find all numbers divisible by 7 but not multiples of 5, 
# within the range 2000 and 3200 (including 2000 and 3200). 
# The resulting numbers will be printed as a string on one line, separated by commas.
for solutions in range(2000, 3201):
    if(solutions % 7 == 0 and solutions % 5 > 0):
        print(f'{solutions}', end=', ')