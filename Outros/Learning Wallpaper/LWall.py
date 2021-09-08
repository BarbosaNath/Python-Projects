from PIL import Image, ImageDraw, ImageFont
import os
import csv
import json
import ctypes
import argparse
from args import args

SPI_SETDESKWALLPAPER = 20

# simple function to convert text points to screen pixels
def points_to_pixels(_points):
    return _points * 4/3


def draw_words(words, text_obj, color,
               font, font_size=30, img_size=[1920, 1080],
               offset=10, margin=10):
    try:
        len(offset)
    except exception:
        offset = [offset, offset]
    try:
        len(margin)
    except exception:
        margin = [margin, margin]

    max_len = 0
    for word in words:
        if font.getlength(word) > max_len:
            max_len = font.getlength(word)

    index = 0
    for word in words:
        text_obj.text((
            margin[0] + index*(offset[0]), margin[1]),
            word, fill=color, font=font)
        index += 1

# Open json file containing the words
with open('words.json', 'r') as json_file:
    words = json.load(json_file)['words']

# Add Words
if args.add != []:
    for word in args.add:
        words.append(word)
    # Save new json file
    with open('words.json', 'w') as json_file:
        json.dump({"words": words}, json_file)
# Remove words
if args.delete != []:
    for dele in args.delete:
        i = 0
        for word in words:
            if dele == word:
                del words[i]
            i += 1
    del i
    # Save new json file
    with open('words.json', 'w') as json_file:
        json.dump({"words": words}, json_file)

text_offset = args.offset.split('x')
text_offset = (int(text_offset[0]), int(text_offset[1]))

split_words = []
i = j = 0
line_break = '\n'
for word in words:
    if i >= int(args.wordsrows):
        j += 1
        i = 0
    try:
        split_words[j] += f'{word}{line_break*text_offset[1]}'
    except Exception:
        split_words.append('')
        split_words[j] += f'{word}{line_break*text_offset[1]}'

    i += 1
del i, j

mode = 'RGB'
size = args.imagesize.split('x')
size = (int(size[0]),  int(size[1]))
color = args.color


text_color = args.textcolor
text_size = int(args.fontsize)
font = ImageFont.truetype(args.font, text_size)

text_margin = args.margin.split('x')
text_margin = (int(text_margin[0]), int(text_margin[1]))

# Create Image
img = Image.new(mode, size, color)

# Edit Image
text = ImageDraw.Draw(img)
draw_words(split_words, text, text_color,
           font, text_size, offset=text_offset, margin=text_margin)

if args.show:
    img.show()
# Save Images
if args.save is not None:
    img.save(args.save)
if args.set:
    img.save(os.getcwd() + r'\image.png')
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.getcwd() + r'\image.png', 0)
