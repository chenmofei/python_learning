from guizero import App, Text, Picture
app = App("Wanted")
app.bg = (251, 251, 208)

wanted_text = Text(app, "Wanted")
wanted_text.text_size = 50
wanted_text.font = "Times New Roman"

cat = Picture(app, image="/home/pi/Downloads/145747qqrbrxxbxgza001x.gif")

app.display()