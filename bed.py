# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class BedSpider(scrapy.Spider):
    name = 'bed'
    allowed_domains = ['bedbathandbeyond.com']
    start_urls = ['https://bedbathandbeyond.com/store/category/clearance-savings/10009/']

    def parse(self, response):
        products = response.xpath('//*[@class="prodName"]/a/@href').extract()
        for product in products:
            absolute_product = response.urljoin(product)
            yield Request(absolute_product, callback=self.product_data)
        next_page = response.xpath('//*[@class="lnkNextPage arrow"]/a/@href').extract_first()
        absolute_next_page = response.urljoin(next_page)
        yield Request(absolute_next_page)

    def product_data(self, response):
        request = {}
        try:
            price = response.xpath('//*[@itemprop="lowPrice"]/text()').extract_first()
            if not price:
                price = response.xpath('//*[@itemprop="price"]/text()').extract_first()
                request["SNR_Price"] = price
            else:
                price = response.xpath('//*[@itemprop="lowPrice"]/text()').extract_first()
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            price_before = response.xpath('//*[@itemprop="highPrice"]/text()').extract_first()
            if not price_before:
                price_before = response.xpath('//*[@class="wasPrice"]/text()').extract_first().strip()
                price_before = price_before.replace('Was\xa0$', '')
                request["SNR_PriceBefore"] = price_before
            else:
                price_before = response.xpath('//*[@itemprop="highPrice"]/text()').extract_first()
                request["SNR_PriceBefore"] = price_before
        except Exception:
            pass
        try:
            img = response.xpath('//*[@id="mainProductImg"]/@src').extract_first()
            if not img:
                img = 'Not Available'
                request["SNR_ImageURL"] = img
            else:
                img = response.xpath('//*[@id="mainProductImg"]/@src').extract_first()
                img = img.replace('//', 'https://')
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        try:
            reviews = response.xpath('//*[@class="bvTotalReviewCountClass"]/text()').extract_first()
            if not reviews:
                reviews = '0'
                request["SNR_CustomerReviews"] = reviews
            else:
                reviews = response.xpath('//*[@class="bvTotalReviewCountClass"]/text()').extract_first()
                request["SNR_CustomerReviews"] = reviews
        except Exception:
            pass
        try:
            title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            description = response.xpath('//*[@class="noprint"]/text()').extract_first().strip()
            if not description:
                description = 'Visit site to see description'
                request["SNR_Description"] = description
            else:
                description = response.xpath('//*[@class="noprint"]/text()').extract_first().strip()
                request["SNR_Description"] = description
        except Exception:
            pass
        request["SNR_ProductURL"] = response.url
        request["SNR_Brand"] = "Not Available"
        request["SNR_Category"] = "Deals"
        request["SNR_ModelNo"] = "00"
        request["SNR_UPC"] = "00"
        request["SNR_SKU"] = '00'
        request["SNR_Available"] = 'Bed Bath & Beyond'
        request["SNR_Date"] = '00'
        request["SNR_SubCategory"] = "0"
        request["SNR_Condition"] = "00"
        request["SNR_isShow"] = True
        # url = "https://backend.shopnroar.com/products/InsertProduct/"
        # header = {'Content-Type': 'application/json'}
        # yield requests.put(url, headers=header, data=json.dumps(request))
        print request


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(BedSpider)

process.start()
