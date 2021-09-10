from PIL import Image, ImageDraw, ImageFont
import os
import csv
import json
import ctypes
import pandas as pd
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
    for word_del in args.delete:
        csv_file = pd.read_csv(editor.file_path)
        csv_file.get_index('word', inplace(True))
        csv_file.drop(word_del)
        csv_file.to_csv(editor.file_path)

# recreated the editor so any new config is updated
editor = ImageEditor(config_dict)

if args.show:
    editor.draw().show()
# Save Images
if args.save is not None:
    editor.draw().save(args.save)
if args.set:
    editor.draw().save(os.getcwd() + r'\image.png')
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.getcwd() + r'\image.png', 0)
