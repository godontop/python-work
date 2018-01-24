# coding=utf-8

from urllib.request import urlopen, Request

url = 'https://www.taobao.com'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

headers = {'Usre-Agent': user_agent}
page = urlopen(Request(url, data=None, headers)).read()
