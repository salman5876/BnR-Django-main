from scrapetools import *

cat_mapping = {
    "Women's Plus".capitalize() : "Women",
    "Maternity" : "Clothes",
    "Baby": "Kids & Baby".capitalize(),
    "Toddler": "Kids & Baby".capitalize(),

}


forb = ["deal","feature","special","deal","new","size","ideas","gift","card","sale","up to","clearance","top-rated"," fan ","trend"]

start_url = "http://oldnavy.gap.com"
def oldnavy_data(cid,page):
    api_url = "http://oldnavy.gap.com/resources/productSearch/v1/search?cid={0}&isFacetsEnabled=true&globalShippingCountryCode=us&globalShippingCurrencyCode=USD&locale=en_US&pageId={1}"
    return getRawData(api_url.format(cid,page),json=True)

item_url_pat = "http://oldnavy.gap.com/browse/product.do?pid={0}"
def get_cat():
    temp = getSoup(url=start_url)
    cats = temp.select("div#divisionContainer ul[class*=mkt_topnav] li a[href*=division.do]")
    temp = []
    for i in cats:
        cat_label = i.text.strip().capitalize()
        cat_label = patSearch("^(\D+)",cat_label).group(1)
        if is_allowed(forb,cat_label):
            cat_label = map_data(cat_mapping,cat_label)
            temp2 = getAbsUrl(start_url,i["href"])
            temp.append( (cat_label,temp2) )

    return temp

def get_data():
    cat_data = get_cat()

    for cat_label,cat_url in cat_data:
        data_soup = getSoup(url=cat_url).select_one("div.g-inner nav.sidebar-navigation").select("a[href*=category.do]")
        sub_cat_data = {}

        for i in data_soup:
            try:

                label = i.text.strip().capitalize()
                if is_allowed(forb,label):
                    temp = patSearch("cid=(\d+)",i["href"]).group(1)
                    if temp:
                        sub_cat_data[label] = temp
            except Exception as e:
                pass

        for subcat_label, subcat_id in sub_cat_data.iteritems():
            current_page = 0
            temp = []
            while True:


                try:
                    data = oldnavy_data(subcat_id,current_page)['productCategoryFacetedSearch']['productCategory']['childCategories']

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
                    request["SNR_Available"] = "OldNavy"
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
                        request["SNR_ImageURL"] = current_item["quicklookimage"]["path"]
                    except:
                        request["SNR_ImageURL"] = list(current_item['avImages'].itervalues())[0]

                    request["SNR_Brand"] = "No Brand"

                    yield request
                except:
                    pass




commit_data(get_data())