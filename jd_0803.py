import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd


myheader= {
'Host':'passport.jd.com',
'Upgrade-Insecure-Requests':'1',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,fr;q=0.2',
'Cache-Control':'max-age=0'
}

jd_login_url = 'https://passport.jd.com/new/login.aspx'


wd.Chrome


session = requests.session()
login_page = session.get(jd_login_url, headers=myheader)


