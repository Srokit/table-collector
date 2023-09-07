"The spider which will crawl the web and collect table tags."

import os
import uuid

import scrapy
from scrapy.http.response.text import TextResponse

from txt import write_to_text_file
from log import log_table
from cleandata import clean_table
from validator import table_is_valid
from save_html import save_html

TXT_FILENAME = 'dataset.txt'
HTML_OUT_DIR = 'html_out'

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
        os.system(f"rm -rf {HTML_OUT_DIR}")
        os.mkdir(HTML_OUT_DIR)

    def parse(self, response):
        if not isinstance(response, TextResponse):
            return
        for table in response.css('table'):
            table_text = table.extract()
            table_text = clean_table(table_text)
            if not table_is_valid(table_text):
                continue
            write_to_text_file(TXT_FILENAME, table_text)
            log_table(table_text)
            save_html_filename = str(uuid.uuid4()) + '.html'
            save_html(table_text, save_html_filename)
        for a in response.css('a::attr("href")'):
            href_txt = a.extract()
            if not href_txt.startswith('http') and not href_txt.startswith('/'):
                continue
            yield response.follow(a, callback=self.parse)

