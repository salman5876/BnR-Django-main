# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
import requests
import json


class AceSpider(scrapy.Spider):
    name = 'ace'
    allowed_domains = ['acehardware.com']
    start_urls = ['http://acehardware.com/category/index.jsp?categoryId=12550841']

    def parse(self, response):
        categories =  response.xpath('//*[@class="families"]/li/a/@href').extract()[:3]
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.all_parser)

    def all_parser(self, response):
    	view_all = response.xpath('//*[@class="results"]/@href').extract_first()
    	absolute_all = response.urljoin(view_all)
    	yield Request(absolute_all, callback=self.product_parser, dont_filter=True)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="fn titleLink"]/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data, dont_filter=True)

    def product_data(self, response):
    	request = {}
    	try:
    		title = response.xpath('//*[@class= "fL w327"]/h2/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//*[@class= "fL w327"]/h2/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//*[@class= "prodC3 prodItemNo"]/script/text()').extract_first()
    		if not sku:
    			sku = '00'
    			request["SNR_SKU"] = sku
    		else:
    			sku = response.xpath('//*[@class= "prodC3 prodItemNo"]/script/text()').extract_first()
    			sku = sku.replace('prodItemNo="','')
    			sku = sku.replace('";','')
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	try:
    		img = response.xpath('//*[@id="mainProdImage"]/@src').extract_first()
    		if not img:
    			img = response.xpath('//*[@class="mainImageSize "]/img/@src').extract_first()
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//*[@id="mainProdImage"]/@src').extract_first()
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		price = response.xpath('//*[@class=""]/text()').extract_first()
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@class=""]/text()').extract_first()
    			price = price.replace('$','')
    			request["SNR_Price"] = price
    	except Exception:
    		pass
    	try:
    		sub_category = response.xpath('//*[@id="crumbs"]/span/a/text()').extract()[-1]
    		if not sub_category:
    			sub_category = '00'
    			request["SNR_SubCategory"] = sub_category
    		else:
    			sub_category = response.xpath('//*[@id="crumbs"]/span/a/text()').extract()[-1]
    			request["SNR_SubCategory"] = sub_category
    	except Exception:
    		pass

    	request["SNR_ProductURL"] = response.url
    	request["SNR_Description"] =  "Visit site to see description"
    	request["SNR_Category"] = "Deals"
    	request["SNR_Brand"] = "Not Available"
    	request["SNR_ModelNo"] = "00"
    	request["SNR_UPC"] = "00"
    	request["SNR_Available"] = "ACE Hardware"
    	request["SNR_Date"] = '00'
    	request["SNR_CustomerReviews"] = "0"
    	request["SNR_PriceBefore"] = '0.00'
    	request["SNR_Condition"] = '00'
    	request["SNR_isShow"] = True
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})

process.crawl(AceSpider)

process.start()