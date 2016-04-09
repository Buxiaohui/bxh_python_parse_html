import urllib
from bs4 import BeautifulSoup
import urllib.request as request_url
import urllib.parse   as psrse_data
import http.cookiejar

url  = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%D5%BD%B6%B7%BB%FA&fr=ala&ori_query=%E6%88%98%E6%96%97%E6%9C%BA&ala=0&alatpl=sp&pos=0'

content = request_url.urlopen(url).read()
filename = request_url.urlretrieve(url, 'test.html')
html_local = open("test.html")
soup_online_html = BeautifulSoup(content,"html.parser")
soup_local_html = BeautifulSoup(str(html_local),"html.parser")
soup_local_str = BeautifulSoup("<html>data</html>","html.parser");
print("---")
print(soup_online_html)
print("---")
print(soup_local_html)
print("---")
print(soup_local_str)