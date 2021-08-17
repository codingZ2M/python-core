# Introduction to OOP
"""
OOP - A way to Destructuring and Organizing the code
In Python everything is an object, because everything is built by 'class' keyword and
we are able to use different methods on our objects to perform some actions on them.
Objects are providing methods.
We can create our own data types with methods and attributes
How can we use OOP to make our more manageable?
OOP is a way to easier to maintain, extend and write the code.

We can break up our code into small objects (our own data types) that represent the real world entities/objects.
Breaking the functionalities and data into different objects that model the real world /objects.
S, different people can work in different parts and combine them finally.
An object can also extend functionality from different objects.

Efficiency of Class: Class code will be stored in memory in one place, every time when we create an object,
object code will be executed in memory
"""

print('---------Creating our own class (Blueprint)--------------')
"""
Class can declare properties and methods, from the class(Blueprint), you can create an objects 
over and over. The class can be instantiated that is the action of creating different instances/objects. 
"""
class EmployeeDetails: # Creating a class
    pass

# Creating multiple objects/instances by instantiating a class 'EmployeeDetails'
obj1 = EmployeeDetails()
obj2 = EmployeeDetails()
obj3 = EmployeeDetails()

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
print(type(obj1))
