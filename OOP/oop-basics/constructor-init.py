# More about constructor __init__()
''' The constructor gives lot control,so in order to instantiate an object you
have to gave to do it in a right way.
'''
class PlayerCharacter:
    membership = True  # Class Object Attribute

# Here PlayerCharacter object is not instantiated properly, because of the condition
    def __init__(self, name='Not Given', age=0):
        if (age > 18):
            self.name = name  # attributes / properties are unique to an object
            self.age = age  # attribute / property

    def run(self):  # Custom method..takes self as argument
        print(f'Player Name: {self.name} & Id: {self.age}')

try:
    player1 = PlayerCharacter('Tom, 15');  # Error!.. object is not instantiated
    player1.run()
except AttributeError as error:
    print('Age should be >= 18')

print()

player2 = PlayerCharacter('Coery', 21);
player2.run()
