# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class KaySpider(scrapy.Spider):
    name = 'kay'
    allowed_domains = ['kay.com']
    start_urls = ['http://kay.com/en/kaystore/cms/Clearance']

    def parse(self, response):
        categories = response.xpath('//*[@class="timeControlledSections"]/ul/li/a/@href').extract()[7:]
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.products)

    def products(self, response):
    	products = response.xpath('//*[@class="row plp-products"]/div/div/a/@href').extract()
    	for product in products:
    		yield Request(product, callback=self.product_data)

    def product_data(self, response):
    	request = {}
    	try:
    		price = response.xpath('//*[@class="product-price"]/text()').extract_first().strip()
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@class="product-price"]/text()').extract_first().strip()
    			price = price.replace('$','')
    			request["SNR_Price"] = price
    	except Exception:
    		pass
    	try:
    		price_before = response.xpath('//*[@class="product-price"]/text()').extract()[1].strip()[14:23].strip()
    		if not price_before:
    			price_before = '0.00'
    			request["SNR_PriceBefore"] = price_before
    		else:
    			price_before = response.xpath('//*[@class="product-price"]/text()').extract()[1].strip()[14:23].strip()
    			price_before = price_before.replace('$','')
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass
    	try:
    		img = response.xpath('//*[@class="main-responsive-image"]/@src').extract()[1]
    		if not img:
    			img = response.xpath('//*[@class="thumbnail-responsive-image"]/@data-src').extract_first()
    			img = 'http://www.kay.com/' + img
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//*[@class="main-responsive-image"]/@src').extract()[1]
    			img = 'http://www.kay.com/' + img
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//*[@class="productSKU"]/text()').extract_first()[7:]
    		if not sku:
    			sku = '00'
    			request["SNR_SKU"] = sku
    		else:
    			sku = response.xpath('//*[@class="productSKU"]/text()').extract_first()[7:]
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	try:
    		description = response.xpath('//*[@class="pip-accordion__text large-9 columns"]/text()').extract_first().strip()
    		if not description:
    			description = 'Visit site to see description'
    			request["SNR_Description"] = description
    		else:
    			description = response.xpath('//*[@class="pip-accordion__text large-9 columns"]/text()').extract_first().strip()
    			request["SNR_Description"] = description
    	except Exception:
    		pass
    	try:
    		title = response.xpath('//h1/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//h1/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Brand"] = 'Not Available'
    	request["SNR_Category"] = "Deals"
    	request["SNR_ModelNo"] = '00'
    	request["SNR_UPC"] = "00"
    	request["SNR_Available"] = 'Kay'
    	request["SNR_Date"] = '00'
    	request["SNR_CustomerReviews"] = "0"
    	request["SNR_Condition"] = "00"
    	request["SNR_SubCategory"] = 'Clearance'
    	request["SNR_isShow"] = True
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(KaySpider)

process.start()



