# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess


class FanasSpider(scrapy.Spider):
    name = 'fanas'
    allowed_domains = ['fanastic.com']
    start_urls = ['https://www.fanatics.com/']

    def parse(self, response):
    	all_urls = response.xpath('//*[@class="top-nav-component pointer"]/li/a/@href').extract()[1:10]
    	for all_url in all_urls:
    		absolute_all_urls = response.urljoin(all_url)
    		yield Request(absolute_all_urls, callback=self.parses, dont_filter=True)
    
    def parses(self, response):
	    sub_urls = response.xpath('//*[@class="team-list-link"]/@href').extract()
	    for sub in sub_urls:
	    	absolute_sub_urls = response.urljoin(sub)
	    	yield Request(absolute_sub_urls, callback=self.pars, dont_filter=True)


    def pars(self, response):
    	sub_products = response.xpath('//*[@class="dept-card"]/a/@href').extract()
    	for sub_product in sub_products:
    		absolute_sub_products = response.urljoin(sub_product)
    		yield Request(absolute_sub_products, callback=self.products, dont_filter=True)

    def products(self, response):
    	products =  response.xpath('//*[@class="product-image-container"]/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request (absolute_product, callback=self.product_data, dont_filter=True)

    def product_data(self, response):
    	request = {}
    	try:
    		price = response.xpath('//*[@class="regular-price"]/text()').extract_first()[13:]
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = prices
    		else:
    			price = response.xpath('//*[@class="regular-price"]/text()').extract_first()[13:]
    			request["SNR_Price"] = prices
    	except Exception:
    		pass

    	try:
    		title= response.xpath('//*[@class="product-title-container"]/h1/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title= response.xpath('//*[@class="product-title-container"]/h1/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass

    	try:
    		product_id = response.xpath('//*[@class="breadcrumb-text"]/text()').extract_first()[12:]
    		if not product_id:
    			product_id = '0'
    			request["SNR_UPC"] = product_id
    		else:
    			product_id = response.xpath('//*[@class="breadcrumb-text"]/text()').extract_first()[12:]
    			request["SNR_UPC"] = product_id
    	except Exception:
    		pass

    	try:
    		img_url = response.xpath('//*[@class="carousel transition"]/img/@src').extract_first()
    		if not img_url:
    			img_url = '0'
    			request["SNR_ImageURL"] = img_url
    		else:
    			img_url = response.xpath('//*[@class="carousel transition"]/img/@src').extract_first()
    			img_url = img_url.replace('//','https://')
    			request["SNR_ImageURL"] = img_url
    	except Exception:
    		pass

    	try:
    		description = response.xpath('//*[@class="description-box-content"]/div/text()').extract_first()
    		if not description:
    			description = 'Visit to see Description'
    			request ["SNR_Description"] = description
    		else:
    			description = response.xpath('//*[@class="description-box-content"]/div/text()').extract_first()
    			request ["SNR_Description"] = description
    	except Exception:
    		pass

    	product_url =  response.url
    	request["SNR_ProductURL"] = product_url

    	try:
    		brand =  response.xpath('//*[@class="description-box-content"]/ul/li/text()').extract()[-1][7:]
    		if not brand:
    			brand = 'Not Available'
    			request["SNR_Brand"] = brand
    		else:
    			brand =  response.xpath('//*[@class="description-box-content"]/ul/li/text()').extract()[-1][7:]
    			request["SNR_Brand"] = brand
    	except Exception:
    		pass

    	request["SNR_SKU"] = '00'
        request["SNR_SubCategory"] = '00'
        request["SNR_Available"] = 'Fanatics'
        request["SNR_Condition"] = '00'
        request["SNR_CustomerReviews"] = '00'
        request["SNR_isShow"] = True
        request["SNR_PriceBefore"] = '0.00'
        request["SNR_Date"] = 'Not Available'
        request["SNR_ModelNo"] = '00'
        request["SNR_Category"] = 'Deals'

    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	headers = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=headers, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(FanasSpider)

process.start()






