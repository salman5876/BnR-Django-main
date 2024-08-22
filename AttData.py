
import os, django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from HTMLParser import HTMLParser
from products.models import AllProducts

from products.serializers import AllProducts_Serializer
hparse = HTMLParser()
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
start_url = "https://www.att.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

def appendLog(data):
    with codecs.open("attLog.txt","a","utf-8") as w:
        w.write(data+"\n")

visited = []

try:
    with codecs.open("attLog.txt",encoding="utf-8") as w:
        visited = w.read().split("\n")
except IOError:
    visited = []

forbidden_words = ["shop","about"]
data_l = ["Card"]

valid_cat = ["Wireless","Accessories"]
cat = "Cellphones & Accessories".capitalize()

def getRawData(url):
    while True:
        try:
            print "Getting Data From {0}".format(url)
            temp = requests.get(url,timeout=60,headers=headers)
            if temp.status_code == 200:
                return temp.text
            else:
                raise KeyboardInterrupt("saas")
        except KeyboardInterrupt as e:
            raise e
        except:
            print "Failed Getting Data From {0},Retrying.".format(url)

def saveJson(data,f="a.json"):
    with open(f,"w") as w:
        json.dump(data,w,indent=3)


def save_to_file(d,f="was.html"):
    with codecs.open(f,"w",encoding="utf-8") as w:
        w.write(d)

def forb(data):
    global forbidden_words


    data = data.lower()

    for i in forbidden_words:
        i = i.lower()

        if i in data:
            return False



    return True



def scrape_data(ur,su,mycat):
    top_url = ur

    ur_raw = getRawData(top_url)
    if "Neworking & Connectivity".capitalize() == su:
        tax = "EQUIPMENT"
        cat = "equipment"
    else:
        soup = [i for i in BeautifulSoup(ur_raw,"lxml").select("a[name=taxoCategory]") if i["data-tokencontent"].capitalize() == su]

        ur = ur[:-4]
        cat = ur = ur[ur.rindex("/") + 1:].lower().replace(".","")
        if soup:
            tax = soup[0]["value"]
        else:
            tax = cat.upper()


    data_url = "https://www.att.com/shop/wireless/accessories/{0}.accessoryListGridView.html?taxoCategory={1}"
    data_url += "&sortByProperties=bestSelling&showMoreListSize=100000&offset=1&offsetValue=1"

    data_url = data_url.format(cat,tax)

    data = getRawData(data_url)
    soup = BeautifulSoup(data,"lxml").select("div.listViewItem div.listGridAcc-item div.listGridAcc-titleImgPrice")
    total_items = getitems(soup,su,mycat,data_url)
    return total_items

def getitems(soup,su,cat,data_url="https://www.att.com/"):
    total_items = []
    if soup:
        all_items = total_items
        for current_item in soup:
            current_data_item = {}

            title_div = current_item.select_one("div.listGridAcc-title h3 a")

            if not title_div:
                title_div = current_item.select_one("div.listGridAcc-titleWithBanner h3 a")
            try:
                temp = urlparse.urljoin(data_url, title_div["href"]).split("#sku=sku")
            except:
                raise Exception()

            try:
                current_data_item["SNR_ProductURL"] = temp[0]
                current_data_item["SNR_SKU"] = "ATT" + temp[-1]
                current_data_item["SNR_Title"] = title_div.text.strip()
            except:
                continue

            temp = current_item.find("img", id="image-sku%s" % temp[-1])
            try:
                current_data_item["SNR_ImageURL"] = temp["src"]
            except:
                try:
                    current_data_item["SNR_ImageURL"] = current_item.find("div", class_="listGridAcc-image").find("img")["src"]
                except:
                    continue

            try:
                rating = float(current_item.select_one("span.user-rating-review").text)
            except:
                rating = 0.0

            try:
                price = float(current_item.select_one(
                    "div.listGridAcc-priceInfo div.listGridAcc-price").text.strip().replace("$", "").replace(",","")
                              )
            except:
                continue

            current_data_item["SNR_CustomerReviews"] = rating
            current_data_item["SNR_Price"] = price

            # default

            current_data_item["SNR_Available"] = "AT&T"
            current_data_item["SNR_Description"] = "Visit site to see description"
            current_data_item["SNR_ModelNo"] = "00"
            current_data_item["SNR_Condition"] = "00"
            current_data_item["SNR_UPC"] = "00"
            current_data_item["SNR_Condition"] = "00"
            current_data_item["SNR_PriceBefore"] = -1.0
            current_data_item["SNR_Brand"] = "00"
            current_data_item["SNR_Category"] = cat
            current_data_item["SNR_SubCategory"] = su

            all_items.append(current_data_item)
    return total_items
def get_cats():
    data_raw = getRawData(start_url)

    acc_raw = BeautifulSoup(data_raw,"lxml").select_one('ul[aria-label=Accessories]').select("a[data-analytics-info]")
    acc_raw = [json.loads(i["data-analytics-info"].replace("'",'"')) for i in acc_raw]
    acc_raw = [i for i in acc_raw if forb(i['events.linkName'])]
    acc_raw = [i for i in acc_raw if "m.att.com" not in i['events.linkDestinationUrl']]
    all_data = []

    for i in acc_raw:
        try:
            i['events.linkDestinationUrl'].index("/shop/")
            if i['events.linkName'] == 'Internet equipment'.capitalize():
                all_data.append(
                    ("Neworking & Connectivity".capitalize(),"Computers & Tablets".capitalize(),i['events.linkDestinationUrl'])
                )
            else:
                all_data.append( (i['events.linkName'].capitalize(),cat,i['events.linkDestinationUrl']))
        except:
            pass

    return list(set(all_data))


def get_data():
    yield cellscrape()
    for i in get_cats():
        subcat,cat,ur = i
        yield scrape_data(ur,subcat,cat)



def cellscrape():
    data_raw = getRawData("https://www.att.com/shop/wireless/devices/cellphones.deviceListView.flowtype-NEW.deviceGeoTarget-US.deviceGroupType-Cellphone.paymentType-postpaid.packageType-undefined.json?showMoreListSize=100000").strip()
    data =  json.loads(data_raw)["devices"]

    cat = "Cellphones & Accessories".capitalize()
    subcat = "Cell Phones & Smartphones".capitalize()
    data_url = "https://www.att.com/shop/wireless/devices/smartphones.html"
    all_items = []
    while data:
        try:
            item = data.pop()
            htmlbody = hparse.unescape(item["usingTheBody"])
            product_json = item["product"]
            try:
                temp = int(next(re.finditer("<span property=.ratingValue.>(.)", htmlbody)).group(1))
                rating = float( "{0}{1}".format(temp,product_json['aggregateRating']['ratingValue']))
            except:
                rating = 0.0

            price = item["itemprice"]



            current_data_item = {}
            current_data_item["SNR_Available"] = "AT&T"
            current_data_item["SNR_Description"] = "Visit site to see description"

            try:
                temp = hparse.unescape(product_json["description"])
                current_data_item["SNR_Description"] = temp
            except:
                pass



            current_data_item["SNR_ModelNo"] = "00"

            try:
                temp = product_json["model"]
                current_data_item["SNR_ModelNo"] = temp
            except:
                pass


            current_data_item["SNR_Condition"] = "00"

            try:
                temp = product_json["itemCondition"]
                current_data_item["SNR_Condition"] = temp
            except:
                pass

            current_data_item["SNR_UPC"] = "00"

            current_data_item["SNR_PriceBefore"] = -1.0


            current_data_item["SNR_Brand"] = "00"

            try:
                temp = product_json["brand"]
                current_data_item["SNR_Brand"] = temp
            except:
                pass


            current_data_item["SNR_Category"] = cat
            current_data_item["SNR_SubCategory"] = subcat

            current_data_item["SNR_ProductURL"] = urlparse.urljoin(data_url,product_json["url"])

            current_data_item["SNR_SKU"] = "ATT" + product_json["sku"].replace("sku","")

            current_data_item["SNR_Title"] = product_json["name"]

            current_data_item["SNR_ImageURL"] = product_json["image"]
            current_data_item["SNR_CustomerReviews"] = rating
            current_data_item["SNR_Price"] = price
            all_items.append(current_data_item)
        except Exception as e:
            pass
    return all_items



class AttData():
    def __init__(self):
        pass
    def commit_data(self):
        data = get_data()
        c=0

        for dataarray in data:
            for request in dataarray:
                serializer = AllProducts_Serializer(data=request)
                c += 1
                if c == 1000:
                    c = 0
                    os.system("clear")

                if serializer.is_valid():
                    print("---")
                    serializer.save()
                else:
                    print("bad json")


AttData().commit_data()