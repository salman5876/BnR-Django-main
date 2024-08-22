# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess


class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['appoutdoors.com']
    start_urls = ['http://appoutdoors.com/clearance_c19611.htm']

    def parse(self, response):
    	try:
    		products = response.xpath('//*[@class="product_grid_list-content"]/a/@href').extract()
    		for product in products:
    			absolute_product = response.urljoin(product)
    			yield Request(absolute_product, callback=self.product_data, dont_filter=True)
    	except Exception:
    		pass

    	next_page_url = response.xpath('//*[@class="cd-pagination"]/li/a/@href').extract()
    	for page in next_page_url:
    		absolute_next_page = response.urljoin(page)
    		yield Request(absolute_next_page)
    		try:
    			products = response.xpath('//*[@class="product_grid_list-content"]/a/@href').extract()
    			for product in products:
    				absolute_product = response.urljoin(product)
    				yield Request(absolute_product, callback=self.product_data, dont_filter=True)
    		except Exception:
    			pass

    def product_data(self, response):
    	request = {}
    	try:
    		img = response.xpath('//img/@src').extract()[6]
    		if not img:
    			img = 'Not Available'
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//img/@src').extract()[6]
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass


    	try:
    		model_num = response.xpath('//*[@class="modelNum"]/text()').extract_first()
    		if not model_num:
    			model_num="00"
    			request["SNR_ModelNo"] = model_num
    		else:
    			model_num = response.xpath('//*[@class="modelNum"]/text()').extract_first()
    			request["SNR_ModelNo"] = model_num
    	except Exception:
    		pass


    	try:
    		title = response.xpath('//*[@class="productDetailHeader"]/h1/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//*[@class="productDetailHeader"]/h1/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass


    	try:
    		price_before = response.xpath('//*[@id="pricing"]/p/text()').extract_first()[1:]
    		if not price_before:
    			price_before = "00"
    			request["SNR_PriceBefore"] = price_before
    		else:
    			price_before = response.xpath('//*[@id="pricing"]/p/text()').extract_first()[1:]
    			price_before = price_before .replace('Original','')
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass


    	try:
    		category = response.xpath('//*[@class="bcrumb"]/li/a/text()').extract()[-1]
    		if not category:
    			category = "00"
    			request["SNR_Category"] = category
    		else:
    			category = response.xpath('//*[@class="bcrumb"]/li/a/text()').extract()[-1]
    			request["SNR_Category"] = category
    	except Exception:
    		pass


    	try:
    		price = response.xpath('//*[@id="pricing"]/p[2]/text()').extract_first()[1:]
    		if not price:
    			price = "0.00"
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@id="pricing"]/p[2]/text()').extract_first()[1:]
    			price = price.replace('Price','')
    			request["SNR_Price"] = price
    	except Exception:
    		pass


    	try:
    		brand = response.xpath('/html/body/main/div/form/section[2]/div[3]/p[3]/a[1]/text()').extract_first()
    		if not brand:
    			brand = 'Not Available'
    			request["SNR_Brand"] = brand
    		else:
    			brand = response.xpath('/html/body/main/div/form/section[2]/div[3]/p[3]/a[1]/text()').extract_first()
    			brand = brand.replace('»', '')
    			request["SNR_Brand"] = brand
    	except Exception:
    		pass


    	try:
    		sub_category = response.xpath('/html/body/main/div/form/section[2]/div[3]/p[3]/a[2]/text()').extract_first()
    		if not sub_category:
    			sub_category = "00"
    			request["SNR_SubCategory"] = sub_category
    		else:
    			sub_category = response.xpath('/html/body/main/div/form/section[2]/div[3]/p[3]/a[2]/text()').extract_first()
    			sub_category = sub_category.replace('»', '')
    			request["SNR_SubCategory"] = sub_category
    	except Exception:
    		pass

    	product_url = response.url
    	request["SNR_ProductURL"] = product_url


    	request["SNR_isShow"] = True
    	request["SNR_Condition"] = "00"
    	request["SNR_CustomerReviews"] = "0"
    	request["SNR_Date"] = "0"
    	request["SNR_Available"] = "AppOutDoors"
    	request["SNR_SKU"] = "00"
    	request["SNR_UPC"] = "00"
    	request["SNR_Description"] = "Visit site to see description"

    	url = "http://127.0.0.1:9000/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})

process.crawl(AppSpider)

process.start()