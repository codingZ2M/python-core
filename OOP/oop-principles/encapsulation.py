# Four Pillars (Encapsulation, Abstraction, Inheritance, Polymorphism) of OOP
# Encapsulation - Binding Data(Attributes) & Functions(methods) that manipulate the data.

"""
By using Encapsulation, All the functionalities are encapsulated, packaged up into a Blueprint (Class)
A real world object has full of data & actions. By packaging data & functions into instances, we are able to mimic what
happens in the real world entity with our code.

we can make objects for the class, and invoke the functions on these objects.
Because of oop-principles, Built-In string class encapsulated many functionalities, that can be accessed on the
string objects. For example, because of Encapsulation, we are able to access the methods (functionalities)
on the String object, methods are encapsulated in the String object.
"""

class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name, id):
        if (PlayerCharacter.membership):
            self.name = name  # attributes / properties are unique to an object
            self.id = id  # attribute / property

    def run(self):  # Custom method..takes self as argument
        print(f'Player Name: {self.name} & Id: {self.id}')

player1 = PlayerCharacter('Rick', 'P01');
player1.run()

player2 = PlayerCharacter('Coery', 'P02');
player2.run()
