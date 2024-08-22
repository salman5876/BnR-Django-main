from scrapetools import *

def get_saving_url(page):
    samsclub = "https://www.samsclub.com/soa/services/v1/catalogsearch/search?limit=100000&navigate="\
               +"{0}&offset={1}&pageView=grid&recordType=all&searchCategoryId=6930116&totalLimit=100000&xid=hdr:message:instant-savings"
    return samsclub.format(page,(page-1)*48)


my_proxy = getProxyWorking("https://www.samsclub.com")

def getDeals():
    count = 1
    inu = "https://www.samsclub.com/sams/redesign/evalues/offers.jsp?page=1&sortKey=mostRelevant&selectedFilter=all"
    deal_init = getRawData(url=inu,proxy=my_proxy)
    ind = getreIndex("soaHeaders\s*=\s*({)",deal_init)
    headers = getJsonData(deal_init[ind:],"{","}")


    try:
        req_obj = getRawData(get_saving_url(count),proxy=my_proxy,headers=headers,json=True)["payload"]["records"]
        for current_deal in req_obj:
            try:
                if not current_deal["isDead"]:
                    item_image = getAbsUrl(inu,current_deal["listImage"])
                    try:
                        category = current_deal["parentCategory"]['categoryName']
                    except:
                        category = "Not Available"
                    item_id = "SM"+current_deal["productId"]
                    item_title = current_deal["productName"]
                    item_url = getAbsUrl(inu,current_deal["seoUrl"])
                    price_div = current_deal["onlinePricing"]

                    try:
                        list_price = float(price_div["listPrice"]["currencyAmount"])

                        before_price = list_price
                        after_price = list_price
                    except:
                        before_price = -1.0

                    try:
                        after_price = float(price_div["finalPrice"]["currencyAmount"])
                    except:
                        pass

                    if after_price == before_price:
                        before_price = -1.0

                    current_item =  {
                        "SNR_SKU": item_id,
                        "SNR_Title": item_title,
                        "SNR_ProductURL": item_url,
                        "SNR_ImageURL": item_image,
                        "SNR_Category": category,
                        "SNR_PriceBefore": before_price,
                        "SNR_PriceAfter": after_price,
                        "SNR_Available": "Samsclub"
                    }

                    yield current_item

            except Exception as e:
                pass

    except Exception as e:
        pass

if __name__ == '__main__':
    for i in getDeals():
        commitdeal(i)