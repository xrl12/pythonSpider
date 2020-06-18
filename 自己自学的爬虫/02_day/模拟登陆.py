import urllib.request
import urllib.parse
from http.cookiejar import CookieJar
import random


class YanZhengSpider(object):
    def __init__(self):
        self.heards = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Referer': 'http://182.92.188.50/login/',
            'Cookie': 'csrftoken = g1PMs7ZVPNo6HKwtE5A30R2fjFGhXYnPofu1CrXiJoS1e7VRMF32bWhcPS2ORtUB'
        }
        self.froms = {
            'csrfmiddlewaretoken': 'cQM0pfHhXYAfXmvejUWcug1HhXoEvYV8k4rfzzFERz4auJUCrupbFlgENaKbptsU',
            'name': 'mrxu',
            'pwd': '123456'
        }
        self.cookjia = CookieJar()

    def send_request(self):
        # all_proxy = self.get_proxy()
        # randon_proxy = random.choice(all_proxy)
        # print(randon_proxy)
        # list_proxy = randon_proxy.split(',')
        # proxy = {
        #     list_proxy[2][0:4]: list_proxy[0] + ':' + list_proxy[1]
        # }
        # proxy_handler = urllib.request.ProxyHandler(proxy)
        # opener = urllib.request.build_opener(proxy_handler)
        # response = opener.open(request)

        login_url = ' http://182.92.188.50/login/'
        url = 'http://182.92.188.50/'
        froms = urllib.parse.urlencode(self.froms).encode('utf8')
        HTTPCookieProcessor = urllib.request.HTTPCookieProcessor(self.cookjia)
        opener = urllib.request.build_opener(HTTPCookieProcessor)
        request = urllib.request.Request(url=login_url, data=froms, headers=self.heards)
        response = opener.open(request)
        print(response.info())
        print(self.cookjia)

    def parse(self):
        pass

    # def get_proxy(self):
    #     with open('../爬取数据的文档/xici代理.csv', 'r') as f:
    #         data = f.readlines()
    #         print(data)
    #         return data

    def run(self):
        pass


if __name__ == '__main__':
    yanzheng = YanZhengSpider()
    # yanzheng.run()
    # yanzheng.get_proxy()
    yanzheng.send_request()
