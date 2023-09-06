"The spider which will crawl the web and collect table tags."

import os

import scrapy

from txt import write_to_text_file
from log import log_table
from cleandata import clean_table
from validator import table_is_valid

TXT_FILENAME = 'dataset.txt'

class TableCollectSpider(scrapy.Spider):
    name = "table_collect"
    start_urls = [
            # Reddit is a starting point with a lot of links
            'http://www.reddit.com/',
    ]

    def __init__(self, *args, **kwargs):
        "Delete dataset file so that it is fresh"
        super(TableCollectSpider, self).__init__(*args, **kwargs)
        if os.path.exists(TXT_FILENAME):
            os.remove(TXT_FILENAME)

    def parse(self, response):
        for table in response.css('table'):
            table_text = table.extract()
            table_text = clean_table(table_text)
            if not table_is_valid(table_text):
                continue
            write_to_text_file(TXT_FILENAME, table_text)
            log_table(table_text)
        for a in response.css('a'):
            yield response.follow(a, callback=self.parse)

