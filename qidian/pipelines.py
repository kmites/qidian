# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class QidianPipeline(object):
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.qidian

    def close_spider(self):
        self.client.close()

    def process_item(self, item, spider):
        self.db.bookinfo.insert(dict(item))