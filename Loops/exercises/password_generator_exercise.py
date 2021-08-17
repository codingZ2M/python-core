# STRONG Random Password Generator
# Hint:
# for loops and the range() function
# range() function used to generate a range of numbers to loop through.
# https://www.w3schools.com/python/ref_func_range.asp

import random
lower_case_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
upper_case_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['$', '#', '%', '!', '*', '+', '&']
ambiguous_chars = [ '{', '}', '[', ']',  '~', '<', '>', '~', '(', ')', '`' ]


print("STRONG Random Password Generator")
no_of_lower_case_chars = int(input("How many lower case letters would you like in your password?\n"))
no_of_upper_case_chars = int(input("How many upper case letters would you like in your password?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_ambiguous_chars = int(input("How many ambiguous chars would you like?\n"))

password_list = []

seq_lower_case_chars = range(1, no_of_lower_case_chars + 1 )  # Creating a sequence of numbers..
for char in seq_lower_case_chars:
  password_list.append(random.choice(lower_case_chars)) # returns a randomly selected element from the specified sequence.

seq_upper_case_chars = range(1, no_of_upper_case_chars + 1)  # Creating a sequence of numbers..
for char in seq_upper_case_chars:
  password_list.append(random.choice(upper_case_chars))

seq_numbers = range(1, no_of_numbers + 1)  # Creating a sequence of numbers..
for char in seq_numbers:
  password_list.append(random.choice(numbers))

seq_symbols = range(1, no_of_symbols + 1)  # Creating a sequence of numbers..
for char in seq_symbols:
  password_list.append(random.choice(symbols))

seq_ambiguous_chars = range(1, no_of_ambiguous_chars + 1)  # Creating a sequence of numbers..
for char in seq_ambiguous_chars:
  password_list.append(random.choice(ambiguous_chars))

print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:    # 'FOR LOOP' with Lists
  password += char

print(f"Your strong password is: {password}")