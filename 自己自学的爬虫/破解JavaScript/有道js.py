import time
import requests
import hashlib
from random import randint


class YouDaoSpider(object):
    def __init__(self):
        self.kw = self.get_kw()
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.browers_verson = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        self.salt = self.get_salt()
        self.sign = self.get_sign()
        self.ts = self.get_ts()
        self.bv = self.get_bv()
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "251",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=642684389@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=693990345.976119; JSESSIONID=aaaO3itroGRftfGaODofx; ___rl__test__cookies=1586159477004",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

        # self.headers = {
        #     "Accept": "application/json, text/javascript, */*; q=0.01",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        #     "Connection": "keep-alive",
        #     "Content-Length": "251",
        #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        #     "Cookie": "OUTFOX_SEARCH_USER_ID=176749517@115.171.169.35; _ga=GA1.2.1662752829.1511871905; OUTFOX_SEARCH_USER_ID_NCOO=946221981.7179613; UM_distinctid=16bd730091f2af-01cf01d3c287a2-37677e02-1fa400-16bd7300920678; P_INFO=496155678@qq.com|1570068375|0|youdao_fanyi|00&99|bej&1554687101&epay#tij&null#10#0#0|&0||496155678@qq.com; _ntes_nnid=abdd37d51134afdbba36713e9ede27c0,1573051175079; JSESSIONID=aaa1gzT-kYArp6WORIl6w; ___rl__test__cookies=1574300624075",
        #     "Host": "fanyi.youdao.com",
        #     "Origin": "http://fanyi.youdao.com",
        #     "Referer": "http://fanyi.youdao.com/",
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        #     "X-Requested-With": "XMLHttpRequest",
        # }

        self.data = {
            'i': self.kw,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': self.bv,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

    def get_kw(self):
        return input('请输入您要翻译的文字')

    def get_salt(self):
        time = self.get_ts()
        random_int = str(randint(0,10))
        return time+random_int

    def get_sign(self):
        # sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        return self.get_md5("fanyideskweb" + self.kw + self.salt + "n%A-rKaT5fb[Gy?;N5@Tj")

    def get_ts(self):
        return str(int(time.time()*1000))

    def get_bv(self):
        return self.get_md5(data=self.browers_verson)


    def get_md5(self,data):

        md5 = hashlib.md5()
        md5.update(data.encode())
        return md5.hexdigest()

    def send_request(self):
        response = requests.post(url=self.url,data=self.data,headers=self.headers)
        return response.text

    def run(self):
        print('这里是kw',self.kw)
        print('这里是bv的值',self.get_bv())
        print('这里是salt的值',self.get_salt())
        print('这里是sign的值',self.get_sign())
        print('这里是ts的值',self.get_ts())
        print(self.send_request())



if __name__ == '__main__':
    yds = YouDaoSpider()
    yds.run()

