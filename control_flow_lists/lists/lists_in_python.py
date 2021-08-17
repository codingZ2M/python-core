# List:
# (Data Structure) - Used to organizing and storing data
# List is an ordered sequence of objects, that can be of any type, index based
# List is used to store grouped pieces of data(ordered items), in one variable.

# List Data Type: https://docs.python.org/3/tutorial/datastructures.html

iPhone_12_pro_max = ['iPhone 12 Pro Max', 512 , ' A2410', 6.7, True ]
iPhone_12_pro = ['iPhone 12 Pro', 512 , ' A2406', 6.1, True ]
iPhone_12 = ['iPhone 12', 256 , 'A2404', 6.1, True ]

print(f"iPhone_12_pro_max specifications: {iPhone_12_pro_max}")

print(f" iPhone Model: {iPhone_12_pro_max[0]} | "
      f"Capacity: {iPhone_12_pro_max[1]} | "
      f" Model numbers {iPhone_12_pro_max[2]}"
      )
#print (iPhone_12_pro_max[7]) # Error!


print("************** iMac *********************")
iMac = [ "MacBook Air", 999.00, 13.3, "Apple M1 chip", "2TB" ]


print(f"Number of Fields {len(iMac)} ")
index = input("Enter '0' index to get the Mac Notebook Name:")
print( iMac[int (index) ] )


print("************** Using Negative Index *********************")
mac_book_property = iMac[-1]
print(mac_book_property)

print("************** Changing Property in a List (Mutable) *********************")
iMac[-1] = "3TB"
print(iMac[-1] )

print("************** Adding an Item in a List (Mutable) *********************")
iMac.append("Up to 18 hours battery life")
print(iMac[-1] )

print("************** Extending List *********************")
iMac.extend( ["720p FaceTime HD camera", "2.8 lb", "Touch ID"]  )
print(iMac)

print("************* Nested Lists ************* \n")

mac_desktop = [["iMac 24"], ["Green", "Yellow", "Purple", "Orange", "Pink" ]]

print(f"Color: {mac_desktop [1][1]}")
