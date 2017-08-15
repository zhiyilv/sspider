from selenium import webdriver as wd
import pickle
import os
import time
from bs4 import BeautifulSoup as bs


jd_url = 'http://www.jd.com/'
login_url = 'https://passport.jd.com/login.aspx'
myorder_url = 'http://order.jd.com/center/list.action'
mycookie_file = 'jd_zhiyilv_cookies.pkl'


def login_first_time():
    browser = wd.Chrome()
    global mycookie_file
    if input('have you logged in? y/n: ') == 'y':
        save_cookies(browser, mycookie_file)
        return browser
    else:
        raise ValueError('you should login manually for the first time')


def load_cookies(browser, cookie_file):
    cookies = pickle.load(open(cookie_file, 'rb'))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
    time.sleep(3)
    return browser


def save_cookies(browser, cookie_file):
    pickle.dump(browser.get_cookies(), open(cookie_file, 'wb'))

# -------- main process ------------
if mycookie_file not in os.listdir('.//'):
    mybrowser = login_first_time()
else:
    mybrowser = wd.Chrome()
    mybrowser.get(jd_url)
    mybrowser = load_cookies(mybrowser, mycookie_file)

mybrowser.get(myorder_url)

time.sleep(3)  # wait for page to finish loading

soup = bs(mybrowser.page_source, 'lxml')
print('The most recent order has the following items:')
for item in soup.tbody(class_='tr-bd'):
    name = item.text.strip().split('\n')[0]
    print(name)








