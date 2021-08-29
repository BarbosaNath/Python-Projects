import argparse

# Add word
# Set Wallpaper
# Delete a word
# Set size
# Set font
# Set font size

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add',
                    help='adds word to json/wallpaper',
                    required=False,
                    action='append')
parser.add_argument('-s', '--set',
                    help='set the wallpaper',
                    required=False,
                    action='store_true')
args = parser.parse_args()

print(args)
