# Attributes & Methods

class PlayerCharacter:
    # Declaring Class Object Attribute... static but not dynamic.. actual attribute on this class
    # All the objects will have the same copy 'membership', it means class object attribute doesn't change across objects.
    # class object attribute can be used anywhere inside the class.
    membership = True  # Class Object Attribute
    pi = 3.14

    def __init__(self, name, id):
        # if (self.membership):
        if (PlayerCharacter.membership):
            self.name = name  # attributes / properties are unique to an object
            self.id = id  # attribute / property

    def run(self):  # Custom method..takes self as argument
        print(f'Player Name: {self.name} & Id: {self.id}')
    #   print(f'Player Name: {PlayerCharacter.name} & Id: {PlayerCharacter.id}')


player1 = PlayerCharacter('Rick', 'P01');
player1.run()

player2 = PlayerCharacter('Coery', 'P02');
player2.run()
