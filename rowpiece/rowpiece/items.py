# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RowpieceItem(scrapy.Item):
    # 电影院名字
    cinema_name = scrapy.Field()
    # 电影名
    movie_name = scrapy.Field()
    # 放映日期
    date = scrapy.Field()
    # 时间
    begin_time = scrapy.Field()
    end_time = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 放映厅
    hall = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 每个电影排片天数
    date_count = scrapy.Field()
    # 每个电影每天排片场数
    show_count = scrapy.Field()