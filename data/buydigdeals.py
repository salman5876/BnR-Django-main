import codecs
import os, django
import json
from HTMLParser import HTMLParser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import AllProducts

from products.serializers import AllProducts_Serializer

import re
hparse = HTMLParser()
from requests import Timeout
import urlparse
start_url = "https://www.newegg.com/"
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



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}



def getRawUrlData(url,json=False):
    while True:
        try:
            print "Getting Data From {0}.".format(url)
            temp = requests.get(url,timeout=30,headers=headers)
            if temp.status_code == 200:
                return temp.json() if json else temp.text
            else:
                raise KeyboardInterrupt("sasa")

        except KeyboardInterrupt as e:
            raise e
        except:
            print "Error Getting Data From {0}., Retrying".format(url)


deals_url = "https://thereal.buydig.com/hotlistSnippet/responsive.phtml?id=7"
def getDeals():
    data = getRawUrlData(deals_url)
    data = data[data.index("(")+1:]
    data = data[:data.rindex("\")")]
    t = "</style>"
    data = data[data.index(t)+len(t):]
    t = data
    while True:
        try:
            t.index('\\"')
            t = t.replace('\\"','"')
        except:
            break
    #data = data.replace('\"','"')
    soup = BeautifulSoup("<p><waryam>"+t+"</waryam></p>","lxml").select("waryam div")

    all_items = []
    for current_item in soup:
        try:
            request = {
                "SNR_Available": "BuyDig",
                "SNR_Category" : "Not Available"
            }
            heading_div = current_item.find("p",class_="heading").find("a")
            image_div = current_item.select_one("a img.img-responsive")

            request["SNR_ProductURL"] = item_url =  heading_div["href"]
            request["SNR_SKU"] = "BG" + item_url[item_url.index("sku=")+len("sku="):]
            request["SNR_Title"] = heading_div.text.strip()
            request["SNR_ImageURL"] =  image_div["src"]

            raw = str(current_item)
            raw = raw[raw.index("List Price:"):]
            raw = raw[raw.index("$")+1:]
            try:
                temp = next(re.finditer("^([\d\.\,]+)",raw)).group(1).replace(",","")
                request["SNR_PriceBefore"] = float(temp)
            except:
                request["SNR_PriceBefore"] = -1


            raw = raw[raw.index("Our Price"):]
            raw = raw[raw.index("$")+1:]
            try:
                temp =  float( next(re.finditer("^([\d\.\,]+)",raw)).group(1).replace(",","") )
                request["SNR_PriceAfter"] = temp
            except:
                continue

            yield request
        except Exception as e:
            print e.message


