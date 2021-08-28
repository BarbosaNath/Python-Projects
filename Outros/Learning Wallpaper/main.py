import tkinter as tk  # noqa
from tkinter import Tk  # noqa
from PIL import Image, ImageDraw, ImageFont  # noqa


def points_to_pixels(points):
    return points * 4/3


# Getting Variables
words = ['ありがとう', '雨']

mode = 'RGB'
size = (1920, 1080)
color = (20, 0, 30)

text_color = (240, 200, 20)
text_size = 65
font = ImageFont.truetype('HachiMaruPop-Regular.ttf', text_size)

ui_size = (300, 200)
tk_size = f'{ui_size[0]}x{ui_size[1]}'

# Create Image
img = Image.new(mode, size, color)

# Edit Image
text = ImageDraw.Draw(img)
text.text(
    (
        size[0]/2 - font.getlength(words[0])/2,
        size[1]/2 - points_to_pixels(text_size)/2
    ),
    words[0] + words[1],
    fill=text_color,
    font=font
)

# Add Words
# Save Images

img.show()

# Graphical User Interface
# root = Tk()
# root.geometry(tk_size)
#
# text = tk.Text(root, height=2, width=16, font=("Arial", 24))
# text.grid(columnspan=5)
#
# root.mainloop()
