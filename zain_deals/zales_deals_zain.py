# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class ZaleSpider(scrapy.Spider):
    name = 'zale'
    allowed_domains = ['zales.com']
    start_urls = ['https://zales.com/clearance/view-all-clearance/c/0110050000']

    def parse(self, response):
        categories = response.xpath('//*[@class="facet-list js-facet-list "]/li/span/a/@href').extract()
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.products)

    def products(self, response):
    	products = response.xpath('//*[@class="name"]/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
    	request = {}
    	try:
    		img = response.xpath('//*[@class="lazyOwl"]/@data-src').extract_first()
    		if not img:
    			img = 'Not Available'
    			request["SNR_ImageURL"] = img
    		else:
    			img = response.xpath('//*[@class="lazyOwl"]/@data-src').extract_first()
    			img = 'https://www.zales.com/'+img
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass

    	try:
    		title = response.xpath('//*[@class="name"]/text()').extract_first()
    		if not title:
    			title = 'Not Available'
    			request["SNR_Title"] = title
    		else:
    			title = response.xpath('//*[@class="name"]/text()').extract_first()
    			request["SNR_Title"] = title
    	except Exception:
    		pass

    	try:
    		price = response.xpath('//*[@itemprop="price"]/text()').extract_first()
    		if not price:
    			price = '0.00'
    			request["SNR_Price"] = price
    		else:
    			price = response.xpath('//*[@itemprop="price"]/text()').extract_first()
    			request["SNR_Price"] = price
    	except Exception:
    		pass

    	try:
    		price_before =  response.xpath('//*[@class="original-price"]/div/text()').extract_first()[6:]
    		if not price_before:
    			price_before = '0.00'
    			request["SNR_PriceBefore"] = price_before
    		else:
    			price_before =  response.xpath('//*[@class="original-price"]/div/text()').extract_first()[6:]
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass

    	try:
    		sku = response.xpath('//*[@class="product-details"]/b/text()').extract_first()
    		if not sku:
    			sku = '00'
    			request["SNR_SKU"] = sku
    		else:
    			sku = response.xpath('//*[@class="product-details"]/b/text()').extract_first()
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass

    	try:
    		sub_category = response.xpath('//*[@class="breadcrumb"]/li/a/text()').extract()[-1]
    		if not sub_category:
    			sub_category = '00'
    			request["SNR_SubCategory"] = sub_category
    		else:
    			sub_category = response.xpath('//*[@class="breadcrumb"]/li/a/text()').extract()[-1]
    			request["SNR_SubCategory"] = sub_category
    	except Exception:
    		pass

    	request["SNR_Brand"] = "Not Available"
    	request["SNR_Category"] = "Deals"
    	request["SNR_ModelNo"] = "00"
    	request["SNR_UPC"] = "00"
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Available"] = "Zales"
    	request["SNR_Date"] = "00"
    	request["SNR_CustomerReviews"] = "0"
    	request["SNR_Condition"] = "00"
    	request["SNR_isShow"] = True
    	request["SNR_Description"] = "Visit site to see description"
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(ZaleSpider)

process.start()


