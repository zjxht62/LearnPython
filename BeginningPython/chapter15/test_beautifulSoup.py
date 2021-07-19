from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('http://python.org/jobs').read()
soup = BeautifulSoup(text, 'html.parser')

# 使用soup.body来获取文档体，再访问其中的第一个section。使用参数'h2' 调用返回的对象，这与使用其方法find_all等效——返回其中的所有h2元素。
jobs = set()
for job in soup.body.section('h2'):
    # 每个h2元素都表示 一个职位，而我感兴趣的是它包含的第一个链接job.a。属性string是链接的文本内容，而a['href'] 为属性href。
    jobs.add('{} ({})'.format(job.a.string, job.a['href']))

print('\n'.join(sorted(jobs, key=str.lower)))