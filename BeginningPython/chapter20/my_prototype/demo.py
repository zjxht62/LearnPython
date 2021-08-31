import pprint
import re


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


print('<html><head><title>...</title><body>')

title = True
for block in get_blocks():
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')


