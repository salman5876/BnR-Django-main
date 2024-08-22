from scrapetools import *
import scrapy
from products.models import AllProducts
from scrapy.crawler import CrawlerProcess

#request.meta['proxy'] = my_proxy

my_proxy = getProxyWorking("https://www.walmart.com")["http"]

class WalmartSpider(scrapy.Spider):
    name = "walmart"

    start_urls = ["https://www.walmart.com/browse"]
    custom_settings = {
        'CONCURRENT_REQUESTS': 700,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 350,
        'DOWNLOAD_DELAY': 0.05,
        "HTTP_PROXY" : my_proxy
    }


    def __init__(self):
        pass


    def parse(self,response):
        """
        facets = [i["values"] for i in self.get_facets(response.body, response.url)
                  if i["type"] == "special_offers"
                  ][0]

        notcat = ['Price Shown at Cart','Price at Checkout']
        notcat = []
        facets_urls = [ "https://www.walmart.com/browse?{0}".format(i["url"])
            for i in facets
            if i["name"] not in notcat
        ]


        for i in facets_urls:
            yield scrapy.Request(url=i,callback=self.only_price_data)
        """

        yield scrapy.Request(url=response.url,callback=self.only_price_data)




    def only_price_data(self,response):
        cats = self.get_cats(response.body,response.url)
        for i in cats:

            request = scrapy.Request(url=i["url"],callback=self.start_processing)
            request.meta["cat"] = i["cat"]
            request.meta['proxy'] = my_proxy

            yield request


    def cat_done(self,cats,current_cat):
        all_cats = []
        done = []

        for i in cats:
            if "electronics" == current_cat.lower():
                current_cat = i["cat"]

            if i["count"] > 1000:
                all_cats.append((current_cat, i["cat"],i["count"], i["url"]))
            else:
                done.append((current_cat, i["cat"], i["url"]))

        return (done,all_cats)

    def start_processing(self,response):
        cats = self.get_cats(response.body,response.url)
        current_cat = response.meta['cat']
        done,all_cats = self.cat_done(cats,current_cat)

        for i in self.process(done,self.scrape_data):
            yield i

        for i in self.process(all_cats, self.filter_further):
            yield i

    def process(self,done,callback):
        for i in done:


            i = list(i)
            count = False
            i[-1] = i[-1].replace("&page=25", "").replace("&sort=new","")

            i[-1]+= "&sort=new"
            if len(i) == 4:
                i[-1]+="&page=25"
                count = i[-2]
            i = tuple(i)



            request = scrapy.Request(url=i[-1],callback=callback,errback=self.errback)
            if count:
                request.meta["count"] = count

            request.meta['cat'] = i[0]
            request.meta['subcat'] = i[1]
            request.meta['proxy'] = my_proxy
            yield request




    def get_data_json(self,raw):
        st = 'items":(\[){'
        data = []
        try:
            ind = getreIndex(st, raw)
            data = getJsonData(raw[ind:])
        except Exception as e:
            pass

        return data

    def get_last_sku(self,data):
        temp = data[::-1]

        for i in temp:
            try:
                return "WM"+i["productId"]
            except:
                pass


        raise Exception("")

    def non_function(self,response):
        yield {}

    def is_sku_exist(self,sku):
        return AllProducts.objects.filter(SNR_SKU=sku).exists()

    def scrape_data(self,response):
        cat = response.meta['cat']
        subcat = response.meta['subcat']
        raw = response.body

        data = self.get_data_json(raw)
        last_sku = "waryamsoomro"
        for current_item in data:
            try:
                inv = json.dumps(current_item["inventory"])
                if "OUT_OF_STOCK" in inv:
                    continue
            except:
                pass
            try:
                request = {}

                request["SNR_SKU"] = "WM"+current_item["productId"]
                last_sku = request["SNR_SKU"]
                request["SNR_ProductURL"] = response.urljoin(current_item['productPageUrl'])
                request["SNR_Price"] = ""
                primary_offer = offer_div = current_item["primaryOffer"]

                item_after_price = u"{}".format(primary_offer.pop(u"offerPrice"))

                try:
                    # is there before price
                    item_before_price = u"{}".format(primary_offer.pop(u"listPrice"))
                except:
                    # is there pickup discount
                    try:
                        temp = u"{}".format(primary_offer.pop(u"pickupDiscountOfferPrice"))
                        item_after_price, item_before_price = temp, item_after_price
                    except:
                        item_before_price = u"-1"

                # print(item_after_price,item_before_price)
                request["SNR_Price"] = float(item_after_price.replace(",", ""))
                request["SNR_PriceBefore"] = float(item_before_price.replace(",", ""))

                try:
                    request["SNR_Description"] = current_item["description"]
                except:
                    request["SNR_Description"] = "Visit site to see description"

                try:
                    request["SNR_CustomerReviews"] = current_item['customerRating']
                except:
                    request["SNR_CustomerReviews"] = 0.0

                image = response.urljoin(current_item["imageUrl"])
                try:
                    ind = image.rindex("?")
                    image = image[:ind]
                except:
                    pass
                request["SNR_ImageURL"] = image

                request["SNR_Title"] = parseHtml(current_item["title"])
                request["SNR_Category"] =cat
                request["SNR_Available"] = "Walmart"

                request["SNR_ModelNo"] = "00"
                try:
                    request["SNR_UPC"] = current_item["upc"]
                except:
                    request["SNR_UPC"] = "00"

                request["SNR_SubCategory"] = subcat
                request["SNR_Condition"] = "00"


                try:
                    request["SNR_Brand"] = current_item["brand"][0]
                except:
                    request["SNR_Brand"] = "Not Available"

                try:
                    request["SNR_Category"] = map_data(cap_dict, request["SNR_Category"])
                except:
                    pass

                yield scrapy.Request(url="http://127.0.0.1:8000/products/sendData",method="POST",
                                     headers={"Content-Type":"application/json"},
                                     body = json.dumps(request),callback= self.non_function
                                     )
            except Exception as e:
                pass

        if data:

            try:
                exist = self.is_sku_exist(last_sku)

            except Exception as e:
                exist = False

            if not exist:
                try:
                    next_link = response.css("link[rel=next]::attr(href)").extract_first()
                    if next_link:
                        next_link = response.urljoin(next_link)
                        if "waryam" in response.url:
                            pass
                        request = scrapy.Request(url=next_link,callback=self.scrape_data,errback=self.errback)
                        request.meta['cat'] = cat
                        request.meta['subcat'] = subcat
                        request.meta['proxy'] = my_proxy
                        yield request
                except:
                    pass

    def errback(self,failure):
        try:
            response = failure.value.response
            exists = response.status !=404
        except:
            response = failure.request
            exists=True

        current_cat = response.meta['cat']
        subcat = response.meta['subcat']
        temp = [current_cat,subcat]
        callback = self.scrape_data
        try:

            count = response.meta['count']
            callback = self.filter_further
            temp.append(count)
        except:
            pass
        url = response.url
        temp.append(url)

        yield self.process(tuple(temp),callback)

    def filter_further(self,response):
        current_cat = response.meta['cat']
        subcat = response.meta['subcat']
        count = response.meta['count']
        data = self.get_data_json(response.body)
        ur = response.url
        yield {}

        try:
            sku = self.get_last_sku(data)
            exist = self.is_sku_exist(sku)
        except Exception as e:
            exist = False

        if exist:

            done = [(current_cat,subcat,ur.replace("page=25","page=1"))]
            for i in self.process(done, self.scrape_data):
                yield i

        else:
            cats = self.get_cats(response.body,response.url)
            if cats:
                done,all_cats = self.cat_done(cats,current_cat)

                for i in self.process(done, self.scrape_data):
                    yield i

                for i in self.process(all_cats, self.filter_further):
                    yield i

            else:

                    url = ur
                    url, attrs = get_part_attr(url)
                    temp = list(attrs.iterkeys())
                    facet ="waryamalisoomro"

                    if "facet" in attrs:
                        facet = attrs["facet"][0]

                    current_count = 0
                    done_count = 0

                    facets = [i for i in self.get_facets(response.body, url)
                              if i["type"] not in temp and i["type"]+":" not in facet]

                    current_done = []
                    current_all = []
                    for current_facet in facets:
                        values = current_facet["values"]
                        local_count = 0
                        local_done = 0
                        local_data = []
                        local_all = []

                        for cval in values:

                            try:
                                if cval["isSelected"]:
                                    continue
                            except:
                                pass

                            try:
                                cval["count"] = cval["itemCount"]
                            except Exception as e:
                                continue

                            curl = "https://www.walmart.com/browse?{0}".format(cval["url"])
                            if cval["count"]>1000:
                                local_all.append((current_cat,subcat,cval["count"],curl))
                            else:
                                local_data.append((current_cat, subcat, curl))
                                local_done+=cval["count"]

                            local_count+=cval["count"]

                        if local_count>count and local_done>done_count:
                            current_all = local_all
                            current_done = local_data
                            done_count = local_done
                            current_count = local_count
                            continue

                        if local_count>current_count:
                            current_all = local_all
                            current_done = local_data
                            done_count = local_done
                            current_count = local_count
                        elif local_count==current_count:
                            if local_done>done_count:
                                current_all = local_all
                                current_done = local_data
                                done_count = local_done
                                current_count = local_count



                    if current_count<1000:
                        current_all = []
                        current_done = [ (current_cat,subcat,ur+"&waryam=true")]
                        try:
                            with open("walex.txt","a") as w:
                                w.write(response.url+"\n")
                        except:
                            pass

                    done , all_cats = current_done,current_all

                    for i in self.process(done, self.scrape_data):
                        yield i

                    for i in self.process(all_cats, self.filter_further):
                        yield i



        yield {}


    def get_cats(self,data,url):
        facets = self.get_facets(data,url)
        temp = facets
        facets = []
        for i in temp:
            if i["type"] == "cat_id":
                facets = i["values"]
                break

        url,attrs = get_part_attr(url)
        temp = []
        for i in facets:
            attrs["cat_id"] = [i["id"]]

            curl = join_attr(url,attrs)

            temp.append(  {"cat":i["name"],"url":curl,"count":i['itemCount']} )

        return temp

    def get_facets(self,data,url):
        temp = getreIndex('"facets"\s*:\s*(\[)', data)
        data = data[temp:]
        temp = getJsonData(data)
        return temp


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(WalmartSpider)

process.start()