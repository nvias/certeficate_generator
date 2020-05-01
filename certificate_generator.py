import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

"""
:param text
 writes normal-length name in picture
"""


def normal_name(text, size, image):

    draw = ImageDraw.Draw(image)
    W = image.width
    H = image.height
    w, h = draw.textsize(text, font=font(size))

    counter = 0
    while w > 2300:
        counter = counter + 1
        size = size - 1
        w, h = draw.textsize(text, font=font(size))

    posH = (H - h) / 2 + 30
    posW = (W / 2) - 0.5 * w

    draw.text((posW, posH), text, fill="black", font=font(size))
    if not __debug__:
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
    if not __debug__:
        path = Path("certificates/" + "certificat_" + jmeno + "_" + prijmeni + ".png")
        image.save(path.as_posix())  # for testing purposes
    return image


def font(size):
    path = Path("fonts/introhead.otf")
    path = path.as_posix()

    font = ImageFont.truetype(path, size=size)
    return font


"""
:param text
 writes text on picture
"""


def certificat(text, size=300, image='certifikatAI.png'):
    image = Image.open(image)
    path = Path("certificates/")
    path = path.as_posix()

    if not os.path.exists(path):
        os.makedirs(path)

    text1 = text.split(" ")
    if len(text1) > 2:
        img = long_name(text1, size, image)

    else:
        img = normal_name(text, size, image)
    return img


if __name__ == "__main__":
    size = 300
    certificat("Dave")
