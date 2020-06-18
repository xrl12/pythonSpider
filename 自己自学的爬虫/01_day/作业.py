import urllib.parse
import urllib.request


class TieBa():
    def __init__(self, url):
        # https: // tieba.baidu.com / f?kw = % E7 % BE % 8 E % E5 % A5 % B3 & pn = 150
        # https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3
        # https: // tieba.baidu.com / f?kw = % C3 % C0 % C5 % AE & fr = ala0 & tpl = 5
        self.url = url

    def get(self,url,page):
        print('正在发送第{}次请求'.format(page))
        response = urllib.request.urlopen(url)
        self.write(response.read(),page)


    def write(self,content,page):
        with open('/home/mrxu/Desktop/美女贴吧{}.html'.format(page),'wb') as f:
            f.write(content)
            f.close()

    def start(self):
        person = int(input('请输入您要爬去的页数'))
        if person <= 0:
            person = 1
        for i in range(1,person+1):
            pn = (i-1)*50
            kw = {'kw':"美女","pn":pn}
            result = urllib.parse.urlencode(kw)
            full_url = self.url + result
            data = self.get(full_url,i)
            # self.write(data,i)


tiba = TieBa('https://tieba.baidu.com/f?')
tiba.start()



