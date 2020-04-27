from PIL import Image, ImageDraw, ImageFont
import os


"""
:param text,image,font
 writes text to console
"""
def certificat(text):
    # nacte obrazek
    image = Image.open('certifikat.png')
    draw = ImageDraw.Draw(image)
    # create font object with the font file and specify
    # desired size
    font = ImageFont.truetype("arial.ttf", size=45)
    # draw the message on the background
    W = image.width
    H = image.height
    w, h = draw.textsize(text, font=font)
    posH = (H - h) / 2 + 145
    posW = (W / 2) - 0.5 * w
    draw.text((posW, posH), text, fill="black", font=font)
    # save the edited image
    image.save('certificat_'+text+'.png')


certificat("Barbora Soukupova")
