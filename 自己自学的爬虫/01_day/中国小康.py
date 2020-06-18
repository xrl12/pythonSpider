import urllib.request
import urllib.parse

# url = http://news.chinaxiaokang.com/yaowen/2020/0303/907375.html
# url = http://news.chinaxiaokang.com/yaowen/2020/0303/907375

class ZhuongGuo(object):
    def __init__(self,url):
        self.url = url

    def write_file(self,content,page):
        print('这是第{}次保存文件'.format(page))
        with open('/home/mrxu/Desktop/中国小康网{}.html'.format(page),'wb') as f:
            f.write(content)
            f.close()

    def get_request(self,url,page):
        print("这是第{}次爬取".format(page))
        reqpsone = urllib.request.urlopen(url)
        self.write_file(reqpsone.read(),page)

    def run(self):
        for i in range(0,6):
            i += 907375
            full_url = self.url + str(i)+'.html'
            # print(full_url)
            self.get_request(full_url,i)

if __name__ == '__main__':
    zhongguo = ZhuongGuo('http://news.chinaxiaokang.com/yaowen/2020/0303/')
    zhongguo.run()



