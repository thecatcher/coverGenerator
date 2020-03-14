from PIL import Image
from config import *
import datetime
from os import path
import pymongo

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


class CoverGenerator(object):
    def __init__(self, color):
        self.color = color


    def generate(self):
        return Image.new('RGB', (COVER_WIDTH, COVER_HIGHT), self.color)

    def save(self, img):
        now = datetime.datetime.now()
        file_name_prefix = ''.join(list(map(str, (now.year, now.month, now.day, now.hour, now.minute, now.second))))
        file_name = file_name_prefix + '.jpg'

        file_full_path = path.join(FILE_PATH, file_name)

        with open(file_full_path, 'w+') as f_img:
            img.save(f_img)
        if path.exists(file_full_path):
            print(f"file {file_name}  is saved to disk successful")
            return file_full_path
        return None

    def save_to_mongo(self, digest, color, feeling, file_path):
        res = {
            'digest': digest,
            'color': color,
            'dscp': feeling,
            'path': file_path
        }

        if db[MONGO_TABLE].insert_one(res):
            print('cover save to database successful!')
            return True
        return False


if __name__ == '__main__':
    generator = CoverGenerator(240, 240, 240)
    img = generator.generate()
    generator.save(img)
