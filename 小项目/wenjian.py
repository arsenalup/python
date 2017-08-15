import sys
import os
import string


def wc(file_name):
    line_nums = 0
    word_nums = 0
    with open(file_name)as f_in:
        for line in f_in:
            flag = False
            for c in line:
                if not flag and c not in string.whitespace:
                    flag = True
                    word_nums +=1
                elif c in string.whitespace:
                    flag = False
            line_nums +=1
    return (line_nums, word_nums, os.path.getsize(file_name), file_name)

if __name__ == '__main__':
    if len(sys.argv) ==2:
        print(wc(sys.argv[1]))
    elif len(sys.argv) ==1:
        print(wc('in.txt'))
    else:
        print('args.error!')
