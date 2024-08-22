import codecs
import json,requests
import urlparse
import re
from bs4 import BeautifulSoup
start_url = "https://www.buydig.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

from scrapetools import *

cat_map = {
    "photography".capitalize():"Cameras & Photo".capitalize(),
    "Television".capitalize():"TV, Audio & Surveillance".capitalize(),
    "Computers".capitalize():"Computers & Tablets".capitalize(),
    "Audio".capitalize():"TV, Audio & Surveillance".capitalize(),
    "Kitchen & Housewares".capitalize(): "Electronics".capitalize(),
    "Video".capitalize(): "Electronics".capitalize(),
    "Sports & Fitness".capitalize(): "Sporting Goods".capitalize(),
    "Cellular & Auto".capitalize(): "Vehicle Electronics & GPS".capitalize(),
    "Office Products".capitalize() : "Office".capitalize()
}

def extract_data(jsonData,walmartUrl):
    data_items = []

    while jsonData:
        single_item = jsonData.pop()
        try:
            if single_item[u"department"] in [u"Gifts & Registry", u"Photo Center"]:
                raise KeyError(u"Not Needed This Item")

            primary_offer = single_item.pop(u"primaryOffer")
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
            item_after_price = float(item_after_price)
            item_before_price = float(item_before_price)

            item_id = single_item.pop(u"productId")
            item_title = single_item.pop(u"title")
            item_url = urlparse.urljoin(
                walmartUrl, single_item.pop(u"productPageUrl"))
            item_image = single_item.pop(
                u"imageUrl").rsplit(u"?odnHeight=")[0]



            try:
                item_rating = single_item[u"customerRating"]
            except:
                item_rating = 0

            try:
                item_brand = single_item["brand"][0]
            except:
                item_brand = "No Brand"

            try:
                item_special_text = single_item["specialOfferText"]
            except:
                item_special_text = u""
            yield {
                "Item_Id": item_id,
                "Item_Title": item_title,
                "Item_Url": item_url,
                "Item_Image": item_image,
                "Item_BeforePrice": item_before_price,
                "Item_AfterPrice": item_after_price,
                "Item_Rating": item_rating,
                "Item_Brand": item_brand,
                "Item_Sp_Text":item_special_text
            }


        except KeyboardInterrupt as e:
            raise e
        except Exception, e:
            pass


def getRawData(url):
    while True:
        try:
            print "Getting Data From {0}".format(url)
            temp = requests.get(url,timeout=30,headers=headers)
            if temp.status_code == 200:
                return temp.text
        except KeyboardInterrupt as e:
            raise e
        except:
            print "Failed Getting Data From {0},Retrying.".format(url)

def saveJson(data,f="a.json"):
    with open(f,"w") as w:
        json.dump(data,w,indent=3)

def getSoup(data):
    return BeautifulSoup(data,"lxml")


def scrape_data(ur):

    urls = [ur]

    is_done = False
    while urls:
        ur = urls.pop()


        while True:
            soup = getSoup(getRawData(ur))
            results_div = soup.find("div", id="panResults")
            if results_div:
                break
            try:
                temp = soup.find("div", class_="owl-carousel").select("a[href*=category]")
            except:
                is_done = True
                break

            for i in temp:
                try:
                    urls.append(i["href"])
                except:
                    pass


            urls = list(set(urls))
            if not urls:
                is_done = True
                break
            ur = urls.pop()

        if is_done:
            break

        current_page = 1
        isNext = True

        while isNext:
            isNext = False
            items_div = results_div.select("div.results-container div.result-item")
            for item_div in items_div:
                image_div = item_div.select_one("div.item-image a img")
                item_id = image_div["alt"]
                item_image = image_div["src"]

                desc_div = item_div.find("div",class_="item-description")
                url_div = desc_div.a

                try:
                    item_price = float( item_div.select_one("div.item-price span span.price"
                                                    ).text.split("$")[-1].strip().replace(",",""))


                    item_url = url_div["href"]

                    try:
                        item_brand = url_div["data-brand"]
                    except:
                        item_brand = "No Brand"

                    item_title = url_div["data-name"]

                    try:
                        item_desc = next(
                            re.finditer("sep-line[^<]+</div>(.*)",str(desc_div))
                            ).group(1).strip()
                    except:
                        item_desc = "Visit site to see description"

                    if not item_desc:
                        item_desc = "Visit site to see description"

                    yield {
                    "SNR_SKU": "BG"+item_id,
                    "SNR_Title" : item_title,
                    "SNR_ProductURL" : item_url,
                    "SNR_ImageURL" : item_image,
                    "SNR_Price" : item_price,
                    "SNR_Description" : item_desc,
                    "SNR_Brand" : item_brand,
                    "SNR_PriceBefore" : -1,
                        "SNR_Condition" : "00",
                        "SNR_Available" : "BuyDig",
                        "SNR_UPC" : "00",
                        "SNR_ModelNo" : "00",
                        "SNR_CustomerReviews" : 0.0


                        }
                except:
                    pass




            next_page_div = results_div.select("div.page-numbers span#lblPaging a")

            if next_page_div:
                current_page += 1
                for url in next_page_div:
                    try:
                        temp = int(url.text.strip())

                        if current_page == temp:
                            isNext = True

                            ur = urlparse.urljoin(ur,url["href"])
                            soup = getSoup(getRawData(ur))
                            results_div = soup.find("div", id="panResults")
                            break
                    except:
                        pass



def get_data():
    start_raw = getRawData(start_url)
    soup = getSoup(start_raw).select("div#menuProducts div.menu-container div.menu-item")
    for cat_raw in soup:
        cat = cat_raw.a.h5.text.strip()
        subcat_divs = cat_raw.ul.select("li a")
        for i in subcat_divs:
            subcat_label = i.text.strip()
            subcat_url = i["href"] + "?lmt=100"

            subcat_data = scrape_data(subcat_url)

            for current_item in subcat_data:

                current_item["SNR_Category"] = map_data(cat_map,cat)
                current_item["SNR_SubCategory"] = subcat_label.capitalize()

                yield current_item


commit_data(get_data())