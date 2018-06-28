import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from news.items import NewsItem

class newSpider(scrapy.Spider):
	name = 'MaoYanNews'

	base_url = 'http://maoyan.com/news?showTab=2&offset='
	offset=0
	start_urls=[base_url+str(offset),]

	def parse(self, response):
		news = response.xpath('//div[@class="news-box clearfix"]')

		for sel in news:

			title = sel.xpath('./div/h4/a/text()').extract_first()
			abstract = sel.xpath('./div/div[1]/text()').extract_first()
			article = sel.xpath('./div/div[2]/span[3]/a/text()').extract_first()
			if (article):
				article = article.strip()
			cover_img_src = sel.xpath('./a/img/@src').extract_first()
			news_url = sel.xpath('./div/h4/a/@href').extract_first()
			news_date = sel.xpath('./div/div[2]/span[2]/text()').extract_first()
			view_count = sel.xpath('./div/div[2]/span[4]/text()').extract_first()

			item = NewsItem()
			item['title'] = title
			item['abstract'] = abstract
			item['article'] = article
			item['cover_img_src'] = cover_img_src
			item['news_url'] = news_url
			item['news_date'] = news_date
			item['view_count'] = view_count

			yield item

		if self.offset < 3000:
			self.offset += 10
			yield scrapy.Request(url=self.base_url+str(self.offset),callback=self.parse)