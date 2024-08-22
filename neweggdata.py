import codecs
import os, django
import json
from HTMLParser import HTMLParser
from time import sleep

"""
from selenium import webdriver
firefoxProfile =profile=webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
    ## Disable images
firefoxProfile.set_preference('permissions.default.image', 2)
profile.set_preference("javascript.enabled", False);
browser=webdriver.Firefox(profile)
"""
all_vis = set()
import socket
import socks

ip='127.0.0.1' # change your proxy's ip
port = 9150 # change your proxy's port
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
socket.socket = socks.socksocket


hparse = HTMLParser()

start_url = "https://www.newegg.com/"
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
    "Computer Systems".capitalize(): "Computers & Tablets".capitalize(),
    "Components".capitalize() : "Computers & Tablets".capitalize(),
    "Gaming".capitalize() : "Video Games & Consoles".capitalize(),
    "Home & Tools".capitalize(): "Home & Garden".capitalize(),
    "Health & Sports".capitalize() :"Health, Fitness & Beauty".capitalize(),
    "Apparel & Accessories".capitalize(): "Fashion".capitalize()
}



subcat_mapping = {
"Laptops / Notebooks".capitalize():"Laptops & Notebooks".capitalize(),
    "Tablets".capitalize():"iPads & Tablets".capitalize(),
"Desktops".capitalize() : "Desktops & All-In-Ones".capitalize()
}

elec_map = {
    "Mobile Phones".capitalize(): ("Cellphones & Accessories".capitalize(),"Cell Phones & Smartphones".capitalize()),
    "Tablets".capitalize(): ("Computers & Tablets".capitalize(),"iPads & Tablets".capitalize()),
    "Home Appliances".capitalize(): ("Electronics".capitalize(),"Home Appliances".capitalize()),
    "TV & Home Theater".capitalize() : ("TV, Audio & Surveillance".capitalize(),"Home Theater Systems".capitalize())
                }



forb_key = ["shop".lower(),"Services".lower(),"find".lower()]
elec = "Electronics"
from scrapetools import *
my_proxy ={}
#my_proxy = {'http': 'socks5://127.0.0.1:9150','https': 'socks5://127.0.0.1:9150'}

all_proxies = []

def getRawUrlData(url,json=False):
    global my_proxy
    global all_proxies
    global req_s
    while True:
        try:
            print "Getting Data From {0}.".format(url)
            temp = requests.get(url,timeout=50)

            if temp.status_code == 200:
                if "CommonReCaptchaValidate" in temp.url:
                    print "Caught"
                    sleep(20)
                    continue
                    if my_proxy:
                        all_proxies.append(my_proxy["http"])

                    temp = getProxyWorking(url,visited=all_proxies)
                    if temp:
                        my_proxy = temp
                    else:
                        my_proxy = {}
                        all_proxies = []
                    raise Timeout("Captcha")
                return temp.json() if json else temp.text
            else:
                raise KeyboardInterrupt("sasa")

        except KeyboardInterrupt as e:
            raise e
        except Exception as e:
            print "Error Getting Data From {0}., Retrying".format(url)


def getSoup(data="",url=False):
    if url:
        data = getRawUrlData(url)
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


def map_cat(dt,subcat=False):
    if subcat:
        try:
            return subcat_mapping[dt]
        except:
            return dt

    try:
        return cat_mapping[dt]
    except:
        return dt


def get_subs(ur):

    soup = getSoup(url=ur)
    temp = soup.select("div.left-nav dl.is-category")

    if temp:
        data = {}
        for subcat in temp:
            try:
                subcat_label = subcat.find("dt", class_="filter-box-title").text.strip().capitalize()
                subcat_label = is_al(subcat_label)
                if not subcat_label:
                    continue
                temp = subcat_mapping[subcat_label]
                subcat_label = temp
            except:
                pass

            data_sub = {}

            subcat_lists = subcat.select("dd.filter-box-body ul.filter-box-list li")

            for i in subcat_lists:
                i = i.find("a",class_="filter-box-label")
                temp2 = is_al(i["title"].strip().capitalize())
                if not temp2:
                    continue
                data_sub[temp2] = i["href"]

            data[subcat_label] = data_sub

        return (True,data)

    return (False,soup)

def is_al(w):
    temp = w.lower()
    for i in forb_key:
        if i in temp:
            return False
    return w

def get_cat_sub():
    soup = getSoup(url=start_url).select("ul.main-nav-categories li.main-nav-item a.main-nav-item-title")
    cats = {map_cat(i["name"].capitalize().strip()):i["href"] for i in soup }
    url_data = []
    for cat_label, cat_url in cats.iteritems():
        cat_label = is_al(cat_label)
        if cat_label:
            temp = get_subs(cat_url)[1]
            for subcat_label,subcat_data in temp.iteritems():
                nowcat = cat_label
                if cat_label == "Electronics".capitalize():
                    try:
                        temp2 = elec_map[subcat_label]
                        nowcat = temp2[0]
                        subcat_label = temp[1]
                    except:
                        pass

                for label,url in subcat_data.iteritems():

                    if label == "Apple".capitalize():
                        now_cat = "Apple"
                        temp2 = get_subs(url)[1]
                        for i in temp2.itervalues():
                            for subcat, ur in i.iteritems():
                                url_data.append((now_cat,subcat,ur))
                    else:
                        url_data.append((nowcat,subcat_label,url))

    return url_data

def scrape_data(soup,ur):
    is_next = True
    cp = 1
    while is_next:
        is_next = False
        items_div = soup.select("div.items-view div.item-container")
        cp+=1
        if ur in all_vis:
            continue
        try:
            next_link = soup.find("link",{"rel":"next"})["href"]
        except:
            try:
                next_link = re.sub("Page=\d+","Page={0}".format(cp),ur,count=1)
            except Exception as e:
                next_link = False

        for current_item_div in items_div:
            image_div = current_item_div.find("a",class_="item-img")
            request = {
                "SNR_Available" : "NewEgg",
                "SNR_UPC" : "00",
                "SNR_Condition" : "00",
                "SNR_Description" : "Visit site to see description"
            }

            temp = request["SNR_ProductURL"] = image_div["href"]
            temp = temp[temp.rindex("=")+1:]
            request["SNR_SKU"] = "NG"+ temp
            image_div = image_div.img
            request["SNR_Title"] = image_div["alt"]
            try:
                image_d = image_div["data-src"]
            except:
                image_d = image_div["src"]

            if image_d[:2] == "//":
                image_d = "https://"+image_d[2:]

            request["SNR_ImageURL"] = image_d


            try:
                request["SNR_Brand"] = current_item_div.select_one("a.item-brand img[alt]")["alt"]
            except:
                request["SNR_Brand"] = "No Brand"

            try:
                request["SNR_ModelNo"] = next(re.finditer("Model #: </strong>([^<]+)",str(current_item_div))).group(1).strip()
            except:
                request["SNR_ModelNo"] = "00"

            price_div = current_item_div.find("ul",class_="price")


            try:
                request["SNR_PriceBefore"] = float(price_div.select_one("span.price-was-data").text().strip())
            except:
                request["SNR_PriceBefore"] = -1.0

            price_div = price_div.select_one("li.price-current")


            temp = next(re.finditer(r"\$<strong>(\d+)</strong><sup>([\d+\.]+)</sup>",str(price_div)))
            request["SNR_Price"] = float(temp.group(1) + temp.group(2))
            temp = 0.0
            try:
                rating_div = current_item_div.find("i",class_="rating")["class"]

                for i in rating_div:
                    try:
                        temp = float(int(i[-1]))
                        break
                    except:
                        pass

            except Exception as e:
                pass

            request["SNR_CustomerReviews"] = temp

            yield request




        all_vis.add(ur)
        try:
            next_div = str(soup.select("button[title=Next]")[0])
            next_div.index("disabled")
        except:
            if "Submit=" not in next_link:
                if next_link:
                    ur = next_link
                    is_next = True
                    soup = getSoup(url=next_link)








def get_data():
    all_cats = get_cat_sub()

    for cat,subcat,cat_url in all_cats:
        cat_url = re.sub("\s+","&",cat_url)
        if not cat_url in all_vis:
            if "Submit=" in cat_url:
                continue

            data_urls = [cat_url]
            while data_urls:
                s = data_urls.pop()
                temp = get_subs(s)
                ind,cd = temp
                if not ind:
                    data = scrape_data(cd,cat_url)
                    for request in data:
                        request["SNR_Category"] = cat
                        request["SNR_SubCategory"] = subcat
                        yield request
                else:
                    temp = list(cd.itervalues())
                    for i in temp:
                        data_urls.extend(list(i.itervalues()))

            all_vis.add(cat_url)




commit_data(get_data(),100)