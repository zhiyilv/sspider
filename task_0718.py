# import modules
# requests, beautifulsoup, re, time
import requests
import time
from bs4 import BeautifulSoup as bs
import re
from pprint import pprint


start_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/' \
            'term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:1'
# get all urls for different grades, store the urls into a list
# grade_urls = []
soup = bs(requests.get(start_url).content, 'lxml')
search_panel = soup.find(id='search-term')
grade_a = search_panel.find('dl')('a')[4:]
domain = 'http://ssh.speiyou.com'
grade_urls = [domain + i.get('href') for i in grade_a]


# -------------------define methods
# parse_c for parsing a container in page
def parse_c(container):
    teacher = container.find(class_='s-r-list-photo').p.text
    if teacher == '无':
        return None
    title = container.find(class_='s-r-list-info').h3.text
    price = container.find(class_='price').span.text
    info = container(text=re.compile('：'))[1:]
    # subject, grade, opendate, schedule, location = [i.split('：')[-1].strip() for i in info]
    info = [i.split('：')[-1].strip() for i in info]
    return [teacher, title, price, info]


# parse_page for parsing a page of classes
def parse_page(page_soup):
    containers = page_soup(class_='s-r-list')
    classes = [parse_c(i) for i in containers]
    return [i for i in classes if i]


# pass a grade_url, i.e. the first page of classes of a grade
# loop all pages and parse classes inside
def crawl_grade(grade_url):
    # get the number of maxpage
    soup = bs(requests.get(grade_url).content, 'lxml')
    last_url = soup.find('a', text='尾页').get('href')
    maxpage = last_url.split(':')[-1]
    # get the common url from grade_url
    common_url = domain + last_url.rstrip(maxpage)
    # create url_list
    url_list = [common_url + str(i) for i in range(2, int(maxpage)+1)]

    print('there are {} pages to crawl for this grade'.format(maxpage))

    page_class_list = [parse_page(soup)]
    print('found {} valid classes on first page'.format(len(page_class_list[0])))
    show(page_class_list[0])

    for url in url_list:
        print('in page: {}'.format(url))
        page_soup = bs(requests.get(url).content, 'lxml')
        page_class = parse_page(page_soup)

        print('found {} valid classes'.format(len(page_class)))
        show(page_class)
        page_class_list.append(page_class)

        # sleep for 5 seconds
        time.sleep(5)
    return page_class_list


# define a method to show results
def show(result):
    pprint(result)


# for each grade, crawl its all classes
# store classes for each grade as a list
# store all those lists into a list
speiyou = []
for g_url in grade_urls:
    print('\n\n Crawl grade {}'.format(g_url))
    grade_class_list = crawl_grade(g_url)  # use crawl_grade method as a blackbox
    speiyou.append(grade_class_list)
    print('finished crawling {} pages in this grade\n\n'.format(len(grade_class_list)))

with open('all.txt', 'w') as f:
    f.write(str(speiyou))










