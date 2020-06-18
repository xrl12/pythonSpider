import requests
import urllib.parse
import pymysql
import re
import random
import time

class WeiBo(object):
    def __init__(self):
        self.url = 'https://s.weibo.com/weibo?'

        self.heads = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Cookie':'SINAGLOBAL=8513499968037.61.1584145990686; login_sid_t=213043f43e113183ce0534925026eb28; cross_origin_proto=SSL; _s_tentry=-; Apache=4582355390837.585.1584234870489; ULV=1584234870495:3:3:3:4582355390837.585.1584234870489:1584170182250; crossidccode=CODE-yf-1JdigA-3mFB83-F7ST3gzLdG2RRfgc9c795; ALF=1615772443; SSOLoginState=1584236443; SUB=_2A25zaffMDeRhGeBP6VYU8S_Iwz6IHXVQH24ErDV8PUNbmtANLRGkkW9NRX3xwk7jr-QKKT3cuGw5c4yKFaiv-s_E; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFVAUWNzkbfVCVbRHR_wbds5JpX5KzhUgL.FoqpeoBfeK2X1hz2dJLoIE.LxKnL1hMLB-2LxK-LBKnLBo2LxKnL1hMLB-2LxKBLBo.L1K5XShqXS5tt; SUHB=0mxU7Bl2zArx0U; wvr=6; UOR=,,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1584236442079%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A35%2C%22msgbox%22%3A0%7D',
        #     Cookie: SINAGLOBAL=8513499968037.61.1584145990686; login_sid_t=213043f43e113183ce0534925026eb28; cross_origin_proto=SSL; _s_tentry=-; Apache=4582355390837.585.1584234870489; ULV=1584234870495:3:3:3:4582355390837.585.1584234870489:1584170182250; ALF=1615772443; SSOLoginState=1584236443; SUB=_2A25zaffMDeRhGeBP6VYU8S_Iwz6IHXVQH24ErDV8PUNbmtANLRGkkW9NRX3xwk7jr-QKKT3cuGw5c4yKFaiv-s_E; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFVAUWNzkbfVCVbRHR_wbds5JpX5KzhUgL.FoqpeoBfeK2X1hz2dJLoIE.LxKnL1hMLB-2LxK-LBKnLBo2LxKnL1hMLB-2LxKBLBo.L1K5XShqXS5tt; SUHB=0mxU7Bl2zArx0U; wvr=6; UOR=,,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1584237908317%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A36%2C%22msgbox%22%3A0%7D
        }
        self.connect = pymysql.connect(password='123456', user='root', port=3306, database='xici', charset='utf8mb4',
                                       host='localhost')
        self.cursor = self.connect.cursor()
        self.proxy = self.get_proxy()

    def send_response(self,url):
        print('正在发送的请求是{}'.format(url))
        time.sleep(10)
        response = requests.get(url,headers = self.heads,proxies=self.proxy)
        return response.content

    def parse(self,content):
        pattern = re.compile(r'<div class="card-wrap".*?>.*?<div class="avator">.*?<a href="(.*?)" target="_blank"',re.S)
        urls = pattern.findall(content.decode('utf8'))
        for url in urls:
            # //weibo.com/5071206030?refer_flag=1001030103_
            url = 'http:'+url
            response = self.send_response(url)
            with open('../爬取数据的文档/微博跳转页面.html','wb') as f:
                f.write(response)
                f.close()
            print(response)



    def run(self):
        kw = {
            'q':'成都七中美食'
        }
        result = urllib.parse.urlencode(kw)
        full_url = self.url + result
        resposne = self.send_response(full_url)
        self.parse(resposne)

    def get_proxy(self):
        sql = 'select * from proxy'
        self.cursor.execute(sql)
        proxy_all = self.cursor.fetchall()
        proxy_one = random.choice(proxy_all)
        proxy = {
            proxy_one[2]: str(proxy_one[0]) + ':' + str(proxy_one[1])
        }
        print('使用的代理', proxy)
        return proxy

if __name__ == '__main__':
    weibo = WeiBo()
    weibo.run()




