#  A program that calculates the highest score from a List of scores.
# Hint:
# for loops and the range() function
# range() function used to generate a range of numbers to loop through.
# https://www.w3schools.com/python/ref_func_range.asp

#Sample Data:
# Scores: 1,3,4,2
# Countries: Netherlands,Norway,England,Germany

# Split a string into a list where each word is a list item:
football_scores = input("Enter list of scores ").split(',')
countries = input("Enter list of countries").split(',')

for n in range(0, len(football_scores)):
    football_scores[n] = int(football_scores[n])
print(football_scores)



highest_score = 0
country =''

# using 'enumerate' function that takes an iterable object( List) and returns item & its index
# Built-in Functions: https://docs.python.org/3/library/functions.html

for index, score in enumerate(football_scores):
    if score > highest_score:
        highest_score = score
        country = countries[index]

print(f" {country} has highest score: {highest_score}")