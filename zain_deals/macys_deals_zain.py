# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess

class MacySpider(scrapy.Spider):
    name = 'macy'
    allowed_domains = ['macys.com']
    start_urls = ['http://macys.com/']
    custom_settings = {'CONCURRENT_REQUESTS': 700,'CONCURRENT_REQUESTS_PER_DOMAIN': 350,'DOWNLOAD_DELAY': 0.05}

    def parse(self, response):
        all_links = response.xpath('//*[@id="mainNavigationFobs"]/li/a/@href').extract()
        for link in all_links:
            absolute_link = response.urljoin(link)
            yield Request(absolute_link, callback=self.sales)

    def sales(self, response):
        try:
            sale = response.xpath('//*[@class="header  highlighted"]/span/a/@href').extract_first()
            yield Request(sale, callback=self.products)
        except Exception:
            pass

    def products(self, response):
        product_url = response.xpath('//*[@class="productDetail"]/div/a/@href').extract()
        for product in product_url:
            absolute_product = response.urljoin(product)
            yield Request(absolute_product, callback=self.product_data)

    def product_data(self, response):
        request = {}
        try:
            img = response.xpath('//*[@class="c-reset scroller swiper animated"]/li/img/@src').extract_first()
            if not img:
                img = 'Not Available'
                request["SNR_ImageURL"] = img
            else:
                img = response.xpath('//*[@class="c-reset scroller swiper animated"]/li/img/@src').extract_first()
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        try:
            reviews = response.xpath('//*[@class="columns small-16"]/span[2]/a/text()').extract_first().strip()
            if not reviews:
                reviews = '00'
                request["SNR_CustomerReviews"] = reviews
            else:
                reviews = response.xpath('//*[@class="columns small-16"]/span[2]/a/text()').extract_first().strip()
                reviews = reviews.replace('reviews','')
                request["SNR_CustomerReviews"] = reviews
        except Exception:
            pass
        try:
            brand = response.xpath('//*[@data-auto="product-title"]/h4/a/text()').extract_first().strip()
            if not brand:
                brand = 'Not Available'
                request[ "SNR_Brand"] = brand
            else:
                brand = response.xpath('//*[@data-auto="product-title"]/h4/a/text()').extract_first().strip()
                request[ "SNR_Brand"] = brand
        except Exception:
            pass
        try:
            price_before = response.xpath('//*[@class="price"]/text()').extract_first()
            if not price_before:
                price_before = '0.00'
                request["SNR_PriceBefore"] = price_before
            else:
                price_before = response.xpath('//*[@class="price"]/text()').extract_first()
                price_before = price_before.replace('USD ','')
                request["SNR_PriceBefore"] = price_before
        except Exception:
            pass
        try:
            price = response.xpath('//*[@data-auto="sale-price"]/text()').extract_first().strip()
            if not price:
                price = response.xpath('//*[@class="price"]/text()').extract_first()
                price = price.replace('USD ','')
                request["SNR_Price"] = price
            else:
                price = response.xpath('//*[@data-auto="sale-price"]/text()').extract_first().strip()
                price = price.replace('Now ','')
                price = price.replace('USD ','')
                price = price.replace('Sale ','')
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            description = response.xpath('//*[@class="reset-font c-margin-1v"]/text()').extract_first().strip()
            if not description:
                description = 'Visit site to see description'
                request["SNR_Description"] = description
            else:
                description = response.xpath('//*[@class="reset-font c-margin-1v"]/text()').extract_first().strip()
                request["SNR_Description"] = description
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@class="reset-font"]/li/text()').extract()[-1]
            if not sku:
                sku = '00'
                request["SNR_SKU"] = sku
            else:
                sku = response.xpath('//*[@class="reset-font"]/li/text()').extract()[-1]
                sku = sku.replace('Web ID:','')
                request["SNR_SKU"] = sku
        except Exception:
            pass
        try:
            title = response.xpath('//*[@data-auto="product-title"]/h1/text()').extract_first().strip()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//*[@data-auto="product-title"]/h1/text()').extract_first().strip()
                request["SNR_Title"] = title
        except Exception:
            pass
        products_url = response.url
        request["SNR_ProductURL"] = products_url
        request["SNR_Category"] = "Deals"
        request["SNR_ModelNo"] = "00"
        request["SNR_UPC"] = "00"
        request["SNR_Available"] = "Macy's"
        request["SNR_Date"] = 'Not Available'
        request["SNR_Condition"] = "00"
        request["SNR_isShow"] = True
        request["SNR_SubCategory"] = "00"
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))
process = CrawlerProcess({
	'User-Agent':	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})

process.crawl(MacySpider)

process.start()

