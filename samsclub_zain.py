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
        pages_url = response.xpath('//*[@class="subcategories"]/li/span/a/@href').extract()
        for page in pages_url:
            absolute_pages_url = response.urljoin(page)
            yield Request(absolute_pages_url, callback=self.parsers)

    def parsers(self, response):
        sub_pages_url = response.xpath('//*[@class="catLeftNav"]/li/a/@href').extract()
        for sub_page in sub_pages_url:
            absolute_sub_pages_url = response.urljoin(sub_page)
            yield Request(absolute_sub_pages_url, callback=self.parses)

    def parses(self, response):
        sub_links = response.xpath('//*[@class="catLeftNav"]/li/a/@href').extract()
        for sub_link in sub_links:
            absolute_sub_links = response.urljoin(sub_link)
            yield Request(absolute_sub_links, callback=self.pars)

    def pars(self, response):
        products_link = response.xpath('//*[@class="cardProdLink"]/@href').extract()
        for product_link in products_link:
            absolute_products_link = response.urljoin(product_link)
            yield Request(absolute_products_link, callback=self.products)

    def products(self, response):

        request = {}
        try:
            title = response.xpath('//h1/span/text()').extract_first()
            if not title:
                request["SNR_Title"] = '0'
            else:
                request["SNR_Title"] = title
        except Exception:
            pass

        try:
            img_url = response.xpath('//*[@class="imgHolder2 span5 zoom"]/img/@src').extract_first()
            img_url = img_url.replace('//', 'https://')
            if not img_url:
                request["SNR_ImageURL"] = '0'
            else:
                request["SNR_ImageURL"] = img_url
        except Exception:
            pass

        try:
            item_number = response.xpath('//*[@class="itemId"]/span[1]/text()').extract_first()
            if not item_number:
                request["SNR_ModelNo"] = '0'
            else:
                request["SNR_ModelNo"] = item_number
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
            description = response.xpath(
                '//*[@class="itemBullets span7 offset0 pull-left ft14 gray6 short-desc"]/ul/li/text()').extract()
            if not description:
                request["SNR_Description"] = '0'
            else:
                request["SNR_Description"] = description
        except Exception:
            pass

        try:
            price = response.xpath('//*[@class="lgFont "]/li/span[2]/text()').extract_first()
            if not price:
                request["SNR_Price"] = '0.00'
            else:
                request["SNR_Price"] = price
        except Exception:
            pass

        try:
            sub_category = response.xpath('//*[@class="breadcrumb-child"]/a/span/text()')[-1].extract()
            if not sub_category:
                request["SNR_SubCategory"] = '0'
            else:
                request["SNR_SubCategory"] = sub_category
        except Exception:
            pass

        try:
            request["SNR_ProductURL"] = response.url
        except Exception:
            pass

        request["SNR_SKU"] = '0'
        request["SNR_UPC"] = '0'
        request["SNR_Available"] = "Sam's Club"

        request["SNR_PriceBefore"] = '0'
        request["SNR_Category"] = '0'
        request["SNR_Condition"] = '0'
        request["SNR_CustomerReviews"] = '0'
        request["SNR_isShow"] = True

        url = "http://127.0.0.1:8000/products/InsertProduct/"
        headers = {'Content-Type': 'application/json'}

        yield requests.put(url, headers=headers, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SamsSpider)

process.start()
