import hashlib
import random


class Encoder(object):

    def __init__(self, raw_input_str):
        self.raw_input_str = raw_input_str

    def encode(self):
        return hashlib.md5(self.raw_input_str.encode('utf-8')).hexdigest()

    def color_generator(self, raw_digest):
        r_index = random.randint(0, 30)
        g_index = random.randint(0, 30)
        b_index = random.randint(0, 30)

        r_color = int(raw_digest[r_index:r_index + 2],base=16)
        g_color = int(raw_digest[g_index:g_index + 2],base=16)
        b_color = int(raw_digest[b_index:b_index + 2],base=16)


        return r_color, g_color, b_color


class Decoder(object):
    pass


if __name__ == '__main__':

    color_encoder = Encoder("还行")
    raw_data = color_encoder.encode()
    R, G, B = color_encoder.color_generator(raw_data)
    print(R,G,B)


