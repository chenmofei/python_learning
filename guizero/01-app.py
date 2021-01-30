from tkinter import Message
from guizero import App, Text
app = App(title="Hello, world")
Message = Text(app, text="Welcome to my test app.")
app.display()