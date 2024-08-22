import codecs

from scrapetools import *
import scrapy

from scrapy.crawler import CrawlerProcess

forb = ["deals", "saved","under ",]
data_cat = ["Home & Garden", "Business & Industrial", "Sporting Goods"
    , "Collectibles & Art", "Music", "Toys", "Motors"
            ]

not_cat = ["fitness", "appliances", "food ", "furniture", "office","jewelry","health","shoes"]

ex_fields =["format","price",'category']

def is_not(d,e="waryamsoomro"):
    d = d.lower()

    for i in not_cat:
        if i in d:
            if i in e.lower():
                return True
            return False

    return True


#request.meta['proxy'] = my_proxy

my_proxy = [getProxyWorking("https://www.ebay.com",strip=True)]
#my_proxy = [""]

class EbaySpider(scrapy.Spider):
    name = "ebaysp"

    custom_settings = {
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 50,
        'DOWNLOAD_DELAY': 0.05
    }




    def start_requests(self):
        yield scrapy.Request(url="https://www.ebay.com",callback=self.ebay_home,meta={"proxy":my_proxy[0]})


    def ebay_home(self,response):
        all_cats = []
        b = response.css("ul#s0-container > li")


        for cat in b:
            a = cat.extract()
            try:
                cat = BeautifulSoup(a,"lxml").a
                cat_url = cat["href"].strip()
                cat_url = response.urljoin(cat_url)
                cat_label = cat.text.strip()
                if is_allowed(forb, cat_label.lower()):
                    all_cats.append((cat_label, cat_url))
            except Exception as e:
                pass




        for cat_label,cat_url in all_cats:
            cat_url = re.sub("\?.*", "", cat_url).strip()
            yield scrapy.Request(url=cat_url,callback=self.get_cats,meta={
                "proxy":my_proxy[0],
                "cat" :cat_label,
            },errback=self.errb)


    def get_cats(self,response):
        ur = response.url
        cat = response.meta["cat"]

        try:
            subcat_label = response.meta["subcat"]
        except:
            subcat_label = cat


        if "www.ebay.com" not in ur:
            yield {}
        else:
            contents_data = []
            try:
                main_soup = response.css("div#mainContent")[0]

                data = main_soup.css("li.sresult")
                if not data:
                    data = main_soup.css("li.s-item")

                contents_data = data
            except:
                main_soup = response




            visual_nav = main_soup.css("section[class*=visualnav]")
            if not visual_nav:
                visual_nav = main_soup.css("div.visual-categories")

            catd = False
            if not visual_nav:
                catd = True
                visc = main_soup.css("a[class*=b-guidancecard]")

            if not visual_nav:
                visual_nav = []

            all_data = []
            if catd:
                for i in visc:
                    sub = i.css("::text").extract_first().strip()
                    all_data.append((cat,sub,getAbsUrl(response.url,i.css("::attr(href)").extract_first())))
                if all_data:
                    visual_nav = []

            for visual_c in visual_nav:
                    visual_h = visual_c.css("div[class*=heading] h2::text").extract_first()



                    if not visual_h:
                        visual_h = visual_c.css("h2.visualcategories-title::text").extract_first()
                    else:
                        if "category" not in visual_h.lower():
                            continue



                    cats_data = visual_c.css("div[class*=grid] a[class*=visualnav]")
                    if not cats_data:
                        cats_data = visual_c.css("div.visual-category-card a")
                    for j in cats_data:

                        cat_label = j.css("::attr(title)").extract_first()
                        if not cat_label:
                            cat_label = j.css("::text").extract_first().strip()

                        current_cat = cat
                        subcat = cat_label
                        if not is_not(cat_label,current_cat) or "electronics" == current_cat.lower():
                            current_cat = cat_label




                        cat_url = getAbsUrl(ur, j.css("::attr(href)").extract()[0])
                        cat_url = cat_url.strip().lower()
                        cat_url = re.sub("/?\?.*","",cat_url)
                        cat_url = cat_url.replace("http://","https://")
                        all_data.append((current_cat,cat_label,cat_url))

            if all_data:
                for current_cat,current_subcat,current_url in all_data:
                    yield scrapy.Request(url=current_url,callback=self.get_cats,meta={
                        "proxy" : my_proxy[0],
                        "cat" : current_cat,
                        "subcat" : current_subcat
                    },errback=self.errb)
            elif contents_data:
                url = response.url
                url = re.sub("/?\?.*","",url) + "?LH_BIN=1&rt=nc"
                url.replace("http://","https://")

                yield scrapy.Request(url=url,callback=self.expand_and_scrape,meta={
                    "cat":cat,
                    "subcat": subcat_label,
                    "proxy" : my_proxy[0]
                },errback=self.errb)

    def expand_and_scrape(self,response):

        body = response.body
        cat = response.meta["cat"]

        try:
            subcat_label = response.meta["subcat"]
        except:
            subcat_label = cat

        yield {}
        try:
            listings = patSearch("\s+([\d,]+)\s+Results",body).group(1).replace(",","")
        except Exception as e:
            listings = patSearch("([\d,]+)\s+listings",body).group(1).replace(",","")

        listings = int(listings)

        if listings<17000:
            yield scrapy.Request(url=response.url+"&waryam=true", callback=self.scrape_data, meta={
                "cat": cat,
                "subcat": subcat_label,
                "proxy": my_proxy[0]
            }, errback=self.errb,priority=2)
        else:
            prox = {"http":my_proxy[0],
                    "https":my_proxy[0]}



            ref_url = response.url+"&modules=SEARCH_REFINEMENTS_MODEL_V2"
            try:

                temp = data = getRawData(
                    ref_url,
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    json=True,
                    proxy=prox)

                data = data["group"]
                all_data = []

                ex_f = ex_fields
                try:
                    temp = [i.lower() for i in get_part_attr(response.url.lower())[-1].iterkeys()]
                except:
                    pass



                t = []
                for i in data:
                    if i['fieldId'] not in ex_fields:

                        try:
                            i["paremKey"]
                            t.append(i)
                        except:
                                t.extend(i["entries"])
                                is_next = True

                t = []
                for i in data:
                    try:
                        t.extend(i["entries"])
                    except:
                        t.append(i)

                for j in t:
                    try:
                        i = j["paramKey"].lower()
                        if i not in temp:
                            all_data.append(j)
                    except Exception as e:
                        if "entries" in j:
                            all_data.extend(j["entries"])

                data = all_data
            except Exception as e:
                data = []
                if "_ssan" in response.body:
                    with codecs.open("t.txt","a","utf-8") as w:
                        w.write(response.url+"\n")

            if data:
                data = imap(lambda x: x["entries"] if "entries" in x else [x], data)
                data = reduce(lambda x, y: x + y, data)
                td = data
                data = []
                for i in td:
                    try:
                        if "uction" not in i["paramKey"]:
                            data.append(i)
                    except:
                        pass




                count_data = {}

                for i in data:
                    try:
                        pk = i["paramKey"]
                        c = i['accessoryLabel']["textSpans"][0]["text"].replace(",", "")
                        c = float(c)
                        try:
                            count_data[pk] += c
                        except:
                            count_data[pk] = c
                    except:
                        pass

                count_data = sorted(count_data.iteritems(),key=lambda x:x[1],reverse=True)[0]
                data = filter(lambda x: x["paramKey"] == count_data[0] , data)

            if not data:
                url = response.url
                url += "&waryam=true"
                yield scrapy.Request(url=url, callback=self.scrape_data, meta={
                    "cat": cat,
                    "subcat": subcat_label,
                    "proxy": my_proxy[0]
                }, errback=self.errb)
            else :
                for i in data:
                    c = i['accessoryLabel']["textSpans"][0]["text"].replace(",", "")
                    url = i["action"]["URL"]
                    c = float(c)
                    if c < 17000:
                        url+="&waryam=true"
                    callback = self.scrape_data if c < 17000 else self.expand_and_scrape

                    yield scrapy.Request(url=url, callback=callback, meta={
                            "cat": cat,
                            "subcat": subcat_label,
                            "proxy": my_proxy[0]
                        }, errback=self.errb)


    def errb(self,failure):
        resp = failure.request
        url = resp.url
        resp = resp._meta
        try:
            subcat = resp["subcat"]
        except:
            subcat = resp["cat"]

        if "www.ebay.com" in url:
            if "/s/phone" not in url and "/p/" not in url:
                if "?" in url:
                    url = re.sub("\?.*","",url)
                    yield scrapy.Request(callback=self.expand_and_scrape,url=url,meta={
                        "proxy":my_proxy[0],
                        "cat" :resp["cat"],
                        "subcat" : subcat
                                                                                       })

    def parse(self,response):
        pass

    def scrape_data(self,response):
        cat = response.meta["cat"]

        try:
            subcat_label = response.meta["subcat"]
        except:
            subcat_label = cat

        main_soup = response.css("div#mainContent")[0]

        data = main_soup.css("li.sresult")
        if not data:
            data = main_soup.css("li.s-item")

        for current_item in data:
            try:
                item_div = current_item.css("a.img")
                if not item_div:
                    item_div = current_item.css("div.s-item__image a")
                request = {}

                item_url = item_div.css("::attr(href)").extract_first()

                request["SNR_ProductURL"] = response.urljoin(item_url)
                item_div = item_div.css("img[class*=img]")
                request["SNR_Title"] = item_div.css("::attr(alt)").extract_first()
                request["SNR_Description"] = "Visit site to see description"

                image_url = item_div.css("::attr(data-src)").extract_first()

                if not image_url:
                    image_url = item_div.css("::attr(src)").extract_first()

                item_id = current_item.css("::attr(listingid)").extract_first()

                if not item_id:
                    u = re.sub("\?.*","",request["SNR_ProductURL"])
                    item_id = u.split("/")[-1]

                request["SNR_ImageURL"] = response.urljoin(image_url)
                request["SNR_SKU"] = "EB" + item_id

                price_div = ""
                try:
                    price_div = current_item.css("ul.lvprices")[0]

                    after_div = price_div.css("li.lvprice").extract_first()


                    request["SNR_Price"] = float(patSearch("\$([\d,\.]+)",after_div).group(1).replace(",",""))
                except:
                    after_div = current_item.css("span.s-item__price").extract_first()
                    request["SNR_Price"] = float(patSearch("\$([\d,\.]+)", after_div).group(1).replace(",", ""))

                starts = current_item.css("div.star-ratings a[aria-label*=Rating]::attr(aria-label)").extract_first()

                if not starts:
                    starts = current_item.css("div.b-starrating")

                request["SNR_CustomerReviews"] = 0.0

                if starts:
                    try:
                        request["SNR_CustomerReviews"] = float(patSearch("\s*([\d\.]+)",starts).group(1))
                    except:
                        pass

                before_div = current_item.css("span.stk-thr").extract_first()

                request["SNR_PriceBefore"] = -1.0

                if before_div:
                    request["SNR_PriceBefore"] = float(patSearch("\$([\d,\.]+)",before_div).group(1).replace(",", ""))


                request["SNR_Category"] = cat
                request["SNR_Available"] = "Ebay"

                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"

                request["SNR_SubCategory"] = subcat_label
                request["SNR_Condition"] = "00"
                try:
                    try:
                        br = get_part_attr(response.url.lower())[1]["brand"][0]
                    except:
                        br = current_item.extract().lower()
                        br= patSearch("brand\s*:\s*([^<]+)",br).group(1)
                except:
                    br = ""

                if not br:
                    br="Unavailable"

                request["SNR_Brand"] = br

                yield scrapy.Request(url="https://backend.shopnroar.com/products/sendData",method="POST",
                                     headers={"Content-Type":"application/json"},
                                     body = json.dumps(request)
                                     )
            except Exception as e:
                pass

        current_page = 2
        url = response.url

        try:
            current_page = int(patSearch("_pgn=(\d+)",url).group(1))+1
            url = re.sub("_pgn=(\d+)","_pgn={0}".format(current_page))
        except:
            url+="&_pgn={0}".format(current_page)

        to_search = "_pgn={0}".format(current_page)

        if to_search in response.body:
            yield scrapy.Request(callback=self.expand_and_scrape,url=url,meta={
                        "proxy":my_proxy[0],
                        "cat" :cat,
                        "subcat" : subcat_label
                                                                                       })

        yield  {}

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(EbaySpider)

process.start()