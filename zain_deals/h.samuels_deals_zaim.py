# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class HsamuelsSpider(scrapy.Spider):
    name = 'hsamuels'
    allowed_domains = ['hsamuel.co.uk']
    start_urls = ['http://hsamuel.co.uk/webstore/offers.do?icid=HS-nv-Offers_Page-Shop']

    def parse(self, response):
        categories = response.xpath('//*[@class="hsft2"]/ul/li/a/@href').extract()[:10]
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.product_parser)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="product-tile__text-container"]/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.prosuct_data)

    def prosuct_data(self, response):
    	request = {}
    	try:
    		price_before = response.xpath('//*[@class="buying-info__price--was"]/text()').extract_first()[1:]
    		if not price_before:
    			price_before = '0.00'
    			request["SNR_PriceBefore"] = price_before
    		else:
    			price_before = float(response.xpath('//*[@class="buying-info__price--was"]/text()').extract_first()[1:])
    			price_before = float(price_before*1.34)
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass
    	try:
    		price = response.xpath('//*[@class="buying-info__price--save"]/text()').extract_first()
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@class="buying-info__price--save"]/text()').extract_first()
    			price = price.replace('save\r\n\t\t\t\t\t\t\t\t£','')
    			prices = float(price)
    			request["SNR_Price"] = prices*1.34
    	except Exception:
    		pass
    	try:
    		img = response.xpath('//*[@class="product-image__image"]/@src').extract_first()
    		if not img:
    			img = 'Not Available'
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//*[@class="product-image__image"]/@src').extract_first()
    			img = "http:" + img
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		title =  response.xpath('//h1/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title =  response.xpath('//h1/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//*[@id="js-skuChange"]/text()').extract_first()
    		if not sku:
    			sku = '00'
    			request["SNR_SKU"] = sku
    		else:
    			sku = response.xpath('//*[@id="js-skuChange"]/text()').extract_first()
    			sku = sku.replace('Product\r\n\t\t\t\t\tcode:','')
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	try:
    		description = response.xpath('//*[@class="description__description"]/p/text()').extract_first().strip()
    		if not description:
    			description = 'Visit site to see description'
    			request["SNR_Description"] = description
    		else:
    			description = response.xpath('//*[@class="description__description"]/p/text()').extract_first().strip()
    			request["SNR_Description"] = description
    	except Exception:
    		pass
    	request["SNR_Brand"] = "Not Available"
    	request["SNR_Category"] = "Deals"
    	request["SNR_ModelNo"] = "00"
    	request["SNR_UPC"] = "00"
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Available"] = "H.Samuel"
    	request["SNR_Date"] = '00'
    	request["SNR_CustomerReviews"] = "0"
    	request["SNR_Condition"] = "00"
    	request["SNR_SubCategory"] = '00'
    	request["SNR_isShow"] = True
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})

process.crawl(HsamuelsSpider)

process.start()