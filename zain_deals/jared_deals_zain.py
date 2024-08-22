# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
import requests
import json


class JaredSpider(scrapy.Spider):
    name = 'jared'
    allowed_domains = ['jared.com']
    start_urls = ['http://jared.com/en/jaredstore/cms/jared-vault-values']

    def parse(self, response):
        categories =  response.xpath('//*[@class="site-sidebar__links"]/li/a/@href').extract()
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.product_parser)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="plp-product-anchor"]/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
    	request = {}
    	try:
    		img = response.xpath('//*[@class="main-responsive-image"]/@data-src').extract_first()
    		if not img:
    			img = response.xpath('//*[@class="main-responsive-image"]/@src').extract()[1]
    			img = "http://www.jared.com"+ img
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//*[@class="main-responsive-image"]/@data-src').extract_first()
    			img = "http://www.jared.com"+ img
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		price = response.xpath('//*[@class="product-price"]/text()').extract()[1].strip()
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@class="product-price"]/text()').extract()[1].strip()
    			price = price.replace('$','')
    			request["SNR_Price"] = price
    	except Exception:
    		pass
    	try:
    		price_before = response.xpath('//*[@class="product-price"]/p/text()').extract_first()
    		if not price_before:
    			price_before = '0.00'
    			request["SNR_PriceBefore"] = price_before
    		else:
    			price_before = response.xpath('//*[@class="product-price"]/p/text()').extract_first()
    			price_before = price_before.replace('Orig: $','')
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//*[@class="productSKU"]/text()').extract_first()
    		if not sku:
    			sku = '0'
    			request["SNR_SKU"] = sku
    		else:
    			sku = response.xpath('//*[@class="productSKU"]/text()').extract_first()
    			sku = sku.replace('Stock #','')
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	try:
    		title = response.xpath('//h1/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request[ "SNR_Title"] = title
    		else:
    			title = response.xpath('//h1/text()').extract_first()
    			request[ "SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		description = response.xpath('//*[@class="pip-accordion__text large-9 columns"]/text()').extract_first().strip()
    		if not description:
    			description = 'Visit site to see description'
    			request[ "SNR_Description"] = description
    		else:
    			description = response.xpath('//*[@class="pip-accordion__text large-9 columns"]/text()').extract_first().strip()
    			request[ "SNR_Description"] = description
    	except Exception:
    		pass
    	request["SNR_Brand"] = 'Not Available'
    	request["SNR_Category"] = "Deals"
    	request["SNR_ModelNo"] = "00"
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Available"] = "Jared"
    	request["SNR_Date"] = '00'
    	request["SNR_CustomerReviews"] = "0"
    	request["SNR_Condition"] = "00"
    	request["SNR_UPC"] = '00'
    	request["SNR_SubCategory"] = "00"
    	request["SNR_isShow"] = True
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))
