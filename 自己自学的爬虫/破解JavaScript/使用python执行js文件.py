import requests
import execjs

class DetailDirSpider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
        }
        self.session = requests.session()

    def send_request(self,url):
        return self.session.get(url)

    def write_file(self,content):
        with open('html文件/中国产品大目录.html','wb') as f:
        # with open('js文件/中国产品大目录.js','wb') as f:
            f.write(content.content)

    def execute_js(self):
        # 创建一个执行js对象
        ejs = execjs.get()
        file_name = open('js文件/中国产品大目录.js','r').read()
        # 要执行的js文件
        result = ejs.compile(file_name)
        cookie = result.eval('cookie')
        url = result.eval('url')
        print(cookie,url)
        key,value = cookie.split('=')
        return key,value,url




    def run(self,url):
        self.send_request(url)
        result = self.execute_js()
        self.session.cookies.set(result[0],result[1])
        fullUrl = url+result[2]
        self.send_request(fullUrl)
        response = self.send_request(url)

        self.write_file(response)






if __name__ == '__main__':
    detail = DetailDirSpider()
    detail.run('http://www.300600900.cn')
    # detail.execute_js()
