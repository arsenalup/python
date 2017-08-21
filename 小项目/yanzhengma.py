from PIL import Image, ImageDraw, ImageFont
import os
import random
import string


def deform_char(ch):
    font_list = ['simhei.ttf', 'simsun.ttc', 'simkai.ttf']

    def rd(n):
        return random.randint(0, n)

    new_img = Image.new("RGBA", (120, 120), (255, 255, 255, 255))
    draw_img = ImageDraw.Draw(new_img)
    font = ImageFont.truetype(
        os.path.join("fonts", random.choice(font_list)), 40)
    draw_img.text(
        (40, 40), ch, font=font, fill=(
            rd(255), rd(255), rd(255), 255))
    new_img = new_img.transform((120, 120), Image.QUAD,
        (rd(40) + 0, rd(40) + 0, rd(40) + 0, rd(40) + 80,
        rd(40) + 80, rd(40) + 80, rd(40) + 80, rd(40) + 0),
        Image.BICUBIC)
    return new_img.crop((20, 20, 100, 100))


def deform_word(word):
    word_len = len(word)
    new_img = Image.new('RGBA', (80 * word_len, 80))
    for i, char_i in enumerate(word):
        new_img.paste(deform_char(char_i), (i * 80, 0, i * 80 + 80, 80))
    return new_img


def gen_identifying_code(word_len=4):
    word = random.sample(string.ascii_letters + string.digits, word_len)
    im = deform_word(word)
    im.show()
    im.save('code.png')


if __name__ == '__main__':
    gen_identifying_code()
