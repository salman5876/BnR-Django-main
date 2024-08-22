from scrapetools import *

start_url = "https://www.beallsflorida.com/"
my_proxy = getProxyWorking("https://www.beallsflorida.com/")
print my_proxy
cat_mapping = {
    "For Home".capitalize() : "Home & Garden".capitalize(),
    "Bed & Bath".capitalize() : "Home & Garden".capitalize(),
    "Petites" : "Women",
    "Plus Size".capitalize() : "Fashion",
    "Lingerie": "Women",
    "Juniors".capitalize() : "Kids & Baby".capitalize(),
    "Kids".capitalize(): "Kids & Baby".capitalize()
}

forb = ["clearance"]
def page_soup(soup):
    return soup.select_one("div#Search_Result_div")


def scrape_data(soup,url):
    is_next = True

    while is_next:
        is_next = False

        items_div = soup.select_one("div#category-area div#display-area").find_all("div",class_="item-block")

        for item in items_div:
            try:
                request = {}

                price_div = item.find("div",class_="item-price")
                rating_starts = item.select("div.pr-rating-stars div[aria-checked=true]")
                image_div = item.select_one("div.item-image a.item-img-link")

                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] = "Beallsflorida"
                request["SNR_Description"] = "Visit site to see description"
                request["SNR_SKU"] = "BAF" + image_div["id"].split("_")[-1]
                request["SNR_ProductURL"] = getAbsUrl(url,image_div["href"])
                image_div = image_div.find("img",class_="item-img")
                request["SNR_Title"] = image_div["alt"]
                image_div = image_div["src"]
                request["SNR_Condition"] = "00"
                request["SNR_PriceBefore"] = -1.0
                before_div = price_div.find("div",class_="price-reg")
                after_price = price_div.find("div",class_="price").text.strip()

                if before_div:
                    request["SNR_PriceBefore"] = float(patSearch("\$([\d\.]+)",before_div.text.strip()).group(1))

                request["SNR_Price"] = float(patSearch("\$([\d\.]+)", after_price).group(1))
                request["SNR_CustomerReviews"] = 0.0

                if rating_starts:
                    request["SNR_CustomerReviews"] = float( len(rating_starts))

                if image_div.startswith("//"):
                    image_div = "https:" + image_div

                request["SNR_ImageURL"] = image_div


                request["SNR_Brand"] = "No Brand"

                yield request
            except:
                pass
        next_div = soup.select_one("span.icon-page-next")

        if next_div:
            next_div = next_div.parent["href"]
            is_next = True
            url = getAbsUrl(url,next_div)
            soup = page_soup(getSoup(getRawData(url,proxy=my_proxy)))

            if not soup:
                break

def get_data():
    cat_raw = getRawData(start_url,proxy=my_proxy)
    cat_soup = getSoup(cat_raw).select("a.main-nav-link")
    cats = []

    for i in cat_soup:
        temp ="#"
        try:
            temp = i["data-href"]
        except:
            try:
                temp = i["href"]
            except:
                pass

        if not temp.startswith("#"):
            temp2 = i.text.strip().capitalize()
            if is_allowed(forb,temp2):
                temp2 = map_data(cat_mapping,temp2)
                cats.append(
                    (temp2, temp)
                )


    for cat_label, cat_url in cats:
        temp = [{"label":cat_label,"url":cat_url}]

        while temp:
            current = temp.pop()
            current_url = current["url"]
            current_label = current["label"]
            current_raw = getRawData(current_url,proxy=my_proxy)
            current_soup = getSoup(current_raw)

            posts_soup = page_soup(current_soup)

            if posts_soup:
                data = scrape_data(posts_soup,current_url)
                for request in data:
                    request["SNR_Category"] = cat_label
                    request["SNR_SubCategory"] = current_label.capitalize()
                    yield request
            else:
                try:
                    c = '#js-dynamic-left-nav").addClass("contentLoaded").load("'
                    temp_index = current_raw.index(c)+len(c)
                    temp_data = current_raw[temp_index:]
                    c = "&viewtype=desktop"
                    temp_index = temp_data.index(c) + len(c)
                    temp_data = temp_data[:temp_index]
                    temp_url = getAbsUrl(current_url,temp_data)
                    current_cats = getRawData(url=temp_url,proxy=my_proxy)
                    cats_data = getSoup(current_cats).select("div[data-toggle-id=left-nav-toggle-category] a")
                    for c in cats_data:
                        curl = c["href"]
                        clabel = c.text.strip()
                        clabel = re.split("\(\d+\)",clabel)[0].strip().capitalize()
                        if is_allowed(forb,clabel):
                            if not curl.startswith("#"):
                                temp.append({"label":clabel, "url": curl} )
                except Exception as e:
                    pass

commit_data(get_data())