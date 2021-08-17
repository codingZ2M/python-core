################### Namespaces: Local vs. Global Scope ####################
'''
You have a Television, who can access its internal circuits and do some repairs?
    ... TV Technician.
But anybody can control the color, brightness, contrast of the TV.. right?
'''


# Sample Data:
#      "Guest Suite": 280.00,
#     "Garden Studio": 120.00,
#     "Private Room": 78.00,
#     "Charming Suite": 80.00,
#     "Charming Garden Apartment": 150.00,

holiday_rentals = [    # Global Scope
    {
        "rental": "Guest Suite",
        "amenities": ['Self check-in', 'Private hot tub', 'Travel cot', 'Free on-street parking',
                      'Washing machine', 'Wifi' , 'tv', 'Room-darkening shades', 'Coffee maker',
                      'Pets allowed', 'Travel Cot', 'Iron', 'Dryer'],
        "reviews": "5 Star"
    },
    {
        "rental": "Garden Studio",
        "amenities": ['Self check-in', 'Private hot tub', 'Washing machine', 'Wifi', 'tv',
                      'Room-darkening shades', 'Coffee maker', 'Pets allowed', 'Iron', 'Dryer'],
        "reviews": "4.8 Star"
    }

]

rentals = {}   # Dict  # Global Scope

def add_holiday_rentals(rental_name, amenities_list, rating ):
    rentals["rental"] = rental_name
    rentals["amenities"] = amenities_list
    rentals["reviews"] = rating
    return rentals


def get_rentals():
    # Local Scope: 'index' variable
     for index in range(0, len(holiday_rentals) ):
            print(holiday_rentals[index])



rental_name = input("Enter Rental:")
amenities_list = input("Enter Amenities:").split(',')
rating = input("Enter Reviews:")

rentals = add_holiday_rentals(rental_name, amenities_list, rating)
holiday_rentals.append(rentals)

get_rentals()



'''
Private Room
Self check-in, Private hot tub, Washing machine, Wifi, tv, Room-darkening shades, Coffee maker, Travel cot, Iron, Dryer

Charming Suite
Self check-in, Private hot tub, Washing machine, Wifi, tv, Room-darkening shades, Coffee maker, Iron, Dryer

Charming Garden Apartment
Self check-in, Private hot tub, Washing machine, Wifi, tv, Room-darkening shades, Coffee maker, Pets allowed, Iron, Dryer
'''