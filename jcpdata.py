from scrapetools import *


start_url = "https://www.jcpenney.com/"
my_proxy = getProxyWorking(start_url)
cat_mapping = {
    "For the Home".capitalize() : "Home & Garden".capitalize(),
    "Bed & Bath".capitalize() : "Home & Garden".capitalize(),
    "Window".capitalize() : "Home & Garden".capitalize(),
    "Lingerie": "Women",
     "Juniors" : "Kids & Baby".capitalize(),
    "Kids": "Kids & Baby".capitalize(),
    "Baby": "Kids & Baby".capitalize(),
    "Handbags": "Handbags & Purses".capitalize(),
    "jewelry".capitalize(): "Jewelry and Watches".capitalize()

}

forb_array = ["Helpful".lower(),"Inform".lower(),
              "Promot".lower(),
              "Brand".lower(),"Size".lower(),
              "all","feature","deal"
              ]

def get_cats():
    u = 'desktopDepartmentVisualNav":'
    temp_url = start_url
    for i in range(2):
        raw_data = getRawData(url=temp_url,proxy=my_proxy,headers={})
        temp = raw_data
        raw_data = raw_data[raw_data.index(u)+len(u):]
        raw_data = raw_data[:raw_data.index("</script")]
        data = getJsonData(raw_data)[:-2]
        if data:
            return [ (map_data(cat_mapping,j["title"]),urlparse.urljoin(start_url,j["links"])) for j in data]
        temp_url = "https://www.jcpenney.com/g/shower-curtains/N-bwo3wD1nopgs"


def get_sub_cat(soup):
    data = soup.find("div",class_="DepartmentVisualLeftNav-departmentVisualLeftNav")
    if data:
        items_all_data = data.select("ul li a")
        items = []

        for i in items_all_data:
            items.append({"cat":i.text.strip(),"url":i["href"]})
    return False


def scrape_data(ur,raw_data):
    next_pat = '"pagination":'
    is_next = True
    current_page = 1
    data_pat = '"preservedProducts":'
    raw_data = raw_data[raw_data.index("<script"):raw_data.rindex("</script")]
    img_path_path = 'https://s7d4.scene7.com/is/image/JCPenney/{0}?wid=600&hei=600&op_usm=.4,.8,0,0&resmode=sharp2'
    while is_next:
        is_next = False
        temp = raw_data[raw_data.index(data_pat)+len(data_pat):]
        data = getJsonData(temp)

        all_data = []

        for i in data:
            try:
                all_data.extend( i["productList"])
            except:
                pass

        data = all_data

        all_data = []
        for current_item in data:
            try:
                request = {
                    "SNR_Condition":"00",
                    "SNR_Description":"Visit site to see description",
                    "SNR_Available" : "JCpenney".upper(),
                    "SNR_UPC" : "00",
                    "SNR_ModelNo": "00"
                }

                temp = current_item["imagesInfo"]

                try:
                    request["SNR_ImageURL"] = img_path_path.format(temp['colorizedImageId'])
                except:
                    request["SNR_ImageURL"] = img_path_path.format(next(temp.iterkeys()))

                request["SNR_Title"] = parseHtml(current_item["name"])

                try:
                    request["SNR_Brand"] = parseHtml(current_item["brand"])
                except:
                    request["SNR_Brand"] = "00"

                request["SNR_CustomerReviews"] = 0.0

                try:
                    temp = float(current_item["originalMin"])
                    temp = float( "%0.2f" % temp )
                    request["SNR_PriceBefore"] = temp
                except:
                    request["SNR_PriceBefore"] = -1.0

                temp = float(current_item["currentMin"])
                temp = float("%0.2f" % temp)
                request["SNR_Price"] = temp


                try:
                    temp = current_item["averageRating"]
                    temp = float( "%0.2f" % temp )
                    request["SNR_CustomerReviews"] = temp
                except:
                    pass

                request["SNR_SKU"] = "JCP"+current_item["skuId"]
                request["SNR_ProductURL"] = "https://www.jcpenney.com" + current_item["pdpUrl"]

                all_data.append(request)
            except:
                pass


        try:
            t_index = raw_data.index(next_pat)+len(next_pat)

            raw_data = raw_data[t_index:]
            next_obj = getJsonData(raw_data,"{","}")
            if next_obj["hasNextPage"]:
                is_next = True
                current_page += 1
                t_url = ur+"?page={0}".format(current_page)

                raw_data = getRawData(proxy=my_proxy, url=t_url, headers={})
                raw_data = raw_data[raw_data.index("<script"):raw_data.rindex("</script")]

            yield  all_data
        except:
            pass





def get_data():
    cats = get_cats()

    for cat_label, cat_url in cats:
        temp = [{"cat":cat_label,"url":cat_url}]

        while temp:
            single_item = temp.pop()
            current_url = single_item["url"]
            subcat_label = single_item["cat"]
            try:
                t_index = current_url.rindex("?")
                current_url = current_url[:t_index]
            except:
                pass

            data = getRawData(proxy=my_proxy,url=current_url,headers={})
            single_soup = getSoup(data)
            subs = get_sub_cat(single_soup)

            if subs:
                temp.extend(subs)
            else:
                cat_data = scrape_data(current_url,data)
                for data_array in cat_data:
                    for data_item in data_array:
                        data_item["SNR_Category"] = cat_label
                        data_item["SNR_SubCategory"] = subcat_label
                        yield data_item

commit_data(get_data())