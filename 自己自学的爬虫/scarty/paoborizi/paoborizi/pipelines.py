# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class PaoboriziPipeline(object):
    def __init__(self,host,user,password,database,port):
        self.connect = pymysql.connect(host=host,user=user,password=password,database=database,port=port)
        self.cursor = self.connect.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        pwd = crawler.settings['MYSQL_PASSWORD']
        database = crawler.settings['MYSQL_DB']
        user = crawler.settings['MYSQL_USER']
        port = crawler.settings['MYSQL_PORT']
        return cls(host=host,user=user,password=pwd,database=database,port=port)


    def process_item(self, item, spider):
        sql = 'insert into wangshangchonglang values(%s,%s,%s)'
        content = item['content'].strip()
        title = item['title'].strip()
        nvum = item['nvum'].strip()
        self.cursor.execute(sql,[title,nvum,content])
        self.connect.commit()