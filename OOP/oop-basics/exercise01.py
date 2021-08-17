class Cat:
    species = 'mammal'

    def __init__(self, cat_name, age):
        self.name = cat_name
        self.age = age

    def get_cat_age(self):
        return self.age

    def get_cat_name(self):
        return self.name

# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(peanut.get_cat_age(), garfield.get_cat_age(), snickers.get_cat_age())} years old.")
print(peanut.get_cat_name())