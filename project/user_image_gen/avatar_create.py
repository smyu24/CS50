import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import random

import io
import base64

from templates import color_pick
import objects

def circles_only(dirname, userid, colors):
    for i in range(random.randint(20,30)): # FIX ALL OF THESE TO SPREAD OUT EVENLY; RIGTH NOW ITS CONCNETRATED AT THE CENTER
        objects.circle(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))

def ellipsis_only(dirname, userid, colors):
    for i in range(random.randint(20,30)): # FIX ALL OF THESE TO SPREAD OUT EVENLY; RIGTH NOW ITS CONCNETRATED AT THE CENTER
        objects.ellipsis(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))

def lines_only(dirname, userid, colors):
    for i in range(random.randint(20,30)): # FIX ALL OF THESE TO SPREAD OUT EVENLY; RIGTH NOW ITS CONCNETRATED AT THE CENTER
        objects.lines(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))

def rectangle_only(dirname, userid, colors):
    for i in range(random.randint(20,30)): # FIX ALL OF THESE TO SPREAD OUT EVENLY; RIGTH NOW ITS CONCNETRATED AT THE CENTER
        objects.rectangle(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))

def polygon_only(dirname, userid, colors):
    for i in range(random.randint(20,30)): # FIX ALL OF THESE TO SPREAD OUT EVENLY; RIGTH NOW ITS CONCNETRATED AT THE CENTER
        objects.polygon(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))

def all_only(dirname, userid, colors):
    for i in range(random.randint(20,30)): # FIX ALL OF THESE TO SPREAD OUT EVENLY; RIGTH NOW ITS CONCNETRATED AT THE CENTER
        objects.ellipsis(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))
        objects.circle(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))
        objects.lines(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))

        objects.rectangle(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))
        objects.polygon(fr'{dirname}/profile_images/{str(userid)}.png', random.choice(colors))

def main(userid):
    dirname = os.path.dirname(__file__)

    # sets final image dimensions as 480x480 pixels
    # the original 24x24 pixel image will be expanded to these dimensions
    dimensions = 480, 480

    #calling a random pallate of colors to pick and choose from
    colors = color_pick()
    random.shuffle(colors)

    #randomly select background color from chosen pallate
    bg = colors[0]
    colors.pop(0)

    #print(colors, "colors")
    #print(bg)

    picture = []
    picture = 24*[24*[bg]] # append lines of code tht will
    #after picking the background color and the color pallate, open the user's file and alter its contents to the background color.

    array = np.array(picture, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/profile_images/' + (str(userid)) + '.png'
    print(imgname)
    new_image.save(imgname)

    #message.encode('ascii')
    with Image.open(fr'{dirname}/profile_images/{str(userid)}.png') as file:
        array = np.array(picture, dtype=np.uint8)
        new_image = Image.fromarray(array)
        new_image = new_image.resize(dimensions, resample=Image.ANTIALIAS)
        imgname = fr'{dirname}/profile_images/{str(userid)}.png'
        new_image.save(imgname,quality=100,subsampling=0)

    #modular, stackable filter, objet caller that
    # -240,240 is the entire
    random.choice([all_only(dirname, userid, colors), lines_only(dirname, userid, colors), rectangle_only(dirname, userid, colors), polygon_only(dirname, userid, colors), ellipsis_only(dirname, userid, colors), circles_only(dirname, userid, colors)])
    return

main("417550")

"""1. Rename each photo as per user IDs.
2. Do not store images in database, rather than save them in filesystem and store the image name in database.
3. Create separate directories for small, medium and large pics. (You need to copy the same pic and upload them to their respective directories. This will load up your page faster because small pics will have small size.)"""


"""with Image.open(fr'{dirname}/profile_images/{str(userid)}.png') as file:
        #Rectangle
        draw = ImageDraw.Draw(file)
        draw.rectangle((200, 300, -480, -480), fill=(255,255,255), outline=random.choice(colors))
        file.save(fr'{dirname}/profile_images/{str(userid)}.png',quality=95)"""

"""OriImage = Image.open(fr'{dirname}/profile_images/{str(userid)}.png')

blurImage = OriImage.filter(ImageFilter.BLUR)
#Save blurImage
blurImage.save(fr'{dirname}/profile_images/{str(userid)}.png')"""

"""f = io.BytesIO(base64.b64decode(b64string))
pilimage = Image.open(f)
"""

# return of templates go into pixels


# use PIL to create an image from the new array of pixels
"""new_image = Image.fromarray(array)
new_image = new_image.resize(dimensions, resample=0)
imgname = fr'{dirname}/profile_images/{str(userid)}.png'
print(imgname)
new_image.save(imgname)"""


"""
with open('readme.txt', 'x') as f:
    f.write('Create a new text file!')

from PIL import Image
with Image.open("hopper.jpg") as im:
    im.rotate(45).show()

    f= open("guru99.txt","w+")
"""
#https://newbedev.com/100x100-image-with-random-pixel-colour

"""possible filter

from PIL import Image
image = Image.open("beach1.jpg")
r, g, b = image.split()
image.show()
image = Image.merge("RGB", (b, g, r))
image.show()
"""
"""
    You can convert to a string like this:

import base64

with open("image.png", "rb") as image:
    b64string = base64.b64encode(image.read())
That should give you the same results as if you run this in Terminal:

base64 < image.png
And you can convert that string back to a PIL Image like this:

from PIL import Image
import io

f = io.BytesIO(base64.b64decode(b64string))
pilimage = Image.open(f)

"""

"""
    https://stackoverflow.com/questions/54147694/python-how-to-turn-an-image-into-a-string-and-back
    https://www.geeksforgeeks.org/python-convert-image-to-string-and-vice-versa/
"""