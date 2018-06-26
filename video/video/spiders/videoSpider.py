import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from video.items import VideoItem

class newSpider(CrawlSpider):
	name = 'MaoYanVideos'

	start_urls = ['http://maoyan.com/news?showTab=3']
	rules = (
		Rule(LinkExtractor(allow=(r'http://maoyan.com/news\?showTab=3\&offset=\d+')), callback='parse_item'),
	)

	def parse_item(self, response):
		# print(response.body)
		sel = Selector(response)
		title = sel.xpath('//div[@class="video-box"]/h4/a/text()').extract()
		abstract = []
		cover_img_src = sel.xpath('//div[@class="video-box"]/a/img/@src').extract()
		url = sel.xpath('//div[@class="video-box"]/a/@href').extract()
		date = []
		view_count = sel.xpath('//div[@class="video-box"]/div/span/text()').extract()

		item = VideoItem()
		item['title'] = title
		item['abstract'] = abstract
		item['cover_img_src'] = cover_img_src
		item['url'] = url
		item['date'] = date
		item['view_count'] = view_count

		yield item