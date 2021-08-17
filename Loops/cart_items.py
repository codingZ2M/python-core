# Finding Duplicates

cart_items = ['2020 Y68 Smart Watch', 'Summer antiskid sports shoes',
              'Men 2021 Winter Casual Thick Waterproof Jacket',
             '2020 Y68 Smart Watch', 'Men Military Watch 50m Waterproof',
              'Men 2021 Winter Casual Thick Waterproof Jacket'
              ]

# Python list function | count()
# The Python Tutorial - https://docs.python.org/3/tutorial/index.html
# Python 3.8.3 documentation - https://docs.python.org/3/

cart_items_checkout = []

for item in cart_items:
    if cart_items.count(item) > 1:    # Counts the number of times the character appears in list
        if item not in cart_items_checkout:   # we need one instance of each character to be appended in the array.
            cart_items_checkout.append(item)
    else:
        cart_items_checkout.append(item)

print(cart_items_checkout)