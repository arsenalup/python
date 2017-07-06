import re

def count_the_words(path):
    with open(path)as f:
        text = f.read()
        word_list = re.findall('[a-zA-Z0-9]+', text)
        count = len(word_list)

    return  count

nums = count_the_words(path='')