# Using @classmethod and @staticmethod

# Instance vs. Static vs. Class Methods in Python: The Important Differences
# Ref: https://www.makeuseof.com/tag/python-instance-static-class-methods/

class PlayerCharacter:
    membership = True  # Class Object Attribute (static..not dynamic)

    def __init__(self, name, age):
        self.name = name  # Dynamic attributes / properties are unique to an object
        self.age = age  # Dynamic attribute / property

    def run(self):  # Custom method..takes self as argument
        print(f'Player Name: {self.name} & Age: {self.age}')


    # 'cls' refers our class 'PlayerCharacter'
    # Here, we are instantiating the PlayerCharacter object using class method
    # We can use class method, if we want to use, or modify class state / class attributes.
    @classmethod  # It is a method on the actual class
    def add_numbers(cls, num1, num2, name):
        return cls(name, num1 + num2)


    # We can use static method, if we don't care about class state / class attributes.
    @staticmethod
    def total_value(num1, num2):
        return num1 + num2


# Here, add_numbers() is a method on the actual class 'PlayerCharacter'
# @classmethod can be accessed without instantiating the class
print('-------------Calling Class Method-----------')
player2 = PlayerCharacter.add_numbers(11, 11, 'Tom')
print(f"{player2.name}  {player2.age}")

# Here, total_value() is a method on the actual class 'PlayerCharacter'
# @staticmethod can be accessed without instantiating the class but it doesn't have access to the class
print('-------------Calling Static Method-----------')
print(PlayerCharacter.total_value(11, 11))

print(PlayerCharacter('Rick', 23).run())