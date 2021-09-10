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

def add_to_csv(words, path):
    for word in words:
        word = word.split(',')
        with open(path, 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(word)

def delete_from_csv(words, path):
    for word_del in words:
        csv_file = pd.read_csv(path)
        csv_file.get_index('word', inplace(True))
        csv_file.drop(word_del)
        csv_file.to_csv(path)


# Open json file containing the configuration
with open('config.json', 'r') as json_file:
    config_dict = json.load(json_file)

# Create a new object with the configurations in the json file
editor = ImageEditor(config_dict)


# Add Words
if args.add != []: add_to_csv(args.add, editor.file_path)
# Remove words
if args.delete != []: delete_from_csv(args.delete, editor.file_path)


# recreated the editor so any new config or words are updated
editor = ImageEditor(config_dict)


# open the image on your default image viewer
if args.show:
    editor.draw().show()
# Save Images
if args.save is not None:
    editor.draw().save(args.save)
# set the image made as your new wallpaper
if args.set:
    editor.draw().save(os.getcwd() + r'\image.png')
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.getcwd() + r'\image.png', 0)
