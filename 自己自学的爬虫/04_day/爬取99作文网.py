import random
import urllib.parse
import urllib.request
from time import sleep

import pymysql
from lxml import etree


class NineDocument(object):
    def __init__(self):
        self.url = 'https://www.99zuowen.com/xiaoxuezuowen/'
        self.heads = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }
        self.connect = pymysql.connect(password='123456', user='root', port=3306, database='xici', charset='utf8mb4',
                                       host='localhost')
        self.cursor = self.connect.cursor()
        self.proxy = self.get_proxy()

    def send_response(self, url):
        print('正在发送请求的路由是{}'.format(url))
        proxy = urllib.request.ProxyHandler(self.proxy)
        sleep(10)
        opener = urllib.request.build_opener(proxy)
        response = opener.open(url)
        if response:
            return response

    def parse(self, content):
        print('正在获取标签页的路由')
        html = etree.HTML(content)
        tag_url = html.xpath(
            "//div[@class='main_box main_si clearfix']/div[@class='col260']/dl[@class='type_list2'][1]/dd//a/@href")[
                  0:2]
        for url in tag_url:
            tag_tag_url = urllib.parse.urljoin(self.url, url)
            print('生成的路由是{}'.format(tag_tag_url))
            response = self.send_response(tag_tag_url)
            self.tag_parse(response.read())

    def tag_parse(self, content):
        print('正在获取详情页的路由')
        html = etree.HTML(content)
        detail_url = html.xpath("//ul/li[@class='lis']/h4/a/@href")
        for url in detail_url:
            response = self.send_response(url)
            html = etree.HTML(response.read())
            detail_title = html.xpath("//div[@id='left']//div[@class='title']/h1/text()")
            detail_content = html.xpath("//div[@class='content']/div//p/text()")

            title = ''.join(detail_title).split('_')[0]
            content = ''.join(detail_content)
            self.write_sql(content,title)

    def write_sql(self, contnet, title):
        print('正在往数据库里面存数据')
        sql = 'use zuowenwnag'
        self.cursor.execute(sql)
        self.connect.commit()
        sql = 'insert into document values (%s,%s)'
        self.cursor.execute(sql, [title, contnet])
        self.connect.commit()


    def get_proxy(self):
        sql = 'select * from proxy'
        self.cursor.execute(sql)
        proxy_all = self.cursor.fetchall()
        proxy_one = random.choice(proxy_all)
        proxy = {
            proxy_one[2]: str(proxy_one[0]) + ':' + str(proxy_one[1])
        }
        print('使用的代理', proxy)
        return proxy

    def run(self, url):
        response = self.send_response(url)
        self.parse(response.read())


if __name__ == '__main__':
    ninedocument = NineDocument()
    ninedocument.run('https://www.99zuowen.com/xiaoxuezuowen/')
