#Defining a class includes a class parameter and the same instance parameter
class User:
    def __init__(self, name = None):
        self.name = name
    def getUserName(self):
        self.name = input('Please enter your name: ')
    def greeting(self):
        print(f'Hello, greeting to {self.name}')

clsObj = User()
clsObj.getUserName()
clsObj.greeting()