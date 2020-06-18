import requests
import urllib.parse
from threading import Thread
from multiprocessing import Queue
from time import sleep
from uuid import uuid4
import re


#  生产者
class ShenCanZhe(Thread):
    def __init__(self, name,parems_queue,url,data_queue):
        super().__init__()
        self.name = name
        self.parems = parems_queue
        self.url = url
        self.data_queue = data_queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }


    def run(self):
        while not self.parems.empty():
            data = self.parems.get()
            if isinstance(data,dict):
                print('参数的队列里面有{},这是{}进行工作的'.format(data,self.name))
                response = requests.post(url=self.url,data=data,headers=self.headers)
                print(response.text)
                self.data_queue.put(response.text)
            else:
                url = self.parems.get()
                response = requests.get(url)
                self.data_queue.put(response.content)
            sleep(1)




class XiaoFeiZhe(Thread):
    def __init__(self, name,data_queue,parems_queue):
        super(XiaoFeiZhe, self).__init__()
        self.name = name
        self.data_queue = data_queue
        self.parems_queue = parems_queue

    def run(self):
       while True:
           if not self.data_queue.empty() and not self.parems_queue.empty():
               data = self.data_queue.get()
               if isinstance(data,str):
                   print('这个是返回来response数据{},他的工作者是{}'.format(data,self.name))
                   # "image":"https:\/\/at1.jyimg.com\/86\/93\/c49c132c61152c3b3fae87249e6f\/c49c132c6_1_avatar_p.jpg"
                   pattern = re.compile(r'"image":"(.*?)"')
                   url_list = pattern.findall(data)
                   for url in url_list:
                       img_url = url.replace("\\","")
                       # print('图片的路由是：',img_url)
                       self.parems_queue.put(img_url)
               else:
                   self.save(content=data)
               sleep(1)
    def save(self,content):
        print('我正在保存图片')
        uuid = uuid4()
        with open('佳缘/'+str(uuid)+'.jpg','wb') as f:
            f.write(content)
            f.close()




class JiaYuanSpider(object):
    def __init__(self):
        self.url = 'https://search.jiayuan.com/v2/search_v2.php'
        self.parems_queue = Queue()  # 参数队列
        self.data_queue = Queue()  # 返回的数据的队列
        for i in range(1,4):
            self.data = {
                'sex': 'f',
                'key': '%E5%BC%80%E6%9C%97',
                'stc': '1: 14, 2: 27.36, 3: 173.184, 23: 1',
                'sn': 'default',
                'sv': '1',
                'p': str(i),
                'f': '',
                'listStyle': 'bigPhoto',
                'pri_uid': '181015784',
                'jsversion': 'v5',
            }
            self.parems_queue.put(self.data)

    def start(self):
        shencanzhe = ['爬虫一号', '爬虫二号', '爬虫三号']
        for name in shencanzhe:
            scz = ShenCanZhe(name=name,parems_queue=self.parems_queue,url=self.url,data_queue=self.data_queue)
            scz.start()

        xiaofeizhe = ['解析一号', '解析二号', '解析三号']
        for name in xiaofeizhe:
            xfz = XiaoFeiZhe(name=name,data_queue=self.data_queue,parems_queue=self.parems_queue)
            xfz.start()


if __name__ == '__main__':
    jys = JiaYuanSpider()
    jys.start()
