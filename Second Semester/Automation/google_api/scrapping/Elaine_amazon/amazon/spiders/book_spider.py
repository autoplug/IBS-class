import scrapy
#from items_copy import Book_item
from ..items import Book_item
from scrapy.crawler import CrawlerProcess
import re

# Create a crawler that gets at least 5000 product names, ratings and prices from the book category
class ExceptionEndScy(Exception):
    pass


class Book_spider(scrapy.Spider):
    name = "book_spider"

    start_urls = ['https://www.amazon.com/s?rh=n%3A133140011&fs=true&ref=lp_133140011_sar']

    custom_settings = {'FEEDS': {'books.csv': {"format": 'csv', 'overwrite': True}}}  


    def parse(self, response):
        book_results = response.xpath("//div[@data-asin != '']").xpath(".//@data-index").getall()
        counter = 0

        for index in book_results:
            book = Book_item()
            book['book_title'] = response.xpath(f"//div[@data-index='{index}']/.//span[@class='a-size-medium a-color-base a-text-normal']/text()").get()
            book['book_rating'] = response.xpath(f"//div[@data-index='{index}']").xpath(".//div[@class='a-row a-size-small']/span[1]/@aria-label").get()
            book['kindle_price'] = response.xpath(f"//div[@data-index='{index}']").xpath(".//span[@class='a-offscreen']/text()").get()  
            counter += 1
            yield book

            if counter == 1000:              
                #import sys
                #sys.exit(0)
                raise ExceptionEndScy("Over the given limit")
        
        #go to next page
        next_page = response.xpath("//span[@class='s-pagination-strip']/a[contains(@aria-label,'Go to next page')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)




if __name__ == "__main__":
    process = CrawlerProcess()  # instantiates CrawlerProcess, a Scrapy utility to run a spider from a python script
    process.crawl(Book_spider)   # runs the crawler with the given spider class name
    process.start()             # the script will block here until the crawling is finished
