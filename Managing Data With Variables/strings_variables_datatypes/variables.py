# Variables in Python
# Using built-in functions
# Documentation - https://docs.python.org/3/library/functions.html

# Assigning the value to a variable 'name' returned by the 'input()' method
print("You will get free soft drink and snack, if you win!")
pizza_type_length = len (input("Enter Pizza Type:") )

print("The length of the pizza type you entered: " + str(pizza_type_length))

if pizza_type_length > 15 :
    print("You will get free Chips & Coke with your pizza order")

else:
    print("Sorry! You will get the pizza which you ordered!")

print("Program is over")
