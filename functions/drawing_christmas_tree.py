picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '*'
empty = ' '


def create_tree():
    for row in picture:
        for pixel in row:
            if (pixel):  # Even brackets are not necessary in Python
                print(fill, end="")
            else:
                print(empty, end="")
        print('')  # need a new line after every row


# In the above line 36, the print() is a part of outer for loop, because of Indentation

# Reusing the sayHello() function over and over
create_tree()
print()
create_tree()
print()
create_tree()
print()
