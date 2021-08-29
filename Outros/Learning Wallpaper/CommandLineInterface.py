import os
import sys
import json
# import main

APP_NAME = 'Learning Wallpaper CLI'
SYSTEM = 'win' if sys.platform.startswith('win') else 'unix'


def clear_screen():
    if SYSTEM == 'win':
        os.system('cls')
    else:
        os.system('clear')


# <> make_box()
def make_box(name=APP_NAME, options=[''],
             corner='x', horizontal='-', vertical='|'):
    bigest_option = ''
    for option in options:
        if len(bigest_option) < len(option):
            bigest_option = option
    if len(bigest_option) < len(name):
        bigest_option = name

    len_op = len(str(len(options)))

    offset_double = (len(bigest_option) - 14)
    offset = int(offset_double/2)

    lines = [f'{corner}{horizontal*offset} {name} {horizontal*offset}{corner}']

    space = ' '
    i = 1
    for option in options:
        lenght = len(lines[0])
        lenght -= len(option) + 12 - len_op
        lines.append(
            f'{vertical}{space*(len_op+1-len(str(i)))}{i} {horizontal} {option} {space*lenght} {vertical}')
        i += 1
    lines.append(f'{corner}{horizontal*(len(lines[0])-2)}{corner}')

    for line in lines:
        print(line)
# </>


# Main loop
running = True
while running:

    # Get json

    print(os.getcwd(), end='\n\n')
    with open('words.json', 'r') as json_file:
        words = json.load(json_file)['words']
    make_box(name='Words in words.json', options=words)

    input()

    clear_screen()

    # Get Wallpaper
    # Set Wallpaper
