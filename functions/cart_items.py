

# Finding Duplicates
# Python list function | count()
# The Python Tutorial - https://docs.python.org/3/tutorial/index.html
# Python 3.8.3 documentation - https://docs.python.org/3/

# Function
# Finding Duplicates



# Python list function | count()
# The Python Tutorial - https://docs.python.org/3/tutorial/index.html
# Python 3.8.3 documentation - https://docs.python.org/3/

#  FUNCTION "RETURNINHG" A LIST AS AN OUTPUT
def shopping_cart(shopping_cart):
    cart_items_checkout = []
    for value in shopping_cart:
        if shopping_cart.count(value) > 1:    # Counts the number of times the character appears in list
            if value not in cart_items_checkout:   # we need one instance of each character to be appended in the array.
               cart_items_checkout.append(value)
        else:
           cart_items_checkout.append(value)
    return cart_items_checkout



cart_items = ['2020 Y68 Smart Watch', 'Summer antiskid sports shoes',
              'Men 2021 Winter Casual Thick Waterproof Jacket',
             '2020 Y68 Smart Watch', 'Men Military Watch 50m Waterproof',
              'Men 2021 Winter Casual Thick Waterproof Jacket'
              ]

final_cart_items  = shopping_cart(cart_items)

for item in final_cart_items:
    print(item)