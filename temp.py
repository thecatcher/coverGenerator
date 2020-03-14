import hashlib

import random
from PIL import Image

# with open("demo.jpg",'w+') as img_file:
#     img = Image.new('RGB',(100,100),(255,240,240))
#     img.save(img_file)


with Image.open('demo.jpg') as img:
    r, g, b = img.getpixel((10, 10))
    print(r,g,b)
