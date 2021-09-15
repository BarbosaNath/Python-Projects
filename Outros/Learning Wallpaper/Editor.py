from PIL import Image, ImageDraw, ImageFont
import csv
import json

class ImageEditor:
    """Class containing the image
       manipulation part of LWall."""

    def __init__(self, config_dict):
        self.text_color       = config_dict['text_color']
        self.background_color = config_dict['background_color']
        self.furigana_color   = config_dict['furigana_color']

        self.image_size = config_dict['image_size']
        self.file_path  = config_dict['file_path']

        self.top_margin  = config_dict['top_margin']
        self.left_margin = config_dict['left_margin']

        self.font_size = config_dict['font_size']

        self.furigana_ratio  = config_dict['furigana_ratio']
        self.furigana_offset = config_dict['furigana_offset']
        self.furigana_size   = self.font_size/self.furigana_ratio

        self.offset = config_dict['offset']

        self.line_space = (self.font_size
                        +  self.furigana_size
                        +  self.top_margin)

        self.font          = ImageFont.truetype(config_dict['font'], self.font_size)
        self.furigana_font = ImageFont.truetype(config_dict['font'], int(self.furigana_size))


        self.longest_word    = 0
        self.longest_meaning = 0
        with open(self.file_path, encoding='utf8') as csv_file:
            self.csv_reader = csv.DictReader(csv_file)
            for row in self.csv_reader:
                if isinstance(row['word'], str):
                    self.longest_word = self.font.getlength(row['word']) if self.font.getlength(row['word']) > self.longest_word else self.longest_word
                if isinstance(row['meaning'], str):
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
                word = row['word'] if row['word'] is not None else ''
                mean = row['meaning'] if row['meaning'] is not None else ''
                furi = row['furigana'] if row['furigana'] is not None else ''
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

                # position of equals sign
                equal_pos = (self.longest_word/2+self.offset/2-self.font.getlength('=')/2 +self.longest_meaning/2+self.column_space*j,pos[1])

                # Draw word and furigana
                self.text.text(pos, word, fill=self.text_color,font=self.font)
                self.text.text(furi_pos, furi if furi is not None else '', fill=self.furigana_color,font=self.furigana_font)

                # Draw the meaning of japanese word
                # self.text.text(equal_pos, '=' if mean_len != 0 else '', fill=self.text_color, font=self.font)
                self.text.text(mean_pos, mean if mean is not None else '', fill=self.text_color, font=self.font)
                i += 1
                # print(f'{pos} | {screen_size}')
                if pos[1] >= self.image_size[1] - self.line_space - self.font_size*1.4:
                    j+=1
                    i=1
                if pos[0] >= self.image_size[0]:
                    break
                del pos, furi_pos, mean_pos
            del i, j

        return self.image


def reset_editor():
    with open('config.json', 'r') as json_file:
        config_dict = json.load(json_file)

    config_dict["text_color"]       = "#fff"
    config_dict["background_color"] = "#000"
    config_dict["furigana_color"]   = "#555"

    config_dict["file_path"]  = "words.csv"

    config_dict["image_size"] = [1920, 1080]

    config_dict["top_margin"]  = 20
    config_dict["left_margin"] = 20

    config_dict["font_size"] = 50

    config_dict["furigana_ratio"]  = 1.5
    config_dict["furigana_offset"] = 3

    config_dict["offset"] = 80
    config_dict["font"]   = "HachiMaruPop-Regular.ttf"

    with open('config.json', 'w') as json_file:
        json.dump(config_dict, json_file, indent=4)
