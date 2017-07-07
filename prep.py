import requests as r
from bs4 import BeautifulSoup as bs

start_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/' \
            'term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:1'
page = r.get(start_url)
soup = bs(page.content, 'lxml')









