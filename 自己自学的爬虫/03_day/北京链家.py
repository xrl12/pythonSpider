import  requests
import pymysql
import random
import re
from lxml import etree

class LianJIaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/chengjiao/'
        self.cunn = pymysql.connect(port=3306,
                                    password='123456',
                                    user='root',
                                    database='xici',
                                    charset='utf8',
                                    host='localhost'
                                    )
        self.cursor = self.cunn.cursor()
        self.proxy = self.get_proxy()
    def send_request(self):
        print('正在发送请求')
        response = requests.get(self.url,proxies=self.proxy)
        # print(response.text)
        # self.x_path_parse()
        self.re_parse(response.text)

    def re_parse(self,content):
        print('正在对数据进行解析')
        pattern = re.compile(r'<li>.*?<div class="title"><a.*?>(.*?)</a>.*?</span>(.*?)</.*?dealDate.*?>(.*?)</.*?number>(.*?)',re.S)
        result = pattern.findall(content)
        print(result)

    # 使用xpath进行匹配
    # def x_path_parse(self):
    #
    #     # 所有的li标签里面的内容    //div[@class='leftContent']/ul[@class='listContent']/li
    #     # li标签下面的标题 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='title'/text()]
    #     # 房屋信息 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='address']/div[@class="houseInfo"/text]
    #     # 房屋价格 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='address']/div[@class="dealDate"/text()]
    #     # 房屋时间 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='address']/div[@class="totalPrice"/text()]
    #     # 房屋具体位置  //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='flood']/div[@class="positionInfo"/text()]
    #     # 房屋具体价格 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='flood']/div[@class="unitPrice"/text()]
    #     # 房屋周边情况 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='dealHouseInfo']/span[@class="dealHouseTxt"/text()]
    #     # 房屋标价和售价 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='dealCycleeInfo']/span[@class="dealCycleTxt"/text()]
    #     # 出售人 //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='agentInfoList']/a
    #
    #     parse = etree.HTMLParser(encoding='utf8')
    #     html = etree.parse('../爬取数据的文档/北京链家.html',parser=parse)
    #     house_info= html.xpath(" //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='address']/div[@class='houseInfo']/text()")
    #     house_date = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='address']/div[@class='dealDate']/text()")
    #     house_price = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='address']/div[@class='totalPrice']/span/text()")
    #     house_price_unit = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='address']/div[@class='totalPrice']/text()")
    #     house_address = html.xpath(" //div[@class='leftContent']/ul[@class='listContent']/li//div[@class='flood']/div[@class='positionInfo']/text()")
    #     house_detail_price = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='flood']//div[@class='unitPrice']/span[@class='number']/text()")
    #     house_detail_price_unit = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='flood']/div[@class='unitPrice']/text()")
    #     house_address_info1 = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='dealHouseInfo']/span[@class='dealHouseTxt']/span[1]/text()")
    #     house_address_info2 = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='dealHouseInfo']/span[@class='dealHouseTxt']/span[2]/text()")
    #
    #     house_trade = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='dealCycleeInfo']/span[@class='dealCycleTxt']/span[1]/text()")
    #     house_trage_person = html.xpath("//div[@class='leftContent']/ul[@class='listContent']/li//div[@class='agentInfoList']/a/text()")
    #     print(house_info)
    #     print(house_address)
    #     print(house_price_unit)
    #     print(house_price)
    #     print(house_date)
    #     print(house_address_info1)
    #     print(house_address_info2)
    #     print(house_detail_price_unit)
    #     print(house_trage_person)
    #     print(house_trade)

    def get_proxy(self):
        sql = 'select * from proxy'
        self.cursor.execute(sql)
        proxy_all = self.cursor.fetchall()
        proxy_one = random.choice(proxy_all)
        proxy = {
            proxy_one[2]:str(proxy_one[1])+':'+str(proxy_one[0])
        }
        print('----------------->',proxy)
        return proxy
    def write_file(self,content):
        with open('../爬取数据的文档/北京链家.html', 'w') as f:
            f.write(content)
            f.close()

if __name__ == '__main__':
    lianjiaspider = LianJIaSpider()
    lianjiaspider.send_request()
