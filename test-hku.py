from MyModule import *


url_facility = 'http://hku.hk/faculties/'
page = r.get(url_facility)
soup = bs(page.content, 'lxml')

faculty = dict()
url_spans = soup.find_all('div', class_='directory-page typeface-js')[0].find_all('span')
for element in url_spans:
    href = element.a.get('href')
    letter = href[-6]
    url = 'http://hku.hk' + href
    faculty[letter] = url

# or simply
alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]
# url_alphabets = ['http://hku.hk/faculties/{}.html'.format(i) for i in alphabets]

# for key in faculty.keys():
for key in alphabets:
    all_f = get_faculty(faculty[key])
    print(key + ': ')
    print(all_f)
    faculty[key] = all_f

