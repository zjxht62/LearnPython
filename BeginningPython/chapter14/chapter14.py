from urllib.request import urlopen
import re
# 注意要在编译正则表达式的时候指定是否忽略大小写属性
pat = re.compile(b'<a href="([^"]+)" .*?>about</a>', re.IGNORECASE)
webpage = urlopen('http://www.python.org')
text = webpage.read()
m = pat.search(text)
print(m.group(1))



# 获取Python官网的主页，并将其存储到文件C:\python_webpage.html中
from urllib.request import urlretrieve, urlcleanup
filename, headers = urlretrieve('http://www.python.org')
print(filename)
print(headers)

urlcleanup()