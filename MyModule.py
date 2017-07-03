import requests as r
from bs4 import BeautifulSoup as bs


def get_faculty(url):
    page = r.get(url)
    s = bs(page.content, 'lxml')

    try:
        content = s.find('div', class_='page-result-list').find_all('li')
    except:
        return None

    if content:
        return [i.get_text() for i in content]
