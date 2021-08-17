import  requests
from tkinter import *
from PIL import ImageTk    # pip install 'pillow'

# Requests: HTTP for Humans
# https://docs.python-requests.org/en/master/

#HTTP Status Codes
#https://httpstatuses.com/

#Convert Lat Long to Address
#https://www.latlong.net/Show-Latitude-Longitude.html

# ---------------------------- CONSTANTS ------------------------------- #
BG = "#000000"
TEXT = "#ffffff"
FONT_NAME = "ARIAL"

def currentISSLocation():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    response.raise_for_status()

    data = response.json()
    longitude = data ["iss_position"]["longitude"]
    latitude = data ["iss_position"]["latitude"]
    canvas.itemconfig(longitude_text, text=str(longitude))
    canvas.itemconfig(latitude_text, text=str(latitude))

    iss_position  = (longitude, latitude) # creating a tupple
    print(iss_position)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("ISS Location Finder")
window.minsize(width=1280, height=704)
window.config(padx= 0, pady=20, bg=BG)

location_button = Button(text="Find ISS Location",  command=currentISSLocation, font=(FONT_NAME, 25, "bold"))
location_button.grid(column=0, row=0)


canvas = Canvas(width=1280, height=704, bg=BG)
iss_img = PhotoImage(file="iss.png")
canvas.create_image(0, 0, image=iss_img, anchor=NW)

langitude_label = canvas.create_text(200, 50, text="Longitude:", fill="white", font=(FONT_NAME, 30, "bold"))
longitude_text = canvas.create_text(400, 50, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

latitude_label = canvas.create_text(600, 50, text="Latitude:", fill="white", font=(FONT_NAME, 30, "bold"))
latitude_text = canvas.create_text(800, 50, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

canvas.grid(column=0, row=1)

# The mainloop is listening the events...
window.mainloop()

