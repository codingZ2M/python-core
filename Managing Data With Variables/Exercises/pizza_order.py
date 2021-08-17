# Type Conversion

#Excercise: Pizza Order
# Chicago Pizza
# Ground Beef, Sausage, Pepperoni, Onion, Mushrooms, & Green Peppers
# Price: ?
# New York-Style Pizza
# Ground Beef, Tomato Sauce ,  Red Pepper Flakes, Onion, Mushrooms, & Green Peppers
# Price: ?

print("Order Your Pizza!")

pizza_type = input("Enter Pizza Type: \n")

toppings = input("Enter Toppings For Ypur Pizza Type: \n")

print("Your Pizza Order: \n" +
                        "Pizza Type: " +
                         pizza_type +  '\n'
                        "Toppings Of Your 'Pizza': " + '\n' +
                         toppings)

print( "Thank You For Your Oder!")
print('******************************************')


price_tax = input("Enter 3 digits Number for Pizza Price & Tax without any space: ")

#Check the data type of number
print(type(price_tax ))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(price_tax [0])
second_digit = int(price_tax [1])
third_digit = int(price_tax[2])

pizza_price = first_digit + second_digit
print("Price of the 'Pizza': " + "US$ " +
        str(pizza_price) + '\n'
        " Tax: " +
        str(third_digit) + '.0%'
    )

