import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {"FEEDS": {"../results.json": {"format": "json"}}}

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        for quote in response.css('div.quote'):
            value = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            yield value
            # filename = f'quotes.json'
            # with open(filename, 'wb') as f:
            #     f.write(value)
