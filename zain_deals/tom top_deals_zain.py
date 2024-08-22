# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class TomSpider(scrapy.Spider):
    name = 'tom'
    allowed_domains = ['tomtop.com']
    start_urls = ['https://tomtop.com/clearance']

    def parse(self, response):
        categories = response.xpath('//*[@class="clearance-category"]/ul/li/a/@href').extract()
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.product_parser)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="productTitle"]/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)
    	next_page = response.xpath('//a[text()="Next Page"]/@href').extract_first()
    	absolute_next = response.urljoin(next_page)
    	yield Request(absolute_next)

    def product_data(self, response):
    	request = {}
    	try:
    		img = response.xpath('//*[@class="wrap"]/a/img/@src').extract_first()
    		if not img:
    			img = 'Not Available'
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//*[@class="wrap"]/a/img/@src').extract_first()
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		price =  response.xpath('//*[@id="detailPrice"]/text()').extract_first()
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price =  response.xpath('//*[@id="detailPrice"]/text()').extract_first()
    			request["SNR_Price"] = price
    	except Exception:
    		pass
    	try:
    		title = response.xpath('//h1/span/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//h1/span/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//*[@id="p_sku_s"]/text()').extract_first()
    		if not sku:
    			sku = '00'
    			request["SNR_SKU"] = sku
    		else:
    			sku = response.xpath('//*[@id="p_sku_s"]/text()').extract_first()
    			sku = sku.replace('Item#:','')
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	try:
    		sub_category = response.xpath('//*[@class="Bread_crumbs lbUl"]/li/a/span/text()').extract()[-1]
    		if not sub_category:
    			sub_category = '00'
    			request["SNR_SubCategory"] = sub_category
    		else:
    			sub_category = response.xpath('//*[@class="Bread_crumbs lbUl"]/li/a/span/text()').extract()[-1]
    			request["SNR_SubCategory"] = sub_category
    	except Exception:
    		pass
    	try:
    		reviews = response.xpath('//*[@itemprop="reviewCount"]/text()').extract_first()
    		if not reviews:
    			reviews = '0'
    			request["SNR_CustomerReviews"] = reviews
    		else:
    			reviews = response.xpath('//*[@itemprop="reviewCount"]/text()').extract_first()
    			request["SNR_CustomerReviews"] = reviews
    	except Exception:
    		pass
    	try:
    		description = response.xpath('//*[@id="description"]/text()').extract_first().strip()
    		if not description:
    			description = 'Visit site to see description'
    			request["SNR_Description"] = description
    		else:
    			description = response.xpath('//*[@id="description"]/text()').extract_first().strip()
    			request["SNR_Description"] = description
    	except Exception:
    		pass
    	request["SNR_Brand"] = "Not Available"
    	request["SNR_Category"] = "Deals"
    	request["SNR_ModelNo"] = "00"
    	request["SNR_UPC"] = "00"
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Available"] = "TomTop"
    	request["SNR_Date"] = '00'
    	request["SNR_PriceBefore"] = '0.00'
    	request["SNR_Condition"] = "00"
    	request["SNR_isShow"] = True
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))
process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})

process.crawl(TomSpider)

process.start()