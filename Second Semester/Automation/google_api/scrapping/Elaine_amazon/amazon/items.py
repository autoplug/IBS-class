# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Amazon_item(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()


class Book_item(scrapy.Item):
    book_title = scrapy.Field()
    book_rating = scrapy.Field()
    kindle_price = scrapy.Field()

class Wiki_item(scrapy.Item):
    pass
    
