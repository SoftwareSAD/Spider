import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from maoyan.items import MaoyanItem

class MaoyanSpider(CrawlSpider):
	name = 'maoyan'
	# allowed_domains = ['http://maoyan.com/']
	start_urls = ['http://maoyan.com/films']
	rules = (
		Rule(LinkExtractor(allow=(r'http://maoyan.com/films\?offset=\d+'))),
		Rule(LinkExtractor(allow=(r'http://maoyan.com/films/\d+')), callback='parse_item')
	)

	def parse_item(self, response):
		# print(response.body)
		sel = Selector(response)
		movie_name = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/h3/text()').extract_first()
		movie_ename = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/div/text()').extract_first()
		movie_type = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()').extract_first()
		movie_publish = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()').extract_first()
		country = movie_publish.split('/')[0].strip()
		movie_time = movie_publish.split('/')[1].strip()
		online_time = sel.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').extract_first()
		movie_star = sel.xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/span/span/text()').extract_first()
		movie_total_price = sel.xpath('/html/body/div[3]/div/div[2]/div[3]/div[2]/div/span[1]/text()').extract_first()
		img = sel.xpath('/html/body/div[3]/div/div[1]//img/@src').extract_first()
		director = sel.xpath('//li[@class="celebrity "]/div/a/text()').extract_first()
		director = director.strip()
		director_src = sel.xpath('//li[@class="celebrity "]/a/img/@data-src').extract_first()
		# print(director_src)
		# director_src = director_src.split('@')[0].strip()
		actor = sel.xpath('//li[@class="celebrity actor"]/div/a/text()').extract()
		for i in range(len(actor)):
			actor[i] = actor[i].strip()
		actor_src = sel.xpath('//li[@class="celebrity actor"]/a/img/@data-src').extract()
		
		introduction = sel.xpath('.//div[@class="mod-content"]/span/text()').extract_first()

		item = MaoyanItem()
		item['movie_name'] = movie_name
		item['movie_ename'] = movie_ename
		item['movie_type'] = movie_type
		item['country'] = country
		item['movie_time'] = movie_time
		item['online_time'] = online_time
		item['movie_star'] = movie_star
		item['movie_total_price'] = movie_total_price
		item['img'] = img
		item['director'] = director
		item['director_src'] = director_src
		item['actor'] = actor
		item['actor_src'] = actor_src
		item['introduction'] = introduction

		yield item