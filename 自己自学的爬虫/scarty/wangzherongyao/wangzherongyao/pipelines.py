# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os
image_store = get_project_settings().get('IMAGES_STORE')

import scrapy
class WangzherongyaoPipeline(object):
    def process_item(self, item, spider):
        return item


class WangZhePiFu(ImagesPipeline):
    # 下载图片请求的方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["skin_url"])

    # 修改图片的名字
    def item_completed(self, results, item, info):
        # [{'url': 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/133/133-bigskin-3.jpg', 'checksum': 'ef87cf985470ecd067baab619464fdf3', 'path': 'full/44bcd6b3de9c531ceaa66a3f441ad961bb22d93b.jpg'}]
        # [(True,
        # {'path': 'full/b529ba81b881e8b05a41f8f0834acd4dbb400b89.jpg',
        # 'url': 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/136/136-bigskin-1.jpg',
        # 'checksum': 'd471728c2cf3e84b3e3bcb568bb2c92d'})
        # ]
        # print('result=',results)
        img_name = [x['path'] for ok, x in results if ok][0]
        print('wangzhe/'+img_name)
        os.rename('wangzhe/'+img_name,'wangzhe/'+'full/'+item['cname']+'_'+item['skin_name']+'.jpg')

