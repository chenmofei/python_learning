# Imports
from guizero import App, Text, TextBox, Drawing, PushButton, Combo, Slider

# Functions
def draw_meme():
    meme.clear()
    meme.image(0, 0, "/home/pi/Downloads/145747qqrbrxxbxgza001x.gif")
    meme.text(
        20, 20, top_text.value,
        color="orange",
        size=40,
        font="courier")
    meme.text(
        20, 80, bottom_text.value,
        color=color.value,
        size=size.value,
        font=font.value)


# App
app = App("Meme Generator")

# widgets
title = Text(app, "meme generator")

top_text = TextBox(app, "top_text", command=draw_meme)
bottom_text = TextBox(app, "bottom_text", command=draw_meme)
font = Combo(app,
    options=["times new roman", "verdana", "courier", "impact"],
    command=draw_meme,
    selected="times new roman")
color = Combo(app,
    options=["black", "white", "red", "green", "blue", "orange"],
    command=draw_meme,
    selected="blue")
size = Slider(app,
    start=20,
    end=50,
    command=draw_meme)

meme = Drawing(app, width="fill", height="fill")
draw_meme()
# button = PushButton(app, draw_meme, "Generator")

# Display
app.display()