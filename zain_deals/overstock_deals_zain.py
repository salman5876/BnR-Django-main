# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['overstock.com']
    start_urls = ['https://overstock.com/deals']

    def parse(self, response):
        all_links = response.xpath('//*[@class="category-events-tile common-deals-tile"]/a/@href').extract()
        for link in all_links:
        	absolute_link = response.urljoin(link)
        	yield Request(absolute_link, callback=self.products)

    def products(self, response):
    	products = response.xpath('//*[@class="product-link"]/@href').extract()
    	for product in products:
    		yield Request(product, callback=self.product_data)

    def product_data(self, response):
    	request = {}
    	try:
    		price = response.xpath('//*[@class="monetary-price-value"]/span/text()').extract()[1:]
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = float(response.xpath('//*[@class="monetary-price-value"]/span/text()').extract()[1])
    			price = float(price * 0.0086)
    			request["SNR_Price"] = price
    	except Exception:
    		pass

    	try:
    		img =  response.xpath('//*[@class="thumb-frame"]/ul/li/img/@src').extract_first()
    		if not img:
    			img = 'Not Available'
    			request["SNR_ImageURL"] = img
    		else:
    			img =  response.xpath('//*[@class="thumb-frame"]/ul/li/img/@src').extract_first()
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass


    	try:
    		model_num = response.xpath('//*[@class="item-number"]/text()').extract_first().strip()[6:]
    		if not model_num:
    			model_num = '00'
    			request["SNR_ModelNo"] = model_num
    		else:
    			model_num = response.xpath('//*[@class="item-number"]/text()').extract_first().strip()[6:]
    			request["SNR_ModelNo"] = model_num
    	except Exception:
    		pass

    	try:
    		title = response.xpath('//*[@class="product-title"]/h1/text()').extract_first().strip()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//*[@class="product-title"]/h1/text()').extract_first().strip()
    			request["SNR_Title"] = title
    	except Exception:
    		pass

    	try:
    		reviews = response.xpath('//*[@class="count"]/text()').extract_first()
    		if not reviews:
    			reviews = '00'
    			request["SNR_CustomerReviews"] = reviews
    		else:
    			reviews = response.xpath('//*[@class="count"]/text()').extract_first()
    			reviews = reviews.replace('Reviews','')
    			request["SNR_CustomerReviews"] = reviews
    	except Exception:
    		pass

    	try:
    		brand = response.xpath('//*[@id="brand-name"]/a/text()').extract_first()
    		if not brand:
    			brand = 'Not Available'
    			request["SNR_Brand"] = brand
    		else:
    			brand = response.xpath('//*[@id="brand-name"]/a/text()').extract_first()
    			request["SNR_Brand"] = brand
    	except Exception:
    		pass

    	try:
    		sub_category = response.xpath('//*[@class="breadcrumbs"]/li/a/span/text()').extract()[-1]
    		if not sub_category:
    			sub_category = '00'
    			request["SNR_SubCategory"] = sub_category
    		else:
    			sub_category = response.xpath('//*[@class="breadcrumbs"]/li/a/span/text()').extract()[-1]
    			request["SNR_SubCategory"] = sub_category
    	except Exception:
    		pass

    	try:
    		description = response.xpath('//*[@itemprop="description"]/div/text()').extract_first()
    		if not description:
    			description = 'Visit site to see description'
    			request["SNR_Description"] = description
    		else:
    			description = response.xpath('//*[@itemprop="description"]/div/text()').extract_first()
    			request["SNR_Description"] = description
    	except Exception:
    		pass

    	product_url = response.url
    	request["SNR_ProductURL"] = product_url
    	request["SNR_Category"] = "Deals"
    	request["SNR_UPC"] = "00"
    	request["SNR_SKU"] = "00"
    	request["SNR_Available"] = "OverStock"
    	request["SNR_Date"] = "Not Available"
    	request["SNR_PriceBefore"] = "0.00"
    	request["SNR_Condition"] = "00"
    	request["SNR_isShow"] = True
    	
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header , data=json.dumps(request))

process = CrawlerProcess({
	'User-Agent':	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})
process.crawl(StockSpider)

process.start()

