import re

from scrapetools import *

start_url = "https://www.isnorkel.com/"
top_cat = "Sporting Goods".capitalize()

def get_cats():
    cat_links = getSoup(url=start_url).find("div",id="SideCategoryList").select("ul.sf-menu li a")


    subcats = {}
    for i in cat_links:
        temp = i.text.capitalize()
        if temp != "All":
            if i["href"][-1] == "/":
                i["href"] = i["href"][:-1]
        try:
            a = int(i["href"][-1])
        except:
            subcats[temp] = i["href"]
    return subcats
def scrape_url(ur):
    is_next = True
    currentpage = 1
    current_url = ur
    while is_next:
        is_next = False

        main_container = getSoup(url=current_url).find("div",id="LayoutColumn1",class_="Content")
        products_div = main_container.find("ul",class_="ProductList")



        all_items_div = products_div.find_all("div",class_="cover")
        for single_item_div in all_items_div:
            try:
                request = {
                    "SNR_Available": "ISnorkel",
                    "SNR_PriceBefore": -1.0,
                    "SNR_UPC": "00",
                    "SNR_ModelNo": "00",
                    "SNR_Condition" : "00"
                }
                image_div = single_item_div.find("div",class_="ProductImage")
                d_product = image_div["data-product"]
                image_div = image_div.find("a")

                request["SNR_ProductURL"] = image_div["href"]
                inside_soup = getSoup(url=request["SNR_ProductURL"]).find("div",id="ProductDetails")
                image_div = image_div.find("img")


                request["SNR_Title"] = parseHtml(single_item_div.select_one('div.ProductDetails strong a').text.strip() )
                id_pat = "/products/{0}/images/(\d+)/".format(d_product)

                try:
                    request["SNR_SKU"] = "IS" + inside_soup.find("span",class_="VariationProductSKU").text.strip()
                except:
                    request["SNR_SKU"] = "IS" + next(re.finditer(id_pat, image_div["src"])).group(1)


                try:
                    request["SNR_ImageURL"] = inside_soup.select_one("div.ProductThumbImage a[rel=prodImage]")["href"]
                except:
                    request["SNR_ImageURL"] = image_div["src"]

                try:
                    request["SNR_Brand"] = parseHtml(inside_soup.select_one("div.Value h4.BrandName a").text.strip())
                except:
                    request["SNR_Brand"] = "00"

                try:
                    request["SNR_Description"] = inside_soup.select_one("div#ProductDescription div.ProductDescriptionContainer").text.strip()
                except:
                    request["SNR_Description"] = "Visit site to see description"


                price_rate_div = single_item_div.find("div",class_="ProductPriceRating")
                temp = price_rate_div.find("strong")
                request["SNR_Price"] = float(temp.text.replace("$","").replace(",",""))

                request["SNR_CustomerReviews"] = 0.0
                try:
                    rating_div = price_rate_div.find("span", class_="Rating")["class"]
                    for i in rating_div:
                        try:
                            i = int(i[-1])
                            request["SNR_CustomerReviews"] = float(i)
                            break
                        except:
                            pass
                except:
                    pass
                yield request
            except:
                pass

        try:
            next_div = main_container.find("div",id="CategoryPagingBottom",class_="PagingBottom").select("li a")
            currentpage+=1
            for i in next_div:
                try:
                    if currentpage == int(i.text.strip()):
                        current_url = i["href"]
                        is_next = True
                        break
                except:
                    pass
        except:
            pass


def get_data():
    sub_cats = get_cats()

    for subcat_label, subcat_url in sub_cats.iteritems():
        data = scrape_url(subcat_url)

        for i in data:
            i["SNR_Category"] = top_cat
            i["SNR_SubCategory"] = subcat_label
            yield i





commit_data(get_data())