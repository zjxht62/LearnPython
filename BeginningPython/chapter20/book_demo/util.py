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
        # 通过判断block是否为空来防止连续的空行作为文本块输出
        elif block:
            yield ''.join(block).strip()
            block = []