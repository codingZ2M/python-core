# For Loop

# Here list is an iterable and 'topic' is a variable
# How it works?: for loop allows us to iterate over anything that has a collection of items

for topic in ['Python Core', 'Web Development With Python', 'REST API with Python']:  # Fetching each element in the List
    print(topic, end=" | ")  # Indentation
print("***********************************************")


# While Loop
i =0
while i < 100: # something_is_true
    print("Do something repeatedly")
    print("Then do this")
    if(i == 5):
        break
    i+=1
#  While Loops

print()


counter = 0
while True:        # Indefinite while loop
    print(counter, end=" ")
    counter += 1
    if counter == 15:
        break

print()

"""
While loops are flexible, we can loop any number of times as it has conditional statement,
but we need to declare while loop control variable and either increment or decrement it and 
the while loop will be executed as long as the conditional expression is true.
for loop is simple, which is suitable when we know how many times the body of the loop is executed
"""
while True:
    response = input('Say Something:')
    if response == 'Bye':
        break
