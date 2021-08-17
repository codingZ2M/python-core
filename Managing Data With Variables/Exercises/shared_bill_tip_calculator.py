# Shared Bill Tip Calculator:

# Service Types & Tips:
# restaurants = 10.00
# food_delivery = 12.00
# hairstylists = 10.00
# taxi_limo_drivers = 15.00

tip_in_percentage = 0.00

print("Enter Your Bill Amount, 'Service Type', & No Of Persons!")

total_bill_amount = float(input("Enter Total Bill Amount ($): "))

service_type = input("Enter  'Service Type':")

if service_type == 'restaurants':
    tip_in_percentage = 10.00
elif service_type == 'food_delivery':
    tip_in_percentage = 12.00
elif service_type == 'hairstylists':
    tip_in_percentage = 10.00
elif service_type == 'taxi_limo_drivers':
    tip_in_percentage = 15.00
else:
    tip_in_percentage = 09.00

no_of_people = int(input("How many people are going to split the bill?"))

total_tip_amount = total_bill_amount * (tip_in_percentage /100)
print(f"Total Tip Amount:  {total_tip_amount}" )

total_bill = total_bill_amount + total_tip_amount
print(f"Total Bill: {total_bill}" )

bill_amount_per_person = total_bill / no_of_people
print("Bill Amount / Person: " + str(bill_amount_per_person) )

#Round the result to 2 decimal places.
final_amount_per_person = round(bill_amount_per_person, 2)

print(f" Final Amount / Person After Rounding: ${final_amount_per_person}")