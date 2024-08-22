import scrapy
from scrapetools import *
from scrapy.crawler import CrawlerProcess

deal_url = "http://store.hp.com/api/web/template/prtl-sale-v3?pgKeys=sale%3Aweekly_deals%3A{0}"
price_url = "http://store.hp.com/us/en/HPServices?langId=-1&storeId=10151&catalogId=10051&_=1519909738887&action=pis&catentryId={0}"


class HpDeals(scrapy.Spider):
    name= "hpDeals"
    start_urls =["http://store.hp.com/us/en/cv/weekly-deals"]

    def parse(self, response):
        for i in response.css("li.tab-title a::attr(href)").extract():
            i = i.split("#")[-1]
            yield scrapy.Request(url=deal_url.format(i),callback=self.get_deals)

    def get_deals(self,response):
        all_ids = {}
        for current_product_div in response.css("div.product-card"):

            item_id = current_product_div.css("::attr(\"data-itemid\")").extract_first()

            if not item_id:
                continue

            image_div = current_product_div.css("a.product-img")
            item_url = response.urljoin(image_div.css("::attr(href)").extract_first())
            item_title = image_div.css("::attr(title)").extract_first()
            item_image = image_div.css("img[src]::attr(src)").extract_first()
            item_image = response.urljoin(item_image)



            current_item = {
                "SNR_SKU": "HP" + item_id,
                "SNR_Title": item_title,
                "SNR_ProductURL": item_url,
                "SNR_ImageURL": item_image,
                "SNR_Category": "Not Available",
                "SNR_Available": "HP"
            }

            all_ids[item_id] = current_item


        ids = ",".join(list(all_ids.iterkeys()))
        url=price_url.format(ids)

        prices = getRawData(url,json=True)["priceData"]
        for i in prices:
            try:
                current_item = all_ids[i['productId']]
            except:
                continue
            try:
                before_price = float(i['gsPrice'])
            except:
                try:
                    before_price = float(i['price'])
                except:
                    before_price = -1.0


            after_price = i['lPrice']

            current_item["SNR_PriceBefore"] = before_price
            current_item["SNR_PriceAfter"] = after_price

            commitdeal(current_item)

    def get_price(self,res):
        a = res.body
        b = res





