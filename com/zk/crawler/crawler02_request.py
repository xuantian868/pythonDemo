# -*- coding: utf-8 -*-
'''
Created on 2017-6-13

使用requests获取豆瓣250部电影信息
与urllib区别 获取时
 response = requests.get(url)
读取内容是用 response.content
@author: Administrator
'''
import requests
from lxml import etree
from time import time

url = 'https://movie.douban.com/top250'

def fetch_page(url):
    response = requests.get(url)
    return response

def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page.decode('utf-8'))

    '''
    <p style="font-size: 200%">World News only on this page</p>
　　　　Ah, and here's some more text, by the way.
　　　　<p>... and this is a parsed fragment ...</p>

p = page.xpath(u"//p[@style='font-size:200%']")
这样就取出了body里style为font-size:200%的p节点，
注意：这个p变量是一个lxml.etree._Element对象列表，
p[0].text结果为World News only on this page，即标签之间的值；
p[0].values()结果为font-size: 200%，即所有属性值。
其中 @style表示属性style，类似地还可以使用如@name, @id, @value, @href, @src, @class....

如果标签里面没有属性怎么办？那就可以用text()，position()等函数来过滤，
函数text()的意思则是取得节点包含的文本。比如：<div>hello<p>world</p>< /div>中，
用"div[text()='hello']"即可取得这个div，而world则是p的text()。
函数position()的意思是取得节点的位置。比如“li[position()=2]”表示取得第二个li节点，
它也可以被省略为“li[2]
比如“ul/li[5][@name='hello']”表示取ul下第五项li，并且其name必须是hello，否则返回空。

“*”可以代替所有的节点名，比如用"/html/body/*/span"可以取出body下第二级的所有span，而不管它上一级是div还是p或是其它什么东东
而 “descendant::”前缀可以指代任意多层的中间节点，它也可以被省略成一个“/”。
比如在整个HTML文档中查找id为“leftmenu”的 div，可以用“/descendant::div[@id='leftmenu']”，也可以简单地使用“ //div[@id='leftmenu']””。
    
    '''
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
        
    for url in fetch_list:
        response = fetch_page(url)
        page = response.content
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

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