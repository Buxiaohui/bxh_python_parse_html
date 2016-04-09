import urllib
from bs4 import BeautifulSoup
import urllib.request as request_url
import urllib.parse   as psrse_data
import http.cookiejar
import re

url  = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%D5%BD%B6%B7%BB%FA&fr=ala&ori_query=%E6%88%98%E6%96%97%E6%9C%BA&ala=0&alatpl=sp&pos=0'

content = request_url.urlopen(url).read()
filename = request_url.urlretrieve(url, 'test.html')
# html_local = open("test.html")
soup_online_html = BeautifulSoup(content,"html.parser")
# soup_local_html = BeautifulSoup(html_local.read().encode("utf-8"),"html.parser")
soup_local_str = BeautifulSoup("<html>data</html>","html.parser");
# print("---")
# print(soup_online_html)
# print("---")
# print(soup_local_html)
# print("---")
# print(soup_local_str)
#app.setData('imgData', { ******* and so on
content = content.decode('utf-8')
print("----------------")
print(content)

# 获取所有imgData
# patternImgData = re.compile('\"objURL\":\"http:\/\/.*\.jpg"', re.I)
# print(patternImgData.search(content))

# 获取到所有objURL
patternImgData = re.findall('\"objURL\":\"http:\/\/\S*\.jpg"', content)
print("----------------")
print(patternImgData)
patternImgDataElementParser = re.compile('http:\/\/.*\.jpg', re.I)

for element in patternImgData:
    patternImgDataElementUrl = patternImgDataElementParser.search(element)
    print("element:"+element)
    print("patternImgDataElementUrl:" + patternImgDataElementUrl.group())
# patternImgDataObject = re.compile('\s*app\.setData\(\'imgData\'.*\);', re.I)
# imgData = pattern.search(content)


