# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import requests
from scrapy.crawler import CrawlerProcess


class HpSpider(scrapy.Spider):
    name = 'hp'
    allowed_domains = ['hp.com']
    start_urls = ['https://hp.com']
    def parse(self, response):
        all_links = response.xpath('//*[@class="js_hf_menu  hf_menu level1"]/li/a/@href').extract()[:5]
        for link in all_links:
            yield Request(link, callback=self.parses)

    def parses(self,response):
    	view_all = response.xpath('//*[@class="content"]/div/a/@href').extract_first()
    	absolute_view_all = response.urljoin(view_all)
    	yield Request(absolute_view_all, callback=self.pars)

    def pars(self, response):
        products_url = response.xpath('//*[@class="groupviewallarea"]/a/@href').extract()
        for product in products_url:
            absolute_products_url = response.urljoin(product)
            yield Request(absolute_products_url, callback=self.products)

    def products(self, response):
    	products_data = response.xpath('//*[@class="productInfo2"]/h3/a/@href').extract()
    	for data in products_data:
    		absolute_products_data = response.urljoin(data)
    		yield Request(absolute_products_data, callback=self.datas)

    def datas(self, response):
        request = {}

        try:
            title = response.xpath('//h1/span/text()').extract_first()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title = response.xpath('//h1/span/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass

        try:
            img = response.xpath('//*[@class="pdp_featured_image"]/li/img/@src').extract_first()
            if not img:
                img = '0'
                request["SNR_ImageURL"] = img
            else:
                img = response.xpath('//*[@class="pdp_featured_image"]/li/img/@src').extract_first()
                request["SNR_ImageURL"] = img
        except Exception:
            pass

        try:
            product_num = response.xpath('//*[@class="prodNum"]/text()').extract_first()
            if not product_num:
                product_num = '0'
                request["SNR_SKU"] = product_num
            else:
                product_num = response.xpath('//*[@class="prodNum"]/text()').extract_first()
                request["SNR_SKU"] = product_num
        except Exception:
            pass

        try:
            description = response.xpath('//*[@class="seeAllOffers"]/following-sibling::ul/li/text()').extract()
            if not description:
                description = 'Visit see description'
                request ["SNR_Description"] = description
            else:
                description = response.xpath('//*[@class="seeAllOffers"]/following-sibling::ul/li/text()').extract()
                request ["SNR_Description"] = description
        except Exception:
            pass

        try:
            price =  response.xpath('//span/text()').extract()[55].strip()
            if not price:
                price = response.xpath('//span/text()').extract()[56].strip()
                request["SNR_Price"] = price
            else:
                price =  response.xpath('//span/text()').extract()[55].strip()
                request["SNR_Price"] = price
        except Exception:
            pass

        '''try:
            product_type = response.xpath('//*[@class="prodEnergy"]/text()').extract_first()
            if not product_type:
                product_type = '0'
            else:
                product_type = response.xpath('//*[@class="prodEnergy"]/text()').extract_first()
    	except Exception:
    		pass'''

        request["SNR_Category"] = 'Computer & Laptops'
        request["SNR_SubCategory"] = '0'
        request["SNR_UPC"] = '0'
        request["SNR_Available"] = 'hp'
        request["SNR_Condition"] = '0'
        request["SNR_isShow"] = True
        request["SNR_CustomerReviews"] = '0'
        request["SNR_Brand"] = 'hp'
        request["SNR_Date"] = '00'
        request["SNR_PriceBefore"] = '0.00'
        request["SNR_ProductURL"] = response.url
        request["SNR_ModelNo"] = "00"
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(HpSpider)

process.start()



