# Python Random Module:
# https://www.w3schools.com/python/module_random.asp
# https://www.askpython.com/

# Module: The large piece of source code can be split into individual modules
# (pyhon source files) and, each module is responsible for different functionalities of your application.
# Example: Your car engine is made up of several components each component is responsible for
# separate funtionality.

import random # importing random module
import mac_desktop.iMac_24 as iMac_24_data, mac_desktop.iMac_27 as iMac_27_data

print('Generating a random integer...')
random_number = random.randint(1, 1000)
print(f" Generatedour Random Number (Integer) IS: {random_number}")

print()
print('--------- iMac 24" Details ---------------')
print(f" Product Name: {iMac_24_data.product_name}"
      f" Price: {iMac_24_data.price}"
      f"Display: {iMac_24_data.display}"
      f"Storage: {iMac_24_data.storage}"
      f"Camera: {iMac_24_data.camera}"
      )

print()
print('--------- iMac 27" Details ---------------')
print(f" Product Name: {iMac_27_data.product_name}"
      f" Price: {iMac_27_data.price}"
      f"Display: {iMac_27_data.display}"
      f"Storage: {iMac_27_data.storage}"
      f"Camera: {iMac_27_data.camera}"
      )
