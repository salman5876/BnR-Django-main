# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

import json
import requests
from scrapy.crawler import CrawlerProcess
from selenium import webdriver


class BuySpider(scrapy.Spider):
    name = 'buy'
    allowed_domains = ['buydig.com']
    start_urls = ['http://buydig.com']

    def parse(self, response):
        all_pages_url = response.xpath('//*[@class="ul-arrow"]/li/a/@href').extract()
        for page in all_pages_url:
            yield Request(page, callback=self.parses)

    def parses(self, response):
        products_url = response.xpath('//*[@class="item-description"]/a/@href').extract()
        for product in products_url:
            yield Request(product, callback=self.pars)

    def pars(self, response):

        request = {'detail': 'post'}
        # part_num = response.xpath('//*[@class="sku-part"]/span/text()').extract()[1]
        try:
            img_url = response.xpath('//*[@id="ProductPhotoGallery"]/div[2]/img/@src').extract_first()
            if not img_url:
                request["SNR_ImageURL"] = '00'
            else:
                request["SNR_ImageURL"] = img_url
        except Exception:
            pass

        try:
            title = response.xpath('//h2/span/text()').extract_first()
            if not title:
                request["SNR_Title"] = '00'
            else:
                request["SNR_Title"] = title
        except Exception:
            pass

        try:
            item_num = response.xpath('//*[@class="sku-part"]/span/text()').extract()[0]
            if not item_num:
                request["SNR_ModelNo"] = '00'
            else:
                request["SNR_ModelNo"] = item_num
        except Exception:
            pass

        try:
            last_price = response.xpath('//*[@id="lblPriceDetail"]/del/text()').extract_first()
            if not last_price:
                request["SNR_PriceBefore"] = '0.00'
            else:
                l = list(last_price)
                l[0] = ''
                last_price = "".join(l)
                request["SNR_PriceBefore"] = last_price
        except Exception:
            pass

        try:
            category = response.xpath('//*[@id="catBcrumbs"]/text()').extract_first()
            if not category:
                request["SNR_Category"] = '00'
            else:
                request["SNR_Category"] = category
        except Exception:
            pass

        try:
            price = response.xpath('//*[@id="lblPrice"]/text()').extract_first()
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
            description = response.xpath('//*[@id="lblShortDesc"]/li/text()').extract()
            if not description:
                request["SNR_Description"] = '00'
            else:
                request["SNR_Description"] = description
        except Exception:
            pass

        try:
            request["SNR_ProductURL"] = response.url
        except Exception:
            pass

        request["SNR_SKU"] = '0'
        request["SNR_SubCategory"] = '0'
        request["SNR_UPC"] = '0'
        request["SNR_Available"] = 'BuyDig'
        request["SNR_Condition"] = '0'
        request["SNR_CustomerReviews"] = '0'
        request["SNR_isShow"] = True
        request["SNR_Brand"] = '0'

        url = "http://127.0.0.1:8000/products/InsertProduct/"
        headers = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=headers, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(BuySpider)

process.start()


