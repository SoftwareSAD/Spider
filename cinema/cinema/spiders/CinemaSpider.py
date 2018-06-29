import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from cinema.items import CinemaItem

class CinemaSpider(CrawlSpider):
	name = 'cinema'
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
		# district = sel.xpath().extract_first()
		online_moive = sel.xpath('//div[@class="movie-list"]//img/@src').extract()
		address = sel.xpath('//div[@class="cinema-brief-container"]/div[1]/text()').extract_first()
		telephone = sel.xpath('//div[@class="cinema-brief-container"]/div[2]/text()').extract_first()
		img_url = sel.xpath('//div[@class="avatar-shadow"]/img/@src').extract_first()

		item = CinemaItem()
		item['cinema_name'] = cinema_name
		item['district'] = '从化市'
		item['online_moive'] = online_moive
		item['address'] = address
		item['telephone'] = telephone
		item['img_url'] = img_url

		yield item