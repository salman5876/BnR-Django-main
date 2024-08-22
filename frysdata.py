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
start_url = "https://www.frys.com/"
import requests
from bs4 import BeautifulSoup


def appendLog(data):
    with codecs.open("frysLog.txt","a","utf-8") as w:
        w.write(data+"\n")

visited = []

try:
    with codecs.open("frysLog.txt",encoding="utf-8") as w:
        visited = list(set(w.read().split("\n")))

    with codecs.open("frysLog.txt","w","utf-8") as w:
        w.write("\n".join(visited)+"\n")
except IOError:
    visited = []



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}


cat_mapping = {
    "PC Computers".strip().capitalize():"Computers & Tablets".strip().capitalize(),
    "Apple".strip().capitalize():"Computers & Tablets".strip().capitalize(),
    "Laptops".strip().capitalize():"Computers & Tablets".strip().capitalize(),
    "Networking".strip().capitalize():"Computers & Tablets".strip().capitalize(),
    "PC Components".strip().capitalize():"Computers & Tablets".strip().capitalize(),
    "Electronic Components".strip().capitalize(): "Electronics".strip().capitalize(),
    "Electronics Components".strip().capitalize(): "Electronics".strip().capitalize(),
    "Cell Phones".strip().capitalize(): "Cellphones & Accessories".strip().capitalize(),
    "Audio".strip().capitalize(): "TV, Audio & Surveillance".strip().capitalize(),
    "TV & Video".strip().capitalize(): "Videos, Movies & TV".strip().capitalize(),
    "Cameras, Camcorders & Optics".strip().capitalize(): "Cameras & Photo".strip().capitalize(),
    "Car Electronics".strip().capitalize(): "Vehicle Electronics & GPS".strip().capitalize(),
    "Software & Books".strip().capitalize(): "Software".strip().capitalize(),
     "Video Games".strip().capitalize() : "Video Games & Consoles".strip().capitalize(),
    "Network Infrastructure Products".strip().capitalize() : "Computers & Tablets".strip().capitalize(),

}


subcat_mapping = {
    "Laptops".strip().capitalize():"Laptops & Notebooks".strip().capitalize(),
    "Networking".strip().capitalize(): "Neworking & Connectivity".strip().capitalize(),
    "PC Components".strip().capitalize():"Components & Peripherals".strip().capitalize(),
    "Cell Phones".strip().capitalize(): "Cell Phones & Smartphones".strip().capitalize(),
    "Network Infrastructure Products".strip().capitalize(): "Neworking & Connectivity".strip().capitalize(),
}

def getRawUrlData(url):
    while True:
        try:
            print "Getting Data From {0}.".format(url)
            temp = requests.get(url,timeout=30,headers=headers)
            if temp.status_code == 200:
                return temp.text
            else:
                return IndexError("sasa")

        except KeyboardInterrupt as e:
            raise e
        except:
            print "Error Getting Data From {0}., Retrying".format(url)


def get_cat_sub():
    data_raw = BeautifulSoup(getRawUrlData(start_url),"lxml")
    data_raw = data_raw.select_one("ul.nav li.active ul.dropdown-menu")
    cat_lis = data_raw.select("li[data-submenu-id]")
    data = {}
    for i in cat_lis:

        cat = i.a.text.strip().capitalize()

        temp = {}
        for sub_cat_li in i.find_all("li",class_="menu_li"):
            try:
                sub_cat_link = sub_cat_li.a
                sub_cat_label = sub_cat_link.text
                sub_cat_url = sub_cat_link["href"]
            except:
                continue

            if sub_cat_url not in visited:
                sub_raw = BeautifulSoup(getRawUrlData(sub_cat_url),"lxml")
                try:
                    t = sub_raw.select("select.displaypage option")[-1]["value"]
                    t = urlparse.urljoin(sub_cat_url,t)
                except:
                    print "Something Wrong"
                    continue

                newcat = cat.capitalize()

                try:
                    t1 = cat_mapping[newcat]
                    print t1
                    print cat_mapping[newcat]
                    cat = t1
                except:
                    pass

                try:
                    t1 = subcat_mapping[newcat]
                    sub_cat_label = t1
                except:
                    pass

                for current_item in scrape_data(t):
                    current_item["item_cat"] = cat
                    current_item["item_subcat"] = sub_cat_label
                    yield current_item

                temp[sub_cat_label] = t

                appendLog(sub_cat_url)


        data[cat] = temp



def scrape_data(s_url):
    isNext = True
    current = 1
    current_url = s_url
    items_data = []
    if s_url not  in visited:
        while isNext:

            isNext = False
            current += 1
            if current_url not in visited:
                current_raw = getRawUrlData(current_url)
                soup = BeautifulSoup(current_raw, "lxml").find("div", id="rightCol")
                next_tag = soup.select("ul#pageNumber li a")
                items_soup = soup.find_all("div",id="prodCol")

                for single_item_div in items_soup:
                    image_div = single_item_div.find("div",id="prodImg").a
                    desc_div = single_item_div.find("div",id="prodDesc")
                    prod_div = single_item_div.find("div",class_="prodModel")
                    prod_div_text = str(prod_div)
                    try:
                        item_price = float(
                        single_item_div.find(
                        "li",id="did_price1valuediv").find(
                        "label").b.text.strip().split("$")[-1].replace(",",""))
                    except:
                        continue

                    if not item_price>0:
                        continue

                    item_id = next(re.finditer("Frys #: </b></span>(.*)</p>",prod_div_text)).group(1)

                    try:
                        item_brand = next(re.finditer("<b>Manufacturer: </b></span>(.*)</p>", prod_div_text)).group(1)
                    except:
                        item_brand = "No Brand"

                    if item_brand == "NA":
                        item_brand = "No Brand"

                    try:
                        item_upc = next(re.finditer("<b>UPC : </b></span>(.*)</p>", prod_div_text)).group(1)
                    except:
                        item_upc = "00"

                    try:
                        item_model = next(re.finditer("<b>Model: </b></span>(.*)</p>", prod_div_text)).group(1).strip()
                    except:
                        item_model = "00"


                    item_title = desc_div.p.find("a").text
                    item_url = urlparse.urljoin(current_url,image_div["href"])
                    item_image = image_div.img["src"]

                    current_item = {
                        "item_id" : item_id,
                        "item_title" : item_title,
                        "item_upc" : item_upc,
                        "item_price": item_price,
                        "item_brand" : item_brand,
                        "item_model" : item_model,
                        "item_image" : item_image,
                        "item_url": re.sub(";jsessionid[^\?]+","",item_url),
                    }

                    yield current_item


                appendLog(current_url)

            for i in next_tag:
                try:
                    n = int(i.text.strip())
                except:
                    pass

                if n==current:
                    isNext = True
                    t = re.sub(";jsessionid[^\?]+","",i["href"])
                    current_url = urlparse.urljoin(current_url,t)

                    break;

        appendLog(s_url)
def get_data():
    all_cats = get_cat_sub()
    return all_cats


class FrysData():
    def __init__(self):
        pass
    def commit_data(self):
        data = get_data()

        try:
            request = {}

            request["SNR_Available"] = "Frys"
            request["SNR_Description"] = "Visit site to see description"
            request["SNR_CustomerReviews"] = 0.0
            request["SNR_PriceBefore"] = -1
            request["SNR_Condition"] = "00"
            c = 0
            while True:

                item = next(data)



                request["SNR_SKU"] = "FR" + str(item['item_id'])
                request["SNR_Title"] = item['item_title']
                request["SNR_Category"] = item['item_cat']
                request["SNR_SubCategory"] = item['item_subcat']
                request["SNR_Price"] = item['item_price']
                request["SNR_ProductURL"] = item['item_url']
                request["SNR_ImageURL"] = item['item_image']
                request["SNR_Brand"] = item["item_brand"]
                request["SNR_ModelNo"] = item["item_model"]
                request["SNR_UPC"] = item["item_upc"]
                yield request

        except StopIteration:
            pass


from scrapetools import commit_data
commit_data(FrysData().commit_data())
