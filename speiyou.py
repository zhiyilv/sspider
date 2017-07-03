import requests as r
from bs4 import BeautifulSoup as bs
import re
from time import sleep


class teacher():
    def __init__(self, n, u, taught_class=None):
        self.name = n
        self.url = u
        if taught_class:
            self.classes = [taught_class]
        else:
            self.classes =[]

    def add_class(self, class_id):
        if class_id not in self.classes:
            self.classes.append(class_id)


class detailedClass:
    def __init__(self, i, t, s, g, time_op, time_on, loc):
        self.iden = i
        self.title = t
        self.subject = s
        self.grade = g
        self.time_open = time_op
        self.time_on = time_on
        self.location = loc


def parse_page(s):
    ts = []
    cs = []
    containers = s.find_all('div', class_='s-r-list')
    for c in containers:
        tea, cla = parse_container(c)
        if tea != None and cla != None:
            ts.append(tea)
            cs.append(cla)
    return ts, cs


def parse_container(c):
    name = c.find(class_='s-r-list-photo').p.text
    if name == '无':
        return None, None

    # cla_id = c.get('id')
    cla_id = c.find('h3').a.get('href').split('/')[-1]
    if cla_id == '':
        return None, None

    t_url = c.find(class_='s-r-list-photo').a.get('href')
    tea = teacher(name, t_url, cla_id)

    title = c.find('h3').text
    subject = c.find(text=re.compile('学科：')).split('：')[1].strip()
    grade = c.find(text=re.compile('年级：')).split('：')[1].strip()
    time_open = c.find(text=re.compile('开课日期：')).split('：')[1].strip()
    time_on = c.find(text=re.compile('上课时间：')).split('：')[1].strip()
    loc = c.find(text=re.compile('上课地点：')).split('：')[1].strip()

    cls = detailedClass(cla_id, title, subject, grade, time_open, time_on, loc)

    return tea, cls


start_url = 'http://ssh.speiyou.com/search/index/grade:1/subject:/level:bx/term:/period:/teaid:/m:/d:/time:/bg:n/nu:/service:/curpage:1'
teachers = []
classes = []

page = r.get(start_url)
soup = bs(page.content, 'lxml')
last_page = int(soup.find('a', text=re.compile('尾页')).get('href').split(':')[-1])


for index in range(1, last_page):
    t_in_page, c_in_page = parse_page(soup)
    teachers += t_in_page
    classes += c_in_page

    next_url = start_url[:-1] + str(index+1)
    print('parsed page {}, sleep for 10 secs'.format(index))
    sleep(10)
    try:
        page = r.get(next_url)
    except:
        print('fail to get {}'.format(next_url))
        break
    else:
        soup = bs(page.content, 'lxml')
