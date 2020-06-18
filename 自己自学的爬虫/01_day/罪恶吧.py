import urllib.parse
import urllib.request

class ZuiE(object):
    def __init__(self,url):

        self.url = url

    def get_request(self,url):
        print(url)
        request = urllib.request.urlopen(url)
        self.wiret_file(request.read())

    def wiret_file(self,content):
        with open('/home/mrxu/Desktop/罪恶吧.html','wb') as f:
            f.write(content)
            f.close()

    def start(self):
        # https: // tieba.baidu.com / f?kw = % E7 % BD % AA % E6 % 81 % B6
        kw = {'kw':"罪恶吧"}
        result = urllib.parse.urlencode(kw)
        fulll_url = self.url + result
        self.get_request(fulll_url)



if __name__ == '__main__':
    zuieba = ZuiE('https://tieba.baidu.com/f?')
    zuieba.start()


