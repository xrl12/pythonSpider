import urllib.parse
import urllib.request
import re
# url = 'https://www.qidian.com/finish?&action=hidden&page=2'

class QiDian(object):
    def __init__(self,url):
        self.url = url
        self.heads = {
            "Cookie": "_qda_uuid=64056b98-7e07-bcd3-6924-37936195d9a4; _csrfToken=dkw61kmaGRSOL2aykhaDhNgayXsnM0ThyhPNFO7o; newstatisticUUID=1583499562_767061897; e1=%7B%22pid%22%3A%22qd_P_fin%22%2C%22eid%22%3A%22qd_C44%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_fin%22%2C%22eid%22%3A%22qd_B22%22%2C%22l2%22%3A3%2C%22l1%22%3A4%7D",
            'Referer': 'https://www.qidian.com/finish?&action=hidden&orderId=&page = 2',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.canshu = {
            'action':'hidden',
            'page':'1'
        }
        self.url1 = urllib.request.Request(url=self.parse(self.url,self.canshu),headers=self.heads)
    def send_request(self,url,canshu):
        print('我正在发送请求')
        full_url = self.parse(url,canshu)
        response = urllib.request.urlopen(full_url)
        if response.status == 200:
            # self.write_file(response.read())
            self.get_link(response.read().decode('utf8'))
        else:
            print('你的状态码是{}'.format(response.status))

    def send_datail_request(self,url):
        print('正在获取小说目录页面')
        result = urllib.request.urlopen(url)
        self.write_detail_file(result)

    def get_link(self,content):
        print('我正在获取链接')
        pattern = re.compile(r'<div class="book-img-box">.*?<a\shref="(.*?)".*?>.*?<div class="book-mid-info">.*?<h4><a.*?>(.*?)</a>',re.S)
        result = pattern.findall(content)
        for kw in result:
            data = {
                'link':kw[0],
                'name':kw[1]
            }
            self.pingjie(data.get('link'))
        print(result)

    def write_detail_file(self,content):
        with open('起点小说目录.','a') as f:
            f.write(content)
            f.close()

    def pingjie(self,url):
        # 正在拼接小说页面的路由
        print('正在拼接小说目录')
        detail_url = urllib.parse.urljoin(self.url,url)
        self.send_datail_request(detail_url)


    def parse(self,url,canshu):
        print('我正在拼接路由')
        canshu = urllib.parse.urlencode(self.canshu)
        full_url = self.url+canshu
        return full_url

    def write_file(self,content):
        print('我正在保存文件')
        with open('/home/mrxu/Desktop/起点中文网.html','wb') as f:
            f.write(content)
            f.close()

    def run(self):
        self.send_request(self.url,self.canshu)

if __name__ == '__main__':
    url = 'https://www.qidian.com/finish?'
    qidian = QiDian(url)
    qidian.run()
