from PIL import Image, ImageDraw, ImageFont
import os
import csv
import json
import ctypes
import argparse
from Editor import ImageEditor, reset_editor
from args import args

SPI_SETDESKWALLPAPER = 20


# Open json file containing the configuration
with open('config.json', 'r') as json_file:
    config_dict = json.load(json_file)

# Create a new object with the configurations in the json file
editor = ImageEditor(config_dict)


# Add Words
if args.add != []:
    for word in args.add:
        word = word.split(',')
        with open(editor.file_path, 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(word)

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


if args.show:
    img.show()
# Save Images
if args.save is not None:
    img.save(args.save)
if args.set:
    img.save(os.getcwd() + r'\image.png')
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.getcwd() + r'\image.png', 0)
