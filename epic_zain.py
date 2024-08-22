# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
import requests
from scrapy.crawler import CrawlerProcess


class EpicSpider(scrapy.Spider):
    name = 'epic'
    allowed_domains = ['epicsports.com']
    start_urls = ['http://epicsports.com']

    def parse(self, response):
        all_links = response.xpath('//*[@id="menu"]/li/a/@href').extract()[1:]
        for link in all_links:
        	yield Request(link, callback=self.parses)

    def parses(self, response):
    	sub_links = response.xpath('//*[@class="cat"]/a/@href').extract()
    	for sub in sub_links:
    		yield Request(sub, callback=self.pars)

    def pars(self, response):
    	products = response.xpath('//*[@class="prod"]/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
    	request = {}
    	try:
    		price = response.xpath('//*[@id="spanSkuPrice"]/text()').extract_first()
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@id="spanSkuPrice"]/text()').extract_first()
    			request["SNR_Price"] = price
    	except Exception:
    		pass

    	try:
    		img_url = response.xpath('//center/img/@src').extract_first()
    		if not img_url:
    			img_url = 'Not Available'
    			request["SNR_ImageURL"] = img_url
    		else:
    			img_url = response.xpath('//center/img/@src').extract_first()
    			request["SNR_ImageURL"] = img_url
    	except Exception:
    		pass

    	try:
    		title = response.xpath('//*[@class="prod_name"]/text()').extract_first().strip()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//*[@class="prod_name"]/text()').extract_first().strip()
    			request["SNR_Title"] = title
    	except Exception:
    		pass

    	try:
    		item_num =  response.xpath('//*[@class="p-info"]/text()').extract()[4].strip()
    		if not item_num:
    			item_num = '00'
    			request["SNR_SKU"] = item_num
    		else:
    			item_num =  response.xpath('//*[@class="p-info"]/text()').extract()[4].strip()
    			request["SNR_SKU"] = item_num
    	except Exception:
    		pass

    	try:
    		price_before = response.xpath('//*[@class="p-info"]/text()').extract()[9].strip()
    		if not price_before:
    			price_before = '0.00'
    			request["SNR_PriceBefore"] = price_before
    		else:
    			price_before = response.xpath('//*[@class="p-info"]/text()').extract()[9].strip()
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass


    	try:
    		reviews = response.xpath('//*[@itemprop="ratingCount"]/text()').extract_first()
    		if not reviews:
    			reviews = '00'
    			request["SNR_CustomerReviews"] = reviews
    		else:
    			reviews = response.xpath('//*[@itemprop="ratingCount"]/text()').extract_first()
    			request["SNR_CustomerReviews"] = reviews
    	except Exception:
    		pass

    	description = 'Visit to see description'
    	prodcut_url = response.url
    	request["SNR_ProductURL"] = prodcut_url

    	try:
    		brand = response.xpath('//*[@itemprop="brand"]/text()').extract_first()
    		if not brand:
    			brand = 'Not Available'
    			request["SNR_Brand"] = brand
    		else:
    			brand = response.xpath('//*[@itemprop="brand"]/text()').extract_first()
    			request["SNR_Brand"] = brand
    	except Exception:
    		pass

    	request["SNR_isShow"] = True
    	request["SNR_SubCategory"] = '0'
    	request["SNR_Condition"] = '0'
    	request["SNR_Date"] = 'Not Available'
    	request["SNR_Available"] = 'EpicSports'
    	request[ "SNR_UPC"] = '00'
    	request["SNR_ModelNo"] = '00'

    	url = "http://127.0.0.1:8000/products/InsertProduct/"
    	headers = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=headers, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(EpicSpider)

process.start(stop_after_crawl=False)