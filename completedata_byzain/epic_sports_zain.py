# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
import json
import requests

class EpicSpider(scrapy.Spider):
    name = 'epic'
    allowed_domains = ['epicsports.com']
    start_urls = ['http://baseball.epicsports.com/']

    def parse(self, response):
        menus = response.xpath('//*[@id="menu"]/li/a/@href').extract()[2:]
        for menu in menus:
            yield Request(menu, callback=self.sub_menu, dont_filter=True)

    def sub_menu(self, response):
        sub_menus = response.xpath('//*[@class="main"]/a/@href').extract()
        for sub in sub_menus:
            yield Request(sub, callback=self.products, dont_filter=True)

    def products(self, response):
        products = response.xpath('//*[@class="prod"]/a/@href').extract()
        for product in products:
            absolute_product = response.urljoin(product)
            yield Request(absolute_product, callback=self.product_data, dont_filter=True)
        next_page = response.xpath('//a[text()="Next >>"]/@href').extract_first()
        absolute_next = response.urljoin(next_page)
        yield Request(absolute_next, dont_filter=True)

    def product_data(self, response):
        request = {}
        try:
            price = response.xpath('//*[@id="spanSkuPrice"]/text()').extract_first()
            if not price:
                price = '0.00'
                request["SNR_Price"] = price
            else:
                price = response.xpath('//*[@id="spanSkuPrice"]/text()').extract_first()
                price = price.replace('$','')
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            img =  response.xpath('//center/img/@src').extract_first()
            if not img:
                img = 'Not Available'
                request["SNR_ImageURL"] = img
            else:
                img =  response.xpath('//center/img/@src').extract_first()
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        try:
            title = response.xpath('//*[@class="prod_name"]/text()').extract_first().strip()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//*[@class="prod_name"]/text()').extract_first().strip()
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@class="p-info"]/text()').extract()[4].strip()
            if not sku:
                sku = '00'
                request["SNR_SKU"] = sku
            else:
                sku = response.xpath('//*[@class="p-info"]/text()').extract()[4].strip()
                request["SNR_SKU"] = sku
        except Exception:
            pass
        try:
            price_before = response.xpath('//*[@class="p-info"]/text()').extract()[9].strip()
            if not price_before:
                price_before = response.xpath('//*[@class="p-info"]/text()').extract()[6].strip()
                price_before = price_before.replace('$','')
                request["SNR_PriceBefore"] = price_before
            else:
                price_before = response.xpath('//*[@class="p-info"]/text()').extract()[9].strip()
                price_before = price_before.replace('$','')
                request["SNR_PriceBefore"] = price_before
        except Exception:
            pass
        try:
            reviews = response.xpath('//*[@itemprop="ratingCount"]/text()').extract_first()
            if not reviews:
                reviews = '00'
                request["SNR_CustomerReviews"] = reviews
            else:
                reviews = response.xpath('//*[@itemprop="ratingCount"]/text()').extract_first()
                reviews = reviews.replace('Reviews','')
                request["SNR_CustomerReviews"] = reviews
        except Exception:
            pass
        try:
            brand = response.xpath('//*[@itemprop="brand"]/text()').extract_first()
            if not brand:
                brand = 'Not Available'
                request["SNR_Brand"] = brand
            else:
                brand = response.xpath('//*[@itemprop="brand"]/text()').extract_first()
                request["SNR_Brand"] = brand
        except Exception:
            pass
        request["SNR_ProductURL"] = response.url
        request["SNR_Description"] = "Visit site to see description"
        request["SNR_ModelNo"] = "00"
        request["SNR_UPC"] = "00"
        request["SNR_Available"] = "Epic Sports"
        request["SNR_Date"] = '00'
        request["SNR_Category"] = 'Sports'
        request["SNR_Condition"] = "00"
        request["SNR_SubCategory"] = '00'
        request["SNR_isShow"] = True
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    })

process.crawl(EpicSpider)

process.start()