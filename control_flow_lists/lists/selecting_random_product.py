# Write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

# Split a string into separate components based on some sort of divider.
#  Convert String to List in Python: https://www.askpython.com/python/string/convert-string-to-list-in-python

import random # importing random module
mac_desktops = input("Enter iMac Details, seperated by a comma. ")
# Sample Data: iMac 24,iMac 27,Mac Pro,Mac mini

desktops = mac_desktops.split(",") # Returning a list of words (strings)
print(desktops)

mac_desktop_choice = random.randint(0, len(desktops) - 1)

print( f" Do you want the specifications for {desktops[mac_desktop_choice]}" )

