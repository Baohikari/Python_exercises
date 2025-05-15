#Define a class with at least 2 methods:
#getString: to get a string entered by the user from the console.
#printString: prints the entered string to uppercase.
#Add simple test functions to test class methods.
#For example: The input string is quantrimang.com, the output must be: QUANTRIMANG.COM

class Format_String:
    def __init__(self):
        self.user_string = ""

    def getString(self):
        self.user_string = input('Enter string: ')

    def printString(self):
        print(self.user_string.upper())

strObject = Format_String()
strObject.getString()
strObject.printString()
