# -*- coding: utf-8 -*-
import scrapy


class WzzSpider(scrapy.Spider):
    name = 'wzz'
    allowed_domains = ['wanandroid.com']
    login_urls = 'https://www.wanandroid.com/user/login'
    collect_urls = 'https://www.wanandroid.com/lg/collect'
    start_urls = ['http://www.wanandroid.com//']
    form_data = {
        'username':"mrxu",
        'password':'xrl000824'
    }
    def start_requests(self):
        yield scrapy.FormRequest(url=self.login_urls,formdata=self.form_data,callback=self.parse)

    def parse(self, response):
        print('asdfadsfasdfasdf')
        yield scrapy.Request(url=self.collect_urls,callback=self.parse_collect)

    def parse_collect(self,response):
        # print('asdfasdfsadfasd')
        print(response.request.headers)
        with open('玩安卓.html','wb') as f:
            f.write(response.body)
            f.close()
