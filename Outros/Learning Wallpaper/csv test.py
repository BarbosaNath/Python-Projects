from PIL import Image, ImageDraw, ImageFont
import csv

class ImageEditor:
    """Class containing the image manipulation part of LWall."""

    def __init__(self, arg):
        self.arg = arg


# <> Variables
color       = '#fff'
furi_color  = '#b77'
bg_color    = '#400'

top_margin  = 10
left_margin = 20

font_size   = 30

screen_size = (1600,900)

furi_ratio  = 1.5
furi_offset = 3
furi_size   = int(font_size/furi_ratio)

offset = 80
line_space  = font_size + furi_size + top_margin
# </>

img  = Image.new('RGB', screen_size, bg_color)
text = ImageDraw.Draw(img)
font = ImageFont.truetype('HachiMaruPop-Regular.ttf', font_size)
font_furi = ImageFont.truetype('HachiMaruPop-Regular.ttf', furi_size)

longest_word = 0
longest_mean = 0
with open('words.txt',encoding='utf8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # get longest word and meaning
    for row in csv_reader:
        longest_word = font.getlength(row['word']) \
                    if font.getlength(row['word']) > longest_word \
                    else longest_word
        longest_mean = font.getlength(row['meaning']) \
                    if font.getlength(row['meaning']) > longest_mean \
                    else longest_mean

col_space = longest_word + longest_mean + offset*2
# for some reason I had to split the code in to cause the second loop wasnt running
with open('words.txt',encoding='utf8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    i = 1
    j = 0
    for row in csv_reader:
        # get atributes from dict
        word = row['word']
        mean = row['meaning']
        furi = row['furigana']
        mean_len = font.getlength(mean)

        # position of the japanese word
        pos = (left_margin+(col_space)*j, (line_space-font_size)) if i==1 else (left_margin+ (col_space*j),((line_space+20)*i)-font_size-top_margin/2-10 )
        # position of the furigana centered on the japanese word
        furi_pos = (-(font_furi.getlength(furi)/2-
                   left_margin-font.getlength(word)/2) + col_space*j,
                   pos[1]-furi_offset-furi_size)
        # position of the meaning text
        mean_pos = (pos[0]+longest_word+ longest_mean-mean_len + offset,
                    pos[1])

        # Draw word and furigana
        text.text(pos, word, fill=color,font=font)
        text.text(furi_pos, furi if furi is not None else '', fill=furi_color,font=font_furi)

        # Draw the meaning of japanese word
        text.text((longest_word/2+offset/2+font.getlength('=')/2+longest_mean/2+col_space*j,pos[1]), '=' if mean_len is not None else '', fill=color, font=font)
        text.text(mean_pos, mean if mean is not None else '', fill=color, font=font)
        i += 1
        # print(f'{pos} | {screen_size}')
        if pos[1] >= screen_size[1] - line_space - 10:
            j+=1
            i=1
        if pos[0] >= screen_size[0]:
            break
        del pos, furi_pos, mean_pos
    del i, j

img.show()
