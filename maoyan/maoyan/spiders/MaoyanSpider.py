import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from maoyan.items import MaoyanItem
import urllib.request 
import struct
import zlib
from fontTools.ttLib import TTFont
import xml.dom.minidom as xmldom
import os

def getValue(node, attribute):
	return node.attributes[attribute].value

def getTTGlyphList(xml_path):
	dataXmlfilepath = os.path.abspath(xml_path)
	dataDomObj = xmldom.parse(dataXmlfilepath)
	dataElementObj = dataDomObj.documentElement
	dataTTGlyphList = dataElementObj.getElementsByTagName('TTGlyph')
	return dataTTGlyphList

def isEqual(ttglyph_a, ttglyph_b):
	a_pt_list = ttglyph_a.getElementsByTagName('pt')
	b_pt_list = ttglyph_b.getElementsByTagName('pt')
	a_len = len(a_pt_list)
	b_len = len(b_pt_list)
	if a_len != b_len:
		return False
	for i in range(a_len):
		if getValue(a_pt_list[i], 'x') != getValue(b_pt_list[i], 'x')  or getValue(a_pt_list[i], 'y') != getValue(b_pt_list[i], 'y') or getValue(a_pt_list[i], 'on') != getValue(b_pt_list[i], 'on'):
			return False
	return True

def refresh(dict, ttGlyphList_a, ttGlyphList_data):
	data_dict = {"uniE184":"4","uniE80B":"3","uniF22E":"8","uniE14C":"0",
		"uniF5FB":"6","uniEE59":"5","uniEBD3":"1","uniED85":"7","uniECB8":"2","uniE96A":"9"}
	data_keys = data_dict.keys()
	for ttglyph_data in ttGlyphList_data:
		if 	getValue(ttglyph_data,'name') in data_keys:
			for ttglyph_a in ttGlyphList_a:
				if isEqual(ttglyph_a, ttglyph_data):
					dict[getValue(ttglyph_a,'name')] = data_dict[getValue(ttglyph_data,'name')]
					break
	return dict

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

		#解码
		#下载字体文件
		font_url = sel.xpath('/html/head/style/text()').extract()[0]
		font_url = 'http:'+font_url[font_url.rfind('url')+5:font_url.find('woff')+4]
		print(font_url)
		woff_path = 'tmp.woff'
		f = urllib.request.urlopen(font_url)
		data = f.read()
		with open(woff_path, "wb") as code:
			code.write(data)
		#分析解码字典
		font1 = TTFont('tmp.woff')
		font1.saveXML('tmp.xml')
		decode_dict = dict(enumerate(font1.getGlyphOrder()[2:]))
		decode_dict=dict(zip(decode_dict.values(),decode_dict.keys()))	

		dataTTGlyphList = getTTGlyphList("data.xml")
		tmpTTGlyphList = getTTGlyphList("tmp.xml")
		decode_dict = refresh(decode_dict,tmpTTGlyphList,dataTTGlyphList)
		decode_dict['.'] = '.'
		# print(decode_dict)

		#解码
		_lst_uincode = []
		for item in movie_star.__repr__().split("\\u"):
			_lst_uincode.append("uni" + item[:4].upper())
			if item[4:]:
				_lst_uincode.append(item[4:])
		_lst_uincode = _lst_uincode[1:-1]
		movie_star = "".join([str(decode_dict[i]) for i in _lst_uincode])
		_lst_uincode = []
		for item in movie_total_price.__repr__().split("\\u"):
			_lst_uincode.append("uni" + item[:4].upper())
			if item[4:]:
				_lst_uincode.append(item[4:])
		_lst_uincode = _lst_uincode[1:-1]
		movie_total_price = "".join([str(decode_dict[i]) for i in _lst_uincode])


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
