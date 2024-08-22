from scrapetools import *
import scrapy
from scrapy.crawler import CrawlerProcess

start_url = "https://www.microsoft.com/en-us/store/b/home"
#request.meta['proxy'] = my_proxy

#my_proxy = getProxyWorking(start_url)["http"]
my_proxy = "34.231.147.235:3128"

class WalmartSpider(scrapy.Spider):
    name = "microsoft"

    start_urls = [start_url]
    custom_settings = {
        'CONCURRENT_REQUESTS': 500,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 150,
        'DOWNLOAD_DELAY': 0.05,
        "HTTP_PROXY" : my_proxy
    }


    def __init__(self):
        pass


    def parse(self,response):
        data = []
        for current_cat in response.css('div.c-uhf-menu'):
            cats = current_cat.css("ul")[0]
            t = cats.extract()
            top_cat = cats.css("::attr(data-m)").extract_first().strip()
            try:
                top_cat = json.loads(top_cat)["cN"].split("_",1)[0]
            except:
                pass
            sub_cats = cats.css("li a[class*=nav]")

            for current_sub in sub_cats:
                link = current_sub.css("::attr(href)").extract_first()


                link = response.urljoin(link)
                link = re.sub("\?.+","",link)
                sub= current_sub.css("::text").extract_first()
                cat = top_cat

                cat = cat.lower()

                if "default" in cat:
                    cat = "Entertainment"
                sl = sub.lower()

                if "games" in sl or "xbox" in sl or "gaming" in sl:
                    cat = "Video Games & Consoles".lower()

                if "books" in sl:
                    cat = sl

                if "business" in sl:
                    cat = sl

                if "more" in cat:
                    continue

                if cat in ["devices","other"]:
                    cat = sub

                if "en-us/store" in link:
                    data.append((cat,sub,link))

        for current_cat in data:
            cat,sub,link = current_cat
            yield scrapy.Request(url=link,callback=self.scrape_data,meta={"cat":cat,"sub":sub,"proxy":my_proxy})



    def scrape_data(self,response):
        cat = response.meta["cat"]
        subcat = response.meta["sub"]
        yield

        nested = response.css("div.m-hyperlink-group")

        if nested:
            nested = [i.css("a.c-hyperlink") for i in nested]

            for i in nested:
                subcat = i.css("::text").extract_first()
                link = i.css("::attr(href)").extract_first()

                link = response.urljoin(link)


                yield scrapy.Request(url=link, callback=self.scrape_data,
                                     meta={"cat": cat, "sub": subcat, "proxy": my_proxy})
        else:
            next_div = response.css("ul[class*=pagination] li a[aria-label*=next]::attr(href)").extract_first()
            if next_div:
                next_div = response.urljoin(next_div)
                yield scrapy.Request(url=next_div, callback=self.scrape_data,
                                     meta={"cat": cat, "sub": subcat, "proxy": my_proxy})
            all_data = response.css("section[itemscope=itemscope]")
            for current_item in all_data:
                request = {}
                try:
                    rating_div = float(current_item.css("div.c-rating::attr(data-value)")[0])
                except:
                    rating_div = 0.0
                price_div = current_item.css("span[itemprop=price]::attr(content)").extract_first()
                if not price_div:
                    continue


                item_price = float(price_div)
                url_data = current_item.css("a[data-m]")[0]
                data_div = json.loads(url_data.css("::attr(data-m)").extract_first())
                item_url = response.urljoin(url_data.css("::attr(href)").extract_first())
                try:
                    image_div = current_item.css("div[class*=image] picture img")[0]
                except:
                    continue


                image_url = image_div.css("::attr(data-src)").extract_first()

                if not image_url:
                    image_url = image_div.css("::attr(src)").extract_first()

                if not image_url:
                    continue

                item_desc = current_item.css("div.c-paragraph::text").extract_first()

                if not item_desc:
                    item_desc = "Visit site to see description"

                request["SNR_Price"] = item_price
                request["SNR_CustomerReviews"] = rating_div
                request["SNR_ProductURL"] = item_url
                request["SNR_ImageURL"] = re.sub("\?.*","",image_url)
                request["SNR_SKU"] = "MS" + data_div["id"]
                c = current_item.css("h3[id*=heading]::text").extract_first()
                if not c:
                    c = current_item.css("h3[class*=heading]::text").extract_first()
                request["SNR_Title"] = c
                a = current_item.extract()
                if not request["SNR_Title"]:
                    continue
                request["SNR_Category"] = cat
                request["SNR_Available"] = "Microsoft"

                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Description"] = item_desc
                request["SNR_SubCategory"] = subcat
                request["SNR_Condition"] = "00"
                request["SNR_PriceBefore"] = -1
                try:
                    before = next(i for i in current_item.css("s[aria-label*=price]::attr(aria-label)").extract() if " was" in i)
                except:
                    before = ""

                if before:
                    before = patSearch("was\s+\$([\d,\.]+)",before).group(1).replace(",","")
                    request["SNR_PriceBefore"] = float(before)


                request["SNR_Brand"] = "Not Available"

                try:

                    yield scrapy.Request(url="http://127.0.0.1:8000/products/sendData",method="POST",
                                         headers={"Content-Type":"application/json"},
                                         body = json.dumps(request),callback= self.non_function
                                         )
                except Exception as e:
                    pass



    def non_function(self,response):
        yield {}


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(WalmartSpider)

process.start()