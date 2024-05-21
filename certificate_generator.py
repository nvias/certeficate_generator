import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

"""
:param text
 writes normal-length name in picture
"""

def normal_name(text, size, image, height=-530, bari_posrana_konstanta=2300, text_height=300):
    draw = ImageDraw.Draw(image)
    W = image.width
    H = image.height
    w, h = draw.textsize(text, font=font(size))

    counter = 0
    while w > bari_posrana_konstanta or h > text_height:
        counter = counter + 1
        size = size - 1
        w, h = draw.textsize(text, font=font(size))

    posH = (H - h) / 2 + height
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


def long_name(text1, size, image, height=-530, bari_posrana_konstanta=2300, text_height=300):
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

    while wj > bari_posrana_konstanta or hj > text_height:
        size1 = size1 - 1
        wj, hj = draw.textsize(jmeno, font=font(size1))
    while wp > bari_posrana_konstanta or hp > text_height:
        size2 = size2 - 1
        wp, hp = draw.textsize(prijmeni, font=font(size2))

    posHj = (H - hj) / 2 - 0.5 * hj + height
    posHp = (H - hp) / 2 + 0.5 * hp + height
    posWj = (W / 2) - 0.5 * wj
    posWp = (W / 2) - 0.5 * wp
    draw.text((posWj, posHj), jmeno, fill="black", font=font(size1))
    draw.text((posWp, posHp), prijmeni, fill="black", font=font(size2))
    if not __debug__:
        path = Path("certificates/" + "certificat_" + jmeno + "_" + prijmeni + ".png")
        image.save(path.as_posix())  # for testing purposes
    return image


def font(size):
    path = Path("fonts/Poppins-Black.ttf")
    path = path.as_posix()

    font = ImageFont.truetype(path, size=size)
    return font


"""
:param text
 writes text on picture
"""


def certificat(text, size=300):
    f = open("config", "r")
    conf = f.readlines()
    f.close()
    conf = [item.strip() for item in conf]

    image = Image.open(conf[0])
    path = Path("certificates/")
    path = path.as_posix()

    if not os.path.exists(path):
        os.makedirs(path)

    text1 = text.split(" ")
    if len(text1) > 2:
        img = long_name(text1, size, image, height=int(conf[2]), bari_posrana_konstanta=int(conf[3]),
                        text_height=int(conf[4]))

    else:
        img = normal_name(text, size, image, height=int(conf[2]), bari_posrana_konstanta=int(conf[3]),
                          text_height=int(conf[4]))
    return img


if __name__ == "__main__":
    size = 300
    certificat("Dave")