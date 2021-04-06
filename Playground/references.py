import re

pat = re.compile(r',[0-9]{4}([\.,:].*)')

# M：著作
book_count = 1
# J：期刊文章
journal_articles_count = 1
# G：汇编
collection_count = 1
# S：教育部文件
edu_paper_count = 1
# D：学位论文
graduate_paper_count = 1
# C、N：其他
others_count = 1


def handle_end(line, num):
    # str_list = list(line)
    # str_list.insert(1, str(num))
    # result = ''.join(str_list)
    result = line
    m = pat.search(result)
    if m:
        # print(m.group(0))
        result = result.replace(m.group(1),'')

    result = result.split('\n')[0]
    result = result + '.'
    print(result)

    return result

def addNum(str_no_num, num):
    str_list = list(str_no_num)
    str_list.insert(1, str(num))
    result = ''.join(str_list)
    return result

# M：著作
book_result_list = []
# J：期刊文章
journal_articles_result_list = []
# G：汇编
collection_result_list = []
# S：教育部文件
edu_paper_result_list = []
# D：学位论文
graduate_paper_list = []
# C、N：其他
others_list = []


with open('temp.md') as f:
    num = 1

    while True:
        line = f.readline()
        if not line:
            break
        result_line = handle_end(line, num)
        if '[M]' in result_line:
            book_result_list.append(addNum(result_line, book_count))
            book_count+=1
        if '[J]' in result_line:
            journal_articles_result_list.append(addNum(result_line, journal_articles_count))
            journal_articles_count+=1
        if '[G]' in result_line:
            collection_result_list.append(addNum(result_line, collection_count))
            collection_count+=1
        if '[S]' in result_line:
            edu_paper_result_list.append(addNum(result_line, edu_paper_count))
            edu_paper_count+=1
        if '[D]' in result_line:
            graduate_paper_list.append(addNum(result_line, graduate_paper_count))
            graduate_paper_count+=1
        if '[C]' in result_line or 'N' in result_line:
            others_list.append(addNum(result_line, others_count))
            others_count+=1

def print_list(list):
    for item in list:
        print(item)

print('M：著作')
print_list(book_result_list)
print('J：期刊文章')
print_list(journal_articles_result_list)
print('G：汇编')
print_list(collection_result_list)
print('S：教育部文件')
print_list(edu_paper_result_list)
print('D：学位论文')
print_list(graduate_paper_list)
print('C、N：其他')
print_list(others_list)

