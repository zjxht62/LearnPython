from urllib.request import urlopen
from html.parser import HTMLParser

# 判断是否是工作，href属性的值
def isjob(url):
    try:
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    return a == d == '' and b == 'jobs' and c.isdigit()

class Scraper(HTMLParser):
    # 跟踪是否处于一个链接中
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get('href', '')
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True
            self.chunks = []

    # 不是假定通过调用handle_data一次就能获得所需的所有文本，而是假定这些文本分成多个块，需要多次调用handle_data才能获得。
    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            print('{} ({})'.format(''.join(self.chunks), self.url))
            self.in_link = False


text = urlopen('https://www.python.org/jobs/').read().decode()
parser = Scraper()
parser.feed(text)
parser.close()