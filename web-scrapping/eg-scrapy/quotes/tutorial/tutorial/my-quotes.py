from scrapy.crawler import CrawlerProcess
from spiders.quotes_spider import QuotesSpider
from scrapy.crawler import CrawlerProcess

from spiders.quotes_spider import QuotesSpider

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
