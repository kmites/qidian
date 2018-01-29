# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import QidianItem
from scrapy_redis.spiders import RedisSpider

class BookinfoSpider(RedisSpider):
    name = 'bookinfo'
    allowed_domains = ['qidian.com']

    base_url = "https://www.qidian.com/all?chanId=5&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page="
    offset = 1
    def parse(self, response):
        extractor = LinkExtractor(allow=r'//book.qidian.com/info/[0-9]+')
        links = extractor.extract_links(response)
        if len(links) ==0:
            return

        for link in links:
            url = link.url
            yield scrapy.Request(url, callback=self.parse_bookinfo)

        self.offset += 1
        next_page_url = self.base_url+str(self.offset)
        yield scrapy.Request(next_page_url,callback=self.parse)

    def parse_bookinfo(self, response):
        book_info = response.css('div.book-information.cf > div.book-info')
        item = QidianItem()

        item['name'] = book_info.xpath("//h1/em/text()").extract_first()
        item['author'] = book_info.xpath("//h1/span/a/text()").extract_first()
        item['status'] = book_info.xpath("//p[@class='tag']/span[1]/text()").extract_first()
        item['contract'] = book_info.xpath("//p[@class='tag']/span[2]/text()").extract_first()
        item['isfree'] = book_info.xpath("//p[@class='tag']/span[3]/text()").extract_first()
        item['type'] = book_info.xpath("//p[@class='tag']/a[1]/text()").extract_first()
        item['target'] = book_info.xpath("//p[@class='tag']/a[2]/text()").extract_first()
        item['intro'] = book_info.xpath("//p[@class='intro']/text()").extract_first()
        item['all_words'] = book_info.xpath("//p[3]/em[1]/text()").extract_first()+book_info.xpath("//p[3]/cite[1]/text()").extract_first()
        item['all_click'] = book_info.xpath("//p[3]/em[2]/text()").extract_first()+book_info.xpath("//p[3]/cite[2]/text()").extract_first()
        item['vip_week_click'] = book_info.xpath("//p[3]/cite[2]/text()").extract()[1]
        item['all_recommend'] = book_info.xpath("//p[3]/em[3]/text()").extract_first()+book_info.xpath("//p[3]/cite[3]/text()").extract_first()
        item['week_recommend'] = book_info.xpath("//p[3]/cite[3]/text()").extract()[1]

        yield item