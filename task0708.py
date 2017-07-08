import requests as r
from bs4 import BeautifulSoup as bs
import re


start_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:1'
page = r.get(start_url)
soup = bs(page.content, 'lxml')

containers = soup(class_="s-r-list")
result = []
for c in containers:
    details = []
    name = c.find(class_="s-r-list-photo").p.a.text
    if name != '无':
        title = c.find(class_='s-r-list-info').h3.text
        details.append(title)
        details.append(name)
        # subject_info = c.find(class_='s-r-list-info').p('span')[0].text
        # grade_info = c.find(class_='s-r-list-info').p('span')[1].text
        details += c(text=re.compile('：'))[1:]
        result.append(details)

for index, details in enumerate(result):
    print('class {}: {}'.format(index+1, details[0]))
    print(details[1:])

