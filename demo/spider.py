# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup       # 网页解析，获取数据
import re                           # 正则表达式，进行文字匹配
import urllib.request, urllib.error # 指定URL，获取网页数据
import xlwt                         # 进行excel操作
import sqlite3                      # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    savepath = ".\\Top250.xls"  # 保存路径

    #1.爬取网页


    #3.保存数据

    askURL("https://movie.douban.com/top250?start=0")
#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(10):
        url = baseurl + str(i*25)
        html = askURL(url)

        #2.逐一解析数据


    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head = {        #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
                    #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器（伪装成浏览器），本质上是告诉浏览器，我们可以接收什么水平的文件内容
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print("code : " + str(e.code))
        if hasattr(e, "reason"):
            print("reason : " + str(e.reason))

    # return html




#保存数据
def saveData(savepath):
    print("save...")


if __name__ == '__main__':
    main()








