'''
                  DUNTER / MAGIC METHODS
Ref: https://docs.python.org/3/reference/datamodel.html#special-method-names

Adding “dunder” methods to our class to get the attributes of the object printed
It will overlook the python in built mechanism of representing objects as strings.
So, __str__ method can be overridden to return a printable string representation of any user defined class.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.my_dict = {
            'name': 'HiHi',
            'has_pets': False,
        }

# Called by str(object) and the built-in functions format() and print() to compute the “informal” or nicely printable
    # string representation of an object.
    def __str__(self):
        return "Person: {}, Age: {}".format(self.name, self.age)

    def __len__(self):
        return 5

    def __getitem__(self, i):
        return self.my_dict[i]

    def __del__(self):
        return "deleted"


person = Person('Sarah', 25)

# By default, we got the name of the class along with the id of the object.
#print(person)

print(person.__str__())
print(person.__len__())

'''
For instance, if a class defines a method named __getitem__(), and x is an instance of this class, 
then x[i] is roughly equivalent to type(x).__getitem__(x, i).
'''
print(person['name'])

print(person.__del__())



