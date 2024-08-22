from scrapetools import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

start_url = "http://www.epicsports.com/"
my_proxy = {}
from selenium import webdriver
chrome_options = Options()
chrome_options.add_experimental_option( "prefs", {'profile.managed_default_content_settings.images': 2})
browser = webdriver.Chrome("/home/brainplow123/Desktop/chromedriver",chrome_options=chrome_options)

def get_raw(ur):
    global browser
    browser.get(ur)
    return browser.page_source

"""
def get_raw(ur):
    global my_proxy
    current_raw = ""
    same_proxy = []
    tcond = "<title" not in current_raw
    while tcond:
        current_raw = getRawData(url=ur, proxy=my_proxy)
        tcond = "<title" not in current_raw
        if tcond:
            if my_proxy:
                same_proxy.append(my_proxy["http"])
            temp = getProxyWorking(ur,visited=same_proxy)
            if temp:
                my_proxy = temp
            else:
                my_proxy = {}
                same_proxy = []

    my_proxy = {}
    return current_raw
"""
def get_cats():
    global my_proxy
    soup = False

    current_raw = get_raw(start_url)
    soup = getSoup(current_raw)
    soup = soup.select("ul#menu li a")[1:]

    return [(i.text.strip(),i["href"]) for i in soup]


def scrape_data(ur):
    is_next = True
    current_raw = get_raw(ur)
    current_soup = getSoup(current_raw)

    while is_next:
        is_next = False

        products_div = current_soup.select("div#product-div span.prod a")

        if not products_div:
            break

        for i in products_div:
            request = {}
            try:
                item_url = getAbsUrl(ur,i["href"])
                request["SNR_Title"] = i["title"]

                try:
                    request["SNR_Brand"] = i["title"].split(" ",1)[0]
                except:
                    request["SNR_Brand"] = "No Brand"

                request["SNR_ProductURL"] = item_url
                request["SNR_SKU"] = "ES"+patSearch("/prod/(\d+)",item_url).group(1)
                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] = "EpicSports"
                request["SNR_Description"] = "Visit site to see description"


                request["SNR_Category"] = "Sporting Goods"

                request["SNR_Condition"] = "00"
                request["SNR_PriceBefore"] = -1.0

                strelm = str(i)
                pr = patSearch("<p><dfn>\$([\.\d]+)",strelm).group(1)
                request["SNR_Price"] = float(pr)



                try:
                    rating = patSearch("Average Customer Rating:\s+([\.\d]+)",strelm).group(1)
                    request["SNR_CustomerReviews"] = float(rating)
                except:
                    request["SNR_CustomerReviews"] = 0.0



                request["SNR_ImageURL"] = i.select_one("img.img-product-thumbnail")["src"]
                yield request
            except:
                pass



        next_div = current_soup.select("a.right")
        if next_div:
            next_div = next_div[-1]
            if "Next" in next_div.text.strip():
                ur = getAbsUrl(ur,next_div["href"])
                is_next = True
                current_raw = get_raw(ur)
                current_soup = getSoup(current_raw)


def get_data():
    cat_data = get_cats()

    while cat_data:
        cat_label, cat_url = cat_data.pop()
        try:
            current_raw = ""
            prox = []

            current_raw = get_raw(cat_url)
            current_soup = getSoup(current_raw)
            temp = current_soup.select("ul#navigation li a")
            all_data_urls = [getAbsUrl(cat_url,i["href"]) for i in temp]
        except Exception as e:
            products_div = current_soup.select_one("div#product-div span.prod a")
            if products_div:
                for request in scrape_data(cat_url):
                    request["SNR_SubCategory"] = cat_label
                    yield request

            continue


        for curl in all_data_urls:
            for request in scrape_data(curl):
                request["SNR_SubCategory"] = cat_label
                yield request
    browser.close()
commit_data(get_data())

