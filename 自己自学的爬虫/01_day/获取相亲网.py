import urllib.request
import urllib.parse

class XiQin(object):
    def __init__(self,url):
        # ulr = 'https://www.xiangqinwang.cn/'
        self.url = url

    def get_request(self):
        resposne = urllib.request.urlopen(self.url)
        self.write_file(resposne.read())

    def write_file(self,content):
        with open('/home/mrxu/Desktop/相亲网.html','wb') as f:
            f.write(content)
            f.close()

    def run(self):
        self.get_request()

if __name__ == '__main__':
    xiqin = XiQin('https://www.xiangqinwang.cn/')
    xiqin.run()
