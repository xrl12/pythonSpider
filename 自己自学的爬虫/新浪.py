from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import requests
from lxml import etree
import re
from time import sleep

class XinLangSpider(object):
    def __init__(self):
        self.firefoxBinary = FirefoxBinary('/home/mrxu/Downloads/firefox/firefox')
        self.driver = webdriver.Firefox(executable_path='/home/mrxu/Desktop/geckord/geckord0.26/geckodriver',firefox_binary=self.firefoxBinary)
        self.data_dict = {}

    def send_response(self):
        self.driver.get('https://mobile.sina.com.cn/')
        div_list = self.driver.find_elements_by_xpath("//div[@class='feed-card-content']/div//div[@class='feed-card-item']")
        # self.driver.execute_async_script('scrollTo(0,document.documentElement.offsetHeight)')
        self.driver.execute_script('scrollTo(0,document.documentElement.offsetHeight)')
        sleep(2)
        for div in div_list[1:]:
            title = div.find_element_by_css_selector('h2 > a').text
            info = div.find_element_by_class_name('feed-card-txt-summary').text
            tags = div.find_element_by_class_name('feed-card-tags').text
            nvums = div.find_element_by_class_name('feed-card-actions').text
            detail_url = div.find_element_by_css_selector('h2>a').get_attribute('href')
            self.send_detail_request(detail_url)
            self.data_dict['title'] = title
            self.data_dict['info'] = info
            self.data_dict['tags'] = tags
            self.data_dict['nvums'] = nvums

    def send_detail_request(self,url):
        print('正在发送详情页请求{}'.format(url))
        response = requests.get(url=url)
        return self.parse_Detail(response.content)

    def parse_Detail(self,response):
        print('正在解析详情页请求')
        html = etree.HTML(response)
        article_detail = html.xpath("//div[@id='artibody']//text()")
        str1 = ".tech-quotation{padding:20px20px0px;background:url(//n.sinaimg.cn/tech/content/quote.png)no-repeat00#f4f4f4;margin-bottom:30px;}.tech-conp{margin-bottom:30px}.tech-conpa:visited{color:#4b729f!important;}"
        str2 = "(function(){varadScript=document.createElement('script');adScript.src='//d1.sina.com.cn/litong/zhitou/sinaads/demo/wenjing8/js/yl_left_hzh_20171020.js';document.getElementsByTagName('head')[0].appendChild(adScript);})();"
        detail = ''.join(article_detail).replace('\n\t\s','').replace(str1,'').replace(str2,'')
        pattern = re.compile(r'\s',re.S)
        print('这是没有替换过的{}'.format(detail))
        # detail = pattern.sub('',detail)
        # print('这是替换过的{}'.format(detail))
        return article_detail

# .tech-quotation{padding:20px20px0px;background:url(//n.sinaimg.cn/tech/content/quote.png)no-repeat00#f4f4f4;margin-bottom:30px;}.tech-conp{margin-bottom:30px}.tech-conpa:visited{color:#4b729f!important;}
# .tech-quotation{padding:20px20px0px;background:url(//n.sinaimg.cn/tech/content/quote.png)no-repeat00#f4f4f4;margin-bottom:30px;}.tech-conp{margin-bottom:30px}.tech-conpa:visited{color:#4b729f!important;}


if __name__ == '__main__':
    xls = XinLangSpider()
    xls.send_response()


