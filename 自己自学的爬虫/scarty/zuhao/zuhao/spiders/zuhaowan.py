# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZuhaowanSpider(CrawlSpider):
    name = 'zuhaowan'
    allowed_domains = ['www.zuhaowan.com']
    start_urls = ['https://www.zuhaowan.com/zuhao-17/']

    rules = (
        # /zuhao-17/2.html
        Rule(LinkExtractor(allow=r'/zuhao-17/\d+.html'), process_links='parse_link', follow=True),
        Rule(LinkExtractor(allow=r'/zuhao/\d.*?.html'), process_links='parse_detail_link', follow=False,callback='parse_item'),
    )


    def parse_link(self,link):
        return link

    def parse_detail_link(self,link):
        return link

    def parse_item(self, response):
        item = {}
        item['info-dist'] = response.xpath("//div[@class='info-dist']/text()").get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(item)
        return item
