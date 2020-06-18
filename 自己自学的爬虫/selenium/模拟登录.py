from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from urllib import parse
import requests
import re
import http.client, mimetypes, urllib, json, time



class V2exSpdier(object):

    def __init__(self):
        self.firefoxBinery = FirefoxBinary(firefox_path='/home/mrxu/Downloads/firefox/firefox-bin')
        self.driver = webdriver.Firefox(executable_path='/home/mrxu/Desktop/geckord0.26/geckodriver',
                                        firefox_binary=self.firefoxBinery)
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            'referer': 'https://www.v2ex.com/signin',
            # 'sec-fetch-dest': 'image',
            # 'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            # 'sec - fetch - mode': 'no - cors',
            # 'sec-fetch-site': 'same-origin'
        }

    def send_img_request(self, url):
        print(self.headers)
        print('正在发送图片路由{}'.format(url))
        response = requests.get(url,headers=self.headers)
        # response = request.urlopen(url)
        with open('yzm.png', 'wb') as f:
            f.write(response.content)

    def send_request(self, url):

        self.driver.get(url)
        yzm = self.driver.find_element_by_xpath("//table//tr[last()-2]//td[last()]/div").get_attribute('style')
        img_url = self.get_img_url(yzm, url)
        cookie = self.driver.get_cookies()
        self.parse_cookie(cookie)
        self.send_img_request(img_url)
        result = get_result('yzm.png','3006','20')
        print('我接受的返回值',result)

    def get_img_url(self, data, baseurl):
        print('正在获取图片的地址')
        pattern = re.compile(r'background-image: url\("(.*?)"\)', re.S)
        son_url = pattern.match(data).group(1)
        imgurl = parse.urljoin(baseurl, son_url)
        return imgurl
        # print('这个是验证码地址', imgurl)
        # return request.Request(headers=self.headers, url=imgurl)

    def parse_cookie(self,cookie):
        cookie = [item['name']+'='+item['value'] for item in cookie]
        self.headers['cookie'] = ';'.join(cookie)


    def run(self, url):

        self.send_request(url)











class YDMHttp:
    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text


######################################################################
def get_result(filename, codetype, timeout):
    # 用户名
    username = 'xiaoxu'

    # 密码
    password = 'xrl000824'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 10430

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '2c72877b224c6ce8087ff22dbf4475a0'

    # 图片文件
    filename = 'yzm.png'

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = 1004

    # 超时时间，秒
    timeout = 60

    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login();
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance();
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        print('cid: %s, result: %s' % (cid, result))





if __name__ == '__main__':
    v2ex = V2exSpdier()
    v2ex.run('https://www.v2ex.com/signin')
