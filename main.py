from encryption_utils import Encoder
from generator import CoverGenerator


raw_input = input('Please enter your feeling today:')
encoder = Encoder(raw_input)
raw_digst = encoder.encode()
color = encoder.color_generator(raw_digst)

color_generator = CoverGenerator(color)
img = color_generator.generate()

file_path = color_generator.save(img)
color_generator.save_to_mongo(raw_digst,color,raw_input,file_path)
