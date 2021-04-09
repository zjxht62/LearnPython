import requests
from bs4 import BeautifulSoup

params = {'grade': 11}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    'referer': "https://cache.bdschool.cn"}
history_link_list = []
download_prefix = 'https://cache.bdschool.cn'
download_link_list = []

r = requests.get("https://cache.bdschool.cn/public/bdschool/index/static/migu/2020_d_w.html", params=params,
                 headers=headers)
html_text = r.content
soup = BeautifulSoup(html_text, 'html.parser')
a_list = soup.find_all('a', class_='content_table_td_title')
for a in a_list:
    href_str = a['href']
    if 'grade_id=11&subject_id=6' in href_str:
        history_link_list.append(href_str)

for history_link in history_link_list:
    r2 = requests.get(history_link, headers=headers)
    download_page_html_text = r2.content
    soup2 = BeautifulSoup(download_page_html_text, 'html.parser')
    download_a_list = soup2.find_all('a', class_='file_view_list')
    for download_a in download_a_list:
        download_link_list.append(download_prefix + download_a['href'])

print('总数：', len(download_link_list))
for link in download_link_list:
    print(link)
