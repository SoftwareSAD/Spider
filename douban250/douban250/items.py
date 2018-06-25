# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 豆瓣电影TOP250爬虫 Item

    # 电影名称
    title = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 演员
    actor = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 评价人数
    rating_num = scrapy.Field()
    # 经典台词
    quote = scrapy.Field()
    # 图片
    image = scrapy.Field()
