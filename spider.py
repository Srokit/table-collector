"The spider which will crawl the web and collect table tags."

import scrapy

class TableCollectSpider(scrapy.Spider):
    name = "table_collect"
    start_urls = [
            # Reddit is a starting point with a lot of links
            'http://www.reddit.com/',
    ]

    def parse(self, response):
        for table in response.css('table'):
            table_text = table.extract()
            print(table_text)
        for a in response.css('a'):
            yield response.follow(a, callback=self.parse)

