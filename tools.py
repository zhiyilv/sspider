import requests
import time
from bs4 import BeautifulSoup as bs
import re
from pprint import pprint

domain = 'http://ssh.speiyou.com'
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


# parse_page for parsing a page of classes
def parse_page(page_soup):
    containers = page_soup(class_='s-r-list')
    classes = [parse_c(i) for i in containers]
    return [i for i in classes if i]