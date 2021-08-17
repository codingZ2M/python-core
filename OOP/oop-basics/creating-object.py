# Creating an Objects

"""
__init__ :  A special method (constructor method), that will be called automatically when we
instantiate a class.

'self':
self represents the instance of the class. By using the “self” keyword we can access
the attributes and methods of the class in python. It binds the attributes with the
given arguments.
Whatever, after the 'self' is a parameter.
"""
# OOP - Memory Efficient & Repeatable

class Player:
    # Dunter method / Constructor method.. will be called when we make an object
    def __init__(self, player_name, player_id):
        self.name = player_name  # attribute / property
        self.id = player_id  # attribute / property

    def run(self):  # Custom method
        print('Player Name:' + self.name + " " + 'Age: ' + self.id)
        return 'Completed'


player1 = Player('Rick', 'P01');


#Returning Blueprint of an Object
print(player1) # Returns an player1 object location in memory

# Calling the Python Classes Variables:
print('Player Name:' + player1.name + " " + 'Age: ' + player1.id) # Accessing the attribute/property

print()

player2 = Player('Coery', 'P02');

#Returning Blueprint of an Object
print(player2) # Returns an player2 object location in memory

# Calling the Python Classes Variables:
print('Player Name:' + player2.name + " " + 'Id: ' + player2.id) # Accessing the attribute/property

print()

# Calling the Python Classes Methods:
print(player1.run())
print(player2.run())


print('------Adding another property to player2 object---------')
player2.attack=100
print(player2.attack)

print()
print('--------Returning Blueprint of an Object---------')
help(player1)


