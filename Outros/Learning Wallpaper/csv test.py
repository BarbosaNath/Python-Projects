from PIL import Image, ImageDraw, ImageFont
import csv

img  = Image.new('RGB', (500,500), '#400')
text = ImageDraw.Draw(img)
font = ImageFont.truetype('HachiMaruPop-Regular.ttf', 30)
furi = ImageFont.truetype('HachiMaruPop-Regular.ttf', 15)

with open('words.txt',encoding='utf8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # get longest word and meaning
    longest_word = 0
    longest_mean = 0
    for row in csv_reader:
        longest_word = font.getlength(row['word']) \
                    if font.getlength(row['word']) > longest_word \
                    else longest_word
        longest_mean = font.getlength(row['meaning']) \
                    if font.getlength(row['meaning']) > longest_mean \
                    else longest_mean
# for some reason I had to split the code in to cause the second loop wasnt running
with open('words.txt',encoding='utf8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    i = 1
    print('teste')
    for row in csv_reader:
        print(row)
        # position of the japanese word
        pos = (20,70*i)
        # position of the furigana centered on the japanese word
        furi_pos = (-(furi.getlength(row['furigana'])/2-
                   20-font.getlength(row[  'word'  ])/2),
                   pos[1]-15)
        # position of the meaning text
        mean_pos = (pos[0]+font.getlength(row['word']),
                    pos[1])

        # Draw word and furigana
        text.text(pos, row['word'], fill='#fff',font=font)
        text.text(furi_pos, row['furigana']if row['furigana'] is not None else '', fill='#fff',font=furi)

        # Draw the meaning of japanese word
        text.text(mean_pos, (' = '+row['meaning']) if row['meaning'] is not None else '', fill='#fff', font=font)
        i += 1
        del pos, furi_pos
    del i

img.show()
