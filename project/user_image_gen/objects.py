"""
LINES: # draw.line(xy, fill=None, width=0)
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)


Ellipsis: #draw.ellipse(xy, fill=None, outline=None)
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)

draw.ellipse((200, 125, 300, 200), fill=(255, 0, 0), outline=(0, 0, 0))
img.show()

RECTANGLE: #draw.rectangle(xy, fill=None, outline=None)
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)

draw.rectangle(
   (200, 125, 300, 200),
   fill=(255, 0, 0),
   outline=(0, 0, 0))
img.show()

POLYGON: #draw.polygon(seq, fill=None, outline=None)
img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)

draw.polygon(
   ((200, 200), (300, 100), (480, 50)),
   fill=(255, 0, 0),
   outline=(0, 0, 0))
img.show()
"""

import random
from PIL import Image, ImageDraw

# SOURCE CODE FROM PILLOW
"""https://pillow.readthedocs.io/en/stable/_modules/PIL/ImageDraw.html#ImageDraw.rectangle """

def lines(file_tree, uno):
    """LINES: # draw.line(xy, fill=None, width=0)
    img = Image.new('RGB', (500, 300), (125, 125, 125))
    draw = ImageDraw.Draw(img)
    draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)"""
    with Image.open(file_tree) as file:
        #LINE
        draw = ImageDraw.Draw(file)
        draw.ellipse((random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480)), fill=uno, outline=uno)
        file.save(file_tree,quality=95)


def ellipsis(file_tree, uno): # done
    """Ellipsis: #draw.ellipse(xy, fill=None, outline=None)
    img = Image.new('RGB', (500, 300), (125, 125, 125))
    draw = ImageDraw.Draw(img)

    draw.ellipse((200, 125, 300, 200), fill=(255, 0, 0), outline=(0, 0, 0))
    img.show()"""
    with Image.open(file_tree) as file:
        #ELLIPSE
        one = random.randint(-100,100)
        two = random.randint(-100,100)
        draw = ImageDraw.Draw(file)
        draw.ellipse((random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480)), fill=uno, outline=uno)
        file.save(file_tree,quality=100,subsampling=0)


def rectangle(file_tree, uno):
    """
    RECTANGLE: #draw.rectangle(xy, fill=None, outline=None)
    img = Image.new('RGB', (500, 300), (125, 125, 125))
    draw = ImageDraw.Draw(img)

    draw.rectangle(
       (200, 125, 300, 200),
       fill=(255, 0, 0),
       outline=(0, 0, 0))
    img.show()
    """
    with Image.open(file_tree) as file:
        #Rectangle
        draw = ImageDraw.Draw(file)
        draw.rectangle((random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480)), fill=uno, outline=uno)
        file.save(file_tree,quality=100,subsampling=0)

def polygon(file_tree, uno):
    """
    POLYGON: #draw.polygon(seq, fill=None, outline=None)
    img = Image.new('RGB', (500, 300), (125, 125, 125))
    draw = ImageDraw.Draw(img)

    draw.polygon(
       ((200, 200), (300, 100), (480, 50)),
       fill=(255, 0, 0),
       outline=(0, 0, 0))
    img.show()
    """
    with Image.open(file_tree) as file:
        #polygon
        draw = ImageDraw.Draw(file)
        """Original One: draw.polygon(((200, 200), (300, 100), (480, 50)), fill=uno, outline=uno)
        Draws a triangle at the middle"""
        draw.polygon(((random.randint(-480, 480), random.randint(-480, 480)), (random.randint(-480, 480), random.randint(-480, 480)), (random.randint(-480, 480), random.randint(-480, 480))), fill=uno, outline=uno)
        file.save(file_tree,quality=100,subsampling=0)


def circle(file_tree, uno): # Done
    with Image.open(file_tree) as file:
        # CIRCLE
        draw = ImageDraw.Draw(file)
        draw.ellipse((random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480), random.randint(-480, 480)), fill=uno, outline=uno)
        file.save(file_tree,quality=100,subsampling=0)