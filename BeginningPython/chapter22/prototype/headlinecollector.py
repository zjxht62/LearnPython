from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadlineHandler(ContentHandler):
    # 用于标记是否在指定的标签内
    in_headline=False

    def __init__(self, headlines):
        super(HeadlineHandler, self).__init__()
        self.headlines = headlines
        self.data = []
    # 如果遇到指点标记开头，设置in_headline为True
    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True
    # 处理结束标记，将data中读取的content列表转为一个字符串，清空data，添加h1标题，设置in_headline为False
    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    # 处理标签中的字符串
    def characters(self, content):
        if self.in_headline:
            self.data.append(content)

headlines = []
parse('website.xml', HeadlineHandler(headlines))
print('The following <h1> elements were found:')
for h in headlines:
    print(h)