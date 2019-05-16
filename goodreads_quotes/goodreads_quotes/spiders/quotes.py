# -*- coding: utf-8 -*-
import scrapy
from time import sleep

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.goodreads.com/quotes']
    start_urls = ['http://www.goodreads.com/quotes/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            texttemp = quote.xpath('.//div[@class="quoteText"]/text()[1]').extract()
            text = "".join(texttemp)
            author = quote.xpath('.//span[@class="authorOrTitle"]/text()').extract_first()

            yield {
                'Text': text,
        	    'Author': author
        	}

        next_page_url = response.xpath('//*[@class="next_page"]/@href').extract_first() # quotes?page=2
        if next_page_url is not None:
        	absolute_next_page_url = response.urljoin(next_page_url)	# https://www.goodreads.com/quotes?page=2
        	yield scrapy.Request(absolute_next_page_url, dont_filter=True)
        sleep(5)