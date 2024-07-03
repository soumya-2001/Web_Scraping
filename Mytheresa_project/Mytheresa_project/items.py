# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyprojectItem(scrapy.Item):
    link = scrapy.Field()
    designer = scrapy.Field()
    name = scrapy.Field()
    original_price = scrapy.Field()
    discounted_price = scrapy.Field()
    discount = scrapy.Field()
