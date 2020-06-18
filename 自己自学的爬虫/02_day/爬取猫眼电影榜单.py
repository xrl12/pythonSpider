import urllib.request
import urllib.parse
import re
import pymysql
import csv


class MoYan(object):
    def __init__(self, url):
        self.url = url
        self.heads = {
            'Referer': 'https://maoyan.com/board/4?offset=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }


        self.conn = pymysql.connect(host="localhost", user="root",
                               password="123456", database="maoyan",
                               charset="utf8")

        self.cursor = self.conn.cursor()
        self.scv_f = open('电影排行榜.csv','a')
        self.scv_head = ['pic','name','actor','time','brking','peiming']
        self.write = csv.DictWriter(self.scv_f,self.scv_head)
    def send_request(self,page):
        print('正在发送请求')
        request = self.parse()
        response = urllib.request.urlopen(request)
        # self.write_file(response.read())
        self.write_file(response.read(),page)

    def parse(self):
        print("正在对路由进行编译")
        canshu = urllib.parse.urlencode(self.kw)
        full_url = urllib.request.Request(url=self.url + canshu, headers=self.heads)
        return full_url
    def write_csv(self,content):
        self.write.writerow(content)
    def write_file(self, content,page):
        print('正在保存文件')
        with open('猫眼榜单{}.html'.format(page), 'wb') as f:
            f.write(content)
            f.close()
        self.get_data()

    def get_data(self):
        print("正在使用正则获取指定数据")
        with open('猫眼榜单1.html', 'r+') as f:
            data = f.readlines()
            data1 = ''.join(data)
            f.close()
        pattern = re.compile(
            r'<dd>.*?<i.*?>(.*?)<.*?<img\sdata-src="(.*?)".*? <p class="name"><a.*?>(.*?)<.*?<p class="star">(.*?)<.*?<p class="releasetime">(.*?)<.*?<p class="score"><i.*?>(.*?)</i><i class="fraction">(.*?)<.*?</dd>',
            re.S)
        result = pattern.findall(data1)
        for i in result:
            mv = {
                'pic': i[1],
                'name': i[2],
                'actor': i[3],
                'time': i[4],
                'brking': i[5] + i[6],
                'peiming': i[0]
            }
            # self.write_sql(mv,)
            self.write_csv(mv)
    def write_sql(self, data):
        # 连接数据库
        print('data的数据有', data)
        conn = pymysql.connect(host="localhost", user="root",
                               password="123456", database="maoyan",
                               charset="utf8")

        sql = 'insert into db_move(%s) values(%s)' % (
            ','.join([key for key in data.keys()]), ','.join(['%s'] * (len(data)))
        )
        self.cursor.execute(sql,[values for values in data.values()])
        self.conn.commit()

    def start(self):

        for i in range(1, 11):

            self.kw = {
                'offset': (i-1)*10
            }
            self.send_request(i)

        # self.get_data()


if __name__ == '__main__':
    # https://maoyan.com/board/4?offset=10
    moyan = MoYan('https://maoyan.com/board/4?')
    moyan.start()



