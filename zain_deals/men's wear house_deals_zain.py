# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class MensSpider(scrapy.Spider):
    name = 'mens'
    allowed_domains = ['menswearhouse.com']
    start_urls = ['https://menswearhouse.com/mens-clothing-sale']

    def parse(self, response):
        categories = response.xpath('//*[@id="promos"]/div/a/@href').extract()
        for category in categories:
        	yield Request(category, callback=self.product_parser)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="product-name"]/@href').extract()
    	for product in products:
    		yield Request(product, callback=self.product_data)

    def product_data(self, response):
    	request = {}
    	try:
    		price = response.xpath('//*[@class="final-price clearance regular"]/text()').extract_first()[1:]
    		if not price:
    			request["SNR_Price"] = '0.00'
    		else:
    			request["SNR_Price"] = price
    	except Exception:
    		pass
    	try:
    		price_before = response.xpath('//*[@class="regular markdowns"]/text()').extract_first()[1:]
    		if not price_before:
    			request["SNR_PriceBefore"] = '0.00'
    		else:
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass
    	try:
    		title = response.xpath('//h1/text()').extract_first().strip()
    		if not title:
    			request["SNR_Title"] = 'Not Available'
    		else:
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		sub_ctegory =  response.xpath('//*[@class="breadcrumb"]/span/a/text()').extract()[-2].strip()
    		if not sub_ctegory:
    			request["SNR_SubCategory"] = "Not Available"
    		else:
    			request["SNR_SubCategory"] = sub_ctegory
    	except Exception:
    		pass
    	try:
    		description = response.xpath('//*[@itemprop="description"]/text()').extract_first().strip()
    		if not description:
    			request["SNR_Description"] = "Visit site to see description"
    		else:
    			request["SNR_Description"] = description
    	except Exception:
    		pass
    	try:
    		img =  response.xpath('//*[@itemprop="image"]/@src').extract_first()
    		request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//*[@id="sku"]/span/text()').extract_first().strip()
    		if not sku:
    			request["SNR_SKU"] = '00'
    		else:
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Brand"] = "Not Available"
    	request["SNR_Category"] = "Deals"
    	request["SNR_ModelNo"] = "00"
    	request["SNR_UPC"] = "00"
    	request["SNR_Available"] = "Men's WearHouse"
    	request["SNR_Date"] = '00'
    	request["SNR_CustomerReviews"] = "0"
    	request["SNR_Condition"] = "00"
    	request["SNR_isShow"] = True
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(MensSpider)

process.start()
