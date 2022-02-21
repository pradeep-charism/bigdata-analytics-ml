# bigdata-analytics-ml

Legalality for webscrapping? Is it Ethical?


#Scrapy
https://docs.scrapy.org/en/latest/intro/tutorial.html
scrapy startproject tutorial

import scrapy
from scrapy.crawler import CrawlerProcess
class TestSpider(scrapy.Spider):
    name = 'test'
if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(TestSpider)
  process.start()

