# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess



class HollarSpider(scrapy.Spider):
    name = 'hollar'
    allowed_domains = ['hollar.com']
    start_urls = ['http://hollar.com/']
    custom_settings = {'CONCURRENT_REQUESTS': 700,'CONCURRENT_REQUESTS_PER_DOMAIN': 350,'DOWNLOAD_DELAY': 0.05}

    def parse(self, response):
        all_links = response.xpath('//*[@class="nav-menu-item"]/a/@href').extract()[:14]
        for link in all_links:
        	absolute_all_link = response.urljoin(link)
        	yield Request(absolute_all_link, callback=self.sub_link)

    def sub_link(self, response):
        sub_links = response.xpath('//*[@class="taxon-title-row"]/a/@href').extract()
        for link in sub_links:
            absolute_link = response.urljoin(link)
            yield Request(absolute_link, callback=self.product_parser)

    def product_parser(self, response):
    	products = response.xpath('//*[@class="is-productModal poa db is-overlayed on-desktop"]/@href').extract()
    	for product in products:
    		absolute_product = response.urljoin(product)
    		yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
        request = {}
        img = response.xpath('//*[@class="db master-variant-img"]/@src').extract_first()
        request["SNR_ImageURL"] = img
        try:
            price = response.xpath('//*[@class="l-product-price"]/span/span/strong/text()').extract_first()[1:]
            if not price:
                price = '0.00'
                request["SNR_Price"] = price
            else:
                price = response.xpath('//*[@class="l-product-price"]/span/span/strong/text()').extract_first()[1:]
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            title = response.xpath('//*[@class="l-product-title h3 mtf"]/text()').extract_first()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//*[@class="l-product-title h3 mtf"]/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            sub_catogery = response.xpath('//*[@class="l-breadcrumb"]/li/a/text()').extract()[-1]
            if not sub_catogery:
                sub_catogery = '00'
                request["SNR_SubCategory"] = sub_catogery
            else:
                sub_catogery = response.xpath('//*[@class="l-breadcrumb"]/li/a/text()').extract()[-1]
                request["SNR_SubCategory"] = sub_catogery
        except Exception:
            pass
        request ["SNR_Description"] = "Visit site to see description"
        product_url = response.url
        request["SNR_ProductURL"] = product_url
        request["SNR_PriceBefore"] = "0.00"
        request["SNR_Brand"] = 'Not Available'
        try:
            categry = response.xpath('//*[@class="l-breadcrumb"]/li/a/text()').extract_first()
            if not categry:
                request["SNR_Category"] = 'Deals'
            else:
                request["SNR_Category"] = categry
        except Exception:
            pass
        request["SNR_ModelNo"] = '00'
        request["SNR_UPC"] = '00'
        request["SNR_SKU"] = '00'
        request["SNR_Available"] = 'Hollar'
        request["SNR_Date"] = '00'
        request["SNR_CustomerReviews"] = '00'
        request["SNR_Condition"] = "00"
        request["SNR_isShow"] = True
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    })
process.crawl(HollarSpider)
process.start()
