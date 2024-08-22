# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
import json
import requests


class SamsSpider(scrapy.Spider):
    name = 'sams'
    allowed_domains = ['samsclub.com']
    start_urls = ['https://samsclub.com/sams/all-products/100001.cp?xid=hdr_shop1_all-departments']

    def parse(self, response):
        categories = response.xpath('//*[@class="subcategories"]/li/span/a/@href').extract()
        for categry in categories:
        	absolute_categry = response.urljoin(categry)
        	yield Request(absolute_categry, callback=self.parsers)

    def parsers(self,response):
        try:
            sub_pages_url = response.xpath('//*[@class="catLeftNav"]/li/a/@href').extract()
            for sub_page in sub_pages_url:
                absolute_sub_pages_url = response.urljoin(sub_page)
                yield Request(absolute_sub_pages_url, callback=self.parses)
        except:
            yield Request(callback=self.product_parser)

    def parses(self,response):
    	sub_links = response.xpath('//*[@class="catLeftNav"]/li/a/@href').extract()
    	for link in sub_links:
    		absolute_link = response.urljoin(link)
    		yield Request(absolute_link, callback=self.product_parser)

    def product_parser(self,response):
        try:
            products = response.xpath('//*[@class="cardProdLink"]/@href').extract()
            if not products:
                products = response.xpath('//*[@class="sc-product-card-title"]/a/@href').extract()
                for product in products:
                    absolute_product = response.urljoin(product)
                    yield Request(absolute_product, callback=self.product_data)
            else:
                products = response.xpath('//*[@class="cardProdLink"]/@href').extract()
                for product in products:
                    absolute_product = response.urljoin(product)
                    yield Request(absolute_product, callback=self.product_data)
        except:
            pass

    def product_data(self,response):
        request = {}
        try:
            title = response.xpath('//h1/span/text()').extract_first()
            if not title:
                title = response.xpath('//h1/div/text()').extract_first()
                request["SNR_Title"] = title
            else:
                title = response.xpath('//h1/span/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            img_url = response.xpath('//*[@class="imgHolder2 span5 zoom"]/img/@src').extract_first()
            if not img_url:
                img_url = response.xpath('//*[@class="sc-image-viewer-img"]/@src').extract_first()
                request["SNR_ImageURL"] = '0'
            else:
                img_url = response.xpath('//*[@class="imgHolder2 span5 zoom"]/img/@src').extract_first()
                img_url = img_url.replace('//','https://')
                request["SNR_ImageURL"] = img_url
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@class="itemId"]/span[1]/text()').extract_first()
            if not sku:
                sku = response.xpath('//*[@class="sc-product-header-subtitle"]/div[1]/text()').extract_first()
                sku = sku.replace('Item #','')
                request["SNR_SKU"] = sku
            else:
                sku = response.xpath('//*[@class="itemId"]/span[1]/text()').extract_first()
                request["SNR_SKU"] = sku
        except Exception:
            pass
        try:
            model_num =  response.xpath('//*[@class="modelNum"]/text()').extract_first()
            if not model_num:
                model_num = response.xpath('//*[@class="sc-product-header-subtitle"]/span/text()').extract()[-2]
                model_num = model_num.replace('Model #','')
                request["SNR_ModelNo"] = model_num
            else:
                model_num =  response.xpath('//*[@class="modelNum"]/text()').extract_first()
                request["SNR_ModelNo"] = model_num
        except Exception:
            pass
        try:
            brand_name = response.xpath('//*[@class="prodTitlePlus ft11"]/span/span/text()').extract_first()
            if not brand_name:
                request["SNR_Brand"] = '0'
            else:
                request["SNR_Brand"] = brand_name
        except Exception:
            pass
        try:
            price = response.xpath('//*[@class="lgFont "]/li/span[2]/text()').extract_first()
            if not price:
                price =  response.xpath('//*[@class="price"]/text()').extract_first()
                request["SNR_Price"] = price
            else:
                price = response.xpath('//*[@class="lgFont "]/li/span[2]/text()').extract_first()
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            sub_category = response.xpath('//*[@class="breadcrumb-child"]/a/span/text()')[-1].extract()
            if not sub_category:
                sub_category = response.xpath('//*[@class="breadcrumb-list "]/li/a/text()').extract()[-1]
                request["SNR_SubCategory"] = sub_category
            else:
                sub_category = response.xpath('//*[@class="breadcrumb-child"]/a/span/text()')[-1].extract()
                request["SNR_SubCategory"] = sub_category
        except Exception:
            pass
        request["SNR_ProductURL"] = response.url
        request["SNR_UPC"] = '0'
        request["SNR_Available"] = "Sam's Club"
        request["SNR_Description"] = 'Visit site to see description'
        try:
            price_before = response.xpath('//*[@class="dkGray"]/span[2]/text()').extract_first()
            if not price_before:
                price_before =  '0.00'
                request["SNR_PriceBefore"] = price_before
            else:
                price_before = response.xpath('//*[@class="dkGray"]/span[2]/text()').extract_first()
                request["SNR_PriceBefore"] = price_before
        except Exception:
            pass
        try:
            category = response.xpath('//*[@class="breadcrumb-child"]/a/span/text()').extract()[1]
            if not category:
                category = response.xpath('//*[@class="breadcrumb-list "]/li/a/text()').extract()[1]
                request["SNR_Category"] = category
            else:
                category = response.xpath('//*[@class="breadcrumb-child"]/a/span/text()').extract()[1]
                request["SNR_Category"] = category
        except Exception:
            pass
        request["SNR_Condition"] = '0'
        request["SNR_CustomerReviews"] = '0'
        request["SNR_isShow"] = True
        request["SNR_Date"] = '0'
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    })

process.crawl(SamsSpider)

process.start()
