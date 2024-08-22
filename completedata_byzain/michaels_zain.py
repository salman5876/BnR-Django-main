import scrapy
from scrapy.http import Request
import requests
import json
from scrapy.crawler import CrawlerProcess


class MichaelsZainSpider(scrapy.Spider):
    name = 'michaels_zain'
    allowed_domains = ['michaels.com']
    start_urls = ['http://www.michaels.com/shop-categories/categories']
    custom_settings = {'CONCURRENT_REQUESTS': 700,'CONCURRENT_REQUESTS_PER_DOMAIN': 350,'DOWNLOAD_DELAY': 0.05}

    def parse(self, response):
        products = response.xpath('//h3/a[@class="name-link"]/@href').extract()
        for product in products:
        	absolute_product = response.urljoin(product)
        	yield Request(absolute_product, callback=self.product_data)
        next_page = response.xpath('//*[@class="page-next"]/@href').extract_first()
        yield Request(next_page)

    def product_data(self, response):
        request = {}
        try:
            img = response.xpath('//*[@class="zoom_05"]/@src').extract_first()
            if not img:
                request["SNR_ImageURL"] = "Not Available"
            else:
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        try:
            price_before = response.xpath('//*[@class="price-standard dsp"]/text()').extract_first()
            price_before = price_before.replace('$','')
            request["SNR_PriceBefore"] = price_before
        except:
            request["SNR_PriceBefore"] = '0.00'
        try:
            price = response.xpath('//*[@class="product-pricing"]/div/text()').extract_first().strip()
            price = price.replace('$','')
            request["SNR_Price"] = price
        except:
            price = response.xpath('//*[@class="product-sales-price discounted-sale-price"]/text()').extract_first().strip()
            price = price.replace('$','')
            request["SNR_Price"] = price
        try:
            title = response.xpath('//*[@class="product-header-left"]/h1/text()').extract_first()
            if not title:
                request["SNR_Title"] = "Not Available"
            else:
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            reviews = response.xpath('//*[@itemprop="reviewCount"]/text()').extract_first()
            if not reviews:
                request["SNR_CustomerReviews"] = "00"
            else:
                request["SNR_CustomerReviews"] = reviews
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@itemprop="productID"]/text()').extract_first().strip()
            if not sku:
                request["SNR_SKU"] = "00"
            else:
                request["SNR_SKU"] = sku
        except Exception:
            pass
        request["SNR_Brand"] = 'Not Available'
        request["SNR_Description"] = "Visit site to see description"
        try:
            request["SNR_Category"] = response.xpath('//*[@class="breadcrumb"]/li/a/text()').extract()[1]
        except:
            request["SNR_Category"] = "Home & Garden"
        request["SNR_ModelNo"] = "00"
        request["SNR_UPC"] = "00"
        request["SNR_ProductURL"] = response.url
        request["SNR_Available"] = 'Michaels'
        request["SNR_Date"] = '00'
        request["SNR_Condition"] = "00"
        try:
            request["SNR_SubCategory"] = response.xpath('//*[@class="breadcrumb"]/li/a/text()').extract()[-1]
        except:
            request["SNR_SubCategory"] = "Home & Garden"
        request["SNR_isShow"] = True
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header ,data=json.dumps(request))

process = CrawlerProcess({
	'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
	})
process.crawl(MichaelsZainSpider)
process.start()