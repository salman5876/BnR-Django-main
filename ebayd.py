
import os, django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import AllProducts

from products.serializers import AllProducts_Serializer

from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

timeout = 30


class EbayData():
    def get_cat_urls(self,homeurl="https://www.ebay.com/"):
        while True:
            try:
                ebay_front_raw = requests.get(homeurl,timeout=timeout).text
                soup = BeautifulSoup(ebay_front_raw, 'lxml')
                print 'Getting Data From {0}'.format(homeurl)
                topnav = soup.select("div.topnav table tbody tr td.cat a.rt")
                if not topnav:
                    raise Exception()

                break
            except KeyboardInterrupt as e:
                raise e
            except:
                print "Error Getting Data From {0}, Retrying.".format(homeurl)




        links = []

        link_exclude = ["Daily Deals","More..."]

        for i in topnav:
            cat = i.text
            if cat not in link_exclude:
                url = i["href"]

                links.append({"cat":cat,"url":url})



        return links


    def get_subcat_urls(self,cat_url):
        def ref_url(u):
            try:
                i = u.index("?")
                u = u[:i]
            except:
                pass

            return u

        def ref_cat(url, f):
            try:
                url = url[:url.index(f)]
            except:
                pass

            if url.find("Free Shipping") >= 0 or url.find("All ") >= 0 or url.find(" All") >= 0:
                raise Exception()
            return url

        while True:
            try:
                ebay_cat_raw = requests.get(cat_url, timeout=timeout, headers=headers).text
                soup = BeautifulSoup(ebay_cat_raw, 'lxml')
                print "Getting Data From {0}".format(cat_url)
                # subcats_node = soup.select("div .nav-module li[data-node-id=1] ul.navigation-list a.see-links")
                temp = soup.select("div .nav-module li[data-node-id=1] ul.navigation-list")

                shop_sep = u"\xa0"
                links = []

                datak = {}
                for i in temp:
                    k = i
                    i = i.select_one("a.see-links")
                    url = i["href"]


                    cat = i.text.split(shop_sep, 1)[-1]

                    links.append({"cat": cat, "url": url})

                    k = k.find_all("a")[1:]

                    i = []
                    for j in k:

                        try:
                            if (j["href"].find("ebay.com/rpp") < 0 and j["href"] != "#"):
                                i.append({"url": ref_url(j["href"]), "cat": ref_cat(j.span.text, cat)})
                        except:
                            pass

                    datak[cat] = i

                break;
            except KeyboardInterrupt as e:
                raise e

            except Exception as e:
                print "Error Getting Data From {0}, Retrying.".format(cat_url)

        return datak


    def scrape_data(self,sc_url):
        while True:
            try:
                ebay_page_raw = requests.get(sc_url,timeout=timeout,headers=headers).text
                soup = BeautifulSoup(ebay_page_raw, 'lxml')
                print "Getting Data From {0}".format(sc_url)
                main_page = soup.find("div", {"id": "mainContent"})
                items_data = main_page.find_all("li", {"class": "sresult"})
                pagen = main_page.select_one("table#Pagination tr td.pages").find_all("a")

                if not (items_data and pagen):
                    raise Exception()
                break;
            except KeyboardInterrupt as e:
                raise e
            except:
                print "Error Getting Data From {0}, Retrying.".format(sc_url)









        items = []

        yield pagen


        for item_single_raw in items_data:
            item_id = item_single_raw.attrs["listingid"]

            url_image = item_single_raw.select_one("div.lvpicinner a.img")

            item_url = url_image.attrs["href"]

            image_tag = url_image.img

            try:

                item_image = image_tag.attrs["imgurl"]
            except:
                item_image = image_tag.attrs["src"]

            item_title = image_tag.attrs["alt"]

            item_cond = "UnAvailable"


            try:
                item_cond = item_single_raw.find_all("div",class_="lvsubtitle")[-1].text.strip()
            except:
                pass


            item_reviews = 0
            item_rating = 0

            try:
                rating_div =  str(item_single_raw.select_one("div.star-ratings"))

                try:
                    item_rating = float( next( re.finditer(r'aria-label="Rating: (\S+) out of 5,',rating_div) ).group(1) )
                except TypeError as e:
                    raise e
                except:
                    pass

                try:
                    item_reviews = int( next(  re.finditer(r'aria-label="(\d+) product ratings',rating_div) ).group(1) )
                except TypeError as e:
                    raise e
                except:
                    pass

            except:
                pass

            #lvprice prc
            price_div = item_single_raw.select_one("ul.lvprices li.lvprice")

            try:
                item_before_price = float(item_single_raw.find("span",class_="stk-thr").text[1:].replace(",",""))
            except:
                item_before_price = -1

            item_after_div = price_div.span
            item_after_price = -2

            if not item_after_div.span:
                item_after_price = str(item_after_div)
                item_after_price = item_after_price[: item_after_price.find("<span>to</span>") ].rstrip()

                a = next( re.finditer(r"\$(.+)</s", item_after_price)).group(1)

                try:
                    item_after_price = float(a.replace(",",""));
                except:
                    continue


            else:
                try:
                    item_after_price = str(item_after_div.text.strip()[1:])
                    temp = item_after_price.find(" to")
                    if temp >=0:
                        item_after_price = item_after_price[:temp]
                    if item_after_price.find("Trending at")>0:
                        item_after_price = item_after_price.split("Trending at")[0].strip()

                    item_after_price = float(item_after_price)


                except Exception as e:
                    continue

            next_url = ""

            singleItem = {
                "item_id":item_id,
                "item_title": item_title,
                "item_url": item_url,
                "item_image":item_image,
                "item_cond":item_cond,
                "item_rating": item_rating,
                "item_before_price": item_before_price,
                "item_after_price": item_after_price
            }


            """items.append( singleItem )"""
            yield singleItem

        #return (items,scpage,next_url);

    def commit_data(self):
        data = self.get_data()

        try:
            request = {}
            request["SNR_ModelNo"] = "00"
            request["SNR_UPC"] = "00"
            request["SNR_Brand"] = "No Brand"
            request["SNR_Available"] = "Ebay"
            request["SNR_Description"] = "Visit site to see description"

            while True:
                try:
                    item = next(data)
                except:
                    continue

                request["SNR_SKU"] = "EB" + str(item['item_id'])
                request["SNR_Title"] = item['item_title']
                request["SNR_Category"] = item['item_cat']
                request["SNR_SubCategory"] = item['item_subcat']
                request["SNR_Condition"] = item['item_cond']
                request["SNR_PriceBefore"] = item['item_before_price']
                request["SNR_Price"] = item['item_after_price']
                request["SNR_CustomerReviews"] = item['item_rating']
                request["SNR_ProductURL"] = item['item_url']
                request["SNR_ImageURL"] = item['item_image']

                serializer = AllProducts_Serializer(data=request)
                if serializer.is_valid():
                    print("---")
                    serializer.save()
                else:
                    print("bad json")
                    with open("log.txt","a") as w:
                        try:
                            t = "{0}\n".format(json.dumps(item))
                            w.write(t)

                        except:
                            pass
        except StopIteration:
            pass

    def get_data(self):
        starturl = "https://www.ebay.com/"
        top_cats = self.get_cat_urls()


        for i in top_cats:
            top_cat_url = i["url"]
            top_cat_label = i["cat"]
            subcat_list = self.get_subcat_urls(top_cat_url)
            for subcat,subsubcat_list in subcat_list.iteritems():

                subcat_label = subcat

                for subsubcat in subsubcat_list:
                    subsubcat_url = subsubcat["url"]+"?_ipg=200&rt=nc&LH_BIN=1&_dmd=1&_pgn={0}&_skc={1}"
                    subsubcat_label = subsubcat["cat"]

                    current_url = subsubcat_url
                    current_page = 1

                    items = []

                    isnext = True

                    while isnext:
                        current_url = subsubcat_url.format(current_page, (current_page-1) * 200)
                        """
                        temp_items,current_page,current_url = scrape_data(current_url,current_page)
                        """
                        temp_items = self.scrape_data(current_url)
                        #items.extend(temp_items)
                        pages = next(temp_items)

                        while True:
                            try:
                                currentItem = next(temp_items)
                                currentItem["item_cat"] = subcat_label
                                currentItem["item_subcat"] = subsubcat_label
                                yield currentItem

                            except StopIteration:
                                break

                        isnext = False

                        current_page+=1

                        if current_page<50:
                            for page in pages:
                                try:
                                    str(page).index("pgn={0}".format(current_page))
                                    isnext = True
                                    break
                                except:
                                    pass

                #return items



EbayData().commit_data()