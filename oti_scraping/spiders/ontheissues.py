import scrapy

from oti_scraping.items import * 

state_prefs = ['AK/', 'AL/', 'AR/', 'AZ/', 'CA/', 'CO/', 'CT/', 'DC/', 'DE/', 'FL/', 'GA/', 'HI/', 'IA/', 'ID/', 'IL/', 'IN/', 'KS/', 'KY/', 'LA/', 'MA/',
'MD/', 'ME/', 'MI/', 'MN/', 'MO/', 'MS/', 'MT/', 'NC/', 'ND/', 'NE/', 'NH/', 'NJ/', 'NM/', 'NV/', 'NY/',
'OH/', 'OK/', 'OR/', 'PA/', 'RI/', 'SC/', 'SD/', 'TN/', 'TX/', 'UT/', 'VA/', 'VT/', 'WA/', 'WI/', 'WV/', 'WY/']

class OnTheIssuesSpider(scrapy.Spider):
	name = "oti"

	def start_requests(self):
		urls = [
			#'http://senate.ontheissues.org/Senate/Tom_Udall.htm',
			'http://senate.ontheissues.org/Senate/Senate.htm',
			'http://senate.ontheissues.org/House.htm'
		]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		if response.url == 'http://senate.ontheissues.org/Senate/Senate.htm':
			info = response.xpath('//td/a/@href').extract()
			info = list(info)
			info = list(filter(lambda x: not '/' in x and '_' in x, info))[17:]
			info = set(info)
			# print(info)
			# print(len(info))
			base_url = 'http://senate.ontheissues.org/Senate/'
			for page in info:
				page = base_url + page
				yield scrapy.Request(page, callback=self.parse)
			return
		if response.url == 'http://senate.ontheissues.org/House.htm':
			info = response.xpath('//td/a/@href').extract()
			info = list(info)
			info = list(filter(lambda x: (x[:3] in state_prefs or 'House/' in x) and '_' in x, info))[17:]
			#print(info)
			#print(len(info))
			base_url = 'http://senate.ontheissues.org/'
			for page in info:
				page = base_url + page
				yield scrapy.Request(page, callback=self.parse)
			return
		#print("response:", response.body)
		pol_info = response.xpath('//font[@face="Verdana, Arial, Tahoma, Helvetica, Sans-Serif"]/b/text()').extract()
		name_path = response.url.split("/")[-1].split(".")[0]
		pic_url = 'http://senate.ontheissues.org/pictures/' + name_path + '.jpg'

		politician = PoliticianItem(name=pol_info[1].rstrip(), office=pol_info[0], pic_url=pic_url)

		tables = response.xpath('//ul')
		names = response.xpath('//td[@align="center"]/font[@face="Arial"]/text()').extract()
		issues = list()
		for x in range(0, len(names)):
			#print("hey:", tables[x])
			items = tables[x].xpath('li/text()').extract()
			#print(items)
			# cool = tables[x].xpath('li')
			# print(cool)
			new_items = list()
			skip = False
			for item in items:
				if "Rated" in item:
					skip = True
				elif not skip:
					new_items.append(item)
				else:
					skip = False
			print(new_items)

			issue = IssueItem(issue=names[x].rstrip(), stances=new_items)
			issues.append(dict(issue))

		politician['issues'] = issues
		yield politician
