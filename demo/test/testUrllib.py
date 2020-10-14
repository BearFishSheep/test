# -*- coding: utf-8 -*-


import urllib.request
import urllib.parse

'''
# 获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")   # 对baidu.com信息获取的一个对象
print(response.read().decode("utf-8"))  # 对获取到的网页源码进行解码
'''

# 伪装成浏览器进行访问（封装头部）
url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}   #封装的头部
data = bytes(urllib.parse.urlencode({'name':'Annie'}), encoding='utf-8')    #参数
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req, timeout=1)
# print(response.read().decode("utf-8"))
# print(response.status)
# print(response.getheaders())
print(response.getheader('Set-Cookie'))







