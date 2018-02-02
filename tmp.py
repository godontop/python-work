# coding=utf-8
# Python 3 source code

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.whatismybrowser.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) \
Gecko/20100101 Firefox/58.0'
}

req = Request(url)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
myuseragent = soup.find_all('div', class_="user-agent")[0].a.get_text()
print(myuseragent)
