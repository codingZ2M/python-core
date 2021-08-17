# Type Conversion

chicago_pizza = input("Enter Price for 'chicago_pizza' variable: ")
new_york_style_pizza = input("Enter Price for 'new_york_style_pizza' variable: ")

greek_pizza = 15.00
chicago_pizza = new_york_style_pizza
chicago_pizza = greek_pizza

# Type conversion using 'str' function
print("Price of chicago pizza  " + str(chicago_pizza) +
      " & " + "Price of new york style pizza " + new_york_style_pizza )

print("**********************************")
print ("Total Price of Chicago Pizza & New York Style Pizza: ")
print ( chicago_pizza + float(new_york_style_pizza) )