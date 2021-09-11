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

def str_to_list(_str):
    if _str is not None:
        tup = _str.split('x')
        return [int(tup[0]), int(tup[1])]
    else:
        return None

def to_int(value):
    if value is not None:
        return int(value)
    return value

def to_float(value):
    if value is not None:
        return float(value)
    return value

def update_config(config_dict, config, arg):
    if arg is not None:
        config_dict[config] = arg
    return config_dict

def add_to_csv(words, path):
    for word in words:
        word = word.split(',')
        with open(path, 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(word)

def delete_from_csv(words, path):
    for word_del in words:
        csv_file = pd.read_csv(path)
        csv_file.set_index('word', inplace=True)
        csv_file = csv_file.drop(word_del)
        csv_file.to_csv(path)




# Open json file containing the configuration
with open('config.json', 'r') as json_file:
    config_dict = json.load(json_file)


# Create a new object with the configurations in the json file
editor = ImageEditor(config_dict)

##### json configuration file related
margin = str_to_list(args.margin)
margin = margin if margin is not None else [None,None]
config_dict = update_config(config_dict, 'font', args.font)
config_dict = update_config(config_dict, 'font_size', to_int(args.fontsize))

config_dict = update_config(config_dict, 'image_size', str_to_list(args.imagesize))

config_dict = update_config(config_dict, 'text_color', args.textcolor)
config_dict = update_config(config_dict, 'background_color', args.color)

config_dict = update_config(config_dict, 'offset', to_float(args.offset))

config_dict = update_config(config_dict, 'left_margin', margin[0])
config_dict = update_config(config_dict, 'top_margin',  margin[1])

config_dict = update_config(config_dict, 'furigana_ratio', to_float(args.furigana_ratio))
config_dict = update_config(config_dict, 'furigana_offset', to_float(args.furigana_offset))
config_dict = update_config(config_dict, 'furigana_color', args.furigana_color)

config_dict = update_config(config_dict, 'file_path', args.word_file)

# Save new config
with open('config.json', 'w') as json_file:
    json.dump(config_dict, json_file, indent=4)

if args.reset_config: reset_editor()

##### csv word file related
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
