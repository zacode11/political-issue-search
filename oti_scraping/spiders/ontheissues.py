import scrapy

from political.items import * 

class OnTheIssuesSpider(scrapy.Spider):
	name = "oti"

	def start_requests(self):
		urls = [
			'http://senate.ontheissues.org/Senate/Richard_Shelby.htm',
			'http://senate.ontheissues.org/Senate/Jeff_Sessions.htm',
			'http://senate.ontheissues.org/Senate/Lisa_Murkowski.htm',
			'http://senate.ontheissues.org/Senate/Dan_Sullivan.htm',
			'http://senate.ontheissues.org/Senate/John_McCain.htm',
		]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		#print("response:", response.body)
		pol_info = response.xpath('//font[@face="Verdana, Arial, Tahoma, Helvetica, Sans-Serif"]/b/text()').extract()
		name_path = response.url.split("/")[-1].split(".")[0]
		pic_url = 'http://senate.ontheissues.org/pictures/' + name_path + '.jpg'

		politician = PoliticianItem(name=pol_info[1].rstrip(), office=pol_info[0], pic_url=pic_url)

		tables = response.xpath('//ul')
		names = response.xpath('//td[@align="center"]/font[@face="Arial"]/text()').extract()
		issues = list()
		for x in range(0, len(names)):
			print("hey:", tables[x])
			items = tables[x].xpath('li/text()').extract()
			issue = IssueItem(issue=names[x].rstrip(), stances=items)
			issues.append(dict(issue))
			print("--------------ITEMS:", items)

		politician['issues'] = issues
		yield politician
