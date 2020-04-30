from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os


"""
:param text
 writes normal-length name in picture
"""

def normal_name(text, size, image):
    draw = ImageDraw.Draw(image)
    W = image.width
    H = image.height
    w, h = draw.textsize(text, font=font(size))
    if w > 2300:
        w_change = ((w + 2300) / 2300) * 0.65
        size = round(size / w_change)
    w, h = draw.textsize(text, font=font(size))

   # while w > 2300:
    #    size = size - 1
     #   w, h = draw. textsize(text, font=font(size))

    posH = (H - h) / 2 + 30
    posW = (W / 2) - 0.5 * w
    draw.text((posW, posH), text, fill="black", font=font(size))
    path = Path("certificates/" + "certificat_" + text + ".png")
    image.save(path.as_posix())  # for testing purposes
    return image


"""
:param text
 writes long name on picture
"""


def long_name(text1, size, image):
    draw = ImageDraw.Draw(image)
    size1 = size
    size2 = size
    W = image.width
    H = image.height
    jmeno = text1[0] + " " + text1[1]
    prijmeni = text1[2]
    if len(text1) > 3:
        prijmeni = text1[2] + " " + text1[3]

    w1, h1 = draw.textsize(jmeno, font=font(size1))
    w2, h2 = draw.textsize(prijmeni, font=font(size2))

    if w1 > 2300:
        w_change1 = ((w1 + 2300) / 2300) * 0.65
        size1 = round(size1 / w_change1)

    if w2 > 2300:
        w_change2 = ((w2 + 2300) / 2300) * 0.65
        size2 = round(size2 / w_change2)

    w1, h1 = draw.textsize(jmeno, font=font(size1))
    w2, h2 = draw.textsize(prijmeni, font=font(size2))



    posH1 = (H - h1) / 2 - 0.5 * h1 + 70
    posH2 = (H - h2) / 2 + 0.5 * h2 + 70
    posW1 = (W / 2) - 0.5 * w1
    posW2 = (W / 2) - 0.5 * w2

    draw.text((posW1, posH1), jmeno, fill="black", font=font(size1))
    draw.text((posW2, posH2), prijmeni, fill="black", font=font(size2))
    path = Path("certificates/" + "certificat_" + jmeno + "_" + prijmeni + ".png")
    image.save(path.as_posix())  # for testing purposes
    return image


"""
:param text
 writes text on picture
"""


def certificat(text, size, image):
    text1 = text.split(" ")
    if len(text1) > 2:
        long_name(text1, size, image)

    else:
        normal_name(text, size, image)

    return image


def font(size):
    path = Path("fonts/introhead.otf")
    path = path.as_posix()
    font = ImageFont.truetype(path, size=size)
    return font

if __name__ == '__main__':

    image = Image.open('certifikatAI.png')
    size = 300
    certificat("Zadej Jmeno", size, image)
