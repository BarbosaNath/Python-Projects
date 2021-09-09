from PIL import Image, ImageDraw, ImageFont
import os
import csv
import json
import ctypes
import argparse
from args import args

SPI_SETDESKWALLPAPER = 20

# Open json file containing the configuration
# Open csv file containing the words

# Add Words
if args.add != []:
    pass

# Remove words
if args.delete != []:
    pass

# show image
if args.show: pass
# Save Images
if args.save is not None: pass
# Set wallpaper
if args.set:
    img.save(os.getcwd() + r'\image.png')
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.getcwd() + r'\image.png', 0)
