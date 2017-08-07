def trans_to_words():
    type_in = input(">>")
    with open('filtered_words.txt') as f:
        text = f.read()

    for i in text.split("\n"):
        if i in type_in:
            type_in = type_in.replace(i, '**')
    print(type_in)


if __name__ == '__main__':
    while True:
        trans_to_words()
