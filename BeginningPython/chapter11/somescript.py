#计算sys.stdin中包含多少单词的简单脚本
#可以通过管道将内容写到python的标准输入sys.stdin
# cat somefile.txt | python somescript.py | sort
# somescript.py
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)