import codecs
import os, django
import json
from HTMLParser import HTMLParser

import math

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import AllProducts

from products.serializers import AllProducts_Serializer

import re
hparse = HTMLParser()
from requests import Timeout
import urlparse
start_url = "https://scache.vzw.com/ui-one-digital/global-header/prospect.globalheader.json"
import requests
from bs4 import BeautifulSoup
ver_home = "https://www.verizonwireless.com/"
def appendLog(data):
    with codecs.open("verLog.txt","a","utf-8") as w:
        w.write(data+"\n")

visited = []

try:
    with codecs.open("verLog.txt",encoding="utf-8") as w:
        visited = list(set(w.read().split("\n")))

except IOError:
    visited = []


myua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
headers = {
    'User-Agent': myua
}


cat = {
    "Computers & Tablets".capitalize(): ("https://api.t-mobile.com/raptor/v1/search-promote/?type=browse&ps=internet-device&sort=if&count=72&page={0}","Computers & Tablets".capitalize()
                                         ,"https://www.t-mobile.com/internet-device/{0}"),
    "Cellphones & Accessories".capitalize() : ("https://api.t-mobile.com/raptor/v1/search-promote/?type=browse&pt=accessory&sort=pr&count=72&page={0}","Accessories".capitalize(),
                                               "https://www.t-mobile.com/accessory/{0}"),
    "Cellphones & Accessories".capitalize() : ("https://api.t-mobile.com/raptor/v1/search-promote/?type=browse&ps=handset&sort=if&page={0}&count=72","Cell Phones & Smartphones".capitalize(),
                                               "https://www.t-mobile.com/cell-phone/{0}",)

}

def getRaw(ur,h=False,data={},js=False,post=False):
    if not h:
        h = headers

    req = requests.get
    if post:
        req = requests.post


    while True:
        try:

            data = req(ur,data=data,headers=h,timeout=30)

            if data.status_code == 200:
                if js:
                    return data.json()
                else:
                    return data.text
            else:
                raise KeyboardInterrupt

        except KeyboardInterrupt as e:
            raise e
        except Timeout:
            pass




def get_token():
    h = {
        "Content-Type" : "application/x-www-form-urlencoded",
        'User-Agent': myua
    }

    b = {
        "grant_type": "client_credentials",
        "client_id": "hV6lfg3EBAiVX5EZjbpexLoLhGhuGiWR"
    }

    ur = "https://api.t-mobile.com/oauth/v1/access"

    data = getRaw(ur,h=h,data=b,js=True,post=True)
    return data["access_token"]

def get_data():
    token = get_token()
    headers_token = {
        "Authorization" : "Bearer %s" % token,
        "User-Agent" : myua
    }
    for current_cat,cat_data in cat.iteritems():
        cat_url,subcat_label,map_url = cat_data
        is_next = True
        current_page = 1
        current_url = cat_url.format(current_page)
        current_data = getRaw(current_url,h=headers_token,js=True)
        with open("was.json","w") as w:
            json.dump(current_data,w,indent=3)

        total_pages = int(math.ceil( float(current_data["totals"]["products"])/72))
        while is_next:
            is_next = False
            data_array = []


            data = current_data["values"]["products"]

            for i in data:
                try:
                    if i["availability"] != "y":
                        continue

                    request = {
                        "SNR_Available": "T-Mobile",
                        "SNR_PriceBefore": -1.0,
                        "SNR_UPC": "00",
                        "SNR_Description": "Visit site to see description",
                        "SNR_ModelNo": "00"
                    }

                    try:
                        request["SNR_Condition"] = i["conditions"]
                    except:
                        request["SNR_Condition"] = "00"

                    try:
                        request["SNR_CustomerReviews"] =  float( "%0.2f" % float(i['averageStarRating']) )
                    except:
                        request["SNR_CustomerReviews"] = 0.0

                    try:
                        request["SNR_Brand"] = i['productManufacturer']
                    except:
                        request["SNR_Brand"] = "No Brand"

                    request["SNR_Title"] = i['productName']

                    request["SNR_Price"] = float(i['salePriceSku'].split("|",1)[0])

                    request["SNR_SKU"] = "TM" + i["skuCode"].split("|",1)[0]

                    request["SNR_ImageURL"] = "https://www.t-mobile.com"+i["thumbNail"].split("|",1)[0]

                    temp = "-".join(re.findall("\w+",i['productName'])).lower()
                    temp = map_url.format(temp)

                    request["SNR_ProductURL"] = temp
                    request["SNR_Category"] = current_cat
                    request["SNR_SubCategory"] = subcat_label
                    yield request
                except:
                    pass


            if current_page<total_pages:
                current_page += 1
                current_url = cat_url.format(current_page)
                is_next = True
                current_data = getRaw(current_url,h=headers_token,js=True)


class TmobileData:
    def __init__(self):
        pass
    def commit_data(self):
        data = get_data()
        for request in data:
                request['SNR_CustomerReviews'] = float("%0.2f" % request['SNR_CustomerReviews'])
                request['SNR_Price'] = float("%0.2f" % request['SNR_Price'])
                serializer = AllProducts_Serializer(data=request)

                if serializer.is_valid():
                    print("---")
                    serializer.save()
                else:
                    print serializer.errors
                    print("bad json")


TmobileData().commit_data()
