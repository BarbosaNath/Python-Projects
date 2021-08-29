from PIL import Image, ImageDraw, ImageFont  # noqa
import json


def points_to_pixels(_points):
    return _points * 4/3


def draw_words(words, text_obj, color,
               font, font_size=30, img_size=[1920, 1080],
               offset=10, margin=10):
    try:
        len(offset)
    except Exception:
        offset = [offset, offset]
    try:
        len(margin)
    except Exception:
        margin = [margin, margin]

    max_len = 0
    for word in words:
        if font.getlength(word) > max_len:
            max_len = font.getlength(word)
            print(max_len)

    index = 0
    for word in words:
        text_obj.text((
            margin[0] + index*(max_len+offset[0])*1.05, offset[1] * index),
            word, fill=color, font=font)
        index += 1


# Getting Variables
with open("words.json", "r") as json_file:
    words = json.load(json_file)["words"]
# words = ['ありがとう = Obrigado', '雨 = Chuva']

split_words = []
i = j = 0
for word in words:
    if i >= 5:
        j += 1
        i = 0
    try:
        split_words[j] += f'{word}\n'
    except Exception:
        split_words.append('')
        split_words[j] += f'{word}\n'

    i += 1

mode = 'RGB'
size = (1920, 1080)
color = (20, 0, 30)


text_color = (240, 200, 20)
text_size = 30
font = ImageFont.truetype('HachiMaruPop-Regular.ttf', text_size)

# Create Image
img = Image.new(mode, size, color)

# Edit Image
text = ImageDraw.Draw(img)
draw_words(split_words, text, text_color,
           font, text_size)

# Add Words
# Save Images

img.show()
