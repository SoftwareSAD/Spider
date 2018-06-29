import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from movie_time.items import MovieTimeItem

class MovieTimeSpider(CrawlSpider):
	name = 'movie_time'
	# allowed_domains = ['http://maoyan.com/']
	start_urls = ['http://maoyan.com/cinemas?areaId=-1&districtId=740&offset=0']
	rules = (
		Rule(LinkExtractor(allow=(r'http://maoyan.com/cinema/\d+')), callback='parse_item'),
		Rule(LinkExtractor(allow=(r'http://maoyan.com/cinemas\?areaId=-1&districtId=740&offset=\d+')))
	)

	def parse_item(self, response):
		# print(response.body)
		sel = Selector(response)
		cinema_name = sel.xpath('//div[@class="cinema-brief-container"]/h3/text()').extract_first()
		movie_name = sel.xpath('//div[@class="show-list active"]/div[1]/div[1]/h3/text()').extract_first()
		begin_time = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "begin-time")]/text()').extract()
		end_time = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "end-time")]/text()').extract()
		lang = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "lang")]/text()').extract()
		hall = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "hall")]/text()').extract()
		sellprice = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "sell-price")]/span/text()').extract()

		item = MovieTimeItem()
		item['cinema_name'] = cinema_name
		item['movie_name'] = movie_name
		item['begin_time'] = begin_time
		item['end_time'] = end_time
		item['lang'] = lang
		item['hall'] = hall
		item['sellprice'] = sellprice

		yield item