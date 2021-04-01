# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SenadoresItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    party = scrapy.Field()
    uf = scrapy.Field()
    period = scrapy.Field()
    phones = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
