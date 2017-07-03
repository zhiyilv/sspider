import requests as r


myheaders = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate, sdch, br',
             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,fr;q=0.2',
             'Cache-Control': 'max-age=0',
             'Connection': 'keep-alive',
             'Cookie': 'd_c0="ABDChjHQVwuPTkVOCEgsAkpJeeR-aAUzjwU=|1487651608"; _zap=faad60dc-4b3b-4e36-a459-528db336b7de; r_cap_id="NTdiNTM0NTY1MTBlNDg3NjgzMmFhMjg2MTE4Y2RjM2M=|1495777428|ce0a9be94f0d7f6fbcef002da2262d214e54dd48"; cap_id="MjAxNjg1NmJlMDZkNDRiMzlhOTdhZmI3YTk0N2U0MDQ=|1495777428|dcc73336c2764f18103a1b20ea81a0cec22f75e2"; q_c1=45bc79e44964498b8ef3d06f38335459|1495869568000|1487651608000; _xsrf=98a0f2adf6f33fc8e8f8163fd5738cd2; z_c0=Mi4wQUFBQWJ0VVpBQUFBRU1LR01kQlhDeGNBQUFCaEFsVk5wMDFQV1FEejNJcWIwVkw1c0h5TUluWTBpQzN5TGdwcmJn|1497507436|01284eec207e195dea99841cd795e1aa73849ad6; __utma=51854390.454033745.1495707426.1498024604.1498032684.97; __utmb=51854390.0.10.1498032684; __utmc=51854390; __utmz=51854390.1497255110.71.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20121101=1^3=entry_date=20121101=1; _xsrf=98a0f2adf6f33fc8e8f8163fd5738cd2',
             'Host': 'www.zhihu.com',
             'Referer': 'https://www.zhihu.com/',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36}'
             }

url = 'https://www.zhihu.com/people/luokeke/activities'

page = r.get(url, headers=myheaders)

print(page.text)