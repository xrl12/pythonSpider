import urllib.request
import urllib.parse
from http.cookiejar import CookieJar
class YaoZhiSpider(object):
    def __init__(self,url):
        self.url = url
        self.member_url = 'https://www.yaozh.com/member/'
        self.from_data = {
            'username': '正在学爬虫',
            'pwd': 'xrl000824',
            'formhash': '9480122924',
            'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F'
        }
        self.heads = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            # 'Referer': 'https://www.yaozh.com/login/proxy',
        }

        self.cookiejar = CookieJar()
    def send_request(self):
        opener = self.login()
        from_data = self.parse()
        full_url = urllib.request.Request(url=self.url,data=from_data,headers=self.heads)
        response = opener.open(full_url)
        if response.status == 200:
            member_response = opener.open(self.member_url)
            self.write_file(member_response.read())
        print(response.status)

    def parse(self):
        from_data = urllib.parse.urlencode(self.from_data)
        print(from_data.encode('utf8'))
        return from_data.encode('utf8')
    def login(self):
        http_cookie_processor = urllib.request.HTTPCookieProcessor(self.cookiejar)
        opener = urllib.request.build_opener(http_cookie_processor)
        return opener

    def write_file(self,content):
        with open('../爬取数据的文档/药智网.html','wb') as f:
            f.write(content)
            f.close()

    def main(self):
        self.send_request()

if __name__ == '__main__':
    yaozhi = YaoZhiSpider('https://www.yaozh.com/login/')
    yaozhi.main()
