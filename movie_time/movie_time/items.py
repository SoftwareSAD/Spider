# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieTimeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 影院名称
    cinema_name = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 时间列表
    # begintime
    begin_time = scrapy.Field()
    # endtime
    end_time = scrapy.Field()
    # lang
    lang = scrapy.Field()
    # hall
    hall = scrapy.Field()
    # sellprice
    sellprice = scrapy.Field()
