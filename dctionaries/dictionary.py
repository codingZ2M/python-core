# Dictionaries, Nesting

# Dictionaries - A data structure... used to organize our data and an unordered key/value pair,
# It means, Dictionary key/value pairs are in different spots in memory
# Dict(Dictionary): A container around data

# list is an ordered data structure, can be accessed by index.
# Dictionary can hold lot of information but list can have a index and some sort of value.

soccer_players = {
    'player_id': 'PW0988',
    'player_name': 'L.Messi',
    'player_value': '$523K',
    'player_wage': '$380K',
    'player_nationality': 'Argentina',
    'player_club': 'Napoli',
    'preferred': 'Right',
    'joined': 'July 01 2013'
}

print('Wage of Soccer Player: ' + soccer_players['player_name'] + ' is: ' + soccer_players['player_wage'])

print('-------Looping through Python Dictionary--------')

for k, v in soccer_players.items():
    print(k,  v)

print()

print('-----------------Python List containing a Python Dictionary----------------------------')
# Nesting Dictionaries in Lists
soccer_players_list = [  # List containing a dictionary
    {
        'player_id': 'PW0988',
        'player_name': 'L.Messi',
        'player_value': '$523K',
        'player_wage': '$380K',
        'player_nationality': 'Argentina',
        'player_club': 'Napoli',
        'joined': 'July 01 2013',
        'preferred': ['Right']
    },

    {
        'player_id': 'PW0989',
        'player_name': 'Rick',
        'player_value': '$523K',
        'player_wage': '$380K',
        'player_nationality': 'Argentina',
        'player_club': 'Napoli',
        'joined': 'July 01 2013',
        'preferred': ['Right', 'Left']
    },
{
        'player_id': 'PW0989',
        'player_name': 'Rick',
        'player_value': '$523K',
        'player_wage': '$380K',
        'player_nationality': 'Argentina',
        'player_club': 'Napoli',
        'joined': 'July 01 2013',
        'preferred': ['Right', 'Left']
    }
]

print('Soccer Player: ' + soccer_players_list[0]['player_name'] + ' prefers ' + soccer_players_list[0]['preferred'][0])

soccer_players_list[0]['preferred'][0] = 'Left'

print('Soccer Player: ' + soccer_players_list[1]['player_name'] + ' prefers ' + soccer_players_list[1]['preferred'][1])
print()


print('-----------------Nesting Dictionary in a Dictionary-------------------------')
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log["France"]["cities_visited"][1])