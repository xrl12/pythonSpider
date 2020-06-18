import urllib.request
import urllib.parse
import pymysql
from random import choice
import re

class WangZheSpider():
    def __init__(self):
        self.connect = pymysql.connect( host='localhost', user='root', password="123456",
                 database='xici', port=3306,charset='utf8',)
        self.cursor = self.connect.cursor()
        self.proxy = self.get_proxy()
        self.headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like GeckoChrome/63.0.3239.132 Safari/537.36 QIHU 360SE")

    def send_request(self,url):
        headler = urllib.request.ProxyHandler()
        opener = urllib.request.build_opener(headler)
        opener.add_handler = [self.headers]
        response = opener.open(url)
        return response.read()

    def parse_detail_url(self,url,response):
        pattern = re.compile(r'<a href="(herodetail/\d+\..*?)".*?>',re.S)
        li_list = pattern.findall(response.decode('gbk'))
        # for li in li_list:
        #     hero_detail_img = urllib.parse.urljoin(url,li)
        #     print(hero_detail_img)
        #     response = self.send_request(hero_detail_img)
        return li_list

        # self.write(response)

    def write(self,contnet):
        with open('王者.html','wb' ) as f:
            f.write(contnet)
            f.close()


    def get_proxy(self):
        sql = 'select * from proxy'
        self.cursor.execute(sql)
        proxy = self.cursor.fetchall()
        random_proxy = choice(proxy)
        one_proxy = {
            random_proxy[2] : random_proxy[0]+':'+str(random_proxy[1])
        }
        print('正在是使用的代理是{}'.format(one_proxy))
        return one_proxy

    def start(self):
        url = 'https://pvp.qq.com/web201605/herolist.shtml'
        response = self.send_request(url)
        hero_detail_url = self.parse_detail_url(url,response)
        for detail_url in hero_detail_url:
            full_url = urllib.parse.urljoin(url,detail_url)
            response = self.send_request(full_url)
            self.write(response)


if __name__ == '__main__':
    wzs = WangZheSpider()
    wzs.start()
