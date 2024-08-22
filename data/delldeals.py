from scrapetools import *
from products.serializers import DailyDeals_Serializer

deals_url = "http://deals.dell.com/"

import scrapy
from scrapy.crawler import CrawlerProcess





class DellDealsSpider(scrapy.Spider):
    # Your spider definition
    name = "dell"

    start_urls = [
        "http://deals.dell.com/"
    ]

    def parse(self,response):
        for i in response.css("div.deal-column"):
            try:
                title_div = i.css("div.title-wrapper a")[0]
                title = title_div.css("::text").extract_first()
                url = response.urljoin(title_div.css('::attr("href")').extract_first())
                id = "DL"+url.rsplit("/",1)[-1]
                price_div = i.css("div.price-wrapper")[0]

                try:
                    before_price = price_div.css(".market-value-pricing div span.text-strikethru::text"
                                                 ).extract_first().replace("$","").replace(",","")
                except:
                    before_price = "-1.0"


                after_price = price_div.css("span.sale-price::text"
                                    )[-1].extract().replace("$","").replace(",","")

                before_price = float(before_price.strip())
                after_price = float(after_price.strip())
                image = i.css(".image-wrapper a.image-link img::attr(\"data-src\")").extract_first()
                image = response.urljoin(image)
                current_item = {
                        "SNR_SKU": id,
                        "SNR_Title": title,
                        "SNR_ProductURL": url,
                        "SNR_Category": "No Brand",
                        "SNR_PriceBefore": before_price,
                        "SNR_PriceAfter": after_price,
                        "SNR_Available": "Dell",
                    "SNR_ImageURL" : image
                    }

                commitdeal(current_item)

                """
                yield scrapy.Request(url=url,callback=lambda x:self.get_image(
                    current_image,x
                ))"""



            except Exception as e:
                pass

    def get_image(self,item,response):
        image = response.css("img#heroStaticImage::attr(\"src\")").extract_first()
        image = response.urljoin(image)
        item["SNR_ImageURL"] = image

        commitdeal(item)
        yield item

