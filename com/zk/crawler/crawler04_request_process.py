# -*- coding: utf-8 -*-
'''
Created on 2017-6-13

多线程方式获取和requests获取豆瓣250部电影信息
多线程有效的解决了阻塞等待的问题
@author: Administrator
'''
import requests
from lxml import etree
from time import time
from threading import Thread
import pymysql
import urllib.request

url = 'https://movie.douban.com/top250'

def fetch_page(url):
    response = requests.get(url)
    return response



def saveImg(imageURL,fileName):
     u = urllib.request.urlopen(imageURL)
     data = u.read()
     f = open("c:/flv/"+fileName, 'wb')
     f.write(data)
     f.close()

def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page.decode('utf-8'))

    
    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_img = './/div[@class="pic"]/*/img'
    #取出body下属性id为content下的第一个div下的第一个div下的第二个div下的所有a标签
    xpath_pages = '//*[@id="content"]/div[1]/div[1]/div[2]/a'
    #效果与上面相同。分页的标签class属性是paginator 取第一个下的所有a标签
    #xpath_pages = '//*[@class="paginator"][1]/a'
    
    movieEles = []
    #第一页的电影
    for m in html.xpath(xpath_movie):
        movieEles.append(m)

    pages = []
    pageEles = html.xpath(xpath_pages)
    for p in pageEles:
        pages.append(url+p.get('href'))
        print(p.get('href'))
        
    
    def paseUrl(url):
        response = fetch_page(url)
        content = response.content;
        html = etree.HTML(content)
        for m in html.xpath(xpath_movie):
            movieEles.append(m)
        
    threads = []
    for p in pages:
        thread = Thread(target=paseUrl,args=[url])
        thread.start()
        threads.append(thread)
        
    
    for thread in threads:
        thread.join()
    
    for i,m in enumerate(movieEles,1):
        title = m.find(xpath_title).text
        print('movie %d %s'% (i,title))
    

    


def main():
    start = time()
    parse(url)
    end = time()
    print('获取豆瓣250电影信息所需时间:%d' % (end-start))
    print ('Cost {} seconds'.format((end - start)))

if __name__ == '__main__':
    main()