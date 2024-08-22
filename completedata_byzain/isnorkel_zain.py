# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class IsnorkelSpider(scrapy.Spider):
    name = 'isnorkel'
    allowed_domains = ['isnorkel.com']
    start_urls = ['https://www.isnorkel.com/all']

    def parse(self, response):
        categories = response.xpath('//*[@class="SideCategoryListFlyout"]/ul/li/a/@href').extract()[1:]
        for category in categories:
            yield Request(category, callback=self.sub_link, dont_filter=True)

    def sub_link(self, response):
        try:
            sub_links = response.xpath('//*[@class="SubCategoryList"]/ul/li/a/@href').extract()
            for link in sub_links:
                yield Request(link, callback=self.product_parser, dont_filter=True)
        except:
            yield Request(callback=self.product_parser, dont_filter=True)

    def product_parser(self, response):
    	try:
    		products = response.xpath('//*[@class="ProductDetails"]/strong/a/@href').extract()
    		for product in products:
    			yield Request(product, callback=self.product_data, dont_filter=True)
    		next_page = response.xpath('//*[@class="nav-next fa fa-angle-right"]/@href').extract_first()
    		yield Request(next_page, dont_filter=True)
    	except Exception:
    		pass

    def product_data(self, response):
        request = {}
        try:
            img = response.xpath('//*[@rel="prodImage"]/img/@src').extract_first()
            if not img:
                request["SNR_ImageURL"] = 'Not Available'
            else:
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        try:
            price = response.xpath('//*[@class="ProductPrice VariationProductPrice"]/text()').extract_first()
            if not price:
                request["SNR_Price"] = '0.00'
            else:
                price = response.xpath('//*[@class="ProductPrice VariationProductPrice"]/text()').extract_first()
                price = price.replace('$','')
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@class="VariationProductSKU"]/text()').extract_first().strip()
            if not sku:
                request["SNR_SKU"] = '00'
            else:
                request["SNR_SKU"] = sku
        except Exception:
            pass
        try:
            title = response.xpath('//*[@class="ProductDetailsGrid"]/h1/text()').extract_first()
            if not title:
                request["SNR_Title"] = 'Not Available'
            else:
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            brand = response.xpath('//*[@class="BrandName"]/a/text()').extract_first()
            if not brand:
                request["SNR_Brand"] = 'Not Available'
            else:
                request["SNR_Brand"] = brand
        except Exception:
            pass
        try:
            upc = response.xpath('//*[@class="ProductDetailsGrid prodAccordionContent"]/div/div[2]/text()').extract_first().strip()
            if not upc:
                request["SNR_UPC"] = '00'
            else:
                request["SNR_UPC"] = upc
        except Exception:
            pass
        try:
            sub_category = response.xpath('//*[@class="Block Moveable Panel Breadcrumb"]/ul/li/a/text()').extract()[-1]
            if not sub_category:
                request["SNR_SubCategory"] = '00'
            else:
                request["SNR_SubCategory"] = sub_category
        except Exception:
            pass
        request["SNR_Description"] = "Visit site to see description"
        try:
            categry = response.xpath('//*[@class="Block Moveable Panel Breadcrumb"]/ul/li/a/text()').extract()[1]
            if not categry:
                request["SNR_Category"] = 'Sports'
            else:
                request["SNR_Category"] = categry
        except Exception:
            pass
        request["SNR_ModelNo"] = "00"
        request["SNR_ProductURL"] = response.url
        request["SNR_Available"] = "iSnorkel"
        request["SNR_Date"] = '00'
        request["SNR_CustomerReviews"] = "0"
        request["SNR_PriceBefore"] = '0.00'
        request["SNR_Condition"] = "00"
        request["SNR_isShow"] = True
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(IsnorkelSpider)

process.start()