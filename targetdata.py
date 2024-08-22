from scrapetools import *
from products.models import AllProducts

start_url = "https://www.target.com"
my_proxy = getProxyWorking(start_url)

forb = ["redcard","target "," deals","subscript","browse","category","all "," all"]
page_count = 96

apis_data = "https://redsky.target.com/v1/plp/search/?count=%s&offset={0}&category=%s&sort_by=newest" % (str(page_count),"%s")
visited = set()

def get_cats():
    soup = getSoup(url=start_url,proxy=my_proxy)
    cat_soup = soup.select("a[href*=/c/]")
    useful = []
    for i in cat_soup:
        try:
            a = i["class"]
        except:
            label = i.text.strip().lower()
            if is_allowed(forb,label):
                url = getAbsUrl(start_url,i["href"])

                useful.append((label,url))
    return useful


def is_cat(soup,ur):
    data = soup.select("ul[data-test=pictureNavigationFeatured]")

    for current_cat_nav in data:
        current_title = current_cat_nav.parent.select("div h2")
        for k in current_title:
            k = k.text.strip().lower()
            if "by category" in k:
                temp = current_cat_nav.select("li a[href*=/c/]")

                return [{"cat":i.text.strip(),"url":getAbsUrl(ur,i["href"])} for i in temp]


    return False


def scrape_data(current_url):
    cat_id = current_url.split("N-")[-1]
    is_next = True
    current_api = apis_data % cat_id
    current_page = 1
    while is_next:
        is_next = False
        try:
            temp = getRawData(current_api.format( (current_page-1)*page_count ),
                                          json=True,proxy=my_proxy)["search_response"]["items"]
            current_api_page = temp["Item"]
        except:
            try:
                current_api_page = temp["item"]
            except:
                continue

        current_page+=1
        if not current_api_page:
            break

        is_next = True

        request = {}
        for current_item in current_api_page:
            try:
                request = {}

                request["SNR_Description"] = "Visit site to see description"
                temp = []

                try:
                    for i in current_item["bullet_description"]:
                        s = getSoup("<p>%s</p>" % i).text.strip()
                        temp.append(s)
                except:
                    pass

                if temp:
                    request["SNR_Description"] = parseHtml("\n".join(temp))

                current_desc = "Visit site to see description"


                img_data = current_item["images"][0]

                request["SNR_ImageURL"] = getAbsUrl(img_data["base_url"],img_data["primary"])

                try:
                    request["SNR_PriceBefore"] = current_item["list_price"]["min_price"]
                    if request["SNR_PriceBefore"] == 0.0:
                        request["SNR_PriceBefore"] = current_item["list_price"]["price"]
                except:
                    request["SNR_PriceBefore"] = -1.0

                try:
                    request["SNR_Price"] = current_item["offer_price"]["min_price"]
                    if request["SNR_Price"] == 0.0:
                        request["SNR_Price"] = current_item["offer_price"]["price"]
                except:
                    request["SNR_Price"] = -request["SNR_PriceBefore"]

                if request["SNR_Price"]<0:
                    continue
                elif request["SNR_Price"]==0:
                    pass

                if request["SNR_Price"]== request["SNR_PriceBefore"]:
                    request["SNR_PriceBefore"] = -1.0

                request["SNR_Title"] = parseHtml(current_item["title"])
                request["SNR_SKU"] = "TR"+current_item["tcin"]



                request["SNR_Price"] = current_item["list_price"]["min_price"]
                request["SNR_ProductURL"] = getAbsUrl(current_url,current_item["url"])
                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] = "Target"
                request["SNR_Condition"] = "00"

                try:
                    request["SNR_CustomerReviews"] = current_item["average_rating"]
                except:
                    request["SNR_CustomerReviews"] = 0.0

                request["SNR_Brand"] = "00"
                yield request
            except:
                pass

        if is_next and request:
            try:
                temp = AllProducts.objects.filter(SNR_SKU=request["SNR_SKU"]).count()
                if temp > 0:
                    is_next = False
            except Exception as e:
                print e
                pass



def get_data():
    cats_data = get_cats()

    for cat_label, cat_url in cats_data:

        temp_data = [{"cat":cat_label,"url":cat_url}]


        while temp_data:
            current_data = temp_data.pop()

            current_label = current_data["cat"]
            current_url = current_data["url"]
            if not is_allowed(forb,current_label):
                continue

            if current_url in visited:
                continue



            try:
                temp_index = current_url.rindex("?")
                current_url = cat_url[:temp_index]
            except:
                pass



            temp = scrape_data(current_url)
            for request in temp:
                request["SNR_Category"] = cat_label
                request["SNR_SubCategory"] = current_label
                yield request


            visited.add(current_url)



commit_data(get_data(),batch_size=50)