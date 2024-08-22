import scrapy
from scrapy.crawler import CrawlerProcess
import requests
import json
from scrapy.http import Request


class BurlinSpider(scrapy.Spider):
    name = 'burlin'
    allowed_domains = ['burlington.com']
    start_urls = ['https://www.burlington.com']
    custom_settings = {'CONCURRENT_REQUESTS': 700,'CONCURRENT_REQUESTS_PER_DOMAIN': 350,'DOWNLOAD_DELAY': 0.05}

    def parse(self, response):
        menus =  response.xpath('//*[@class="nav"]/li/a/@href').extract()
        for menu in menus:
        	yield Request(menu, callback=self.categories)

    def categories(self, response):
    	categories = response.xpath('//*[@class="productImage"]/a/@href').extract()
    	for category in categories:
    		absolute_category = response.urljoin(category)
    		yield Request(absolute_category, callback=self.sub_categories)

    def sub_categories(self, response):
        more_sub = response.xpath('//*[@class="category-slider wrap clearfix text-center"]//a/@href').extract()
        for more in more_sub:
            absolute_more = response.urljoin(more)
            yield Request(absolute_more, callback=self.product_parser)

    def more_sub_categories(self, response):
        try:
            more_categories = response.xpath('//*[@class="category-slider wrap clearfix text-center"]//a/@href').extract()
            for more_category in more_categories:
                absolute_more_category = response.urljoin(more_category)
                yield Request(absolute_more_category, callback=self.product_parser)
        except:
            yield Request(callback=self.product_parser)

    def product_parser(self, response):
        products =  response.xpath('//*[@class="product-title clearfix"]/@href').extract()
        for product in products:
            absolute_product = response.urljoin(product)
            yield Request(absolute_product, callback=self.product_data)
    def product_data(self, response):
        request = {}
        try:
            title =  response.xpath('//h1/text()').extract_first()
            if not title:
                title = 'Not Available'
                request["SNR_Title"] = title
            else:
                title =  response.xpath('//h1/text()').extract_first()
                request["SNR_Title"] = title
        except Exception:
            pass
        try:
            price =  response.xpath('//*[@class="clearance price"]/span/text()').extract()[1]
            if not price:
                price = '0.00'
                request["SNR_Price"] = price
            else:
                price =  response.xpath('//*[@class="clearance price"]/span/text()').extract()[1]
                price = price.replace('$','')
                request["SNR_Price"] = price
        except Exception:
            pass
        try:
            price_before =  response.xpath('//*[@class="price price-old"]/text()').extract_first()
            if not price_before:
                price_before = response.xpath('//*[@class="textPriceCompare"]/text()').extract_first()
                price_before = price_before.replace('$','')
                request["SNR_PriceBefore"] = price_before
            else:
                price_before =  response.xpath('//*[@class="price price-old"]/text()').extract_first()
                price_before = price_before.replace('$','')
                request["SNR_PriceBefore"] = price_before
        except Exception:
            pass
        try:
            sku = response.xpath('//*[@class="product-details-codes"]/span/text()').extract_first()[6:]
            if not sku:
                sku = '0.00'
                request["SNR_SKU"] = sku
            else:
                sku = response.xpath('//*[@class="product-details-codes"]/span/text()').extract_first()[6:]
                request["SNR_SKU"] = sku
        except Exception:
            pass
        try:
            model_num = response.xpath('//*[@class="product-details-codes"]/span/text()').extract()[1][7:]
            if not model_num:
                model_num = '00'
                request["SNR_ModelNo"] = model_num
            else:
                model_num = response.xpath('//*[@class="product-details-codes"]/span/text()').extract()[1][7:]
                request["SNR_ModelNo"] = model_num
        except Exception:
            pass
        try:
            description = response.xpath('//*[@class="descriptionContent"]/text()').extract_first()
            if not description:
                description = 'Visit site to see description'
                request["SNR_Description"] = description
            else:
                description = response.xpath('//*[@class="descriptionContent"]/text()').extract_first()
                request["SNR_Description"] = description
        except Exception:
            pass
        try:
            sub_category = response.xpath('//*[@class="breadcrumbs"]/a/text()').extract()[-1]
            if not sub_category:
                sub_category = 'Not Available'
                request["SNR_SubCategory"] = sub_category
            else:
                sub_category = response.xpath('//*[@class="breadcrumbs"]/a/text()').extract()[-1]
                request["SNR_SubCategory"] = sub_category
        except Exception:
            pass
        try:
            img =  response.xpath('//*[@id="productMainImage"]/@src').extract_first()
            if not img:
                img = 'Not Available'
                request["SNR_ImageURL"] = img
            else:
                img =  response.xpath('//*[@id="productMainImage"]/@src').extract_first()
                request["SNR_ImageURL"] = img
        except Exception:
            pass
        request[ "SNR_Brand"] = "Unavailable"
        try:
            categry = response.xpath('//*[@class="breadcrumbs"]/a/text()').extract()[1]
            if not categry:
                request["SNR_Category"] = 'Clothing & Apparel'
            else:
                request["SNR_Category"] = categry
        except Exception:
            pass
        request["SNR_UPC"] = "00"
        request["SNR_ProductURL"] = response.url
        request["SNR_Available"] = 'Burlington'
        request["SNR_Date"] = '00'
        request["SNR_CustomerReviews"] = "0"
        request["SNR_Condition"] = "00"
        request["SNR_isShow"] = True
        url = "https://backend.shopnroar.com/products/InsertProduct/"
        header = {'Content-Type': 'application/json'}
        yield requests.put(url, headers=header, data=json.dumps(request))

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
})

process.crawl(BurlinSpider)

process.start()