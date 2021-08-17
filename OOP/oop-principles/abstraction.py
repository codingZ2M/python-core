# Four Pillars (Encapsulation, Abstraction, Inheritance, Polymorphism) of OOP
# Abstraction - Hiding of information and giving access to only to the programmer or machine is interested in

# Do we need to know how the built-in or user-defined method of class is implemented / coded ?
""" For example, len( (1,2,3)), here we don't need to know how the len() function wss implemented in Python, it
abstracted away from us, so we don't need to waste our time to learning and coding from scratch.
Examples:
television.increaseVolume()
television.increaseColorContrast() - Allows to increase the color contrast without knowing how the engineers actually
implemented this functionality.
"""

"""
 private and public variables?
 If the variable name starts with an underscore symbol, that most likely means that should be a private 
 private variable should not modified.
 If you want to make private variable or method, use underscore in-front of it but there is no guarantee
"""

"""
At the same time, a method with __ (double underscore) is called 'Dunder method' will be discussed soon
Dunder method is built into Python and it should be not be modified. 
We will never write our own Dunter method. 
 We can override a dunter method in our class.    
"""


class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name, id):
        if PlayerCharacter.membership:
            self._name = name
            self._id = id

    def _run(self):  # Custom method..takes self as argument
        print(f' {self._name}  Running with Id: {self._id}')

    def set_name(self, name):  # Custom method..takes self as argument
       # if()
        self._name = name


    def _speak(self):
        print(f' {self._name} Speaking & id is  {self._id}')

    def runAndSpeak(self):
        self._run()
        self._speak()

player1 = PlayerCharacter('Rick', 'P01');
player1.set_name('Jhon')
player1.runAndSpeak()

print('---------------------------')
player2 = PlayerCharacter('Coery', 'P02');
player2.runAndSpeak()

# Example:
# cameraObject.take_picture()
# Here count method is called on tuple object without having to worry about how it is being implemented it.
print ((1,2,3,4, 1, 1).count(1))
