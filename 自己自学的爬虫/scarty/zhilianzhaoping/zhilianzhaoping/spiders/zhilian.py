# -*- coding: utf-8 -*-
import scrapy

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['https://www.baidu.com']   # 允许爬的域
    start_urls = ['https://www.baidu.com/']   #  开始的url

    def parse(self, response):
        # response.text 相当于requests.text
        # response.body 相当于requests.content
        print(response.text)