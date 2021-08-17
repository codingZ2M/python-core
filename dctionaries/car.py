cars_specs_list = [
    {
        'Name': 'Tesla Model S',
        'Wheelbase': '116.5 in ',
        'Length': '195.9 in',
        'Width': '77.3 in',
        'Height': '56.5 in',
        'Power': '778 HP',
        'Torque': '487 lb/ft'

    },
    {
        'Name': 'Polaris Slingshot',
        'Wheelbase': '105 in',
        'Length': '149.6 in',
        'Width': '77.6 in',
        'Height': '51.9 in',
        'Power': '203 HP',
        'Torque': '166 lb/ft'

    },
    {
        'Name': 'Chevrolet Corvette (C8)',
        'Wheelbase': '107.2 in',
        'Length': '182.3 in',
        'Width': '78.1 in',
        'Height': '48.6 in',
        'Power': '495 HP',
        'Torque': '465 lb/ft '
    }
]

print("Welcome to the 2021 car expo! Due to a lack of enthusiasm, we are only able to showcase three types of cars!")
print(" ::::::: List Of Cars ::::::::")
for index in range(0, len(cars_specs_list) ):
    print(cars_specs_list[index]['Name'])

car_selected = True
while car_selected:
    car = input("Choose which car you would like to view the specs:\n")
    if car == '':
        car_selected = False

    for index in range(0, len(cars_specs_list)):
            if car == cars_specs_list[index]['Name']:
                print("Name: " + cars_specs_list[index]['Name'])
                print("Wheelbase: " + cars_specs_list[index]['Wheelbase'])
                print("Length: " + cars_specs_list[index]['Length'])
                print("Width: " + cars_specs_list[index]['Width'])
                print("Height: " + cars_specs_list[index]['Height'])
                print("Power:" + cars_specs_list[index]['Power'])
                print("Torque: " + cars_specs_list[index]['Torque'])



