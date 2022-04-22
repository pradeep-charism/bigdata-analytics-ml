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




Yahoo finance:
-------------
https://algotrading101.com/learn/yahoo-finance-api-guide/

http://theautomatic.net/yahoo_fin-documentation/

