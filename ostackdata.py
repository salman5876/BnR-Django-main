from scrapetools import *
import re



start_url = "https://www.overstock.com/shop-all-departments"

forb = [" by "," seen "]
my_proxy = {}
#my_proxy = getProxyWorking(start_url)
visited_p = []
cookies = {"ostk_aggr_year":"country^US|mxcskupage^60|currency^USD|language^en|mxcuserseed^5798221700760769813"}
def get_start_data():
    global  my_proxy,visited_p
    cat_soup = False

    while not cat_soup:
        data_soup = getSoup(url=start_url,proxy=my_proxy,cookies=cookies)
        cat_soup = data_soup.select_one("ul.allCategories")


    current_cat = False
    all_data = []
    for i in cat_soup.children:
        try:
            link = i.a
            elem = link.text.strip().capitalize()

            if is_allowed(forb,elem):
                raw = str(i)
                if "<lh" in raw:
                    current_cat = elem
                    if current_cat in ["Pet Supplies".capitalize(),"Emergency Preparedness".capitalize()]:
                        all_data.append((current_cat,current_cat,link["href"]))
                elif "<li" in raw:
                    if current_cat == "Electronics":
                        all_data.append( (elem,elem,getAbsUrl(start_url,link["href"])) )
                    else:
                        all_data.append((current_cat,elem,getAbsUrl(start_url,link["href"])))

        except:
            pass

    return all_data


def get_product_soup(soup):
    return soup.select_one("div.product-results-wrapper")


def cat_links(soup):
    temp = soup.select_one("aside#left-search-nav")

    if not temp:
        temp = soup.select_one("div.global-nav")

    return temp.select_one("div.categories").select("a.refinement-link")

def scrape_data(soup,url):
    is_next = True

    while is_next:
        is_next = False

        next_div = soup.select_one("div.pagination-container").select_one("div.next-wrapper a[href]")
        all_items = soup.select("div.product-wrapper div.product-tile")

        for item_div in all_items:
            try:
                temp = item_div.select_one("div[data-product-id]")
                item_div = item_div.select_one("a.product-link")
                price_div = item_div.select_one("div.product-price-container")
                title_div = item_div.select_one("div.product-title")
                image_div = item_div.select_one("div.image-wrapper").select_one("img[src]")


                request = {}

                request["SNR_ProductURL"] = getAbsUrl(url,item_div["href"])


                request["SNR_SKU"] = "OS{0}".format(temp["data-product-id"])
                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] = "OverStock"
                request["SNR_Description"] = "Visit site to see description"

                try:
                    temp = image_div["data-src"]
                except:
                    temp = image_div["src"]
                try:
                    temp = temp[:temp.rindex("?")]
                except:
                    pass

                request["SNR_ImageURL"] = temp



                request["SNR_Title"] = title_div.text.strip()

                request["SNR_Condition"] = "00"
                before_div = price_div.select_one("div.was-reference-price span.reference-price")

                if before_div:
                    request["SNR_PriceBefore"] = float(before_div.text.strip().replace(",","").replace("$",""))
                else:
                    request["SNR_PriceBefore"] = 0.0



                after_div = price_div.select_one("div.product-price span.price-range").select_one("span.from-price")

                temp_price = after_div.select_one("span.price-dollar").text.strip()



                try:
                    temp_price = "{0}.{1}".format(temp_price,after_div.select_one("span.price-cent").text.strip())
                except:
                    pass
                request["SNR_Price"] = float(temp_price)
                request["SNR_CustomerReviews"] = 0.0
                rev_div = item_div.select_one('div.reviews img[alt*=Stars]')
                if rev_div:
                    request["SNR_CustomerReviews"] = float(rev_div["alt"].split(" ")[0])




                request["SNR_Brand"] = "No Brand"
                yield request

            except Exception as e:
                pass


        if next_div:
            temp = next_div["href"]
            if not temp.startswith("#"):
                url = getAbsUrl(url,next_div["href"])
                soup = get_product_soup(getSoup(url=url,cookies=cookies))
                is_next = True


def extract_data(cats_data):
    cat_label, subcat_label, caturl = cats_data
    temp = [ {"cat":subcat_label,"url":caturl}]

    while temp:
        current_data = temp.pop()
        current_cat = current_data["cat"]
        current_url = current_data["url"]

        current_soup = getSoup(url=current_url,cookies=cookies)

        products_soup = get_product_soup(current_soup)

        if products_soup:
            for request in scrape_data(products_soup,current_url):
                request["SNR_Category"] = cat_label
                request["SNR_SubCategory"] = current_cat

                yield request

        else:
            cat_links_all = cat_links(current_soup)

            if cat_links_all:
                cat_links_all = [{"url":getAbsUrl(current_url,i["href"]),"cat":i.text.strip()} for i in cat_links_all]
                temp.extend(cat_links_all)


def all_cat_data(cats_data):
    commit_data(extract_data(cats_data))

def get_data():
    cats_data = get_start_data()

    with ProcessPoolExecutor(max_workers=10) as executor:
        future = executor.map(all_cat_data, cats_data, chunksize=2)
        executor.shutdown(wait=True)




get_data()