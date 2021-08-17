 # break, continue

# break: completely breaks the loop
# continue: allows us to go back to the loop or conditional expression that controls the loop


cart_items = ['2020 Y68 Smart Watch', 'Summer antiskid sports shoes',
              'Men 2021 Winter Casual Thick Waterproof Jacket',
             '2020 Y68 Smart Watch', 'Men Military Watch 50m Waterproof',
              'Men 2021 Winter Casual Thick Waterproof Jacket'
              ]
for item in cart_items:
   print(item, end=" ")

print()
print("***************************************")

index=0;
while index < len(cart_items):
     print(cart_items[index])
     index+=1;
     if(index==5):
         break   # completely breaks the loop


print('----------continue--------------')

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print (letter, end="") #  'end' param, will end the output with a <space>
                           # You can end a print statement with any character
print()


