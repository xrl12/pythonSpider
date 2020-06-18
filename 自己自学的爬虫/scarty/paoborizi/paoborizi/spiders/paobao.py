# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from urllib.parse import urljoin
from paoborizi.items import PaoboriziItem

class PaobaoSpider(scrapy.Spider):
    name = 'paobao'
    # http://www.jcodecraeer.com/
    allowed_domains = ['jcodecraeer.com']   # 不对起止url生效，对第二次或者以后的url生效
    start_urls = ['http://www.jcodecraeer.com/plus/list_tid_4.html']

    def parse(self, response):
        #  使用xpath
        # html = etree.HTML(response.body)
        # li_list = html.xpath("//ul[@class='archive-list']")
        # for li in li_list:
        #     href = li.xpath(".//li[@class='archive-item clearfix']/a/@href")
        #     title = li.xpath(".//li[@class='archive-item clearfix']/a/@title")
        #     nvumm = li.xpath(".//li[@class='archive-item clearfix']//li[@class='list-msg']//span[2]/text()")
        #     for url in href:
        #         detail_url = urljoin(self.allowed_domains[0],url)

        # 使用scarpy自带的解析器
        item = PaoboriziItem()
        li_list = response.css('.archive-list>li')
        for li in li_list:
            # 使用base4  extract_first()表示取单个  extract表示取全部
            # href = li.css('h3>a::text')  返回的数据：[<Selector xpath='descendant-or-self::h3/a/text()' data='谷歌“Fuchsia”操作系统抛弃 Linux：具有崭新的 UI'>]
            title = li.css('h3>a::text').extract_first()  #  返回的数据： 谷歌将为找到顶级app漏洞的黑客提供悬赏
            href = li.css('h3>a::attr(href)').extract_first()

            # 使用xpath
            nvum = li.xpath(".//li[@class='list-msg']//span[2]/text()").extract_first()
            detail_url = urljoin(self.allowed_domains[0],href)
            item['title'] = title
            item['nvum'] = nvum
            full_url = 'http://www.jcodecraeer.com/'+detail_url
            yield scrapy.Request(url=full_url,meta={"item":item},callback=self.detail_parse)
        next = response.xpath("//div[@class='paginate-container']//ul//li[last()-2]/a/@href").extract_first()
        if next.startswith('.'):
            full_url = 'http://www.jcodecraeer.com/' + next[3:]
            print(full_url)
            # http://www.jcodecraeer.com/plus/list_tid_4_TotalResult_596_PageNo_2.html
            yield scrapy.Request(url=full_url, callback=self.parse)



    def detail_parse(self,response):
        item = response.meta.get('item')
        content = ''.join(response.xpath("//div[@class='arc_body']//text()").extract()).replace('\t\n ','')
        item['content'] = content
        yield item







