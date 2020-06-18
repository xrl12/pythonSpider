import urllib.request
import urllib.parse

class Nhb(object):
    def __init__(self,url):
        # url = https://www.neihan8s.com/lxy//index_3.html
        self.url = url

    def get_request(self,page,url):
        reqponse = urllib.request.urlopen(url)
        self.write_file(reqponse.read(),page)

    def write_file(self,content,page):
        with open('/home/mrxu/Desktop/内涵吧{}.html'.format(page),'wb') as f:
            f.write(content)
            f.close()

    def run(self):
        for i in range (0,1):
            i += 1
            if i == 1:
                full_url = self.url + '.html'
            else:
                full_url = self.url + '_'+str(i) + '.html'
            print(full_url)
            self.get_request(page=i,url = full_url)

if __name__ == '__main__':
    nhb = Nhb('https://www.neihan8s.com/lxy//index')
    nhb.run()


