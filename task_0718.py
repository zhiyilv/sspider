# import modules
# requests, beautifulsoup, re, time
import requests
import time
from bs4 import BeautifulSoup as bs
import re
from pprint import pprint
from tools import *


start_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/' \
            'term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:1'
# get all urls for different grades, store the urls into a list
# grade_urls = []
soup = bs(requests.get(start_url).content, 'lxml')
search_panel = soup.find(id='search-term')
grade_a = search_panel.find('dl')('a')

grade_urls = [domain + i.get('href') for i in grade_a]

# for each grade, crawl its all classes
# store classes for each grade as a list
# store all those lists into a list
speiyou = []
for g_url in grade_urls[1:]:
    print('\n\n Crawl grade {}'.format(g_url))
    grade_class_list = crawl_grade(g_url)  # use crawl_grade method as a blackbox
    speiyou.append(grade_class_list)
    print('finished crawling {} pages in this grade\n\n'.format(len(grade_class_list)))

with open('all.txt', 'w') as f:
    f.write(str(speiyou))










