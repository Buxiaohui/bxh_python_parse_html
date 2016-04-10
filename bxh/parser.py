import urllib
from bs4 import BeautifulSoup
import urllib.request as request_url
import urllib.parse   as psrse_data
import http.cookiejar
import re
import os
import mysql.connector

url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%D5%BD%B6%B7%BB%FA&fr=ala&ori_query=%E6%88%98%E6%96%97%E6%9C%BA&ala=0&alatpl=sp&pos=0'

content = request_url.urlopen(url).read()
filename = request_url.urlretrieve(url, 'test.html')
# html_local = open("test.html")
soup_online_html = BeautifulSoup(content, "html.parser")
# soup_local_html = BeautifulSoup(html_local.read().encode("utf-8"),"html.parser")
soup_local_str = BeautifulSoup("<html>data</html>", "html.parser");
# print("---")
# print(soup_online_html)
# print("---")
# print(soup_local_html)
# print("---")
# print(soup_local_str)
# app.setData('imgData', { ******* and so on
content = content.decode('utf-8')
print("----------------")
print(content)

# 获取所有imgData
# patternImgData = re.compile('\"objURL\":\"http:\/\/.*\.jpg"', re.I)
# print(patternImgData.search(content))

# 获取到所有objURL
patternImgData = re.findall('\"objURL\":\"http:\/\/\S*\.jpg"', content)
print("----------------")
# print(patternImgData)
patternImgDataElementParser = re.compile('http:\/\/.*\.jpg', re.I)
# patternImgDataObject = re.compile('\s*app\.setData\(\'imgData\'.*\);', re.I)
# imgData = pattern.search(content)

config = {'host': '127.0.0.1',  # 默认127.0.0.1
          'user': 'root',
          'password': '',
          'port': 3306,  # 默认即为3306
          'database': 'python_test',
          'charset': 'utf8'  # 默认即为utf8
          }
# 这个方式也有效
cnx = mysql.connector.connect(**config)
# cnx = mysql.connector.connect(user ='root', password= '123456', host = 'localhost',port='3306', database='python_test')
cursor = cnx.cursor()


def insert(sql):
    try:
        cursor.execute(sql)
        cnx.commit()
        print("insert success")
    except mysql.connector.Error as err:
        print("insert table 'mytable' failed.")
        print("Error: {}".format(err.msg))
        # sys.exit()


for element in patternImgData:
    patternImgDataElementUrl = patternImgDataElementParser.search(element)
    print("element:" + element)

    url_temp = patternImgDataElementUrl.group()
    index_temp = patternImgData.index(element)
    # insert_sql = "INSERT INTO image(url) VALUES ("+str(url_temp)+")"
    # print("insert_sql:"+insert_sql)
    # cursor.execute(insert_sql)
    print("patternImgDataElementUrl:" + patternImgDataElementUrl.group())
    sql = "INSERT INTO image (url) VALUES ('{}')".format(url_temp)
    print("sql:" + sql)

    # save image to disk,image can not display
    # conn = urllib.request.urlopen(url)
    # f = open('E:\\'+str(index_temp)+'.jpg', 'wb')
    # f.write(conn.read())
    # f.close()
    # so i decide to use urllib
    try:
        urllib.request.urlretrieve(url_temp,str(index_temp)+'.jpg')
    except urllib.request.HTTPError as e:
        print('download erro index:'+str(index_temp))
        print(e.code)
        print('Reason: ', e.reason)
    except urllib.request.URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)


# insert to db
insert(sql)



cursor.close()
cnx.close()


def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()

    
#save to local file
url= url+patternImgDataElementUrl.group()+'\n'
save('image_url.txt', url)
