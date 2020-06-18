# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangzherongyaoItem(scrapy.Item):
    # define the fields for your item here like:
    # 需要爬取的字段
    ename = scrapy.Field()
    cname = scrapy.Field()
    skin_name = scrapy.Field()
    skin_url = scrapy.Field()
    # image_urls = scrapy.Field()