# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
import requests
from scrapy.crawler import CrawlerProcess

class SoftSpider(scrapy.Spider):
    name = 'soft'
    allowed_domains = ['microsoft.com']
    start_urls = ['https://microsoft.com/en-us/store/b/sale']

    def parse(self, response):
    	see_all = response.xpath('//h2/a/@href').extract()
    	for see in see_all:
    		absolute_see_all = response.urljoin(see)
    		yield Request(absolute_see_all, callback=self.products)

    def products(self, response):
    	products = response.xpath('//*[@role="presentation"]/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
    	

    	request = {}
    	try:
    		price = response.xpath('//*[@class="price-disclaimer "]/span/text()').extract_first()[1:]
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@class="price-disclaimer "]/span/text()').extract_first()[1:]
    			request["SNR_Price"] = price
    	except Exception:
    		pass

    	try:
    		title = response.xpath('//*[@id="page-title"]/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//*[@id="page-title"]/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass


    	try:
    		sub_class = response.xpath('//*[@class="c-logo"]/span/text()').extract()[1]
    		if not sub_class:
    			sub_class = '00'
    			sub_class
    		else:
    			sub_class = response.xpath('//*[@class="c-logo"]/span/text()').extract()[1]
    			request["SNR_SubCategory"] = sub_class
    	except Exception:
    		pass

    	try:
    		img = response.xpath('//*[@class="c-image"]/img/@src').extract_first()
    		if not img:
    			img = 'Not Available'
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//*[@class="c-image"]/img/@src').extract_first()
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass

    	try:
    		price_before = response.xpath('//*[@class="price-text srv_price"]/s/text()').extract_first()[1:]
    		if not price_before:
    			price_before = response.xpath('//*[@class="price-text srv_price"]/span/text()').extract_first()[1:]
    			request["SNR_PriceBefore"] = price_before
    		else:
    			price_before = response.xpath('//*[@class="price-text srv_price"]/s/text()').extract_first()[1:]
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass

    	try:
    		reviews = response.xpath('//*[@class="c-rating cli_buybox_ratings"]/a/span/text()').extract_first()
    		if not reviews:
    			reviews = '00'
    			request["SNR_CustomerReviews"] = reviews
    		else:
    			reviews = response.xpath('//*[@class="c-rating cli_buybox_ratings"]/a/span/text()').extract_first()
    			request["SNR_CustomerReviews"] = reviews
    	except Exception:
    		pass


    	product_url = response.url
    	request["SNR_ProductURL"] = product_url

    	request["SNR_Description"] = 'Visit site to see description'
    	request["SNR_SKU"] = '00'
    	request["SNR_UPC"] = '00'
    	request["SNR_Available"] = 'Microsoft'
    	request["SNR_Condition"] = '00'
    	request["SNR_isShow"] = True
    	request["SNR_Brand"] = '00'
    	request["SNR_Category"] = 'Deals'
    	request["SNR_Date"] = '00'
    	request["SNR_ModelNo"] = '00'
    	request["SNR_SubCategory"] = '00'

    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})

process.crawl(SoftSpider)

process.start()


