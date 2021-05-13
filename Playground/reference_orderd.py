import re

pat = re.compile(r'\[(.*?)\].*,([0-9]{4})\.*')


def remove_old_num(line):
    m = pat.search(line)
    if m:
        # 将旧的编号去掉，换成format的占位符
        line = line.replace(m.group(1), '{}', 1)
        line = line[:len(line) - 1]
    return line


def is_foreign_ref(line):
    foreign_pat = re.compile(r'\]\[(.*?)\]')
    match = foreign_pat.search(line)
    if match:
        return True
    else:
        return False


def get_year(line):
    m = pat.search(line)
    if m:
        # 获取year
        year = int(m.group(2))
        # print(type(year))
        return year
    return 0


with open('unordered.md') as f:
    num = 1
    foreign_ref_list = []
    chinese_ref_list = []

    while True:
        line = f.readline()
        if not line:
            break
        if is_foreign_ref(line):
            foreign_ref_list.append((get_year(line), remove_old_num(line)))
        else:
            chinese_ref_list.append((get_year(line), remove_old_num(line)))

    # print(line_list)
    foreign_ref_list.sort(key=lambda x: (x[0]))
    chinese_ref_list.sort(key=lambda x: (x[0]))
    # print(chinese_ref_list)
    # print(foreign_ref_list)
    result_list = chinese_ref_list + foreign_ref_list
    for y, l in result_list:
        print(l.format(num))
        num += 1


def print_list(list):
    for item in list:
        print(item)
