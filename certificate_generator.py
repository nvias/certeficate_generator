from PIL import Image, ImageDraw, ImageFont

"""
:param text
 writes normal-length name in picture
"""


def normal_name(text, size):
    image = Image.open('certifikat.png')
    draw = ImageDraw.Draw(image)
    size = size
    W = image.width
    H = image.height
    font = ImageFont.truetype("fonts\\introhead.otf", size=size)
    w, h = draw.textsize(text, font=font)
    while w > 550:
        size = size - 1
        font = ImageFont.truetype("fonts\\introhead.otf", size=size)
        w, h = draw.textsize(text, font=font)

    posH = (H - h) / 2 - 30
    posW = (W / 2) - 0.5 * w
    draw.text((posW, posH), text, fill="black", font=font)
    image.save('new_certificate.png')  # for testing purposes
    return image


"""
:param text
 writes long name on picture
"""


def long_name(text1, size):
    image = Image.open('certifikat.png')
    draw = ImageDraw.Draw(image)
    size = size
    W = image.width
    H = image.height
    font = ImageFont.truetype("fonts\\introhead.otf", size=size)
    jmeno = text1[0] + " " + text1[1]
    prijmeni = text1[2]
    if len(text1) > 3:
        prijmeni = text1[2] + " " + text1[3]

    wj, hj = draw.textsize(jmeno, font=font)
    wp, hp = draw.textsize(prijmeni, font=font)
    size1 = size
    size2 = size
    while wj > 550:
        size1 = size1 - 1
        font = ImageFont.truetype("fonts\\introhead.otf", size=size1)
        wj, hj = draw.textsize(jmeno, font=font)

    while wp > 550:
        size2 = size2 - 1
        font = ImageFont.truetype("fonts\\introhead.otf", size=size2)
        wp, hp = draw.textsize(prijmeni, font=font)

    posHj = (H - hj) / 2 - 0.75 * hj - 30
    posWj = (W / 2) - 0.5 * wj
    posHp = (H - hp) / 2 + 0.75 * hp - 30
    posWp = (W / 2) - 0.5 * wp
    draw.text((posWj, posHj), jmeno, fill="black", font=font)
    draw.text((posWp, posHp), prijmeni, fill="black", font=font)
    image.save('new_certificate.png')  # for testing purposes
    return image


"""
:param text
 writes text on picture
"""


def certificat(text, size=75):
    image = Image.open('certifikat.png')
    draw = ImageDraw.Draw(image)
    W = image.width
    H = image.height
    font = ImageFont.truetype("fonts\\introhead.otf", size=size)
    text1 = text.split(" ")
    if len(text1) > 2:
        long_name(text1, size)

    else:
        normal_name(text, size)


certificat("Jmeno Prijmeni")
