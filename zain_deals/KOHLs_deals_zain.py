# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class KohlSpider(scrapy.Spider):
    name = 'kohl'
    allowed_domains = ['kohls.com']
    start_urls = ['https://kohls.com/sale-event/clearance.jsp?cc=deals-LN0.0-S-Clearance']

    def parse(self, response):
        categories = response.xpath('//*[@class="grid-box m4x4 d4x4 "]/a/@href').extract()
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.parses)

    def parses(self, response):
    	sub_links = response.xpath('//*[@class="vn-content"]/a/@href').extract()
    	for link in sub_links:
    		absolute_link = response.urljoin(link)
    		yield Request(absolute_link, callback=self.product_parser)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="prod_img_block"]/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
    	request = {}
    	try:
    		title = response.xpath('//*[@class="pdp-product-title"]/text()').extract_first().strip()
    		if not title:
    			request["SNR_Title"] = 'Not Available'
    		else:
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		price = response.xpath('//*[@class="main-price   red-font"]/text()').extract_first().strip()
    		if not price:
    			request["SNR_Price"] = '0.00'
    		else:
    			price = response.xpath('//*[@class="main-price   red-font"]/text()').extract_first().strip()
    			price = price.replace('$','')
    			price = price.replace('\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t\t','')
    			request["SNR_Price"] = price
    	except Exception:
    		pass
    	try:
    		img = response.xpath('//*[@class="PDP_heroimage"]/@src').extract_first()
    		if not img:
    			request["SNR_ImageURL"] = 'Not Available'
    		else:
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		price_before = response.xpath('//*[@class="regorg-small"]/text()').extract_first().strip()
    		if not price_before:
    			request["SNR_PriceBefore"] = '0.00'
    		else:
    			price_before = response.xpath('//*[@class="regorg-small"]/text()').extract_first().strip()
    			price_before = price_before.replace('Original','')
    			price_before = price_before.replace('Regular','')
    			price_before = price_before.strip()
    			price_before = price_before.replace('$','')
    			price_before = price_before.replace('\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t\t\xa0','')
    			price_before = price_before.replace('\xa0','')
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass
    	try:
    		sub_category = response.xpath('//*[@class="main-pricelabel   red-font"]/text()').extract_first().strip()
    		if not sub_category:
    			request["SNR_SubCategory"] = '00'
    		else:
    			request["SNR_SubCategory"] = sub_category
    	except Exception:
    		pass
    	try:
    		brand = response.xpath('//*[@class="pdp_breadcrumb_title"]/a/text()').extract()[-1]
    		if not brand:
    			request["SNR_Brand"] = 'Not Available'
    		else:
    			request["SNR_Brand"] = brand
    	except Exception:
    		pass
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Description"] = "Visit site to see description"
    	request["SNR_Category"] = "Deals"
    	request["SNR_ModelNo"] = "00"
    	request[ "SNR_UPC"] = "00"
    	request["SNR_SKU"] = '00'
    	request["SNR_Available"] = "KOHL'S"
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

process.crawl(KohlSpider)

process.start()