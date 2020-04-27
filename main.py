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
    size = 45
    font = ImageFont.truetype("arial.ttf", size=size)
    # draw the message on the background
    w, h = draw.textsize(text, font=font)
    text = text.split(" ")

    if text.length >= 3:
        text1 = text [0] + text [1]
        for (i = 3;i<=text.lenght-1;i+=1):
            text2 = text2 +text [i]

    print(text)
    while w > 550:
        size = size-1
        font = ImageFont.truetype("arial.ttf", size=size)
        w, h = draw.textsize(text, font=font)

    W = image.width
    H = image.height
    posH = (H - h) / 2 + 145
    posW = (W / 2) - 0.5 * w
    draw.text((posW, posH), text, fill="black", font=font)
    # save the edited image
    image.save('certificat_'+text+'.png') #for testing purposes
    return image


certificat("Katarina-Anna Marie Soukupova")
