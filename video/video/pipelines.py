# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class VideoPipeline(object):
    def __init__(self, mongo_host, mongo_port, mongo_db, mongo_co):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.collection_name = mongo_co

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_host = crawler.settings.get('MONGODB_HOST'),
            mongo_port = crawler.settings.get('MONGODB_PORT'),
            mongo_db = crawler.settings.get('MONGODB_DBNAME'),
            mongo_co = crawler.settings.get('MONGODB_DOCNAME')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host = self.mongo_host, port = self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item