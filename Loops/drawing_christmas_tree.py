# Drawing Christmas Tree!

image = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill = '*'
empty = ' '

for row in image:
  for pixel in row:
    if (pixel):     # Even brackets are not necessary in Python
      print(fill, end="")  #  'end' param, will end the output with a <space>
    else:                    # You can end a print statement with any character
      print(empty, end ="")
  print('') # need a new line after every row