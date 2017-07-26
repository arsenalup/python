import os

def walk_dir(path):
    file_path = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith('.py'):
                file_path.append(os.path.join(root, f))
    return file_path


def count_code(path):
    #得到文件目录
    file_name = os.path.basename(path)
    note_flag = False
    line_num = 0
    empty_line_nums = 0
    note_nums = 0
    with open(path) as f:
        for line in f.read().split('\n'):
            line_num +=1
            if line.strip().startswith('\"\"\"') and not note_flag:
                note_flag = True
                note_nums +=1
                continue
            if line.strip().startswith('\"\"\"'):
                note_flag = False
                note_nums +=1

            if line.strip().startswith('#') or note_flag:
                note_nums +=1

            if len(line) ==0:
                empty_line_nums +=1
    print("在{0}中，共有{1}行代码，其中有{2}空行，有{3}注释".format(file_name, line_num, empty_line_nums, note_nums))


if __name__ == '__main__':
    for f in walk_dir('./'):
        count_code(f)
