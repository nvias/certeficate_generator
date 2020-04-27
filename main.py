from PIL import Image, ImageDraw, ImageFont
import os


"""
:param text,image,font
 writes text to console
"""
def certificat(text,image,font):
    # nacte obrazek
    image = Image.open(image)
    draw = ImageDraw.Draw(image)
    # create font object with the font file and specify
    # desired size
    font = ImageFont.truetype(font, size=45)
    msg = text
    color = 'rgb(0, 0, 0)'  # black color
    # draw the message on the background
    W = image.width
    H = image.height
    w, h = draw.textsize(msg, font=font)
    posH = (H - h) / 2 + 145
    posW = (W / 2) - 0.5 * w
    draw.text((posW, posH), msg, fill="black", font=font)
    # save the edited image
    image.save('greeting_card.png')


certificat("Barbora Soukupova", 'certifikat.png', 'arial.ttf')
