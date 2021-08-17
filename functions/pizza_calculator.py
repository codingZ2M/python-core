
''' 🍕 Pizza Calculator 🍕:
You are planning for a party, How many pizzas should you
 buy for 20, 30, 40, or more?

Slices On A Pizza:
Small (8-10″) Pizza: 6 Slices, serves 2-3 people
Medium 12" Pizza: 8 Slices, serves 3-4 people
Large 14" Pizzaa: 10 Slices, serves 3-5 people
Extra Large 16" Pizza: 12 slices, serves 5-6 people

Calculaet & order the number of Pizza's for your paty.
 '''


import math

# Function
def pizza_calculator(pizza_size , no_of_people, appetite):
    no_of_small_pizzas = 0    # Indendation
    if(pizza_size == 'S' and appetite == 'BIG EATERS'):   # Indendation
        no_of_small_pizzas = no_of_people / 2
    elif (pizza_size == 'S' and appetite == 'AVERAGE' or appetite == 'SMALL'):
        no_of_small_pizzas = no_of_people / 3

    round_up_small_pizzas = math.ceil(no_of_small_pizzas)  # Indendation
    print(f" You'll need {round_up_small_pizzas} Pizzas!")  # Indendation


pizza_size = input("Enter Pizza Size 👉 'S' | 'M' | 'L' | 'XL':").upper()
no_of_people = int(input("Enter No of People:"))
appetite = input("Choose Appetite 👉 'Big Eaters' | 'Average' | 'Small':").upper()

pizza_calculator(pizza_size, no_of_people, appetite)


