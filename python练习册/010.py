from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255, 255, 255)
Image_Font = 'arial.ttf'
text = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))


def colorRandom():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def create_identifying_code(strs, width=400, height=200, chance=2):
    im = Image.new(IMAGE_MODE, (width, height), IMAGE_BG_COLOR)
    draw = ImageDraw.Draw(im)

    for w in range(width):
        for h in range(height):
            if chance < random.randint(1, 100):
                draw.point((w, h), fill=colorRandom())

    font =  ImageFont.truetype(Image_Font, 80)
    font_width, font_height = font.getsize(strs)
    strs_len = len(strs)
    x = (width - font_width)/2
    y = (height - font_height)/2

    for i in strs:
        draw.text((x, y), i, colorRandom(), font)
        x += font_width/strs_len

    im = im.filter(ImageFilter.BLUR)
    im.save('aaa.jpg')


if __name__ == '__main__':
    create_identifying_code(text)
