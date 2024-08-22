import scrapy
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
import json
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from bs4 import BeautifulSoup


class LowesZainSpider(scrapy.Spider):
    name = 'lowes_zain'
    allowed_domains = ['lowes.com']
    start_urls = ['https://lowes.com/c/Departments']
    custom_settings = {'CONCURRENT_REQUESTS': 700,'CONCURRENT_REQUESTS_PER_DOMAIN': 350,'DOWNLOAD_DELAY': 0.05}

    def parse(self, response):
        categories = response.xpath('//li/h6/a/@href').extract()
        for category in categories:
        	absolute_category = response.urljoin(category)
        	yield Request(absolute_category, callback=self.parses)

    def parses(self, response):
    	try:
    		sub_links = response.xpath('//div[@class="category-link"]/h6/a/@href').extract()
    		for sub in sub_links:
    			absolute_sub = response.urljoin(sub)
    			yield Request(absolute_sub, callback=self.product_parser)
    	except:
    		yield Request(callback=self.product_parser)

    def product_parser(self, response):
    	products = response.xpath('//a[@class="display-block met-product"]/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
    	sleep(3)
    	self.driver = webdriver.Chrome(r'C:\Users\Umar\Downloads\chromedriver')
    	self.driver.get(response.url)
    	sleep(3)
    	request = {}
    	try:
    		sleep(3)
    		self.driver.find_element_by_xpath('//*[@id="zipcode-input"]').send_keys('35801')
    		sleep(3)
    		self.driver.find_element_by_xpath('//*[@id="store-locator-form"]/div/div/span[2]/button').click()
    		sleep(5)
    	except:
    		pass
    	try:
    		self.driver.find_element_by_xpath('//*[@id="store-locator-modal"]/div[2]/div/div[2]/div[1]/div/ul/li[1]/div/div[2]/button').click()
    		sleep(5)
    	except:
    		pass
    	sleep(2)
    	price = self.driver.find_element_by_xpath('//*[@id="main"]/div[5]/section[1]/div[3]/div[2]/div[1]/div/span[1]')
    	price = price.text
    	price = price.replace('$','')
    	request["SNR_Price"] = price
    	try:
    		title = response.xpath('//h1[@class="h3"]/text()').extract_first().strip()
    		if not title:
    			request["SNR_Title"] = "Not Available"
    		else:
    			request["SNR_Title"] = title
    	except Exception:
    		pass
    	try:
    		img = response.xpath('//img[@class="product-image met-product-image pd-epc"]/@src').extract_first()
    		if not img:
    			request["SNR_ImageURL"] = 'Not Available'
    		else:
    			request["SNR_ImageURL"] = img
    	except Exception:
    		pass
    	try:
    		sku = response.xpath('//span[@class="met-product-item-number"]/text()').extract_first()
    		if not sku:
    			request["SNR_SKU"] = "Not Available"
    		else:
    			request["SNR_SKU"] = sku
    	except Exception:
    		pass
    	try:
    		model_num = response.xpath('//span[@class="met-product-model"]/text()').extract_first()
    		if not model_num:
    			request["SNR_ModelNo"] = '00'
    		else:
    			request["SNR_ModelNo"] = model_num
    	except Exception:
    		pass
    	try:
    		category = response.xpath('//*[@itemprop="item"]/span/text()').extract()[0]
    		request["SNR_Category"] = category
    	except Exception:
    		pass
    	try:
    		sub_category = response.xpath('//*[@itemprop="item"]/span/text()').extract()[-1]
    		request["SNR_SubCategory"] = sub_category
    	except Exception:
    		pass
    	try:
    		reviews = response.xpath('//*[@class="reviews-count"]/text()').extract_first()
    		if not reviews:
    			request["SNR_CustomerReviews"] = '0'
    		else:
    			reviews = response.xpath('//*[@class="reviews-count"]/text()').extract_first()
    			reviews = reviews.split(' ')
    			request["SNR_CustomerReviews"] = reviews[0]
    	except Exception:
    		pass
    	request["SNR_Brand"] = "Not Available"
    	request["SNR_Description"] = "Visit site to see description"
    	request["SNR_UPC"] = "0"
    	request["SNR_ProductURL"] = response.url
    	request["SNR_Available"] = "Lowe's"
    	request["SNR_Date"] = '0'
    	request["SNR_PriceBefore"] = '0'
    	request["SNR_Condition"] = '0'
    	request["SNR_isShow"] = True
    	url = "https://backend.shopnroar.com/products/InsertProduct/"
    	header = {'Content-Type': 'application/json'}
    	yield requests.put(url, headers=header, data=json.dumps(request))
    	sleep(5)
    	self.driver.close()