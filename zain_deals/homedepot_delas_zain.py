# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from selenium import webdriver
from scrapy.http import Request
from scrapy.selector import Selector
import requests
import json


class HomedepotZainSpider(scrapy.Spider):
    name = 'homedepot_zain'
    allowed_domains = ['homedepot.com']

    def start_requests(self):
        proxy = "46.227.48.48:8080"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        self.driver = webdriver.Chrome(r'C:\Users\Umar\Downloads\Chromedriver',chrome_options=chrome_options)
        self.driver.get('https://homedepot.com/c/site_map')
        sel = Selector(text=self.driver.page_source)
        sleep(3)
        categories = sel.xpath('//li[@class="list__item list__item--padding-none "]/a/@href').extract()[:11]
        request = {}
        for category in categories:
        	sleep(5)
        	self.driver.get(category)
        	sel = Selector(text=self.driver.page_source)
        	products = sel.xpath('//div[@class="pod-plp__description js-podclick-analytics"]/a/@href').extract()
        	for product in products:
        		absolute_product = "https://www.homedepot.com/"+product
        		sleep(5)
        		self.driver.get(absolute_product)
        		sel = Selector(text=self.driver.page_source)
        		sleep(5)
        		try:
        			img = sel.xpath('//img[@id="mainImage"]/@src').extract_first()
        			if not img:
        				request["SNR_ImageURL"] = "Not Available"
        			else:
        				request["SNR_ImageURL"] = img
        		except:
        			pass
        		try:
        			brand = sel.xpath('//h2//span[@class="bttn__content"]/text()').extract_first()
        			if not brand:
        				request["SNR_Brand"] = "Not Available"
        			else:
        				request["SNR_Brand"] = brand
        		except:
        			pass
        		try:
        			title = sel.xpath('//h1[@class="product-title__title"]/text()').extract_first()
        			if not title:
        				request["SNR_Title"] = "Not Available"
        			else:
        				request["SNR_Title"] = title
        		except:
        			pass
        		try:
        			reviews = sel.xpath('//span[@class="BVRRCount BVRRNonZeroCount"]/span[@class="BVRRNumber"]/text()').extract_first()
        			if not reviews:
        				request["SNR_CustomerReviews"] = "Not Available"
        			else:
        				request["SNR_CustomerReviews"] = reviews
        		except:
        			pass
        		try:
        			price_before = sel.xpath('//span[@id="ajaxPriceStrikeThru"]/text()').extract_first().strip()
        			if not price_before:
        				request["SNR_PriceBefore"] = "Not Available"
        			else:
        				price_before = sel.xpath('//span[@id="ajaxPriceStrikeThru"]/text()').extract_first().strip()
        				price_before = price_before.replace('Was ','')
        				price_before = price_before.replace('$','')
        				request["SNR_PriceBefore"] = price_before
        		except:
        			pass
        		try:
        			price = sel.xpath('//span[@class="price__dollars"]/text()').extract_first()
        			if not price:
        				request["SNR_Price"] = "Not Available"
        			else:
        				request["SNR_Price"] = price
        		except:
        			pass
        		try:
        			model_no = sel.xpath('//h2[@class="product_details modelNo"]/text()').extract_first().strip()
        			if not model_no:
        				request["SNR_ModelNo"] = "00"
        			else:
        				model_no = sel.xpath('//h2[@class="product_details modelNo"]/text()').extract_first().strip()
        				model_no = model_no.replace('Model ','')
        				model_no = model_no.replace('#','')
        				request["SNR_ModelNo"] = model_no
        		except:
        			pass
        		try:
        			upc = sel.xpath('//span[@id="product_internet_number"]/text()').extract_first()
        			if not upc:
        				request["SNR_UPC"] = "00"
        			else:
        				request["SNR_UPC"] = upc
        		except:
        			pass
        		try:
        			sku = sel.xpath('//h2[@class="product_details"]/span/text()').extract()[1]
        			if not sku:
        				request["SNR_SKU"] = "00"
        			else:
        				request["SNR_SKU"] = sku
        		except:
        			pass
        		try:
        			sub_category = sel.xpath('//a[@class="breadcrumb__link"]/text()').extract()[-1]
        			if not sub_category:
        				request["SNR_SubCategory"] = "Not Available"
        			else:
        				request["SNR_SubCategory"] = sub_category
        		except:
        			pass
        		request["SNR_isShow"] = True
        		request["SNR_Condition"] = "00"
        		request["SNR_Date"] = "00"
        		request["SNR_Available"] = "Home Depot"
        		request["SNR_ProductURL"] = absolute_product
        		request["SNR_Category"] = "Deals"
        		request["SNR_Description"] = "Visit site to see description"
        		print(request)
        		url = "https://backend.shopnroar.com/products/InsertProduct/"
        		header = {'Content-Type': 'application/json'}
        		requests.put(url, headers=header, data=json.dumps(request))
        	'''next_page = sel.xpath('//li[@class="hd-pagination__item hd-pagination__button"]/a/@href').extract_first()
        	absolute_next_page = "https://www.homedepot.com/"+next_page
        	self.driver.get(absolute_next_page)'''
        self.driver.close()