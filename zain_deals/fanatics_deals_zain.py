# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess


class FanasSpider(scrapy.Spider):
    name = 'fanas'
    allowed_domains = ['fanastic.com']
    start_urls = ['https://www.fanatics.com/']
    custom_settings = {'CONCURRENT_REQUESTS': 700,'CONCURRENT_REQUESTS_PER_DOMAIN': 350,'DOWNLOAD_DELAY': 0.05}

    def parse(self, response):
        sale_urls = response.xpath('//*[@id="11"]/following-sibling::div/div/div/div//div/a/@href').extract()
        for sale in sale_urls:
            absolute_sale_url = response.urljoin(sale)
            yield Request(absolute_sale_url, callback=self.products, dont_filter=True)
    
    def products(self, response):
        sub_products = response.xpath('//*[@class="product-image-container"]/a/@href').extract()
        for sub_product in sub_products:
            absolute_sub_products = response.urljoin(sub_product)
            yield Request(absolute_sub_products, callback=self.product_data, dont_filter=True)

    def product_data(self, response):
        request = {}
        try:
            price = response.xpath('//*[@class="sale-price"]/text()').extract_first()[7:]
            if not price:
                price = '0.00'
                request["SNR_Price"] = price
            else:
                price = response.xpath('//*[@class="sale-price"]/text()').extract_first()[7:]
                request["SNR_Price"] = price
        except Exception:
            pass

        try:
            title= response.xpath('//*[@class="product-title-container"]/h1/text()').extract_first()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title= response.xpath('//*[@class="product-title-container"]/h1/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass

        try:
            product_id = response.xpath('//*[@class="breadcrumb-text"]/text()').extract_first()[12:]
            if not product_id:
                product_id = '0'
                request["SNR_UPC"] = product_id
            else:
                product_id = response.xpath('//*[@class="breadcrumb-text"]/text()').extract_first()[12:]
                request["SNR_UPC"] = product_id
        except Exception:
            pass

        try:
            img_url = response.xpath('//*[@class="carousel large-pdp-image transition"]/img/@src').extract_first()
            if not img_url:
                img_url = '0'
                request["SNR_ImageURL"] = img_url
            else:
                img_url = response.xpath('//*[@class="carousel large-pdp-image transition"]/img/@src').extract_first()
                img_url = img_url.replace('//','https://')
                request["SNR_ImageURL"] = img_url
        except Exception:
            pass

        try:
            description = response.xpath('//*[@class="description-box-content"]/div/text()').extract_first()
            if not description:
                description = 'Not Available'
                request ["SNR_Description"] = description
            else:
                description = response.xpath('//*[@class="description-box-content"]/div/text()').extract_first()
                request ["SNR_Description"] = description
        except Exception:
            pass

        product_url =  response.url
        request["SNR_ProductURL"] = product_url

        try:
            brand =  response.xpath('//*[@class="description-box-content"]/ul/li/text()').extract()[-1][7:]
            if not brand:
                brand = 'Not Available'
                request["SNR_Brand"] = brand
            else:
                brand =  response.xpath('//*[@class="description-box-content"]/ul/li/text()').extract()[-1][7:]
                request["SNR_Brand"] = brand
        except Exception:
            pass

        try:
            price_before = response.xpath('//*[@class="regular-price strike-through"]/text()').extract_first()[10:]
            if not price_before:
                price_before = '0.00'
                request["SNR_PriceBefore"] = price_before
            else:
                price_before = response.xpath('//*[@class="regular-price strike-through"]/text()').extract_first()[10:]
                request["SNR_PriceBefore"] = price_before
        except Exception:
            pass

        request["SNR_isShow"] = True
        request["SNR_SubCategory"] = "00"
        request["SNR_Condition"] = "00"
        request["SNR_CustomerReviews"] = '00'
        request["SNR_Date"] = '00'
        request["SNR_Available"] = "Fanatics"
        request["SNR_SKU"] = "00"
        request["SNR_ModelNo"] = "00"
        request["SNR_Category"] = "Deals"

        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    })

process.crawl(FanasSpider)

process.start()

