import urllib.request
import urllib.parse
import csv
import pymysql
import re


class Xici(object):
    def __init__(self, url, page):
        self.url = url
        self.canshu = page
        self.headrs = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTlmNTAyYzI3NzUyNmFmNjEyODE3ZmFmYjI1ZTVlZGI5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXNUekpWN21aZktaclpqOC9NMHVhdVlwWmtjQktabWFrWlFmYnZCdFp1Q289BjsARg%3D%3D--531c7e0dde1900ea3029cc09d98ed72054837361; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1583565985; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1583570281'
        }
        self.conn = pymysql.connect(host="localhost", user="root",
                                    password="123456", database="xici",
                                    charset="utf8")

        self.cursor = self.conn.cursor()
        self.scv_f = open('../爬取数据的文档/xici代理.csv', 'a')
        self.scv_head = ['ip', 'port', 'protocol']
        self.write = csv.DictWriter(self.scv_f, self.scv_head)
        self.proxy_list = []

    def send_request(self, url):
        # 我正在发送请求
        full_url = self.get_url(url)
        response = urllib.request.urlopen(full_url)
        self.parse(response.read().decode('utf8'))


    def get_url(self, url):
        # 我正在拼接路由
        canshu = urllib.parse.quote(self.canshu)
        full_url = urllib.request.Request(url=url + canshu, headers=self.headrs)
        print('这个是图片地址', full_url)
        urllib.request.Request()
        return full_url

    def parse(self, content):
        print('我正在匹配数据')
        print(content)
        pattern = re.compile(r'<tr.*?>.*?<td>(\d.*?)<.*?<td>(\d+)<.*?<td>(HTTP|HTTPS).*?</tr>', re.S)
        result = pattern.findall(content)
        print(result)
        for info in result:
            kw = {
                'ip': info[0],
                'port': info[1],
                'protocol': info[2]
            }
            temporary_dict = {}
            temporary_dict['type']=kw.get('protocol')
            temporary_dict['ip'] = kw.get('ip')+':'+kw.get('port')
            self.proxy_list.append(temporary_dict)
            # self.write_mysql(kw)
            # self.write_csv(kw)
        print(self.proxy_list)


    def write_json(self,content):
        with open('../爬取数据的文档/xici代理.json','w') as f:
            f.write(content)
            f.close()


    def write_mysql(self, content):
        sql = 'insert into proxy(%s) values(%s)' % (
            ','.join([keys for keys in content.keys()]), ','.join(['%s'] * len(content.values()))
        )
        self.cursor.execute(sql, [values for values in content.values()])
        self.conn.commit()

    def write_csv(self, content):
        self.write.writerow(content)

    def run(self):
        self.send_request(self.url)


if __name__ == '__main__':
    for i in range(1, 2):
        print('正在爬取第{}页'.format(i))
        url = 'https://www.xicidaili.com/nn/'
        xici = Xici(url, str(i))
        xici.run()
    xici.write_json(xici.proxy_list)
