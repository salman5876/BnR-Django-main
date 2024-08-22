from scrapetools import *
start_url = "http://www.bjs.com"

my_proxy = getProxyWorking(start_url)
frb = ["gift","cleara","all"]


cat_map = {
    "Lawn & Garden".capitalize(): "Yard, Garden & Outdoor Living".capitalize(),
    "TV & Electronics".capitalize() : "Electronics",
    "Patio & Outdoor Living".capitalize() : "Yard, Garden & Outdoor Living".capitalize(),
   "Home" : "Home & Garden".capitalize(),
    "Sports & Fitness".capitalize() : "Sporting Goods",
    "Jewelry" : "Jewelry and Watches".capitalize(),
    "Health & Beauty".capitalize() : "Health, Fitness & Beauty".capitalize()
}

def get_cat():
    all_urls = []
    temp = getSoup(getRawData(start_url,proxy=my_proxy))
    cat_items = temp.select(
        "div#offCanvasLeft ul.drilldown li ul")
    all_cat_data = {}
    for single_cat_div in cat_items:
        try:
            cat_label =  parseHtml(single_cat_div.a.text.strip()).capitalize()
        except Exception as e:
            continue
        try:
            subdiv = single_cat_div.find("ul",class_="menu")
            urls_div = subdiv.select("a[href*=category]")
        except Exception as e:
            continue

        if not is_allowed(frb,cat_label):
            continue
        cat_label = map_data(cat_map,cat_label)
        temp = {}
        for i in urls_div:
            temp2 = getAbsUrl(start_url, i["href"])
            if temp2 not in all_urls:
                t = parseHtml(i.text.strip())
                if is_allowed(frb,t):
                    temp[t] = temp2
                    all_urls.append(temp2)
        if temp:
            all_cat_data[cat_label] = temp

    return all_cat_data


def assignBrand(br_array,item):
    for i in br_array:
        if i in item:
            return i

    return "No Brand"

def scrape_data(data_soup,url):
    is_next = True

    while is_next:
        is_next = False

        products_div = data_soup.select("div.plp-products div.product a")



        try:
            brands = [i.parent.find_next_sibling() for i in data_soup.select("h4 span.lilicon")
                      if "brand" in i.parent.text.strip().lower()][0]

            brands = [i.text.strip() for i in brands.select("span.name")]
        except:
            brands = []

        for product_div in products_div:
            try:
                request ={
                    "SNR_Available" : "BJS",
                    "SNR_UPC" : "00",
                    "SNR_ModelNo" : "00",
                    "SNR_Description" : "Visit site to see description",
                    "SNR_Condition" : "00"
                }

                try:
                    request["SNR_ProductURL"] = getAbsUrl(url,product_div["href"])
                except Exception as e:
                    pass



                pimage = product_div.select_one("p.img img")["src"]
                if pimage[:2] == "//":
                    pimage = "http:"+pimage


                temp = "&recipeName=180x180"
                if pimage.endswith(temp):
                    pimage = pimage[:-len(temp)]

                request["SNR_SKU"] = "BJ"+ patSearch("imageID=(\w+)",pimage).group(1)
                request["SNR_ImageURL"] = pimage
                request["SNR_Title"] = product_div.select_one("p.title").text.strip()

                price_div = product_div.select_one("p.price span.display")

                current_price = price_div.select_one("span.inner-display").text.strip().replace(
                    "$","").replace(","," ")

                request["SNR_Price"] = float(current_price)

                try:
                    savings = price_div.select_one("span.savings").text.replace(
                        "$", "").replace(",", "")
                    s = float(patSearch(r"(\d[\.\d]+)",savings).group(1))
                    request["SNR_PriceBefore"] = request["SNR_Price"] + s
                except Exception as e:
                    request["SNR_PriceBefore"] = -1

                request["SNR_CustomerReviews"] = 0.0

                try:
                    rating_div = product_div.select_one("p.rating span stars")["class"]
                    for i in rating_div:
                        try:
                            temp = float(i[-1])
                            request["SNR_CustomerReviews"] = temp
                        except:
                            pass
                except:
                    pass

                request["SNR_Brand"] = assignBrand(brands,request["SNR_Title"])
                yield request
            except:
                pass








        next_div = data_soup.select_one("p.numeral-paginater a.next")
        if next_div:
            is_next = True
            url = getAbsUrl(url,next_div["href"])
            data_soup = getSoup(getRawData(url,proxy=my_proxy))





def urls_page(temp2):
    try:
        t = temp2.rindex("?")
        temp2 = temp2[:t]
    except:
        pass

    temp2 += "?Nrpp=120"
    return temp2

def get_data():
    a = get_cat()

    temp2={}

    for cat_label,d in a.iteritems():
        temp = list(d.itervalues())[0]
        ur = getSoup(getRawData(temp,proxy=my_proxy)).select("ul.breadcrumbs a[href*=category]")[0]["href"]
        top_cat_url = getAbsUrl(temp,ur)
        temp2[cat_label] = top_cat_url


    a = {}

    for cat_label, cat_url in temp2.iteritems():
            temp = {}
            urls_temp = [{"label":cat_label,"url":cat_url}]
            while urls_temp:
                current_data = urls_temp.pop()
                current_url = urls_page(current_data["url"])
                current_label = current_data["label"]
                data_raw = getRawData(current_url,proxy=my_proxy)
                data_soup = getSoup(data_raw)
                cats_div = data_soup.select("div.categories a[href*=category]")

                if cats_div:

                    urls_data = [{
                        "url":getAbsUrl(current_url,i["href"]),"label":i.text.strip().capitalize()
                    } for i in cats_div]

                    urls_temp.extend(urls_data)
                else:
                    products_div = data_soup.select("div.plp-products div.product a")
                    if products_div:
                        for i in scrape_data(data_soup,current_url):
                            i["SNR_Category"] = cat_label
                            i["SNR_SubCategory"] = current_label
                            yield i


commit_data(get_data())