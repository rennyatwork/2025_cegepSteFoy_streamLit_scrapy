import scrapy
from scrapy.crawler import CrawlerProcess

class SimpleSpider(scrapy.Spider):
    name = "simple_spider"
    start_urls = []

    def __init__(self, url=None, *args, **kwargs):
        super(SimpleSpider, self).__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]

    def parse(self, response):
        title = response.css('title::text').get()
        print(f"Title: {title}")

if __name__ == "__main__":
    url = input("Enter URL to scrape: ")
    process = CrawlerProcess()
    process.crawl(SimpleSpider, url=url)
    process.start()
