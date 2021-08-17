#  A program that calculates the your average purchase price from a List of prices.

purchase_prices = input("Give a list of your purchase prices ").split(',')
print(purchase_prices)

for index in range(0, len(purchase_prices)):
    purchase_prices[index] = float(purchase_prices[index])

total_price = 0.00
for price in purchase_prices:
    total_price += price
print(f" Total Price: = {total_price}")

number_of_purchases = 0
for index in purchase_prices:
    number_of_purchases += 1
print(f" Number of purchase: = {number_of_purchases}")

average_purchase_price = round(total_price / number_of_purchases)
print(f"Your Average Purchase Price is: {average_purchase_price}")