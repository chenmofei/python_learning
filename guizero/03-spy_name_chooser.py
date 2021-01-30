# Imports
from guizero import App, Text, PushButton
from random import choice

# Functions
def choose_name():
#    print("Button was pressed")
    first_name = ["Barbara", "Woody", "Tiberius", "Smokey", "Jennifer", "Ruby"]
    last_name = ["Spindleshanks", "Mysterioso", "Dungeon", "Catseye", "Darkmeyer", "Flamingobreath"]
    spy_name = choice(first_name) + " " + choice(last_name)
    # print(spy_name)
    name.value = spy_name

# App
app = App("Top Secret")
app.bg = (231, 166, 153)

# widgets
title = Text(app, text="Push the red button to find out your spy name")
button = PushButton(app, choose_name, text="Tell me!!")
button.bg = (229, 55, 18)
button.text_size = 30
name = Text(app, text="")

# Display
app.display()