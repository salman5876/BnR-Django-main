import codecs
import json,requests
import urlparse
import re
from bs4 import BeautifulSoup
start_url = "https://www.macys.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
cookies = {"currency":"USD"}
forb =["all","shop","brand","new","feature","trend","repair","service","gift","guide", "off","sale"]
from scrapetools import *

cat_mapping = {
    "Home": "Home & Garden".capitalize(),
    "BED & BATH".capitalize() : "Home & Garden".capitalize(),
    "HANDBAGS & ACCESSORIES".capitalize() : "Handbags & Purses".capitalize(),
    "KIDS".capitalize():"Kids & Baby".capitalize() ,
"JUNIORS".capitalize():"Kids & Baby".capitalize(),
"JEWELRY".capitalize():"Jewelry and Watches".capitalize(),
"WATCHES".capitalize():"Jewelry and Watches".capitalize()
               }

def getRawData(url):
    while True:
        try:
            print "Getting Data From {0}".format(url)
            temp = requests.get(url,timeout=30,headers=headers,cookies=cookies)
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
    isNext = True

    while isNext:
        isNext = False
        try:
            soup = getSoup(getRawData(ur))

            if soup.find("span",class_="zeroProduct"):
                break


            results_div = soup.find("div", class_="sortableGrid")

            items_div = results_div.select("li.productThumbnailItem div.productThumbnail")

            next_page = results_div.select_one("li.pagination ul.paginationNumbers li.nextPage a")["href"]
            if len(next_page)>5:
                ur = urlparse.urljoin(ur,next_page)
                isNext = True

            for item_div in items_div:

                rating_div = item_div.find("span","redStarContainer")
                json_div = item_div.find("script",{
                    "data-bootstrap":"component/product-thumbnail"})

                price_div = item_div.find("div", class_="prices")
                item_div = item_div.find("div",class_="productThumbnailImage")
                link_div = item_div.find("a",class_="productDescLink")
                image_div = link_div.img





                if not price_div:
                    continue



                item_price = float(price_div.find("span", class_="regular").text.strip().replace("$", " ").replace(
                    ",","").rsplit(" ", 1)[-1])



                try:
                    price_div = price_div.find("span", class_="discount").text.strip().replace("$", " ").replace(
                        ",", "").rsplit(" ", 1)[-1]
                    item_before = item_price
                    item_price = price_div
                except:
                    item_before = -1.0

                item_price = float(item_price)
                item_before = float(item_before)

                item_id = image_div["id"].split("img_")[-1]
                item_url = urlparse.urljoin(ur,link_div["href"])
                item_title = link_div["alt"].strip()
                item_image = image_div["src"]
                item_desc = "Visit site to see description"
                item_brand = "No Brand"
                item_rating = 0.0

                if json_div:
                    try:
                        temp = json.loads( json_div.text)["detail"]
                        item_brand = temp["brand"].strip()
                        item_desc = temp["description"].strip()
                        item_rating = temp["reviewStatistics"]["aggregate"]["rating"]
                    except KeyError:
                        pass
                elif rating_div:
                    item_rating = rating_div["style"]
                    item_rating = item_rating.replace("width:","")[:-1]
                    item_rating = float("%0.2f" % (float(item_rating)/20))

                yield  {
                    "SNR_SKU": "MC"+item_id,
                    "SNR_Title":item_title,
                    "SNR_ImageURL" : item_image,
                    "SNR_Brand" : item_brand,
                    "SNR_Condition" : "00",
                    "SNR_ProductURL": item_url,
                    "SNR_Description": item_desc,
                    "SNR_CustomerReviews": item_rating,
                    "SNR_Available" :"MACYS",
                    "SNR_UPC" : "00",
                    "SNR_ModelNo" : "00",
                    "SNR_PriceBefore" : item_before,
                    "SNR_Price" : item_price

                }

        except:
            pass


def isAllow(t):
    t = t.lower()

    for i in forb:
        if i in t:
            return False
    return True


def get_data():
    start_raw = getRawData(start_url)
    main_nav = getSoup(start_raw).select("div#mainNavigationFlyouts div[aria-label]")[:-2]
    for cat_div in main_nav:

        cat_label = cat_div["aria-label"].capitalize()

        if isAllow(cat_label):
            subcat_divs = cat_div.div.select("ul.flexLabelLinksContainer li a")
            for subcat_div in subcat_divs:
                subcat_url = re.sub(r"\s+","",urlparse.urljoin(start_url,subcat_div["href"].strip()))

                subcat_label = subcat_div.text.strip().capitalize()
                if isAllow(subcat_label):
                    if "feature" not in subcat_url:
                        data = scrape_data(subcat_url)

                        for item in data:
                            item["SNR_Category"] = map_data(cat_mapping,cat_label)
                            item["SNR_SubCategory"] = subcat_label

                            yield item

commit_data(get_data())