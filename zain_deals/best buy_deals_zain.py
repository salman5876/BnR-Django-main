# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess




class BestSpider(scrapy.Spider):
    name = 'best'
    allowed_domains = ['bestbuy.com']
    start_urls = ['https://www.bestbuy.com/site/clp/sale-page/pcmcat185700050011.c?id=pcmcat185700050011']

    def parse(self, response):
    	try:
    		all_links = response.xpath('//*[@class="offer-link"]/a/@href').extract()
    		for link in all_links:
    			absolute_link = response.urljoin(link)
    			yield Request(absolute_link, callback=self.products)
    	except Exception:
    		pass

    def products(self, response):
    	sub_urls = response.xpath('//*[@class="sku-title"]/h4/a/@href').extract()
    	for sub in sub_urls:
    		absolute_sub_url = response.urljoin(sub)
    		yield Request(absolute_sub_url, callback=self.product_data)

    def product_data(self, response):
        request = {}
        try:
            img = response.xpath('//*[@class="primary-image "]/@src').extract_first()
            if not img:
                img = 'Not Available'
                request["SNR_ImageURL"] = img
            else:
                img = response.xpath('//*[@class="primary-image "]/@src').extract_first()
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        try:
            price =  response.xpath('//*[@class="priceView-hero-price priceView-purchase-price"]/span/text()').extract()[1]
            if not price:
                price = '0.00'
                request["SNR_Price"] = price
            else:
                price =  response.xpath('//*[@class="priceView-hero-price priceView-purchase-price"]/span/text()').extract()[1]
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            price_before = response.xpath('//*[@class="pricing-price__regular-price"]/text()').extract_first()[5:]
            if not price_before:
                price_before = '0.00'
                request["SNR_PriceBefore"] = price_before
            else:
                price_before = response.xpath('//*[@class="pricing-price__regular-price"]/text()').extract_first()[5:]
                request["SNR_PriceBefore"] = price_before
        except Exception:
            pass
        try:
            title = response.xpath('//*[@class="sku-title"]/h1/text()').extract_first()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//*[@class="sku-title"]/h1/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@id="sku-value"]/text()').extract_first()
            if not sku:
                sku = '00'
                request["SNR_SKU"] = sku
            else:
                sku = response.xpath('//*[@id="sku-value"]/text()').extract_first()
                request["SNR_SKU"] = sku
        except Exception:
            pass
        try:
            model = response.xpath('//*[@id="model-value"]/text()').extract_first()
            if not model:
                model = '00'
                request["SNR_ModelNo"] = model
            else:
                model = response.xpath('//*[@id="model-value"]/text()').extract_first()
                request["SNR_ModelNo"] = model
        except Exception:
            pass
        try:
            reviews = response.xpath('//*[@class="c-total-reviews"]/text()').extract()[1]
            if not reviews:
                reviews = '0'
                request["SNR_CustomerReviews"] = reviews
            else:
                reviews = response.xpath('//*[@class="c-total-reviews"]/text()').extract()[1]
                request["SNR_CustomerReviews"] = reviews
        except Exception:
            pass
        try:
            sub_category = response.xpath('//*[@id="breadcrumb-list"]/li/a/text()').extract()[-1]
            if not sub_category:
                sub_category = 'Not Available'
                request["SNR_SubCategory"] = sub_category
            else:
                sub_category = response.xpath('//*[@id="breadcrumb-list"]/li/a/text()').extract()[-1]
                request["SNR_SubCategory"] = sub_category
        except Exception:
            pass
        request["SNR_Brand"] = 'Not Available'
        request["SNR_Category"] = 'Deals'
        request["SNR_isShow"] = True
        request["SNR_Condition"] = "00"
        request["SNR_Description"] = "Visit site to see description"
        request["SNR_UPC"] = "00"
        product_url = response.url
        request["SNR_ProductURL"] = product_url
        request["SNR_Available"] = "BestBuy"
        request["SNR_Date"] = '00'

        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    })

process.crawl(BestSpider)

process.start()

