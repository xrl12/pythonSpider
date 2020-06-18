import urllib.request
import urllib.parse
import os
import re


class BaiDuTieBa(object):
    def __init__(self, url):
        self.url = url

    def get_response(self, url, page):
        print("当前正在爬取第{}页的数据，url是{}".format(page, url))
        self.heads = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
        }
        # 让ua包含在请求里面，更像浏览器请求
        request = urllib.request.Request(url=url,headers=self.heads)
        content = urllib.request.urlopen(request)
        self.parse(content.read().decode('utf8'), page)

    def get_detail_request(self, url):
        print('当前正在爬取的详情页是{}'.format(url))
        response = urllib.request.urlopen(url)
        self.detail_parse(response.read().decode('utf8'))

    def detail_parse(self, content):
        # http://tiebapic.baidu.com/forum/w%3D580/sign=7095d734144f78f0800b9afb49300a83/3e9759ee3d6d55fb39833f467a224f4a20a4dd0d.jpg
        # imgAddress = """
        # <img class="BDE_Image" src="http://tiebapic.baidu.com/forum/w%3D580/sign=7095d734144f78f0800b9afb49300a83/3e9759ee3d6d55fb39833f467a224f4a20a4dd0d.jpg" size="200263" changedsize="true" width="560" height="746" size="200263">
        # """
        print("正在获取图片")
        pattern = re.compile(r'<img.*?src="(.*?)".*?>')
        result = pattern.findall(content)
        for img_name in result:
            try:
                if not img_name[0] is 'h':
                    img_name = ' https:'+img_name
            except:
                break
            print('这里是图片的链接',img_name)
            self.write_img(img_name, img_name)

    def parse(self, content, page):
        # print(content)
        pattern = re.compile(r'<a .*? href="(/p/\d*?)" .*?>.*?</a>')
        result = pattern.findall(content)
        print('这是里面的链接', result)
        # self.write_file(page, result)
        for url in result:
            detail_url = 'https://tieba.baidu.com'+url
            print(detail_url)
            self.get_detail_request(detail_url)

    # def write_file(self, page, content):
    #     tieBaUrl = os.open('/home/mrxu/Desktop/百度贴吧url{}.txt'.format(page),os.O_RDWR|os.O_CREAT )
    #     # <a rel="noreferrer" href="/p/6526808491" title="嗯哼😏" target="_blank" class="j_th_tit ">嗯哼😏</a>
    #     for url in content:
    #         print('这是地{}页的'.format(page),url)
    #         detail_url = 'https://tieba.baidu.com' + url + '\n'
    #         os.write(tieBaUrl,detail_url.encode('utf8'))
    #     os.close(tieBaUrl)

    def write_img(self, content, name):
        print('正在保存图片')
        print("name",name)

        with open('/home/mrxu/Desktop/{}.jpg'.format(name[-5::]), 'wb') as f:
            f.write(content.encode('utf8'))
            f.close()

    def start(self):
        for i in range(1, 6):
            pn = (i - 1) * 50
            kw = {
                'kw': "美女",
                "pn": pn
            }
            canshu = urllib.parse.urlencode(kw)
            self.full_url = self.url + canshu
            self.get_response(self.full_url, i)


if __name__ == '__main__':
    baidutieba = BaiDuTieBa('https://tieba.baidu.com/f?')
    baidutieba.start()

    # https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3
    # imgAddress = """
    # <img class="BDE_Image" src="http://tiebapic.baidu.com/forum/w%3D580/sign=7095d734144f78f0800b9afb49300a83/3e9759ee3d6d55fb39833f467a224f4a20a4dd0d.jpg" size="200263" changedsize="true" width="560" height="746" size="200263">
    # """
    # baidutieba.detail_parse(imgAddress)
    # baidutieba.write_file(content='<a rel="noreferrer" href="/p/6526808491" title="嗯哼😏" target="_blank" class="j_th_tit ">嗯哼😏</a>',page=1)
