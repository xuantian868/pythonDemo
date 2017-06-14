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

url = 'https://movie.douban.com/top250'

def fetch_page(url):
    response = requests.get(url)
    return response

def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page.decode('utf-8'))

    
    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    #取出body下属性id为content下的第一个div下的第一个div下的第二个div下的所有a标签
    xpath_pages = '//*[@id="content"]/div[1]/div[1]/div[2]/a'
    #效果与上面相同。分页的标签class属性是paginator 取第一个下的所有a标签
    #xpath_pages = '//*[@class="paginator"][1]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    #所有的翻页链接
    for p in pages:
        fetch_list.append(url + p.get('href'))#拼出的翻页链接 https://movie.douban.com/top250?start=25&filter=
        print('url:%s' % p.get('href'))
    
    def fetch_content(url):
        response = fetch_page(url)
        page = response.content
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)  
       
    threads = []
    for url in fetch_list:
        t = Thread(target=fetch_content,args=[url])
        t.start()
        threads.append(t)
            
            
    for t in threads:
        t.join()
           

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text         
        print(i, title)


def main():
    start = time()
    parse(url)
    end = time()
    print('获取豆瓣250电影信息所需时间:%d' % (end-start))
    print ('Cost {} seconds'.format((end - start)))

if __name__ == '__main__':
    main()