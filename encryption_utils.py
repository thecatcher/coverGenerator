import hashlib
import random

import pymongo
from PIL import Image
from config import *

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


class Encoder(object):

    def __init__(self, raw_input_str):
        self.raw_input_str = raw_input_str

    def encode(self):
        return hashlib.md5(self.raw_input_str.encode('utf-8')).hexdigest()

    def color_generator(self, raw_digest):
        r_index = random.randint(0, 30)
        g_index = random.randint(0, 30)
        b_index = random.randint(0, 30)

        r_color = int(raw_digest[r_index:r_index + 2], base=16)
        g_color = int(raw_digest[g_index:g_index + 2], base=16)
        b_color = int(raw_digest[b_index:b_index + 2], base=16)

        return r_color, g_color, b_color


class Decoder(object):
    def __init__(self, file_path=None, color=None):
        assert file_path or color, print('please enter the color or file path')

        self.file_path = file_path
        self.color = color

    def get_color_from_file(self):
        with Image.open(self.file_path) as img:
            color = img.getpixel((COVER_WIDTH / 2, COVER_HIGHT / 2))
        return color

    def decode(self):
        if self.file_path:
            self.color = self.get_color_from_file()
        res = db[MONGO_TABLE].find_one({'color': list(self.color)})
        return res['dscp']


if __name__ == '__main__':
    # color_encoder = Encoder("还行")
    # raw_data = color_encoder.encode()
    # R, G, B = color_encoder.color_generator(raw_data)
    # print(R, G, B)

    decoder = Decoder(color=(174, 77, 9))
    print(decoder.decode())

    # res = db[MONGO_TABLE].find_one({'digest':'cfca700b9e09cf664f3ae80733274d9f'})
    # print(res)
