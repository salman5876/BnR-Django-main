from scrapetools import *

deals_api = "https://www.bhphotovideo.com/bnh/controller/?A=middleTierSearch&O=&Q=json&"+\
            "ci=22144&Ns=p_POPULARITY|1&srtclk=sort&pn={0}&fct=fct_a_filter_by%7C04_USA%2Bfct_a_filter_by%7C03_INSTOCK&ipp=52&cff=1"



def getDeals():
    count = 1
    all_data = []

    while True:
        current_url = deals_api.format(count)
        current_page = getRawData(current_url, json=True)
        try:
         current_json = current_page["items"]
         if current_json:
             for current_deal in current_json:
                 try:
                     try:
                        current_feature = current_deal['featuredItemInfo']
                     except:
                        current_feature = {"categoryName":"Not Available"}



                     try:
                         orig = current_deal['originalPrice'].replace("$", "").replace(",", "")
                         orig = float(orig)
                     except:
                         orig = -1.0

                     try:
                         img = getAbsUrl(current_url, current_deal["detailImage"]["fileName"])
                     except:
                         img = getAbsUrl(current_url, current_deal["listingImage"])

                     current_item = {
                         "SNR_SKU": "BH" + current_deal["skuNo"],
                         "SNR_Title": current_deal['shortDescriptionPlusBrand'],
                         "SNR_ProductURL": getAbsUrl(deals_api, current_deal["detailsUrl"]),
                         "SNR_ImageURL": img,
                         "SNR_Category": current_feature["categoryName"],
                         "SNR_PriceBefore": orig,
                         "SNR_PriceAfter": float(current_deal["price"].replace("$", "").replace(",", "")),
                         "SNR_Available": "BHPHOTOVIDEO"
                     }
                     yield (current_item)
                 except Exception as e:
                     pass
        except:
            break

        count+=1