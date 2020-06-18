# -*- coding: utf-8 -*-
import json

import scrapy

from wangzherongyao.items import WangzherongyaoItem


class WzSpider(scrapy.Spider):
    name = 'wz'
    allowed_domains = ['qq.com']
    url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
    start_urls = ['https://pvp.qq.com/web201605/js/herolist.json']

    # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/531/531-bigskin-1.jpg
    # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/524/524-bigskin-1.jpg
    # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/105/105-bigskin-1.jpg
    # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/105/105-bigskin-2.jpg
    # {
    # 	"ename": 105,
    # 	"cname": "廉颇",
    # 	"title": "正义爆轰",
    # 	"new_type": 0,
    # 	"hero_type": 3,
    # 	"skin_name": "正义爆轰|地狱岩魂"
    # }

    def parse(self, response):

        # print('这是body的内容',response.body)   #  返回字节
        hero_dict = json.loads(response.text)
        for hero in hero_dict:
            ename = hero['ename']  # 英雄的id
            cname = hero['cname']  # 英雄的名字   如果么有数据就会报错
            skin_name = hero.get('skin_name')  # 如果没有就会返回None
            if skin_name:
                skin_list = skin_name.split('|')
                for index, skin in enumerate(skin_list, start=1):
                    full_url = self.url.format(ename, ename, index)
                    # print('这是拼接好的路由', full_url)
                    items = WangzherongyaoItem()
                    items['ename'] = ename
                    items['cname'] = cname
                    items['skin_url'] = full_url
                    items['skin_name'] = skin
                    # items['image_urls'] = [full_url]
                    yield items
