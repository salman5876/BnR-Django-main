import codecs
import json,requests
import urlparse
import re
from bs4 import BeautifulSoup
start_url = "https://www.bhphotovideo.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

cat_mapping = {
    "Photography" : "Cameras & Photo".capitalize(),
    "Computers" : "Computers & Tablets".capitalize(),
    "Pro Video".capitalize() :  "Cameras & Photo".capitalize(),
    "Lighting".capitalize() : "Cameras & Photo".capitalize(),
    "Pro Audio".capitalize() : "TV, Audio & Surveillance".capitalize(),
    "Mobile": "Cellphones & Accessories".capitalize(),
    "TVs & Entertainment".capitalize() : "TV, Audio & Surveillance".capitalize(),
    "Camcorders".capitalize() : "Cameras & Photo".capitalize(),
    "Surveillance".capitalize() : "TV, Audio & Surveillance".capitalize()

}

from scrapetools import *



def saveJson(data,f="a.json"):
    with open(f,"w") as w:
        json.dump(data,w,indent=3)

def getSoup(data):
    return BeautifulSoup(data,"lxml")


def scrape_data(soup):
    isNext = True
    current_page = 1
    while isNext:
        isNext = False

        items_div = soup.find_all("div",{"data-selenium":"itemDetail","class":"item"})

        next_page_div = soup.select_one("div.pagination-zone a.pn-next")

        for current_item_div in items_div:
            try:
                item_image_div = current_item_div.find("a",{
                    "name": "image",
                    "class": "itemImg",
                    "data-selenium":"itemImg"
                })

                item_url = item_image_div["href"]
                item_image_div = item_image_div.img
                item_title = item_image_div["alt"]
                try:
                    item_image = item_image_div["data-src"]
                except:
                    item_image = item_image_div["src"]



                item_json =  json.loads( current_item_div["data-itemdata"])
                item_id = item_json["sku"]
                item_price = item_json["price"]



                price_div = current_item_div.find("div",{"data-selenium":"prices"})

                if isinstance(item_price,(str,unicode)):
                    item_price = float(item_price.replace(",",""))

                try:
                    temp = current_item_div.find("span",class_="review-stars-inner")["style"][:-2].replace("width:","").strip()

                    print ""
                    item_rating = float(temp)/100
                    item_rating = 5*item_rating
                except Exception as e:
                    item_rating = 0.0

                try:
                    item_before = float(price_div.p.span.text.strip().replace("$","").replace(",",""))
                except:
                    item_before = -1
                item_desc = "Visit site to see description"


                try:
                    temp = current_item_div.select("div.highlights div.sellingPoints ul li.sellingPoint")
                    temp = "\n".join([i.text.strip() for i in temp])
                    if temp:
                        item_desc = temp
                except:
                    pass



                data_item = {
                    "SNR_SKU": "BHP" + item_id,
                    "SNR_Title": item_title,
                    "SNR_Description": item_desc,
                    "SNR_ImageURL": item_image,
                    "SNR_Price":item_price,
                    "SNR_ProductURL": item_url,
                    "SNR_CustomerReviews" : item_rating,
                    "SNR_PriceBefore" : item_before,
                    "SNR_Brand" : "No Brand",
                    "SNR_Condition" : "00",
                    "SNR_UPC" : "00",
                    "SNR_ModelNo" : "00",
                    "SNR_Available" : "BHPHOTOVIDEO"
                }

                yield data_item
            except:
                pass

        if next_page_div:
            isNext = True
            ur = next_page_div["href"]
            soup = getSoup(getRawData(ur))



def get_data():
    start_raw = getRawData(start_url)
    cats_div = getSoup(start_raw).select("ul.nav-E li")

    def cat_parse(elem):
        link_div = elem.a
        cat_link = link_div["href"]
        cat_label = link_div.text.strip()

        return cat_link,cat_label


    def subcat_get(cat_link):
        soup = getSoup(getRawData(cat_link))
        try:
            subcats_raw = soup.find_all("li",{"data-selenium":"category","class":"clp-category"})
            for subcat_raw in subcats_raw:
                url_raw = subcat_raw.a
                subcat_label = url_raw.find("div",class_="clp-categoryName").text.strip()
                subcat_url = url_raw["href"]

                yield (subcat_label,subcat_url)
        except:
            yield ("waryam",soup)

    def get_items(ur):
        items_url = [ur]

        while items_url:
            current_item_url = items_url.pop()
            if "/c/buy/" in current_item_url:
                if current_item_url[-1] == "/":
                    current_item_url = current_item_url[:-1]
                current_item_url = current_item_url +"/lp/100"

                for i in scrape_data(getSoup(getRawData(current_item_url))):
                    yield i

            else:

                current_data = subcat_get(current_item_url)
                for i in current_data:
                    a,temp = i
                    if a == "waryam":
                        for j in scrape_data(temp):
                            yield j
                    else:
                        items_url.append(temp)

    for i in cats_div:
        classes = i["class"]
        cat_link, cat_label = cat_parse(i)
        subcat_links = subcat_get(cat_link)
        cat_label = cat_label.capitalize()

        for subcat_label,subcat_url in subcat_links:
            subsubcat_links = subcat_get(subcat_url)
            cat_urls = []
            if "/c/buy/" in subcat_url:
                current_item_url = subcat_url
                if current_item_url[-1] == "/":
                    current_item_url = current_item_url[:-1]
                current_item_url = current_item_url + "/lp/100"
                data = scrape_data(getSoup(getRawData(current_item_url)))
            elif "/c/browse/" in subcat_url:
                data = get_items(subcat_url)

            subcat_label = subcat_label.capitalize()

            for item in data:
                item["SNR_Category"] = map_data(cat_mapping,cat_label)
                item["SNR_SubCategory"] = subcat_label
                yield item
        if "last" in classes:
            break


commit_data(get_data())