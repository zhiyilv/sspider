import requests as r
from bs4 import BeautifulSoup as bs
import re
from time import sleep


def parse_c(c):
    details = []
    name = c.find(class_="s-r-list-photo").p.a.text
    if name != '无':
        title = c.find(class_='s-r-list-info').h3.text
        details.append(title)
        details.append(name)
        # subject_info = c.find(class_='s-r-list-info').p('span')[0].text
        # grade_info = c.find(class_='s-r-list-info').p('span')[1].text
        details += c(text=re.compile('：'))[1:]
    return details


def parse_page(url):
    page = r.get(url)
    soup = bs(page.content, 'lxml')
    containers = soup(class_="s-r-list")
    result = []
    for c in containers:
        result_c = parse_c(c)
        if result_c == []:
            continue
        result.append(result_c)
    show(result)
    return result


def show(result):
    for index, details in enumerate(result):
        print('class {}: {}'.format(index + 1, details[0]))
        print(details[1:])


start_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:1'
page = r.get(start_url)
soup = bs(page.content, 'lxml')
# if the maxpage is explicit
maxpage = soup.find_all(class_='pagination mtop40')[0].find(text = re.compile('当前第')).split('页')[0].split('/')[-1]
maxpage = int(maxpage)

# # if the last page button is there
# maxpage = soup.find_all(class_='pagination mtop40')[0].find_all('a')[-1].get('href').split(':')[-1]

# only navigatable through buttons, if current page is a link in the button
# current_page_url = 'search/index/grade:1/subject:/level:bx/term:/period:0/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:1'
# # first find all page links available
# link_list = soup.find_all(class_='pagination mtop40')[0].find_all('a')
# # second, find the index of current page link in the list
# current_page_lable = soup.find_all(class_='pagination mtop40')[0].find(href=current_page_url)
# current_index = link_list.index(current_page_lable)
# next_index = current_index + 1
# max_length = len(link_list)
# if next_index > max_length -1:
#     print('this is the last page already')
#     maxpage = current_page_lable.get('href').split(':')[-1]
# else:
#     next_link = link_list[next_index]

url_list=[]
common_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:'
for index in range(1, maxpage+1):
    dest_url = common_url + str(index)
    url_list.append(dest_url)


all_info = []
for url in url_list:
    result_page = parse_page(url)
    all_info.append(result_page)
    print('--------------------------')
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&')
    sleep(5)

with open('all_info.txt', 'w') as f:
    f.write(str(all_info))