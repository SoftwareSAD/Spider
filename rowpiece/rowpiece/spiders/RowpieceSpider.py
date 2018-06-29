import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from rowpiece.items import RowpieceItem
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

def decode(decode_dict, code):
	_lst_uincode = []
	for item in code.__repr__().split("\\u"):
		_lst_uincode.append("uni" + item[:4].upper())
		if item[4:]:
			_lst_uincode.append(item[4:])
	_lst_uincode = _lst_uincode[1:-1]
	result = "".join([str(decode_dict[i]) for i in _lst_uincode])
	return result


class RowpieceSpider(CrawlSpider):
	name = 'rowpiece'
	# allowed_domains = ['http://maoyan.com/']
	start_urls = ['http://maoyan.com/cinemas?areaId=-1&districtId=740&offset=0']
	rules = (
		Rule(LinkExtractor(allow=(r'http://maoyan.com/cinema/\d+')), callback='parse_item'),
		Rule(LinkExtractor(allow=(r'http://maoyan.com/cinemas\?areaId=-1&districtId=740&offset=\d+')))
	)

	def parse_item(self, response):
		# print(response.body)
		sel = Selector(response)
		# online_moive = sel.xpath('//div[@class="movie-list"]//img/@src').extract()
		# address = sel.xpath('//div[@class="cinema-brief-container"]/div[1]/text()').extract_first()
		# telephone = sel.xpath('//div[@class="cinema-brief-container"]/div[2]/text()').extract_first()
		# img_url = sel.xpath('//div[@class="avatar-shadow"]/img/@src').extract_first()

		# 电影院名字
		cinema_name = sel.xpath('//div[@class="cinema-brief-container"]/h3/text()').extract_first()
		# 电影名
		movie_name = sel.xpath('//div[contains(@class, "show-list")]//h3/text()').extract()
		# 放映日期
		date = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "date-item")]/text()').extract()
		# 时间
		begin_time = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "begin-time")]/text()').extract()
		end_time = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "end-time")]/text()').extract()
		# 语言
		language = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "lang")]/text()').extract()
		# 放映厅
		hall = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "hall")]/text()').extract()
		# 价格
		price = sel.xpath('//div[contains(@class, "show-list")]//span[contains(@class, "sell-price")]/span/text()').extract()
		# 每个电影排片天数
		date_count = []
		movie_count = len(movie_name)
		for i in range(movie_count):
			date_count.append(len(sel.xpath('//div[@data-index = "' + str(i) + '"]//div[@class="show-date"]/span').extract())-1)
		# 每个电影每天排片场数
		show_count = []
		for i in range(movie_count):
			for j in range(date_count[i]):
				show_count.append(sel.xpath('//div[@data-index = "' + str(i) + '"]//tbody').extract()[j].count("</tr>"))



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
		for i in range(len(price)):
			price[i] = decode(decode_dict, price[i])
		
		

		item = RowpieceItem()
		item['cinema_name'] = cinema_name
		item['movie_name'] = movie_name
		item['date'] = date
		item['begin_time'] = begin_time
		item['end_time'] = end_time
		item['language'] = language
		item['hall'] = hall
		item['price'] = price
		item['date_count'] = date_count
		item['show_count'] = show_count

		yield item