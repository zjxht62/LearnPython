'''
在文件最后一行增加一个空行，用于辅助判断文本块
'''
def lines(file):
    for line in file:yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        # elif 在这里的作用是判断文本块list内是否有内容，对于连续的空行，不会通过yield生成
        # 通过判断block是否为空来防止连续的空行作为文本块输出
        elif block:
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':
    print(list(blocks(open('test_input.txt'))))