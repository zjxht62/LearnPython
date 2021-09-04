# 使用print来向文件输出实现log
import sys
import urllib

log = open('logfile.txt', 'w')
url = 'www.baidu.com'
print("开始从网页下载", url, file=log)
# text = urllib.urlopen(url).read()
sys.exit(0)
print('File successfully downloaded', file=log)
