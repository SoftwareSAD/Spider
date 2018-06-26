# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):
    # 视频标题
    title = scrapy.Field()
    # 视频摘要
    abstract = scrapy.Field()
    # 视频封面图
    cover_img_src = scrapy.Field()
    # 视频链接
    url = scrapy.Field()
    # 视频发布时间
    date = scrapy.Field()
    # 视频播放人数
    view_count = scrapy.Field()