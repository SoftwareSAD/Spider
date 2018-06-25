# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # 名字
    movie_name = scrapy.Field()
    # 英文名
    movie_ename = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 类型
    movie_type = scrapy.Field()
    # 时长
    movie_time = scrapy.Field()
    # 上映时间
    online_time = scrapy.Field()
    # 评分
    movie_star = scrapy.Field()
    # 票房
    movie_total_price = scrapy.Field()
    # 图片
    img = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 导演图片
    director_src = scrapy.Field()
    # 演员
    actor = scrapy.Field()
    # 演员图片
    actor_src = scrapy.Field()
    # 电影简介
    introduction = scrapy.Field()