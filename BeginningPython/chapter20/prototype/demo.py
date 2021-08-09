import pprint
def get_blocks():
    f = open("test_input.txt")
    blocks = []
    line_list = f.readlines()
    content = ""
    for line in line_list:
        if line.strip():
            content += line
        else:
            blocks.append(content)
            content = ""
    return blocks


if __name__ == '__main__':
    pprint.pprint(get_blocks())