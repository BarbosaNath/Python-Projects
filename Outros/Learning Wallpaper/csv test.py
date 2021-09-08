from PIL import Image, ImageDraw, ImageFont
import csv

img  = Image.new('RGB', (500,500), '#400')
text = ImageDraw.Draw(img)
font = ImageFont.truetype('HachiMaruPop-Regular.ttf', 30)

with open('words.txt',encoding='utf8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

text.text((20,20), 'teste', fill='#fff',font=font)
img.show()
