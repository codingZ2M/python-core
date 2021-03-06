from PIL import Image
img = Image.open('images/road_bike.jpg')
img.show()

sort_by = ''
price_range = ''
general_size = ''
color =''
frame_type = ''

print("π΄ Select Your Bike! π΄")
sort_by = input("Select Sort By π 'High' | 'Low' | 'Best Sellers':").upper()

if sort_by == "BEST SELLERS":
    price_range = input("You have selected 'Best Sellers'"
                  " Select Price Range π '$1200.00 - $1800.00'"
                  " '$700.00 - $1200.00'"
                  " '$300.00 - $700.00':").upper()

    if price_range == "$1200.00 - $1800.00" or price_range == "$700.00 - $1200.00" or price_range == "$300.00 - $700.00":
        general_size = input("5 models in this price range in 'M' & 'L' sizes. Which size do you wantβ").upper()

        if general_size == "L":
            color = input("Three colors are available for 'L' size π 'Blue' | 'Red' | 'Silver':").upper()
            if color == 'BLUE' or color == 'RED' or color == 'SILVER':
                frame_type = input("Select Frame Type for 'L' size π 'Steel Frame':").lower()
            else:
                print("Choose colors for 'L' size π 'Blue' | 'Red' | 'Silver' Try Again!")
        elif general_size == "M":
            color = input("Three colors are available for 'M' size π 'Pink' | 'Green | 'Silver':").upper()
            frame_type = input("Select Frame Type for 'L' size π 'Aluminium Frame':").upper()
        else:
            print("Choose either π 'L' or 'M' size. Try Again!")

    else:
        print("Select price range π '$1200.00 - $1800.00'"
                  " '$700.00 - $1200.00' "
                  " '$300.00 - $700.00'. Try Again!.")

else:
    print("Choose π 'High' | 'Low' | 'Best Sellers' Try Again!" )


print(f" βΊ Bike Selected: \n"
            f" Sort By: {sort_by} \n"
            f"Price: {price_range} \n"
            f"General Size: {general_size} \n"
            f"Frame Type: {frame_type} \n"
            f"Color: {color} \n")