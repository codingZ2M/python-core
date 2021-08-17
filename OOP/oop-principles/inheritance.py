# Inheritance
"""
Inheritance allows new objects to take on the properties of existing objects.
"""

"""
 Example:
 User can be Wizard or Archer or Ogres in the game but all of them have to be signed in first.
 We can use Inheritance, so that all these sub classes (Wizard, Archer) can access the 
 sign_in method of parent class.
 How do we do Inheritance?
"""


# By default our super takes pre-defined base class 'object'
class User(object):
    # Here, init method is not required as we are not going to assign values to variables of 'User' object.
    def sign_in(self):
        print(f'Logged in: {self.name}')


# sub class / child class / derived class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack_with_Power(self):
        print(f'Attacking with power of {self.power}')


# sub class / child class / derived class
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack_with_arrows(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')


# Here wizard1 and archer1 are going to have attributes, sign-in() (shared) as well as unique 'attack() method.
wizard1 = Wizard('Wizard', 70)
archer1 = Archer('Archer', 50)

wizard1.sign_in()
wizard1.attack_with_Power()

archer1.sign_in()
archer1.attack_with_arrows()

print('-------Using isinstance()---------')
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

# In Python, 'object' is a Base class for all the pre-defined or user-defined classes.
# So the methods defined by object are available to all its sub classes.
print(isinstance(wizard1, object))
