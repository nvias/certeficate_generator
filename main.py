from PIL import Image, ImageDraw, ImageFont
import os

"""
:param text
 writes normal-length name in picture
"""

def normal_name(text):
    image = Image.open('certifikat.png')
    draw = ImageDraw.Draw(image)
    size = 45
    W = image.width
    H = image.height
    font = ImageFont.truetype("arial.ttf", size=size)
    w, h = draw.textsize(text, font=font)
    while w > 550:
        size = size - 1
        font = ImageFont.truetype("arial.ttf", size=size)
        w, h = draw.textsize(text, font=font)

    posH = (H - h) / 2 + 145
    posW = (W / 2) - 0.5 * w
    draw.text((posW, posH), text, fill="black", font=font)
    image.save('certificat_' + text + '.png')  # for testing purposes
    return image
"""
:param text
 writes long name on picture
"""
def long_name(text1):
    image = Image.open('certifikat.png')
    draw = ImageDraw.Draw(image)
    size = 45
    W = image.width
    H = image.height
    font = ImageFont.truetype("arial.ttf", size=size)
    jmeno = text1[0] + " " + text1[1]
    prijmeni = text1[2]
    if len(text1) > 3:
        prijmeni = text1[2] + " " + text1[3]

    wj, hj = draw.textsize(jmeno, font=font)
    wp, hp = draw.textsize(prijmeni, font=font)
    size1 = 45
    size2 = 45
    while wj > 550:
        size1 = size1 - 1
        font = ImageFont.truetype("arial.ttf", size=size1)
        wj, hj = draw.textsize(jmeno, font=font)

    while wp > 550:
        size2 = size2 - 1
        font = ImageFont.truetype("arial.ttf", size=size2)
        wp, hp = draw.textsize(prijmeni, font=font)

    posHj = (H - hj) / 2 + 145 - 0.75 * hj
    posWj = (W / 2) - 0.5 * wj
    posHp = (H - hp) / 2 + 145 + 0.75 * hp
    posWp = (W / 2) - 0.5 * wp
    draw.text((posWj, posHj), jmeno, fill="black", font=font)
    draw.text((posWp, posHp), prijmeni, fill="black", font=font)
    image.save('certificat_' + jmeno + " " + prijmeni + '.png')  # for testing purposes
    return image

"""
:param text
 writes text on picture
"""

def certificat(text):
    image = Image.open('certifikat.png')
    draw = ImageDraw.Draw(image)
    size = 45
    W = image.width
    H = image.height
    font = ImageFont.truetype("arial.ttf", size=size)
    text1 = text.split(" ")
    if len(text1) > 2:
        long_name(text1)

    else:
        normal_name(text)





certificat("Katarina-Anna Marie")
