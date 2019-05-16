# -*- coding: utf-8 -*-
import scrapy
from time import sleep


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.criminalminds.wikia.com/wiki/']
    start_urls = ['http://criminalminds.wikia.com/wiki/Extreme_Aggressor']

    def parse(self, response):
        ep_detail = response.xpath('//*[@class="pi-navigation pi-item-spacing pi-secondary-background pi-secondary-font"]/center/i/text()').extract_first()
        title = response.xpath('//*[@class="page-header__title"]/text()').extract_first()
        quotes = response.xpath('//*[@id="Bookend_Quotes"]/following::ul[1]/li/text()').extract()
        for quote in quotes:
        	yield{
        		'Quote': quote,
        		'Detail': ep_detail,
        		'Episode Name': title
        	}

        next_page_url = response.xpath('//aside/section//tbody//td[last()]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url, dont_filter=True)
        sleep(10)