import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from video.items import VideoItem

class newSpider(CrawlSpider):
	name = 'MaoYanVideos'

	base_url = 'http://maoyan.com/news?showTab=3&offset='
	offset=0
	start_urls=[base_url+str(offset),]

	def parse(self, response):

		videos = response.xpath('//div[@class="video-box"]')

		for sel in videos:

			title = sel.xpath('./h4/a/text()').extract_first()
			cover_img_src = sel.xpath('./a/img/@src').extract_first()
			url = sel.xpath('./a/@href').extract_first()
			view_count = sel.xpath('./div/span/text()').extract_first()

			item = VideoItem()
			item['title'] = title
			item['cover_img_src'] = cover_img_src
			item['url'] = url
			item['view_count'] = view_count

			yield item

		if self.offset < 270:
			self.offset += 30
			yield scrapy.Request(url=self.base_url+str(self.offset),callback=self.parse)