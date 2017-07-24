import os
from PIL import Image

pic_WIDTH = 1136
pic_HEIGHT = 640


def resize_pic(path, new_path, width=pic_WIDTH, height=pic_HEIGHT):
    im = Image.open(path)
    w,h = im.size

    if w > width:
        h = width * h // w
        w = width
    if h > height:
        w = height * w // h
        h = heightt

    im_resized = im.resize((w, h), Image.ANTIALIAS)
    im_resized.save(new_path)


def walk_dir_and_resize(path):
    for root, dirs, files in os.walk(path):
        for f_name in files:
            if f_name.lower().endswith('jpg'):
                path_dst = os.path.join(root, f_name)
                f_new_name = os.path.join(root, 'pic'+f_name)
                print(path_dst)
                print(f_new_name)
                resize_pic(path=path_dst, new_path=f_new_name)

if __name__ == '__main__':
    walk_dir_and_resize('./')

