from scrapetools import *
start_url = "https://www.sprint.com/en/shop/cell-phones.html"

my_proxy = getProxyWorking(start_url)
frb = ["gift","cleara","all"]


def newObj():
    return {
            "SNR_Available": "Sprint",
            "SNR_UPC" : "00",
            "SNR_Condition" : "00",
            "SNR_ModelNo" : "00",
            "SNR_PriceBefore" : -1,
        "SNR_CustomerReviews" : 0.0,
        "SNR_Brand" : "No Brand",
        "SNR_Description" : "Visit site to see description"
        }


app_headers = {
    "applicationid": "ECMW",
    "applicationuserid": "ECMW",
    "messageid" :"506324813",
    "enterprisemessageid":"ECMW506324813",
    "conversationid" : "CARE506324813",
    "messagedatetimestamp" : "2019-02-14T08:36:31.068Z"
}

price_url ="https://www.sprint.com/api/digital/devices/v1/lookup/devices?defaultSKUPrice=SINGLE_PRICING&deviceType={0}&flow=GROSS_ADD"

def scrape_acc(ur,pr):
    data_soup = getSoup(getRawData(proxy=my_proxy, url=ur,timeout=90)).select("div.accessoryDataSection")
    for i in data_soup:
        try:
            request = newObj()
            image_div = i.select_one("div.accessoryImage img")
            image = getAbsUrl(ur,image_div["src"]).replace("80x80","180x160")
            request["SNR_ImageURL"] = image
            request["SNR_Title"] = image_div["alt"]
            temp = i.select_one("a.launchAccessoryDetails")

            try:
                request["SNR_Description"] = i.select_one("div.accessoryDetails").text.strip()
            except:
                pass
            link_div = str(temp["href"])
            request["SNR_SKU"] = "SPR"+patSearch("accSKU=(\w+)",link_div).group(1)
            try:
                temp = "ao_details.jsp"
                temp = link_div.index(temp) + len(temp)
                temp2 = "?accSKU"

                temp2 = link_div.index(temp2)

                link_div = link_div[:temp] + link_div[temp2:]
            except:
                pass

            request["SNR_ProductURL"] = getAbsUrl(ur,link_div)

            price_div = i.select_one("div.accessoryPricing")

            price_after = price_div.select_one("div.total div.price em").text.replace("$","")
            request["SNR_Price"] = float(re.sub("\s+","",price_after))
            try:
                price_before_div = price_div.select_one("div.regular div.price").text.replace("$", "")
                request["SNR_PriceBefore"] = float(re.sub("\s+", "", price_before_div))
            except:
                pass
            yield request
        except Exception as e:
            pass




def scrape_other(ur,pr):
    data_soup = getSoup( getRawData(proxy=my_proxy,url=ur) ).select("li[data-sku]")
    prices_json =  getRawData(price_url.format(pr),proxy=my_proxy,headers=app_headers,json=True)
    prices_list = []
    prices_dic = {}
    for i in prices_json:
        try:
            temp = i["products"][0]["items"][0]
            prices_dic[temp["deviceSKU"]] = temp["srp"]
            prices_list.append(temp)
        except:
            pass

    for current_item_div in data_soup:
        try:
            request = newObj()
            sku = current_item_div["data-sku"]
            try:
                request["SNR_Price"] = prices_dic[sku]
            except:
                continue
            request["SNR_SKU"] = "SPR"+sku
            try:
                request["SNR_Brand"] = current_item_div["data-manufacturer"]
            except:
                request["SNR_Brand"] = "No Brand"

            link_div = current_item_div.find("a")

            request["SNR_ProductURL"] = getAbsUrl(ur,link_div["href"])
            request["SNR_Title"] = link_div["title"]

            image_div = link_div.find("img")
            temp = request["SNR_ImageURL"] = getAbsUrl(ur,image_div["src"])
            try:
                temp = temp[:temp.index("png/_jcr_content/renditions/")+3]
                request["SNR_ImageURL"] = temp
            except:
                pass
            rating_div = current_item_div.select_one("div.ratings div[style*=calc]")
            request["SNR_CustomerReviews"] = 0.0
            if rating_div:
                try:
                    request["SNR_CustomerReviews"] = float(patSearch(r"\(\(([\d\.]+)\*"
                                                               ,str(rating_div)).group(1))
                except:
                    pass

            yield request
        except:
            pass




data_urls = [
    ("Accessories","Accessories","https://shop.sprint.com/mysprint/shop/accessory/ao_accessorywall.jsp?accCatId=acc9080cat&deviceIndependent=true&INTNAV=ATG:ACC_Landing",scrape_acc,""),
    ("Computers & tablets","Tablets","https://www.sprint.com/en/shop/tablets.html?INTNAV=TopNav:Shop:Tablets&credit=A2&sort=FEATURED",scrape_other,"TABLETS_AND_LAPTOPS"),
    ("Cellphones & accessories", "Cellphones","https://www.sprint.com/en/shop/cell-phones.html",scrape_other,"PHONES"),
    ("Network & Connectivity Equipment","Hotspots","https://www.sprint.com/en/shop/hotspots.html?INTNAV=TopNav:Shop:HotspotsMore&credit=A2&sort=FEATURED",scrape_other,"HOTSPOTS_AND_MBB")
]


def get_data():
    for cat_label, subcat_label, url, scrape_func, pr in data_urls:
        for i in scrape_func(url, pr):
            i["SNR_Category"] = cat_label
            i["SNR_SubCategory"] = subcat_label
            # print i
            yield i

commit_data(get_data())