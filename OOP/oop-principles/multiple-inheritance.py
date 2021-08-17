# Multiple Inheritance
# NOTE: Method Resolution Order (MRO) in Python: http://www.srikanthtechnologies.com/blog/python/mro.aspx

# By default our super takes pre-defined base class 'object'
class User(object):
    # Here, init method is not required as we are not going to assign values to variables of 'User' object.
    def sign_in(self):
        print(f'Logged in  {self.name}')


# sub class / child class / derived class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


# sub class / child class / derived class
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack_with_arrows(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')

    def run(self):
        print('Ran really fast')

#  HybridBorg is going have all of the methods from Wizard, Archer
# HybridBorg is inheriting Wizard & Archer (Multiple Inheritance)
# Note: Technically, HybridBorg inherits Wizard first, then Archer..
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

# Here wizard1 and archer1 are going to have attributes, sign-in() (shared) as well as unique 'attack() method.
wizard1 = Wizard('Rick', 70)
archer1 = Archer('Coery', 50)
wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack_with_arrows()

print()
hb1 = HybridBorg('Borgie', 50, 100)
print(hb1.run())
print(hb1.attack_with_arrows())
print(hb1.attack())
print(hb1.sign_in())
