from scrapetools import *


start_url = "https://www.costco.com/view-more.html"

my_proxy = getProxyWorking(start_url)

inside =["Electronics & Computers".capitalize(),"For the Home".capitalize()]

forb =["card","gift","feature","support","service"]


def get_cat_sub():
    soup = getSoup( getRawData(start_url,proxy=my_proxy) ).select_one("div#search-results").select("div.row div ul.viewmore-list")
    all_data = []
    for i in soup:
        cat_title = i.parent.h3.text.strip().capitalize()
        cat_links = i.select("li a.viewmore-list")
        for j in cat_links:
            subcat_label = j.text.strip().capitalize()
            subcat_url = getAbsUrl(start_url,j["href"])

            if cat_title in inside:
                all_data.append((subcat_label,subcat_url))
            else:
                all_data.append( (cat_title,subcat_url) )

    return all_data

def get_page_soup(soup):
    return soup.select_one("div.product-list")


def scrape_data(soup,url):
    is_next = True

    while is_next:
        is_next = False

        products_div = soup.select("div.product div.product-tile-set")

        for current_item_div in products_div:
            try:
                request = {}

                request["SNR_ProductURL"] = getAbsUrl(url,current_item_div["data-pdp-url"])

                data_div = soup.select_one("div.thumbnail")
                request["SNR_SKU"] = "CC"+data_div["itemid"]
                image_div = data_div.select_one("div.product-img-holder img")
                request["SNR_Title"] = image_div["alt"]
                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] ="CostCo"
                request["SNR_ImageURL"] = image_div["src"]
                request["SNR_Description"] = "Visit site to see description"
                desc_div = soup.select_one("div div.caption")

                products_features = desc_div.select("ul.product-features li")

                if products_div:
                    request["SNR_Description"] = "\n".join( [j.text.strip() for j in products_features] )

                price_div = desc_div.select_one("div.price-parent div.price").text.strip().replace("$","").replace(",","")
                request["SNR_Price"] = float(price_div)


                try:
                    promo_div = current_item_div.select_one("p.promo").text.strip()
                    before = re.split("\s+After\s+", promo_div)[-1]
                    before = float(patSearch("\$([\.,\d]+)", before).group(1))
                    request["SNR_PriceBefore"] = request["SNR_Price"] + before
                except:
                    request["SNR_PriceBefore"] = -1





                request["SNR_Condition"] = "00"



                try:
                    rating_div = current_item_div.select_one("div[itemprop=aggregateRating]").select_one(
                        "meta[itemprop=ratingValue]")["content"]
                    request["SNR_CustomerReviews"] = float(rating_div)
                except:
                    request["SNR_CustomerReviews"] = 0.0
                request["SNR_Brand"] = "No Brand"

                yield request
            except:
                pass


        next_div = soup.select_one("div.paging ul li.forward a")

        if next_div:
            url = getAbsUrl(url,next_div["href"])
            is_next = True
            soup = get_page_soup(getSoup(url=url,proxy=my_proxy))


def get_subcats(soup):
    return soup.select("div.categoryclist div.row div a")

def get_data():
    cats_data = get_cat_sub()
    for cat_label, cat_url in cats_data:
        subcats = [{"cat":cat_label,"url":cat_url}]

        while subcats:
            current_cat_data = subcats.pop()
            current_url = current_cat_data["url"]
            current_label = current_cat_data["cat"].capitalize()

            soup = getSoup(url=current_url,proxy=my_proxy)

            page_soup = get_page_soup(soup)

            if page_soup:
                for request in scrape_data(page_soup,current_url):
                    request["SNR_Category"] = cat_label
                    request["SNR_SubCategory"] = current_label
                    yield request

            else:
                cat_soup = get_subcats(soup)
                if cat_soup:
                    for i in cat_soup:
                        curl = getAbsUrl(current_url,i["href"])
                        ctitle = i["title"].capitalize()
                        if curl.startswith("https://www.costco.com"):
                            subcats.append({"url":curl,"cat":ctitle})

commit_data(get_data(),batch_size=100)