import os
import re


def walk_dir(path):
    file_path = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith('txt'):
                file_path.append(os.path.join(root, f))
    return file_path


def find_key_word(filepath):
    word_dic = {}
    filename = os.path.basename(filepath)
    with open(filepath) as f:
        text = f.read()
        word_list = re.findall(r'[A-Za-z]+', text.lower())
        for i in word_list:
            if i in word_dic:
                word_dic[i] +=1
            else:
                word_dic[i] = 1
        sorted_word_list = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
        print("在文件{}中，{}共出现了{}次".format(filename, sorted_word_list[0][0], sorted_word_list[0][1]))


if __name__ == '__main__':
    for filepath in walk_dir(os.getcwd()):
        find_key_word(filepath)
