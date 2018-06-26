# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
	# 新闻标题
	title = scrapy.Field()
	# 新闻摘要
	abstract = scrapy.Field()
	# 热点人物
	article = scrapy.Field()
	# 新闻封面图
	cover_img_src = scrapy.Field()
	# 新闻链接
	news_url = scrapy.Field()
	# 新闻发布时间
	news_date = scrapy.Field()
	# 新闻浏览人数
	view_count = scrapy.Field()