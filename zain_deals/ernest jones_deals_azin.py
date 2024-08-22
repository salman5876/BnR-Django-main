# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class ErnestSpider(scrapy.Spider):
    name = 'ernest'
    allowed_domains = ['ernestjones.com']
    start_urls = ['http://ernestjones.co.uk/webstore/offers.do?icid=ej-tn-summer-sp']

    def parse(self, response):
        categories = response.xpath('//*[@class="contents"]/@href').extract()
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.product_parser, dont_filter=True)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="product-tile js-product-item"]/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data, dont_filter=True)

    def product_data(self, response):
    	request = {}
    	try:
    		img = response.xpath('//*[@id="productImage"]/a/img/@src').extract_first()
    		if not img:
    			request["SNR_ImageURL"] = 'Not Available'
    		else:
    			request["SNR_ImageURL"] = 'http:'+ img
    	except Exception:
    		pass
    	try:
    		price = response.xpath('//*[@class="buying-info__price--current "]/strong/text()').extract_first()
    		if not price:
    			request["SNR_Price"] = '0.00'
    		else:
    			price = float(response.xpath('//*[@class="buying-info__price--current "]/strong/text()').extract_first())
    			price = price*1.34
    			request["SNR_Price"] = price
    	except Exception:
    		pass
    	try:
    		price_before = response.xpath('//*[@class="buying-info__price--was"]/text()').extract_first()
    		if not price_before:
    			request["SNR_PriceBefore"] = '0.00'
    		else:
    			price_before = response.xpath('//*[@class="buying-info__price--was"]/text()').extract_first()
    			price_before = price_before.replace('was £','')
    			price_before = float(price_before)
    			price_before = price_before*1.34
    			request["SNR_PriceBefore"] = price_before
    	except Exception:
    		pass
    	try:
    		title = response.xpath('//*[@class="buying-info"]/div/h1/text()').extract_first()
    		if not title:
    			request["SNR_Title"] = 'Not Available'
    		else:
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		description = response.xpath('//*[@class="description__description"]/p/text()').extract_first().strip()
    		if not description:
    			request["SNR_Description"] = 'Not Available'
    		else:
    			request["SNR_Description"] = description
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//*[@id="js-skuChange"]/text()').extract_first()
    		if not sku:
    			request["SNR_SKU"] = '00'
    		else:
    			sku = response.xpath('//*[@id="js-skuChange"]/text()').extract_first()
    			sku = sku.replace('Product code:','')
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	try:
    		brand = response.xpath('//dt[text()="Brand"]/following-sibling::dd/text()').extract_first()
    		if not brand:
    			request["SNR_Brand"] = 'Not Available'
    		else:
    			request["SNR_Brand"] = brand
    	except Exception:
    		pass
    	try:
    		moderl_num = response.xpath('//dt[text()="Model number"]/following-sibling::dd/text()').extract_first()
    		if not moderl_num:
    			request["SNR_ModelNo"] = '00'
    		else:
    			request["SNR_ModelNo"] = moderl_num
    	except Exception:
    		pass
    	request["SNR_Category"] = "Deals"
    	request["SNR_UPC"] = "00"
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Available"] = "Ernest Jones"
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

process.crawl(ErnestSpider)

process.start()