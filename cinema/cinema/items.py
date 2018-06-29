# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CinemaItem(scrapy.Item):
	# 电影院名字
	cinema_name = scrapy.Field()
	# 区
	district = scrapy.Field()
	# 上映电影的图片地址
	online_moive = scrapy.Field()
	# 地址
	address = scrapy.Field()
	# 电话
	telephone = scrapy.Field()
	# 图片
	img_url = scrapy.Field()
