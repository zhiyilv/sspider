# the task is to get info after running javascript
# save the info into an excel file

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import re
import pandas


def testjs(url):
    nojs = requests.get(url)
    soup1 = bs(nojs.content, 'lxml')
    print('from requests: {}'.format(soup1.find(class_='pf').text))

    browser = webdriver.Chrome()
    browser.get(url)
    soup2 = bs(browser.page_source, 'lxml')
    print('from ChromeDriver: {}'.format(soup2.find(class_='pf').text))
    browser.quit()

    nobrowser = webdriver.PhantomJS()
    nobrowser.get(url)
    soup3 = bs(nobrowser.page_source, 'lxml')
    print('from PhantomJS: {}'.format(soup3.find(class_='pf').text))


def testexcel():
    a = [[1, 2, 3], [4, 3, 2]]
    df = pandas.DataFrame(a, columns=['a', 'b', 'c'], index=['1st', 2])
    df.to_excel('test.xlsx', sheet_name='testSheet')


# ----------- functions from task_0718



# parse_page for parsing a page of classes
def parse_page(page_soup):
    containers = page_soup(class_='s-r-list')
    classes = [parse_c(i) for i in containers]
    return [i for i in classes if i]

def parse_c(container):
    teacher = container.find(class_='s-r-list-photo').p.text
    if teacher == '无':
        return None
    title = container.find(class_='s-r-list-info').h3.text
    price = container.find(class_='price').span.text
    intprice = int(price)
    satisfaction = container.find(class_='pf').find_all('div')[-2].text[:-1]
    intsa = int(satisfaction)
    info = container(text=re.compile('：'))[1:]
    # subject, grade, opendate, schedule, location = [i.split('：')[-1].strip() for i in info]
    info = [i.split('：')[-1].strip() for i in info]
    return [teacher, title, intprice, intsa, *info]


# using webdriver to load page
def get(url):
    nobrowser = webdriver.PhantomJS()
    nobrowser.get(url)
    return nobrowser.page_source


def save(data, filename):
    df = pandas.DataFrame(data, columns=['teacher', 'title', 'price', 'satisfaction', 'subject', 'grade', 'duration', 'time', 'location'])
    df.to_excel('{}.xlsx'.format(filename))

# --------run
start_url = 'http://ssh.speiyou.com/search/index/subject:/grade:1/level:bx/term:/gtype:time'
soup = bs(get(start_url), 'lxml')
results = parse_page(soup)
save(results, 'grade1')




