import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from news.items import NewsItem

class newSpider(CrawlSpider):
	name = 'MaoYanNews'

	start_urls = ['http://maoyan.com/news?showTab=2']
	rules = (
		Rule(LinkExtractor(allow=(r'http://maoyan.com/news\?showTab=2\&offset=\d+')), callback='parse_item'),
	)

	def parse_item(self, response):
		# print(response.body)
		sel = Selector(response)
		title = sel.xpath('//div[@class="news-box clearfix"]/div/h4/a/text()').extract()
		abstract = sel.xpath('//div[@class="news-box clearfix"]/div/div[1]/text()').extract()
		article = sel.xpath('//div[@class="news-box clearfix"]/div/div[2]/span[3]/a/text()').extract()
		for i in range(len(article)):
			article[i] = article[i].strip()
		cover_img_src = sel.xpath('//div[@class="news-box clearfix"]/a/img/@src').extract()
		news_url = sel.xpath('//div[@class="news-box clearfix"]/div/h4/a/@href').extract()
		news_date = sel.xpath('//div[@class="news-box clearfix"]/div/div[2]/span[2]/text()').extract()
		view_count = sel.xpath('//div[@class="news-box clearfix"]/div/div[2]/span[4]/text()').extract()

		item = NewsItem()
		item['title'] = title
		item['abstract'] = abstract
		item['article'] = article
		item['cover_img_src'] = cover_img_src
		item['news_url'] = news_url
		item['news_date'] = news_date
		item['view_count'] = view_count

		yield item