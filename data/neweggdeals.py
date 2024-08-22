from urllib import unquote

from scrapetools import *
from scrapy.crawler import CrawlerProcess

my_proxy = getProxyWorking("https://www.newegg.com/")

data_url = "https://www.newegg.com/Common/Ajax/LoadDailyDeal.aspx?page={0}&N=&srchInDesc=&Order=InStock&HasResults=1&CanBeCompare=0&TotalRecordCount=72&RealCount=24&Submit=DailyDeals&action=Biz.ProductList.DailyDeal.jsonpCallBack"


import scrapy


class NewEggDeals(scrapy.Spider):
    name="neweggdeals"
    start_urls = [
        data_url.format(1)
    ]

    def parse(self,response):
        try:
            count = response.meta["count"]
        except:
            count = 1
        for i in self.parse_json(response.body.strip(),response.url,count):
            yield i

    def parse_json(self,data,url,count):
        count+=1
        try:
            ind = getreIndex('jsonpCallBack\((")',data)+1
            raw = data[ind:-3]

            u = raw.replace('\\"','"').replace('\\/','/').replace("\\'","'").replace("\u000d","").replace("\u000a","")
            raw = BeautifulSoup(u, "lxml")
            all_items = raw.select("div.item-container")

            if all_items:
                next_url = data_url.format(count)
                request = scrapy.Request(url=next_url,callback=self.parse)
                request.meta["count"] = count
                yield request

                for current_item in all_items:
                    image_div = current_item.select_one("a.item-img")
                    item_url = getAbsUrl(url,image_div["href"])
                    item_id = patSearch("Item=(\\w+)",item_url).group(1)
                    img = image_div.img
                    image_url = getAbsUrl(url,img["src"])
                    item_title = img["alt"]
                    price_div = current_item.select_one("ul.price")
                    current_div = current_item.select_one("li.price-current")
                    pat = "\$<strong>(\d+)</strong><sup>([\.\d]+)</sup>"
                    current_price = patSearch(pat,str(current_div))
                    p = current_price.group(1)+ current_price.group(2)
                    try:
                        before = price_div.select_one("span.price-was-data").text.strip().replace(",","")
                        print ""
                    except:
                        before = "-1.0"

                    p = p.replace(",","")
                    p = float(p)
                    before = float(before)

                    current_item = {
                        "SNR_SKU": "NG"+item_id,
                        "SNR_Title": item_title,
                        "SNR_ProductURL": item_url,
                        "SNR_ImageURL": image_url,
                        "SNR_Category": "Not Available",
                        "SNR_PriceBefore": before,
                        "SNR_PriceAfter": p,
                        "SNR_Available": "NewEgg"
                    }

                    commitdeal(current_item)






        except Exception as e:
            pass

        yield {}


if __name__ == '__main__':

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(NewEggDeals)

    process.start()