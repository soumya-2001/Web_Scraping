import scrapy
from Mytheresa_project.items import MyprojectItem

class MytheresaSpider(scrapy.Spider):
    name = "mytheresa_spider"
    start_urls = ['https://www.mytheresa.com/int/en/men/shoes?rdr=mag'] # Replace with the actual URL you want to scrape
    

    def parse(self, response):
        item = MyprojectItem()
        for product in response.css('div.item'):
            item['link'] = product.css('a.item__link::attr(href)').get()
            item['designer'] = product.css('div.item__info__header__designer::text').get()
            item['name'] = product.css('div.item__info__name a::text').get()
            item['original_price'] = product.css('span.pricing__prices__value--original::text').get()
            item['discounted_price'] = product.css('span.pricing__prices__value--discount::text').get()
            item['discount'] = product.css('div.pricing__extra::text').get()
            yield item

        next_page = response.css('a.pagination__item__text--active[href*="nextPage"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)