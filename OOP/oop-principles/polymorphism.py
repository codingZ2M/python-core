# Polymorphism - Many Forms
"""
In Python, Polymorphism refers to the way in which objects, classes can share the same
method name but those method names cannot be differently based on what object calls it.
"""

# By default our super takes pre-defined base class 'object'
class User(object):
    # Here, init method is not required as we are not going to assign values to variables of 'User' object.
    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do Nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    # attack() overrides method in the super class with different implementation
    def attack(self):
        User.attack(self)  # Calling super class method
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    # attack() overrides method in the super class with different implementation
    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Rick', 70)
archer1 = Archer('Coery', 50)

# Note: Same function gives different outputs.. because of different objects...
def player_attack(userObject):
   userObject.attack()  #Same method gives different outputs.. because of different objects...


player_attack(wizard1)
player_attack(archer1)

print('-------Calling SAME attack method on two different objects using for loop--------------')

for userObject in [wizard1, archer1]:
    userObject.attack()
