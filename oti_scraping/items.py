# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PoliticianItem(scrapy.Item):
	name = scrapy.Field()
	office = scrapy.Field()
	pic_url = scrapy.Field()
	issues = scrapy.Field()

class IssueItem(scrapy.Item):
    issue = scrapy.Field()
    stances = scrapy.Field()

