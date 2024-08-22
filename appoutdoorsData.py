import codecs
import os, django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import AllProducts

from products.serializers import AllProducts_Serializer

import re

from requests import Timeout
import urlparse
start_url = "http://www.appoutdoors.com/"
import requests
from bs4 import BeautifulSoup


def appendLog(data):
    with codecs.open("appoutLog.txt","a","utf-8") as w:
        w.write(data+"\n")

visited = []

try:
    with codecs.open("appoutLog.txt",encoding="utf-8") as w:
        visited = list(set(w.read().split("\n")))

except IOError:
    visited = []



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}


cat_mapping = {
    "Footwear".capitalize():"Shoes".capitalize(),
    "Mens".capitalize(): "Men",
    "Womens".capitalize(): "Women",
     "Kids": "Kids & Baby".capitalize(),
    "Camp/Hike".capitalize():"Sporting Goods".capitalize(),
    "Packs/Bags".capitalize(): "Handbags & Purses".capitalize(),
    "Climb".capitalize():"Sporting Goods".capitalize(),
    "Snow".capitalize(): "Sporting Goods".capitalize(),
    "Other".capitalize() : "Life-Style".capitalize(),
    "Auto".capitalize() : "Vehicle Electronics & GPS".capitalize()
}


subcat_mapping = {
"Packs/Bags".capitalize():"Backpacks & Bookbags".capitalize(),
"Other".capitalize() : "Life-Style".capitalize()
}

def getRawUrlData(url):
    while True:
        try:
            print "Getting Data From {0}.".format(url)
            temp = requests.get(url,timeout=30,headers=headers)
            if temp.status_code == 200:
                return temp.text
            else:
                return KeyboardInterrupt("sasa")

        except KeyboardInterrupt as e:
            raise e
        except:
            print "Error Getting Data From {0}., Retrying".format(url)


def getSoup(data):
    return BeautifulSoup(data,"lxml")

def get_cat_sub():
    soup = getSoup(
        getRawUrlData(start_url)
    ).select("ul.respnav li a")



    cat_data = []
    for i in soup:
        cat = i.text.strip()
        subcat = cat

        try:

            try:
                temp = subcat_mapping[cat]
                subcat = temp
            except KeyError:
                pass

            cat = cat_mapping[cat]

            cat_url = urlparse.urljoin(start_url,i["href"])

            cat_data.append( (cat,subcat,cat_url) )
        except KeyError:
            pass


    return cat_data





def scrape_data(s_url):
    is_next = True
    current_url = s_url
    currentp = 1
    while is_next:
        is_next = False
        currentp += 1

        soup = getSoup( getRawUrlData(current_url) )
        top_url = current_url
        try:

            try:
                next_page_divs = soup.select("ul.cd-pagination li a")

                for i in next_page_divs:
                    try:
                        temp = int(i.text.strip())
                        if temp == currentp:
                            current_url = urlparse.urljoin(current_url,i["href"])
                            is_next = True
                            break
                    except:
                        pass
            except:
                pass


            items_soup = soup.find_all("div",class_="product_grid_list-content")

            if not items_soup:
                raise Exception()

        except:
            break


        for current_item_div in items_soup:
            # Default Attribs
            current_data_item = {
                "SNR_Available" : "AppOutDoors",
                "SNR_Description" : "Visit site to see description",
                "SNR_ModelNo" : "00",
                "SNR_Condition" : "00",
                "SNR_UPC" : "00",
                "SNR_CustomerReviews": 0.0
            }

            image_div = current_item_div.select_one("div.imgframe").find("img")



            try:
                price = current_item_div.find(
                    "p",class_="grid_page_price_reduced").text.replace("$","").replace(",","")
                current_data_item["SNR_Price"] = price
            except:
                continue


            try:
                current_data_item["SNR_ImageURL"] = image_div["src"]
                item_id = current_item_div.find("span",class_="uniqueId").text.strip()
                current_data_item["SNR_SKU"] = "AOD"+item_id
                title_data = [i.strip() for i in image_div["alt"].strip().split(item_id)]
                current_data_item["SNR_ProductURL"] = urlparse.urljoin(current_url,current_item_div.a["href"])

                current_data_item["SNR_Brand"] = "No Brand"

                try:
                    brand_data = title_data[-1][1:-1]
                    current_data_item["SNR_Brand"] = brand_data
                except:
                    pass

                current_data_item["SNR_Title"] = title_data[0]

                current_data_item["SNR_PriceBefore"] = -1

                try:
                    temp = current_item_div.select_one("p.grid_page_price_full s").text.strip().replace("$","").replace(",","")
                    current_data_item["SNR_PriceBefore"] = float(temp)
                except:
                    pass



            except:
                continue

            yield current_data_item


def get_data():
    all_cats = get_cat_sub()
    for cat,subcat,cat_url in all_cats:
        if cat not in visited:
            data = scrape_data(cat_url)

            for i in data:
                i["SNR_Category"] = cat
                i["SNR_SubCategory"] = subcat
                yield i

            appendLog(cat)


class AppOutDoors():
    def __init__(self):
        pass
    def commit_data(self):
        data = get_data()
        for request in data:
                serializer = AllProducts_Serializer(data=request)

                if serializer.is_valid():
                    print("---")
                    serializer.save()
                else:
                    print("bad json")


AppOutDoors().commit_data()