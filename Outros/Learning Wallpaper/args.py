import argparse

# Add word
# Set Wallpaper
# Delete a word
# Set size
# Set font
# Set font size
# Set background color
# Set text color


parser = argparse.ArgumentParser()

# --add
parser.add_argument('-a', '--add',
                    help='adds word to json/wallpaper',
                    default=[],
                    action='append')
# --set
parser.add_argument('-s', '--set',
                    help='saves the image and set the new wallpaper',
                    action='store_true')
# --save
parser.add_argument('--save',
                    help='saves the image in the provided path')
# --delete
parser.add_argument('-d', '--delete',
                    help='deletes the specified word/s',
                    default=[],
                    action='append')
# --imagesize
parser.add_argument('-i', '--imagesize',
                    help='defines the size of the output image (must be formated as the default: 1920x1080)')
# --font
parser.add_argument('-f', '--font',
                    help='defines the font to be used in the wallpaper')
# --fontsize
parser.add_argument('--fontsize',
                    help='defines the font size in points (default: 50)')
# --color
parser.add_argument('-c', '--color',
                    help='set background color in hexadecimal')
# --textcolor
parser.add_argument('-t', '--textcolor',
                    help='set text color in hexadecimal')
# --offset
parser.add_argument('-o', '--offset',
                    help='sets the offset between words (default: 80)')
# --margin
parser.add_argument('-m', '--margin',
                    help='sets the margin between the border of the image and the words (must be formated as the default: 30x20)',
                    default='30x20')
# --show
parser.add_argument('--show',
                    help='opens result image after the program runs',
                    action='store_true')

parser.add_argument('--furigana_color',
                    help='set furigana color to the parsed hexadecimal value')

parser.add_argument('--furigana_ratio',
                    help='set the how much smaller the furigana should be compared to the normal text (furigana size = text size / furigana ratio)')
parser.add_argument('--furigana_offset',
                    help='how far away from the text should the furigana be')
parser.add_argument('--word_file',
                    help='where the csv file containing the words should be')

parser.add_argument('-r','--reset_config', help='reset config file', action='store_true')

args = parser.parse_args()
