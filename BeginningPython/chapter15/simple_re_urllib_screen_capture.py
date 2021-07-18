from urllib.request import urlopen
import re
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('https://www.python.org/jobs/').read().decode()
for url, name in p.findall(text):
    print('{} ({})'.format(name, url))