import random

import pymysql
import requests
from bs4 import BeautifulSoup


class CarFamily(object):
    def __init__(self):
        self.url = 'https://www.autohome.com.cn/all/#pvareaid=3311230'
        self.headrs = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }
        self.cunn = pymysql.connect(port=3306,
                                    password='123456',
                                    user='root',
                                    database='xici',
                                    charset='utf8mb4',
                                    host='localhost'
                                    )
        self.cursor = self.cunn.cursor()
        self.proxy = self.get_proxy()

    def send_response(self, url):
        print('正在发送的请求是{}'.format(url))
        response = requests.get(url, headers=self.headrs,
                                proxies=self.proxy)
        return response.content

    def parse(self, content):
        source = BeautifulSoup(content, 'lxml')
        print(source.select('div id=auto-channel-lazyload-article>a>'))

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

    def run(self):
        response = self.send_response(self.url)
        self.parse(response)


if __name__ == '__main__':
    carfamily = CarFamily()
    carfamily.run()
