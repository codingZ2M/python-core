
#Excercise: Pizza Order
# Chicago Pizza
# Ground Beef, Sausage, Pepperoni, Onion, Mushrooms, & Green Peppers
# Price: ?
# New York-Style Pizza
# Ground Beef, Tomato Sauce ,  Red Pepper Flakes, Onion, Mushrooms, & Green Peppers
# Price: ?

print("Order Your Pizza!")
pizza_type = input("Enter Pizza Type: \n")
mushrooms = input("Do You Want Add Mushrooms?:  'Y' | 'N' \n")
ground_beef = input("Do You Want Add Ground Beef?: 'Y' | 'N' \n")
size = input("Select Your Pizza Size?: Enrter 'S', | 'M', |'L' ")

pizza_order_value =0.00

if size == "S":
    pizza_order_value += 12
elif size == "M":
    pizza_order_value += 20
else:
    pizza_order_value += 25

if mushrooms  == "Y":
    if size == "S":
        pizza_order_value += 3
    else:
        pizza_order_value += 4

if ground_beef == "Y":
    if size == "S":
        pizza_order_value += 3
    else:
        pizza_order_value += 4

print("Your Pizza Order: \n" +
                        "Pizza Type: " +
                         pizza_type +  '\n'
                        "Toppings Of Your 'Pizza': " + '\n' +
                         mushrooms if 'Musrooms' else "NA"  + '\n' +
                         ground_beef if 'Ground Beef' else "NA"  + '\n'
          )

print(f"Your final bill is: ${pizza_order_value}.")

print( "Thank You For Your Oder!")
print('******************************************')