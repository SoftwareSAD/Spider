import scrapy
from douban250.items import Douban250Item


class Douban250Spider(scrapy.Spider):
    """豆瓣电影Top250爬虫Spider"""

    name = 'douban250'
    allowed_domains=['movie.douban.com',]

    base_url='https://movie.douban.com/top250?start=0'
    offset=0
    start_urls=[base_url+str(offset),]

    def parse(self, response):
        # 包含本页所有电影的SelectorList
        movies=response.css('.article .grid_view li')

        for each in movies:
            # 电影名称
            title = each.css('.item .hd .title:nth-child(1)::text').extract_first()
            # 导演
            dire_actor = each.css('.item .bd p::text').extract()[0].strip()
            director = dire_actor.split('\xa0\xa0\xa0')[0].strip()
            # 演员
            if (len(dire_actor.split('\xa0\xa0\xa0')) > 1):
                actor = dire_actor.split('\xa0\xa0\xa0')[1].strip()
            # 年代
            info = each.css('.item .bd p::text').extract()[1].strip()
            year = info.split('/')[0].strip()
            # 国家
            country = info.split('/')[1].strip()
            # 类型
            type = info.split('/')[2].strip()
            # 评分
            rating_num = each.css('.item .bd .star .rating_num::text').extract_first()
            # 经典台词
            quote = each.css('.item .bd .quote span::text').extract_first()
            # 海报
            image = each.css('.item .pic a img::attr(src)').extract_first()

            item = Douban250Item()
            item['title'] = title
            item['director'] = director
            item['actor'] = actor
            item['year'] = year
            item['country'] = country
            item['type'] = type
            item['rating_num'] = rating_num
            item['quote'] = quote
            item['image'] = image

            yield item

        if self.offset<225:
            self.offset+=25
            yield scrapy.Request(url=self.base_url+str(self.offset),callback=self.parse)
            
            