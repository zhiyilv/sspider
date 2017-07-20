import requests as r
from bs4 import BeautifulSoup as bs
import re

start_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/' \
            'term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:2'
page = r.get(start_url)
soup = bs(page.content, 'lxml')






#
#
# numbers = []
# prices = soup.find_all(class_='price')
# for price in prices:
#     number = price.span.text
#     numbers.append(number)
#
# # numbers = [price.span.text for price in prices]
#
# print(numbers)



containers = soup.find_all(class_='s-r-list')
index=1
for c in containers:
    details = []
    name = c.select('p > a')[0].text
    if name == '无':
        continue
    details.append(name)

    title = c.select('h3 > a')[0].text

    for a in c.find_all(text=re.compile('：'))[1:]:
        details.append(a)

    print('Class{}: {}'.format(index, title))
    print(details)
    index = index+1













