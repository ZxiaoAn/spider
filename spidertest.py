# __author__ = 'lecheng'
# -*- coding: UTF-8 -*-

import io
import sys
from urllib import request
import chardet
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
	file = open('58租房爬取.txt', 'w', encoding='utf-8')
	url = "http://g.58.com/j-glchicago/glchuzu/?PGTID=0d000000-050c-5794-b843-0f784bc7d41b&ClickID=1"
	proxy = {'http': '223.221.203.53:4310'}
	proxy_support = request.ProxyHandler(proxy)
	opener = request.build_opener(proxy_support)
	opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0')]
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
	request.install_opener(opener)
	response = request.urlopen(url, timeout=600)
	html = response.read()
	charset = chardet.detect(html)
	html = html.decode(charset["encoding"])
	soup = BeautifulSoup(html, 'html.parser')
	for child in soup.find_all('div', class_='info'):
		url_next = child.a.get('href')
		response_next = request.urlopen(url_next)
		html_next = response_next.read()
		charset = chardet.detect(html_next)
		html_next = html_next.decode(charset["encoding"])
		soup_next = BeautifulSoup(html_next, 'html.parser')
		for child_next in soup_next.find_all('div', class_='com-para'):
			if child_next.p!= None:
				d = re.sub('<[^>]+>', '', str(child_next))
				print(d.string)
	file.close()