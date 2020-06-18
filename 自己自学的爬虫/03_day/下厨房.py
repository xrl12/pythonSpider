import requests
import pymysql
from lxml import etree
import random
import urllib.parse
import re


class XiaChuFangSprider(object):
    def __init__(self):
        self.url = 'http://www.xiachufang.com/category/40076/'
        self.cunn = pymysql.connect(port=3306,
                                    password='123456',
                                    user='root',
                                    database='xici',
                                    charset='utf8mb4',
                                    host='localhost'
                                    )
        self.cursor = self.cunn.cursor()
        self.proxy = self.get_proxy()
        self.heads = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }

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

    def send_request(self, url):
        print('这在发送的请求是{}'.format(url))
        response = requests.get(url, headers=self.heads, proxies=self.proxy)
        if response.status_code == 200:
            return response

    def parse(self, response):
        print('正在解析配置文件')
        html = etree.HTML(response.content)
        link_detail = html.xpath(
            "//ul[@class='list']/li/div[@class='recipe recipe-215-horizontal pure-g image-link display-block']/a/@href")
        for link_details in link_detail:
            detail_full_link = urllib.parse.urljoin(self.url, link_details)
            detail_response = self.send_request(detail_full_link)
            detail_html = etree.HTML(detail_response.content)

            cai_name = detail_html.xpath("//h1[@class='page-title']/text()")
            img_link = detail_html.xpath("//div[@class='cover image expandable block-negative-margin']/img/@src")[0]
            zuoliaos = detail_html.xpath("//tr[contains(@itemprop,'recipeIngredient')]")
            step = detail_html.xpath("//div[@class='steps']//li[@class='container']/p[@class='text']/text()")
            all_zl = ''
            for zuoliao in zuoliaos:
                zl = zuoliao.xpath(".//td//text()")
                all_zl += ','.join(zl).replace('\n', '').replace(' ', '')

            self.write_sql(cai_name, img_link, all_zl, step)

    def write_sql(self, cai_name, img_link, all_zl, step):
        print('正在往数据库里面存取数据')
        caiping_list = []
        cai_name_str = ''.join(cai_name).replace('\n', '').replace(' ', '')
        step_str = ''.join(step).replace('\n', '').replace(' ', '')
        print(cai_name_str, img_link, all_zl, step_str)
        caiping_list.append(cai_name_str)
        caiping_list.append(img_link)
        caiping_list.append(all_zl)
        caiping_list.append(step_str)
        print(caiping_list)
        sql = 'use xiachufang;'
        self.cursor.execute(sql)
        self.cunn.commit()

        sql = 'insert into caiping values (%s,%s,%s,%s);'
        self.cursor.execute(sql, [value for value in caiping_list])
        self.cunn.commit()


if __name__ == '__main__':
    xcf = XiaChuFangSprider()
    response = xcf.send_request(xcf.url)
    xcf.parse(response)

#     create database caiping ( cai_name varchar(20), img_link varchar(255), zuoliao varchar(200));
