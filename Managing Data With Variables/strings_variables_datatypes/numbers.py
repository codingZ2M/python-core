#  Number Manipulation

print('************ Rounding a number & Floor Division ***************')

print( round(23.347, 2) ) # Rounding a number to a given number of decimals.

print('*****************Using Assignment Operators & formated string **********************')

game_score =10

game_score *=2
 # game_score = game_score * 2

game_score /=3
game_score -=1
game_score +=1

is_winning = True

 # Using f-string
print(f"Your score is {game_score}, you are winning is {is_winning}")

print('*********************************************')

# Math Operations
100 + 111
100 - 111
100 * 111

# Using floor division.. Removing all the numbers after the decimal places and retuns it as int
print( type(19//3) )

print(8 ** 3) # Exponent

# PEMDAS - Execution Order
# ()
# **
# *  /
# + -
print(5 * 5 + 5 / 5 - 5 ) # Calculation goes from left to right
#  25 + 5 / 5 - 5
# 25 + 1 - 5
# 26 - 5
# 21
