# Introspection - The ability to determine the type of an object at runtime
'''
Python allows introspection (inspecting an object) with some helper functions.
'''


class User(object):

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

        # attack() overrides method in the super class with different implementation

    def attack(self):
        print(f'Attacking with power of {self.power}, User Email:  {self.email}')


wizard1 = Wizard('Rick', 70, 'rick@gmail.com')
print('---------Inspecting an Object-------')
print(dir(wizard1))
print()


def player_attack(char):
    char.attack()


player_attack(wizard1)
