def trans_to_words():
    type_in = input('<<')
    judge_flag = False
    with open('data.txt') as f:
        text = f.read()
        
    for i in text.split('\n'):
        if i in type_in:
            judge_flag = True
        
    if judge_flag:
        print("freedom")
    else:
        print("human rights")
        
if __name__ == '__main__':
    while True:
        trans_to_words()
