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



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}


cat_mapping = {

    "Smartphones".capitalize():"Cellphones & Accessories".capitalize(),
    "Tablets".capitalize(): "Computers & Tablets".capitalize(),
    "Smart home".capitalize(): "Smart home".capitalize(),
    "Wearable tech".capitalize(): "Cellphones & Accessories".capitalize(),
    "Audio" : "TV, Audio & Surveillance".capitalize(),
     "Car and travel".capitalize() : "Vehicle Electronics & GPS".capitalize(),
     "Cases & Protection".capitalize() : "Cellphones & Accessories".capitalize(),
    "Kids".capitalize(): "Cellphones & Accessories".capitalize(),
    "Mobile hotspots".capitalize() : "Computers & Tablets".capitalize()
}


subcat_mapping = {
"Smartphones".capitalize():"Cell Phones & Smartphones".capitalize(),
    "Tablets".capitalize():"iPads & Tablets".capitalize(),
}

deep_cat = ["Audio".capitalize(),"Smart home".capitalize()]
# deep_cat = ["Audio".capitalize(),"Smart home".capitalize()]

def getRawUrlData(url,json=False):
    print("getting data")
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


def getSoup(data):
    return BeautifulSoup(data,"lxml")


def getJsonData(inputData,st=u"[",en=u"]"):
    jsonIndex = temp = 0

    for i in inputData:
        if i == st:
            temp += 1
        elif i == en:
            temp -= 1
            if (temp == 0):
                temp = inputData[:jsonIndex + 1]
                return json.loads(temp)

        jsonIndex += 1


def getDeep(url):
    print("getting deep")
    data = getRawUrlData(url)
    temp = 'var shpJSON = {"popularCategoryList":'
    print temp
    data = data[data.index(temp)+len(temp):]
    data = data[:data.index("</script>")]
    a = getJsonData(data)
    temp = {}
    for i in a:
        print(i)
        if not i["subCategories"]:
            sub_url = "https://www.verizonwireless.com/accessories" + i['navigationState']
            subcat = i["name"]
            temp[subcat] = sub_url

    return temp

def get_cat_sub():
    print( "in get cat sub")
    sub_json = getRawUrlData(start_url,True)["gNavMenu"]

    for i in sub_json:
        # print(i)
        if i["label"] == "Shop":
            temp = i["subMenu"]
            break

    cat_data = []
    for i in temp:
        try:
            i["label"] = i["label"].capitalize()
            cat = cat_mapping[i["label"]]
            cat_url = urlparse.urljoin(ver_home, i["URL"])
            subcat = i["label"]
            print subcat

            try:
                temp = subcat_mapping[i["label"]]
                subcat = temp
            except KeyError:
                pass

            if i["label"] in deep_cat:
                temp = getDeep(cat_url)
                for subcat_deep,subcat_url in temp.iteritems():
                    cat_data.append((cat,subcat_deep,subcat_url))
            else:
                cat_data.append((cat,subcat,cat_url))

        except KeyError:
            pass
    return cat_data


def scrape_devices(data_json,ur):

    print("scrapping")
    all_data = []

    for item in data_json:
        item_attrib = item['attributes']
        if not item_attrib['product.isOutOfStock'][0]:
            try:
                request = {
                    "SNR_Available":"Verizon",
                    "SNR_PriceBefore" : -1.0,
                    "SNR_UPC" : "00",
                    "SNR_Condition" : "00",
                    "SNR_Description":"Visit site to see description",
                    "SNR_ModelNo" : "00"
                }


                try:
                    request["SNR_Brand"] = hparse.unescape(item_attrib["Brand"][0])
                except:
                    request["SNR_Brand"] = "No Brand"


                try:
                    request["SNR_CustomerReviews"] = float( item_attrib['product.averageRating'][0] )
                except:
                    request["SNR_CustomerReviews"] = 0.0

                try:
                    request["SNR_Title"] = hparse.unescape( item_attrib['sku.displayName'][0] )
                except:
                    request["SNR_Title"] = hparse.unescape( item_attrib['product.displayName'][0] )

                request["SNR_ProductURL"] = urlparse.urljoin(ur,item_attrib['product.pdpUrl'][0])

                price_json = item_attrib['product.gridwallDevicePriceVO'][0]

                try:
                    request["SNR_Price"] = price_json['fullRetailPrice']
                except:
                    request["SNR_Price"] = price_json['actualFullRetailPrice']

                ver_image = "https://ss7.vzw.com/is/image/VerizonWireless/{0}"
                request["SNR_ImageURL"] = ver_image.format(item_attrib['sku.imageName'][0])
                request["SNR_SKU"] = "VZ" + next(re.finditer("[^\d](\d+)$",item_attrib['product.repositoryId'][0])).group(1)
                all_data.append(request)
            except:
                pass

    return all_data

def scrape_data(s_url):
    is_next = True
    current_url = s_url
    top_url = s_url

    while is_next:
        all_items = []
        is_next = False
        try:
            data_raw = getRawUrlData(current_url)
        except:
            continue
        soup = BeautifulSoup(data_raw,"lxml")


        next_div = soup.find("link",{"rel":"next"})
        try:
            try:
                temp = data_raw.index('<script id="serviceContentId">')
                temp = data_raw[temp:]
                temp = temp[:temp.index("</script>")]
                temp1 = '"devices":'
                temp1 = temp.index(temp1) + len(temp1)
                data_raw = temp[temp1:]
                data = getJsonData(data_raw)
                all_items.extend(scrape_devices(data,current_url))
            except:
                item_divs = soup.find_all("li",class_="content-item")
                num_map = {"one":1.0,
                           "two":2.0,
                           "three":3.0,
                           "four":4.0,
                           "five":5.0
                           }
                if item_divs:
                    for item_div in item_divs:
                        product_detail_div = item_div.select("div.content-details form")[0]
                        item_div = item_div.find("div",class_="content-link")

                        request = {
                            "SNR_Available": "Verizon",
                            "SNR_PriceBefore": -1.0,
                            "SNR_UPC": "00",
                            "SNR_Condition": "00",
                            "SNR_Description": "Visit site to see description",
                            "SNR_ModelNo": "00"
                        }

                        request["SNR_SKU"] = "VZ" + product_detail_div["id"].split("sku")[-1]

                        image_div = item_div.select_one('figure.content-fig img[id*="content-item"]')
                        temp = image_div["src"]

                        try:
                            temp_index = temp.rindex("?")
                            temp = temp[:temp_index]
                        except:
                            pass

                        request["SNR_ImageURL"] = temp
                        request["SNR_Title"] = hparse.unescape( image_div["alt"] )
                        detail_dev = item_div.find("section",class_="content-detail")
                        temp = detail_dev.find("div",class_="name")
                        brand_div = temp.find("h6",class_="fontsz_label")

                        try:
                            request["SNR_Brand"] = brand_div.text.strip()
                        except:
                            request["SNR_Brand"] = "No Brand"

                        request["SNR_ProductURL"] = temp.find("a")["href"]
                        request["SNR_Price"] = float(
                            detail_dev.find("strong",id="formatted-currency").text.strip().replace("$","").replace(",","")
                                )

                        request["SNR_CustomerReviews"] = 0.0

                        temp = detail_dev.find("div",id="pdp-rating-stars")["class"]

                        for i in temp:
                            i = i.lower()

                            try:
                                t = num_map[i]
                                request["SNR_CustomerReviews"] = t
                                break
                            except:
                                pass

                        all_items.append(request)

            if next_div:
                is_next = True
                current_url = next_div["href"]
        except:
            pass

        yield all_items








def get_data():
    all_cats = get_cat_sub()
    for cat,subcat,cat_url in all_cats:
        print cat_url
        data = scrape_data(cat_url)
        #request["SNR_Category"] = item['item_cat']
        #request["SNR_SubCategory"] = item['item_subcat']

        for j in data:
            for i in j:
                i["SNR_Category"] = cat
                i["SNR_SubCategory"] = subcat
                yield i


class VerizonData:
    def __init__(self):
        pass
    def commit_data(self):
        data = get_data()
        for request in data:
                print("main fun")

                request['SNR_CustomerReviews'] = float("%0.2f" % request['SNR_CustomerReviews'])
                request['SNR_Price'] = float("%0.2f" % request['SNR_Price'])
                serializer = AllProducts_Serializer(data=request)

                if serializer.is_valid():
                    print("---")
                    serializer.save()
                else:
                    print serializer.errors
                    print("bad json")


VerizonData().commit_data()