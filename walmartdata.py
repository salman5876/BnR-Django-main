
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

import re

from requests import Timeout
import urlparse

import codecs
import json,requests
import urlparse
import re
start_url = "https://www.walmart.com/all-departments"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

def appendLog(data):
    pass

visited = []



forbidden_words = ["Shop","Preorder","Shipping","Deal","Release","Card","Instawatch","Top","Saving","Brand"]
forb_cat = ["Home, Furniture & Appliances","Clothing, Shoes & Jewelry","Baby & Toddler","Food, Household & Pets","Photo & Personalized Shop"]
data_l = ["Card"]

cat_mapping = {
    "Patio & Garden".capitalize() : "Home & Garden".capitalize(),
    "Personal Care".capitalize():"Health, Fitness & Beauty".capitalize(),
    "Beauty".capitalize() : "Health, Fitness & Beauty".capitalize(),
    "Garden Center".capitalize() : "Home & Garden".capitalize(),
    "Oral Care".capitalize() : "Health, Fitness & Beauty".capitalize(),
    "Video Games".capitalize() :"Video Games & Consoles".strip().capitalize(),
    "Heating & Cooling".capitalize():"Appliances".capitalize(),
"Exercise Machines".capitalize(): "Health, Fitness & Beauty".capitalize(),
"Recreation".capitalize(): "Sporting Goods".capitalize(),
"Bikes & Ride-Ons".capitalize():"Sporting Goods".capitalize(),
"Cell Phones":"Cellphones & Accessories".strip().capitalize(),
"Strength and Weight Training".capitalize(): "Health, Fitness & Beauty".capitalize(),
"Computers".capitalize():"Computers & Tablets".strip().capitalize(),
"iPod & Portable Audio".capitalize(): "Computers & Tablets".strip().capitalize(),
"Exercise and Fitness".capitalize(): "Health, Fitness & Beauty".capitalize(),
"iPad & Tablets".capitalize(): "Computers & Tablets".strip().capitalize(),
"Auto Electronics".capitalize(): "Vehicle Electronics & GPS".strip().capitalize(),
"Health".capitalize(): "Health, Fitness & Beauty".capitalize(),
"Auto Electronics".capitalize():"Vehicle Electronics & GPS".strip().capitalize(),
"TV & Video".capitalize(): "Videos, Movies & TV".capitalize(),
"Toys".capitalize():"Toys, Kids and Baby".capitalize().capitalize(),
"Bath & Body".capitalize():"Health, Fitness & Beauty".capitalize()
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
                item_upc = single_item["upc"]
            except:
                item_upc = "00"

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
                "item_id": item_id,
                "item_title": item_title,
                "item_url": item_url,
                "item_image": item_image,
                "item_beforePrice": item_before_price,
                "item_afterPrice": item_after_price,
                "item_rating": item_rating,
                "item_brand": item_brand,
                "item_sp_text":item_special_text,
                "item_upc" : item_upc
            }


        except KeyboardInterrupt as e:
            raise e
        except Exception, e:
            pass


def getRawData(url):
    while True:
        try:
            print "Getting Data From {0}".format(url)
            temp = requests.get(url,timeout=60,headers=headers)
            if temp.status_code == 200:
                return temp.text

            else:
                raise IndexError("saas")
        except KeyboardInterrupt as e:
            raise e
        except:
            return "";
            # continue
            # print "Failed Getting Data From {0},Retrying.".format(url)

def saveJson(data,f="a.json"):
    with open(f,"w") as w:
        json.dump(data,w,indent=3)

def getJsonData(inputData,st=u"[",en=u"]"):
    jsonIndex = temp = 0


    for i in inputData:
        # print i
        if i == st:
            temp += 1
        elif i == en:
            temp -= 1
            if (temp == 0):
                return json.loads(inputData[:jsonIndex + 1])

        jsonIndex += 1


def save_to_file(d,f="was.html"):
    with codecs.open(f,"w","utf-8") as w:
        w.write(d)

def forb(data):
    global forbidden_words

    data = data.lower()

    for i in forbidden_words:
        i = i.lower()

        if i in data:
            return False

    return True

def get_cat_sub():
    start_str = '"departments":'
    while True:
        try:
            data_raw = getRawData(start_url)
            # print data_raw
            start_index = data_raw.index(start_str)+len(start_str)
            end_index = data_raw.index("</script>",start_index)
            data_raw = data_raw[start_index:end_index]
            # print(data_raw)
            save_to_file(data_raw)

            try:
                data_cat = getJsonData(data_raw)

            except Exception as e:
                raise e



            data = {}
            for i in data_cat:
                try:
                    if i["name"] not in forb_cat:
                        saveJson(i,"b.json")
                        current_data = i["departments"]
                        for cat in current_data:
                            temp = cat["department"]["title"].replace("Shop ","").strip()

                            try:
                                if cat["categories"] and forb(temp):
                                    current_cat = temp
                                    temp = {}
                                    sub_cats = cat["categories"]
                                    for sub_cat in sub_cats:
                                        sub_cat = sub_cat["category"]
                                        sub_cat_label = sub_cat["title"]
                                        sub_cat_url = urlparse.urljoin(start_url,
                                                                       sub_cat["clickThrough"]["value"])
                                        if sub_cat_url.startswith("https://www.walmart.com/browse") and forb(sub_cat_label):
                                            temp[sub_cat_label] = sub_cat_url
                                    if temp:
                                        data[current_cat] = temp
                            except KeyError:
                                continue

                except Exception as e:
                    raise e


            break
        except KeyboardInterrupt as e:
            raise e
        except ValueError as e:
            raise e

        except Exception as e:
            raise e

    return data


def getNextUrl(data):
    next_pat = '"next":{"url":'
    l = len('"next":')
    try:
        next_index = data.index(next_pat)+l
        l = data[next_index:]
        a = getJsonData(data[next_index:],u"{",u"}")
        if a:
            return a

        raise ValueError()

    except ValueError as e:
        return False

def getEachData(data_raw):
    for sub_cat,data_url in data_raw.iteritems():
        if data_url not in visited:
            url_raw = getRawData(data_url)
            next_url_rel = True
            try:
                current_page=1
                while next_url_rel:
                    st_index = url_raw.index("<script")
                    end_index = url_raw.rindex("</script>")
                    url_raw = url_raw[st_index:end_index]
                    next_url_rel = getNextUrl(url_raw)

                    if next_url_rel:
                        next_url = "{0}?{1}".format(data_url,next_url_rel["url"])

                    st_index = url_raw.index('items":[{') + len('items":')
                    url_raw = url_raw[st_index:]
                    data_items = getJsonData(url_raw)
                    saveJson(data_items)
                    d = extract_data(data_items,data_url)
                    while True:
                        try:
                            current_item = next(d)
                            current_item["item_subcat"] = sub_cat.strip().capitalize()
                            yield current_item
                        except StopIteration:
                            break;


                    if next_url_rel:
                        current_page += 1
                        if "page={0}".format(current_page) in next_url:
                            url_raw = getRawData(next_url)
                        else:
                            next_url_rel = False

            except KeyboardInterrupt as e:
                raise e

            except ValueError as e:
                raise e

            except Exception as e:
                pass

            appendLog(data_url)

def getData():
    cats = get_cat_sub()
    for cat,data_raw in cats.iteritems():
        print cat,data_raw
        current_cat_data = getEachData(data_raw)

        while True:
            try:

                cat = cat.strip().capitalize()
                current_item = next(current_cat_data)
                try:
                    temp = cat_mapping[cat]
                    cat = temp
                except:
                    pass
                current_item["item_cat"] = cat
                yield current_item
            except StopIteration:
                break

class WalmartData():
    def __init__(self):
        pass
    def commit_data(self):
        data = getData()

        try:
            request = {}

            request["SNR_Available"] = "Walmart"
            request["SNR_Description"] = "Visit site to see description"
            request["SNR_ModelNo"] = "00"
            request["SNR_Condition"] = "00"
            c = 0
            while True:
                try:
                    item = next(data)
                except StopIteration as e:
                    raise e
                except:
                    continue

                request["SNR_SKU"] = "WM" + str(item['item_id'])
                request["SNR_Title"] = item['item_title']
                request["SNR_Category"] = item['item_cat']
                request["SNR_SubCategory"] = item['item_subcat']
                request["SNR_PriceBefore"] = item["item_beforePrice"]
                request["SNR_Price"] = item["item_afterPrice"]
                request["SNR_ProductURL"] = item['item_url']
                request["SNR_ImageURL"] = item['item_image']
                request["SNR_Brand"] = item["item_brand"]
                request["SNR_UPC"] = item["item_upc"]
                request["SNR_CustomerReviews"] = float(item["item_rating"])
                yield request


        except StopIteration:
            pass



from scrapetools import  commit_data

commit_data(WalmartData().commit_data())