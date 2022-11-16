import scrapy
from amazon.items import Amazon_item
from scrapy.crawler import CrawlerProcess

# Create a crawler that gets all the product names, ratings and prices from this page: https://www.amazon.com/s?k=kindle

class Amazon_spider(scrapy.Spider):
    name = "amazon_spider"

    start_urls = ['https://www.amazon.com/s?k=kindle']

    custom_settings = {'FEEDS': {'amazon.csv': {"format": 'csv', 'overwrite': True}}}  


    def parse(self, response):
        product_names = response.css("span.a-size-medium.a-color-base.a-text-normal::text").getall()
        ratings = response.css("span.a-icon-alt::text").getall()
        prices = response.css("span.a-price span.a-offscreen::text").getall()
        product_dict = {"product_names": product_names, "ratings": ratings, "prices":prices}
      
        for item in range(len(product_names)-1):
            product = Amazon_item()
            product['product_name'] = product_dict['product_names'][item]
            product['rating'] = product_dict['ratings'][item]
            product['price'] = product_dict['prices'][item]
            yield product



# to run the crawler script as a standalone python file (i.e., not from main.py)
if __name__ == "__main__":
    process = CrawlerProcess()  # instantiates CrawlerProcess, a Scrapy utility to run a spider from a python script
    process.crawl(Amazon_spider)   # runs the crawler with the given spider class name
    process.start()             # the script will block here until the crawling is finished

