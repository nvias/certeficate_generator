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
    while w > 2300:
        size = size - 1
        w, h = draw.textsize(text, font=font(size))

    posH = (H - h) / 2 + 30
    posW = (W / 2) - 0.5 * w
    draw.text((posW, posH), text, fill="black", font=font(size))
    image.save("certificates\\certificat_' + text + '.png")  # for testing purposes
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

    wj, hj = draw.textsize(jmeno, font=font(size1))
    wp, hp = draw.textsize(prijmeni, font=font(size2))
    while wj > 2300:
        size1 = size1 - 1
        wj, hj = draw.textsize(jmeno, font=font(size1))
    while wp > 2300:
        size2 = size2 - 1
        wp, hp = draw.textsize(prijmeni, font=font(size2))

    posHj = (H - hj) / 2 - 0.5 * hj + 70
    posHp = (H - hp) / 2 + 0.5 * hp + 70
    posWj = (W / 2) - 0.5 * wj
    posWp = (W / 2) - 0.5 * wp
    draw.text((posWj, posHj), jmeno, fill="black", font=font(size1))
    draw.text((posWp, posHp), prijmeni, fill="black", font=font(size2))
    image.save("certificates\\certificat_' + jmeno + " " + prijmeni + '.png")  # for testing purposes
    return image


"""
:param text
 writes text on picture
"""


def certificat(text, size, image):
    draw = ImageDraw.Draw(image)
    W = image.width
    H = image.height
    text1 = text.split(" ")
    if len(text1) > 2:
        long_name(text1, size, image)

    else:
        normal_name(text, size, image)

def font(size):
    font = ImageFont.truetype("fonts\\introhead.otf", size=size)
    return font


image = Image.open('certifikatAI.png')
size = 300
certificat("Zadej Jmeno", size, image)
