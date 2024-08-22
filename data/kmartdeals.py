from scrapetools import *

deals_url = "http://www.kmart.com/deals/search?qt=search&q=*&facet.fields=BrandName,Category,Department,sys_event_ss&rows=100000&start=0&sort=FeaturedDeals_s&sort.order=asc&facet.sort=index&facet.limit=10000"


def get_deals():
    while True:
        try:
            deals = getRawData(deals_url,json=True)["deals"]
            for current_deal in deals:
                try:
                    temp = current_deal["FlagText"].lower()
                    if temp == "bluelight":
                        continue

                    try:
                        regular_price = patSearch("^\$([\d\.,]+)",current_deal['RegularPrice']).group(1).replace(",","")
                        regular_price = float(regular_price)
                    except Exception as e:
                        regular_price = -1.0

                    current_price = float(current_deal["MinPrice"])

                    try:
                        category = current_deal["Category"]
                    except:
                        category = "Not Available"


                    current_item = {
                        "SNR_SKU": "KM"+current_deal["PID"],
                        "SNR_Title": parseHtml(current_deal['DescriptionName']),
                        "SNR_ProductURL": getAbsUrl(deals_url,current_deal["Link"]),
                        "SNR_ImageURL": current_deal["MainImageUrl"],
                        "SNR_Category": category,
                        "SNR_PriceBefore": regular_price,
                        "SNR_PriceAfter": current_price,
                        "SNR_Available": "Kmart"
                    }

                    yield current_item
                except:
                    pass
        except:
            sleep(5)

if __name__ == '__main__':
    for i in get_deals():
        pass