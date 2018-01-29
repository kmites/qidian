# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianItem(scrapy.Item):

    #name
    name = scrapy.Field()
    #author
    author = scrapy.Field()
    #status
    status = scrapy.Field()
    #contract
    contract = scrapy.Field()
    #isfree
    isfree = scrapy.Field()
    #type
    type = scrapy.Field()
    #target
    target = scrapy.Field()
    #introduce
    intro = scrapy.Field()
    #all words
    all_words = scrapy.Field()
    #all click number
    all_click = scrapy.Field()
    #vip week click
    vip_week_click = scrapy.Field()
    #all recommend
    all_recommend = scrapy.Field()
    #week recommend
    week_recommend = scrapy.Field()
