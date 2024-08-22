# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class VerizSpider(scrapy.Spider):
    name = 'veriz'
    allowed_domains = ['verizon.com']
    start_urls = ['https://www.verizonwireless.com/accessories/allproducts/']
    
    def parse(self, response):
    	products_url = response.xpath('//*[@class="fontsz_sub2 bold color_red"]/a/@href').extract()
    	for product in products_url:
    		yield Request(product, callback=self.parses, dont_filter=True)


    	next_page = response.xpath('//*[@id="pageNav"]/a[2]/@href').extract_first()
    	absolute_next_page = response.urljoin(next_page)
    	yield Request(absolute_next_page,
                      callback=self.parse,
                      dont_filter=True)
    	
    def parses(self,response):
        request ={}
    	
        try:
            title = response.xpath('//*[@class="product-title"]/span[2]/text()').extract_first()
            if not title:
                title = '00'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//*[@class="product-title"]/span[2]/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass
    	
        try:
        	price = response.xpath('//*[@id="pdp-cart-actual-price"]/text()').extract_first().strip()
        	if not price:
        		request["SNR_Price"] = '0.00'
        	else:
        		m = list(price)
        		m[0] = ''
        		price = "".join(m)
        		request["SNR_Price"] = price
        except Exception:
            pass

        try:
        	brand = response.xpath('//*[@class="brand"]/text()').extract_first().strip()
        	if brand =='':
        		brand = 'Not Available'
        		request  ["SNR_Brand"] = brand
        	else:
        		brand = response.xpath('//*[@class="brand"]/text()').extract_first().strip()
        		request["SNR_Brand"] = brand
        except Exception:
        	pass

        try:
        	reviews = response.xpath('//*[@class="review-link"]/span[3]/text()').extract_first()
        	if not reviews:
        		request["SNR_CustomerReviews"] = '00'
        	else:
        		reviews = response.xpath('//*[@class="review-link"]/span[3]/text()').extract_first()
        		request["SNR_CustomerReviews"] = reviews
        except Exception:
        	pass

        try:
            images = response.xpath('//*[@id="pdp-img1"]/@src').extract_first()
            if not images:
                request["SNR_ImageURL"] = '00'
            else:
                request["SNR_ImageURL"] = images
        except Exception:
            pass

        try:
            sku_code = response.xpath('//*[@id="sku-id"]/text()').extract_first().strip()[5:]
            if not sku_code:
                request["SNR_SKU"] = '00'
            else:
                request["SNR_SKU"] = sku_code
        except Exception:
            pass

        try:
        	price_before = response.xpath('//*[@class="strike"]/text()').extract_first()[2:]
        	if not price_before:
        		price_before = '0.00'
        		request["SNR_PriceBefore"] = price_before
        	else:
        		price_before = response.xpath('//*[@class="strike"]/text()').extract_first()[2:]
        		request["SNR_PriceBefore"] = price_before
        except Exception:
        	pass
        
        product_url = response.url
        request["SNR_ProductURL"] = product_url
        try:
            sub_category = response.xpath('//*[@id="pdp-hero-brdcrb"]/span/a/span/text()').extract()[-1]
            if not sub_category:
                request["SNR_SubCategory"] = 'Not Available'
            else:
                request["SNR_SubCategory"] = sub_category
        except Exception:
            pass
        request["SNR_UPC"] = '0'
        request["SNR_Available"] = 'Verizon'
        request["SNR_Condition"] = '0'
        request["SNR_isShow"] = True
        request["SNR_Date"] = '00'
        try:
            category = response.xpath('//*[@id="pdp-hero-brdcrb"]/span/a/span/text()').extract()[1]
            if not category:
                request["SNR_Category"] = 'Accessories'
            else:
                request["SNR_Category"] = category
        except Exception:
            pass
        request["SNR_ModelNo"] = '00'
        request ["SNR_Description"] = 'Visit Site to see description'

        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(VerizSpider)

process.start()






