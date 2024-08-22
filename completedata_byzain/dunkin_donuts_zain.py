# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess

class DonutsSpider(scrapy.Spider):
    name = 'donuts'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['https://shop.dunkindonuts.com/store/']

    def parse(self, response):
        menus = response.xpath('//*[@class="HorizontalCatNav"]/li/a/@href').extract()
        for menu in menus:
        	absolute_menu = response.urljoin(menu)
        	yield Request(absolute_menu, callback=self.products)

    def products(self, response):
    	products = response.xpath('//*[@class="ProductGrid"]/li/div/a/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
        request = {}
        try:
            img = response.xpath('//*[@class="ProductImg"]/@src').extract_first()
            if not img:
                img = 'Not Available'
                request["SNR_ImageURL"] = img
            else:
                img = response.xpath('//*[@class="ProductImg"]/@src').extract_first()
                img = img.replace('//','https://')
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        try:
            sub_category =  response.xpath('//*[@class="Breadcrumbs hidden-xs hidden-sm"]/li//span/text()').extract()[-1]
            if not sub_category:
                sub_category = '00'
                request["SNR_SubCategory"] = sub_category
            else:
                sub_category =  response.xpath('//*[@class="Breadcrumbs hidden-xs hidden-sm"]/li//span/text()').extract()[-1]
                request["SNR_SubCategory"] = sub_category
        except Exception:
            pass
        try:
            title = response.xpath('//*[@class="ProductNameComponent"]/div/text()').extract_first().strip()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//*[@class="ProductNameComponent"]/div/text()').extract_first().strip()
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            price = response.xpath('//*[@class="PriceValue"]/text()').extract_first()[1:]
            if not price:
                price = '0.00'
                request["SNR_Price"] = price
            else:
                price = response.xpath('//*[@class="PriceValue"]/text()').extract_first()[1:]
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@class="ProductPfidComponent"]/div/text()').extract_first().strip()
            if not sku:
                sku = '00'
                request["SNR_SKU"] = sku
            else:
                sku = response.xpath('//*[@class="ProductPfidComponent"]/div/text()').extract_first().strip()
                request["SNR_SKU"] = sku
        except Exception:
            pass
        request["SNR_Brand"] = "Dunkin Donuts"
        request["SNR_Description"] = "Visit site to see description"
        try:
            category = response.xpath('//*[@class="Breadcrumbs hidden-xs hidden-sm"]/li/a/text()').extract()[1]
            if not category:
                request["SNR_Category"] = "Food"
            else:
                request["SNR_Category"] = category
        except Exception:
            pass
        request["SNR_ModelNo"] = "00"
        request["SNR_UPC"] = "00"
        request["SNR_ProductURL"] = response.url
        request["SNR_Date"] = '00'
        request["SNR_CustomerReviews"] = '00'
        request["SNR_PriceBefore"] = '0.00'
        request["SNR_Available"] = "Dunkin Donuts"
        request["SNR_Condition"] = "00"
        request["SNR_isShow"] = True
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})

process.crawl(DonutsSpider)

process.start()
