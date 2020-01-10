from PIL import Image
from math import floor
from pathlib import Path

BASE_PATH = '/home/milan/Projects/iedc-web-v2/assets/uploads/images/'
MAX_SIZE = 100000   # bytes
REDUCTION_COEFF = 0.9
QUALITY = 85
FORMATS = ['.jpeg', '.jpg', '.png']

# Helper functions

def get_size(image_file):
    return len(image_file.fp.read())

# Main script

files = []

for f in FORMATS:
    for i in Path(BASE_PATH).rglob('*' + f):
        files.append(i)


for image in files:
    image_file = Image.open(image)
    flag = 0
    while get_size(image_file) > MAX_SIZE:
        flag += 1
        if flag == 1:
            print("Optimizing " + str(image))
        x, y = image_file.size
        x *= REDUCTION_COEFF
        y *= REDUCTION_COEFF
        image_file = image_file.resize((floor(x),floor(y)), Image.ANTIALIAS)
        image_file.save(image, optimize=True, quality=QUALITY)
        image_file = Image.open(image)
    if flag != 0:
        print(str(flag) + " passes done!")



