# import socket
# import socks
# ip='127.0.0.1' # change your proxy's ip
# port = 9150 # change your proxy's port
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
# socket.socket = socks.socksocket


from scrapetools import *
proxy = getProxyWorking()
start_url = "https://www.amazon.com/gp/site-directory"

temp_url = 'https://www.amazon.com/b/ref=s9_acss_bw_cg_wdresnav_2c1_w?_encoding=UTF8&node=2346728011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=5M1MN2X4QVW8B15RX4KK&pf_rd_r=5M1MN2X4QVW8B15RX4KK&pf_rd_t=101&pf_rd_p=eb5b44b5-1205-563e-acf8-186f9156ec8c&pf_rd_p=eb5b44b5-1205-563e-acf8-186f9156ec8c&pf_rd_i=1045024'

forb = ["Clothing, shoes, jewelry & watches", "Women"]

r_t ="Robot Check"


def appendLog(data):
    try:
        with open("amlog.txt","a") as w:
            w.write(re.sub("\?.*","",data)+"\n")
    except Exception as e:
        pass

visited = []
try:
    with open("amlog.txt") as w:
        visited = w.read().split("\n")
except:
    pass

def get_cats_Data():
    raw = getRawData(temp_url,proxy= proxy)
    if "did not match any products" in raw:
        return []
    soup = getSoup(raw)
    post_soup = get_post_soup(soup)

    commit_data(get_data_all(
        scrape_data(post_soup, start_url),
        'Women Clothing', 'Dresses'), batch_size=500)





def get_cats():
    raw = getRawData(start_url,proxy= proxy)
    if "did not match any products" in raw:
        return []
    soup = getSoup(raw)
    cat_soup = soup.select("div.fsdContainerWrapper div.fsdColumn div.fsdDeptBox")
    all_data = []
    for i in cat_soup:

        cat_label = i.select_one("h2.fsdDeptTitle").text.strip().capitalize()
        print cat_label
        if is_allowed(forb,cat_label):
            print 'INNNNNNNNNNNNn'
            links_div = i.select("div.fsdDeptCol a.fsdDeptLink")

            for link in links_div:
                current_label = link.text.strip().capitalize()
                print 'Subbbbbb' , current_label
                if is_allowed(forb,current_label):
                    current_link = getAbsUrl(start_url,link["href"])
                    all_data.append((cat_label,current_label,current_link))

    return all_data



def get_post_soup(soup):
    temp = soup.select_one("div#rightResultsATF")
    if not temp:
        temp = soup.select_one("div[id*=search-results]")

    return temp


def scrape_data(soup,url):
    is_next = True
    while is_next:
        is_next = False
        try:
            items_div = soup.select("ul.s-result-list li[id*=result] div.s-item-container")
        except:
            break


        for current_item_div in items_div:
            request = {}
            try:
                request["SNR_SKU"] = "AZ" + current_item_div.parent["data-asin"]

                image_div = current_item_div.select_one("img.s-access-image")

                try:
                    temp =  re.split(",\s+",image_div["srcset"])[-1]
                    request["SNR_ImageURL"] = temp.split(" ")[0].strip()
                except:
                    request["SNR_ImageURL"] = image_div["src"]
                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] = "Amazon"
                request["SNR_Description"] = "Visit site to see description"
                request["SNR_Title"] = image_div["alt"]
                link_div = current_item_div.select_one("a.s-access-detail-page")

                request["SNR_ProductURL"] = getAbsUrl(url,link_div["href"])



                request["SNR_Condition"] = "00"
                try:
                    temp = patSearch("Suggested\s+[^\$]+\$([\d\.,]+)",item_raw).group(1).replace(",","")
                    request["SNR_PriceBefore"] = float(temp)
                except:
                    request["SNR_PriceBefore"] = -1



                try:
                    request["SNR_CustomerReviews"] = float(
                        current_item_div.select_one("i[class*=a-star] span.a-icon-alt").text.strip().split("out of")[0].strip()
                    )
                except:
                    request["SNR_CustomerReviews"] = 0.0





                item_raw = str(current_item_div)
                brand ="No Brand"

                try:
                    temp = patSearch("by\s+</span><span[^>]+>(\w+)<",item_raw).group(1)
                    brand = temp
                except:
                    pass

                request["SNR_Brand"] = brand
                price_div = current_item_div.select_one("span.sx-price")
                try:
                    price = price_div.select_one("span.sx-price-whole").text.strip()

                    try:
                        temp = ".%s" % price_div.select_one("sup.sx-price-fractional").text.strip()
                        price += temp
                    except Exception as e:
                        pass

                except:
                    try:
                        price = patSearch('a-color-base">\$([\.\d\,]+)',item_raw).group(1)
                    except:
                        temp = current_item_div("span.acs_product-price__buying").text.strip()
                        price = 0.0
                        if temp:
                            try:
                                price = patSearch("\$([\d\.,]+)",temp).group(1)
                            except:
                                if "FREE" not in temp:
                                    continue

                request["SNR_Price"] = float(price.replace(",",""))

                yield request

            except Exception as e:
                pass



        try:
            next_div = soup.select_one("a#pagnNextLink")["href"]
        except:
            break


        if next_div:
            url = getAbsUrl(url,next_div)
            raw = getRawData(url,proxy= proxy)
            if "did not match any products" not in raw:
                soup = get_post_soup(getSoup(raw))
                is_next = True


def get_subcat_urls(soup,url):
    all_data = []


    try:

        if False:
            pass

        else:
            data_soup = soup.select_one("div[aria-label*=Categories] div#leftNav")
            if data_soup:
                data_soup = soup.select("ul[class*=-indent-] div[aria-live=polite] li span.a-list-item a")

            if data_soup:
                for i in data_soup:
                    cl = i.text.strip().capitalize()
                    if is_allowed(forb,cl):
                        all_data.append({"url":getAbsUrl(url,i["href"]),"cat":i.text.strip().capitalize()} )
                if all_data:
                    return all_data
            try:
                temp = str(soup)
                temp_index = temp.index('"faceoutConfig"')
                temp = temp[temp_index:temp.rindex("</script")]
                temp_index = temp.index("[")
                temp = temp[temp_index:]
                return  [ {"cat":i["value"].capitalize(),"url":getAbsUrl(url,i["redirectLink"])}
                    for i in getJsonData(temp)]
            except Exception as e:
                data_soup = soup.select("div.bxc-grid__content div.bxc-grid__image a")

                if data_soup:
                    return [{"cat": i.img["alt"].split("Shop ")[-1].strip().capitalize(), "url": getAbsUrl(url, i["href"])}
                            for i in data_soup]
                data_soup = soup.select("div.left_nav ul li a")
                if data_soup:
                    for i in data_soup:
                        cl = i.text.strip().capitalize()
                        if is_allowed(forb, cl):
                            all_data.append({"url": getAbsUrl(url, i["href"]), "cat": i.text.strip().capitalize()})

                if all_data:
                    return all_data




        if not all_data:
            data_soup = soup.select("a.acswidget-carousel__seemore")

            if not data_soup:
                data_soup = soup.select_one("div[class*=carousels-container] div[id*=category]").select(
                    "div.acs_tile a[href*=a-link]")

            if data_soup:
                all_data = [{"url":getAbsUrl(url,i["href"]),"cat":i.text.capitalize().replace("See all","").strip()} for i in data_soup]


        if not all_data:
            data_soup = soup.select("a.list-item__category-link")

            if data_soup:
                all_data = [{"url":getAbsUrl(url,i["href"]),"cat":i.text.capitalize().replace("See all","").strip()} for i in data_soup]

    except Exception as e:
        if data_soup:
            all_data = [{"url": getAbsUrl(url, i["href"]), "cat": i.text.capitalize().replace("See all", "").strip()} for i in data_soup]

    if not all_data:
        cor = soup.select_one("div.a-carousel-container")
        if cor:
            all_data =[
                {"url": getAbsUrl(url, i["href"]), "cat": i.text.capitalize().strip()} for i in cor.select("a[id*=cat-]")
            ]

    return all_data


def get_data_all(dt,cat,subcat):
    for request in dt:
        request["SNR_Category"] = cat
        request["SNR_SubCategory"] = subcat
        yield request
#all_visited = set()
def extract_data(elem):
    all_visited = set()
    cat_label, subcat_label, cat_url = elem
    current_urls = [{"url": cat_url, "cat": cat_label}]

    while current_urls:
        temp = current_urls.pop()
        url_temp = temp["url"]
        if "/samples/" in url_temp:
            continue

        if "redirect.html" in url_temp:
            continue

        if url_temp not in all_visited:
            cat_temp = temp["cat"]
            n = True
            count=0

            while n:
                n = False
                try:
                    raw = getRawData(url_temp,proxy= proxy)
                    if "did not match any products" in raw:
                        break
                    current_soup = getSoup(raw)
                except Exception as e:
                    if count<3:
                        n = True
                        count+=1

                page_soup = get_post_soup(current_soup)
                temp = get_subcat_urls(current_soup, url_temp)

                if page_soup:
                    if is_allowed(forb, cat_temp):
                        if cat_temp == cat_label:
                            cat_temp = subcat_label

                        commit_data(get_data_all(
                            scrape_data(page_soup,url_temp),
                            cat_label,cat_temp),batch_size=500)
                elif temp:
                    temp.extend(current_urls)
                    current_urls = temp
                else:
                    if count<3:
                        n = True
                        count+=1
                    if "/dp/" not in url_temp and "/gp/" not in url_temp and "/coin/" not in url_temp:
                        with open("amazonurlex.txt","a") as w:
                            w.write(url_temp+"\n")
                    else:
                        break


            all_visited.add(url_temp)


    return elem[-1]
import itertools
def get_data():
    cats_data = [i for i in get_cats() if re.sub("\?.*","",i[-1]) not in visited]
    print cats_data
    def par():
        with ProcessPoolExecutor(max_workers=3) as executor:
            future = executor.map(extract_data, cats_data,chunksize=3)
            for i in future:
                appendLog(i)
            executor.shutdown(wait=True)

    def serial():
        for i in imap(extract_data, cats_data):
            appendLog(i)
    serial()


u = "https://www.amazon.com/s/ref=lp_979455011_nr_n_8?fst=as%3Aoff&rh=n%3A468642%2Cn%3A%2111846801%2Cn%3A979455011%2Cn%3A10111205011&bbn=979455011&ie=UTF8&qid=1519628449&rnid=979455011"

#a = get_subcat_urls(getSoup(url=u),u)
#b=""

get_cats_Data()