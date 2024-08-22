from urllib import unquote

from scrapetools import *
t = "Kids & Baby".capitalize()
cat_mapping = {
"toddler girl".capitalize():t,
    "toddler boy".capitalize():t,
    "baby girl".capitalize():t,
    "baby boy".capitalize():t,
    "Gapbody" : "Fashion",
    "Gapfit" : "Fashion",
    "GapMaternity".capitalize(): "Fashion",
    "Womens".capitalize() : "Women",
    "Mens".capitalize() : "Men"
}


forb = ["deal","feature","special","deal","new","size","ideas","gift","card","sale","up to","clearance","top-rated"," fan ","trend"]

start_url = "http://gap.com"
def gap_data(cid,page):
    api_url = "http://www.gap.com/resources/productSearch/v1/search?cid={0}&isFacetsEnabled=true&globalShippingCountryCode=us&globalShippingCurrencyCode=USD&locale=en_US&&pageId={1}"
    return getRawData(api_url.format(cid,page),json=True)

item_url_pat = "http://www.gap.com/browse/product.do?pid={0}"
def get_cat():
    temp = getSoup(url=start_url)
    cat_data = []

    data_soup = temp.select("li[class*=reporting-child-ele] div[class*=catnav] a[href*=category.do]")
    for i in data_soup:
        j = i.parent.parent
        cid = j["data-cid"]
        a = re.split(",\s+",j["data-site-cat-key"])

        cat = a[0].capitalize()
        cat = map_data(cat_mapping,cat)
        subcat = a[-1].capitalize()

        cat_data.append((cid,cat,subcat))

    return cat_data


def get_data():
    cat_data = get_cat()

    for subcat_id,cat_label,subcat_label in cat_data:
        current_page = 0
        temp = []
        while True:

            try:
                data = gap_data(subcat_id,current_page)['productCategoryFacetedSearch']['productCategory']['childCategories']
                temp2 = []

                for i in data:
                    try:
                        temp2.extend(i['childProducts'])
                    except:
                        pass

                current_page+=1

                if not temp2:
                    break
                temp.extend(temp2)


            except:
                break

        for current_item in temp:
            try:
                pid = current_item["businessCatalogItemId"]
                request = {}
                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] = "GAP"
                request["SNR_Description"] = "Visit site to see description"
                request["SNR_SKU"] = "ON" + pid
                request["SNR_Title"] = current_item["name"]
                request["SNR_Category"] = cat_label
                request["SNR_SubCategory"] = subcat_label
                request["SNR_Condition"] = "00"

                pr = current_item["price"]
                try:
                    request["SNR_PriceBefore"] = float(pr["regularMinPrice"])
                except:
                    request["SNR_PriceBefore"] = -1


                request["SNR_Price"] = float(pr['currentMinPrice'])

                if request["SNR_PriceBefore"] == request["SNR_Price"]:
                    request["SNR_PriceBefore"] = -1

                request["SNR_CustomerReviews"] = 0.0
                request["SNR_ProductURL"] = item_url_pat.format(pid)
                try:
                    request["SNR_ImageURL"] = current_item['quicklookImage']["path"]
                except:
                    request["SNR_ImageURL"] = list(current_item['avImages'].itervalues())[0]

                request["SNR_Brand"] = "No Brand"

                yield request
            except:
                pass




commit_data(get_data())