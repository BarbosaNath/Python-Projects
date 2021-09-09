from PIL import Image, ImageDraw, ImageFont
import csv
import json

class ImageEditor:
    """Class containing the image manipulation part of LWall."""

    def __init__(self,
        text_color='#fff',
        background_color='#000', file_path='words.csv',
        furigana_color='#555', image_size=(1920, 1080),
        top_margin=20, left_margin=20,
        font_size=30, furigana_ratio=1.5,
        furigana_offset=3, offset=80, font='HachiMaruPop-Regular.ttf'
    ):
        self.text_color       = text_color
        self.background_color = background_color
        self.furigana_color   = furigana_color

        self.image_size = image_size
        self.file_path  = file_path

        self.top_margin  = top_margin
        self.left_margin = left_margin

        self.font_size = font_size

        self.furigana_ratio  = furigana_ratio
        self.furigana_offset = furigana_offset
        self.furigana_size   = self.font_size/self.furigana_ratio

        self.offset = offset

        self.line_space = (self.font_size
                        +  self.furigana_size
                        +  self.top_margin)

        self.font          = ImageFont.truetype(font, self.font_size)
        self.furigana_font = ImageFont.truetype(font, int(self.furigana_size))


        self.longest_word    = 0
        self.longest_meaning = 0
        with open(file_path, encoding='utf8') as csv_file:
            self.csv_reader = csv.DictReader(csv_file)
            for row in self.csv_reader:
                self.longest_word = self.font.getlength(row['word']) if self.font.getlength(row['word']) > self.longest_word else self.longest_word
                self.longest_meaning = self.font.getlength(row['meaning']) if self.font.getlength(row['meaning']) > self.longest_meaning else self.longest_meaning

        self.column_space = (self.longest_word
                          +  self.longest_meaning
                          +  self.offset*2)

        self.image  = Image.new('RGB', self.image_size, self.background_color)
        self.text = ImageDraw.Draw(self.image)


    def draw(self):
        i = 1
        j = 0
        with open(self.file_path, encoding='utf8') as csv_file:
            self.csv_reader = csv.DictReader(csv_file)
            for row in self.csv_reader:
                # get atributes from dict
                word = row['word']
                mean = row['meaning']
                furi = row['furigana']
                mean_len = self.font.getlength(mean)

                # position of the japanese word
                pos = (self.left_margin+self.column_space*j, (self.line_space-self.font_size)) if i==1 else (self.left_margin+self.column_space*j,((self.line_space+20)*i)-self.font_size-self.top_margin/2-10)
                # position of the furigana centered on the japanese word
                furi_pos = (-(self.furigana_font.getlength(furi)/2-
                           self.left_margin-self.font.getlength(word)/2) + self.column_space*j,
                           pos[1]-self.furigana_offset-self.furigana_size)
                # position of the meaning text
                mean_pos = (pos[0]+self.longest_word+self.longest_meaning-mean_len + self.offset,
                            pos[1])

                # Draw word and furigana
                self.text.text(pos, word, fill=self.text_color,font=self.font)
                self.text.text(furi_pos, furi if furi is not None else '', fill=self.furigana_color,font=self.furigana_font)

                # Draw the meaning of japanese word
                self.text.text((self.longest_word/2+self.offset/2+self.font.getlength('=')/2+self.longest_meaning/2+self.column_space*j,pos[1]), '=' if mean_len is not None else '', fill=self.text_color, font=self.font)
                self.text.text(mean_pos, mean if mean is not None else '', fill=self.text_color, font=self.font)
                i += 1
                # print(f'{pos} | {screen_size}')
                if pos[1] >= self.image_size[1] - self.line_space - 10:
                    j+=1
                    i=1
                if pos[0] >= self.image_size[0]:
                    break
                del pos, furi_pos, mean_pos
            del i, j

        self.image.show()

ie = ImageEditor()
ie.draw()
