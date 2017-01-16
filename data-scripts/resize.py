import sys
from PIL import Image
from io import BytesIO

import yaml
import requests
from resizeimage import resizeimage
from slugify import slugify

shows = yaml.load(sys.stdin)

for show in shows:
    slug = slugify(show['title'])
    filename = '../img/shows/' + slug + '.jpg'

    response = requests.get(show['thumbnail'])
    with Image.open(BytesIO(response.content)) as img:
        img_resized = resizeimage.resize_height(img, 425)
        img_resized.save(filename, img_resized.format)
