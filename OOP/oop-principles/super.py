# super : Calling super class constructor method from the sub class constructor method..
class User(object):

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do Nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

        # attack() overrides method in the super class with different implementation
    def attack(self):
        print(f'Attacking with power of {self.power}, User Email:  {self.email}')

    def sign_in(self):
        print(f'Logged in: {self.name}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    # attack() overrides method in the super class with different implementation
    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}, User Email:  {self.email}')

    def sign_in(self):
        print(f'Logged in: {self.name}')


wizard1 = Wizard('Rick', 70, 'rick@gmail.com')
archer1 = Archer('Coery', 50, 'coery@gmail.com')


def player_attack(User):
   User.attack()
   User.sign_in()

player_attack(wizard1)

player_attack(archer1)

