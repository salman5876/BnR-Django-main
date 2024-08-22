from scrapetools import *
from datetime import datetime as dt

MinuteNow = dt.now()
proxy = getProxyWorking()

def TimeStatus():
    global MinuteNow
    minute = dt.now()
    timeDiff = minute - MinuteNow
    difference = timeDiff.total_seconds() / 60
    if difference > 10:
        MinuteNow = dt.now()
        return True
    return False

def ProxyTimeTest():
    global proxy
    if TimeStatus():
        proxy = getProxyWorking()

# proxy = getProxyWorking()
start_url = 'https://www.amazon.com/gp/site-directory'


###################################################   Collecting Category URLs to File    ######################################################



CategoryList = ['Electronics, computers & office']

def appendLog(data):  #############  Appending URLs in File #############
    try:
        with open("AmazonElectronicsURLs.txt","a") as w:
            w.write(data+"\n")
            print data
    except Exception as e:
        pass


def get_cats():  ################### Getting All Category and SubCategory Links ############################
    ProxyTimeTest()
    raw = getRawData(start_url,proxy= proxy)
    if "did not match any products" in raw:
        return []
    soup = getSoup(raw)
    cat_soup = soup.select("div.fsdContainerWrapper div.fsdColumn div.fsdDeptBox")
    all_data = []
    for i in cat_soup:

        cat_label = i.select_one("h2.fsdDeptTitle").text.strip().capitalize()
        print cat_label
        if is_allowed(CategoryList,cat_label):
            print 'INNNNNNNNNNNNn'
            links_div = i.select("div.fsdDeptCol a.fsdDeptLink")

            for link in links_div:
                current_label = link.text.strip().capitalize()
                print 'Subbbbbb' , current_label

                current_link = getAbsUrl(start_url,link["href"])
                all_data.append((cat_label,current_label,current_link))

    return all_data

def extract_data(elem):  ########### Requesting each Category URL #################
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
                    ProxyTimeTest()
                    raw = getRawData(url_temp,proxy= proxy)
                    if "did not match any products" in raw:
                        break
                    current_soup = getSoup(raw)
                except Exception as e:
                    if count<3:
                        n = True
                        count+=1

                SubCat(current_soup,url_temp,subcat_label)


def get_data():  ############ Main Function to get Category URLs and then extracting URLs one by one ##################
    cats_data = [i for i in get_cats()]
    print cats_data

    def serial():
        for i in imap(extract_data, cats_data):
            pass
    serial()


def getSub_Cat(url,cat):  ######## Sub Function to get SubCat URLs ################
    all_data1 = []
    all_data2 = []
    ProxyTimeTest()
    url1 = getRawData(url, proxy=proxy)
    soup1 = getSoup(url1)
    data_soup1 = soup1.select_one("div[aria-label*=Categories] div#leftNav")
    if data_soup1:
        try:
            data_soup1 = soup1.select("ul.s-ref-indent-one")
            data_soup1 = data_soup1[1].select("div[aria-live=polite] li span.a-list-item a")
        except:
            data_soup1 = soup1.select("ul.s-ref-indent-two")
            data_soup1 = data_soup1[0].select("div[aria-live=polite] li span.a-list-item a")

    if data_soup1:
        for i in data_soup1:
            cl1 = i.text.strip().capitalize()
            all_data1.append({"url": getAbsUrl(url, i["href"]), "Cat": cat, "SubCat": cl1})

        if all_data1:
            for k in all_data1:
                ProxyTimeTest()
                url2 = getRawData(k['url'], proxy=proxy)
                soup2 = getSoup(url2)
                data_soup2 = soup2.select_one("div[aria-label*=Categories] div#leftNav")
                try:
                    data_soup2 = soup2.select("ul.s-ref-indent-one")
                    data_soup2 = data_soup2[2].select("div[aria-live=polite] li span.a-list-item a")
                    for l in data_soup2:
                        cl2 = l.text.strip().capitalize()
                        all_data2.append({"url": getAbsUrl(k['url'], l["href"]), "Cat": k['Cat'], "SubCat": cl2})

                    # print all_data1
                    all_data1.remove(k)
                except:
                    pass

            for m in all_data2:
                all_data1.append(m)



        return all_data1

def SubCat(soup,url,subcat): ############## Getting All URLs for every Category. ##################
    all_data = []
    all_data1 = []
    all_data2 = []
    data_soup = soup.select_one("div[aria-label*=Categories] div#leftNav")
    if data_soup:
        data_soup = soup.select("ul[class*=-indent-] div[aria-live=polite] li span.a-list-item a")

    if data_soup:
        for i in data_soup:
            cl = i.text.strip().capitalize()
            all_data.append({"url": getAbsUrl(url, i["href"]), "cat": cl})
        if all_data:
            for j in all_data:
                # print j
                try:
                    all_data1 =[i for i in getSub_Cat(j['url'],j['cat'])]
                    for data in all_data1:
                        all_data2.append(data)
                except:
                    all_data1 = {'SubCat': j['cat'], 'url': j['url']}
                    all_data2.append(all_data1)

            if all_data1:
                print all_data2
                for k in all_data2:
                    appendLog(str(subcat + ','+ k['SubCat'] + ',' + k['url']))
                    # appendLog(str(j['url']))
                # raw = getRawData(j['url'], proxy=proxy)
                # souup = getSoup(raw)


####################################################################### Scraping Data after fetching URLs From File. #############################################################

def get_data_Textfile():
    data=[]
    with open('AmazonElectronicsURLs.txt', 'r') as f:

        data = [i.split(',') for i in f]
        for j in data:
            j[len(j)-1] = j[len(j)-1][:-1]
        print data

        for k in data:
            Data_Scraper2(k)

        return 'Completed'


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
            ProxyTimeTest()
            raw = getRawData(url,proxy= proxy)
            if "did not match any products" not in raw:
                soup = get_post_soup(getSoup(raw))
                is_next = True

def get_data_all(dt,cat,subcat):
    for request in dt:
        request["SNR_Category"] = cat
        request["SNR_SubCategory"] = subcat
        yield request


def get_post_soup(soup):
    temp = soup.select_one("div#rightResultsATF")
    if not temp:
        temp = soup.select_one("div[id*=search-results]")

    return temp


def Data_Scraper(data):
    print ','.join(data[1:-1])
    ProxyTimeTest()
    raw = getRawData(data[len(data)-1],proxy= proxy)
    if "did not match any products" in raw:
        return []
    soup = getSoup(raw)
    post_soup = get_post_soup(soup)

    commit_data(get_data_all(
        scrape_data(post_soup, start_url),
        data[0], ','.join(data[1:-1])), batch_size=500)


def Data_Scraper2(elem):
    all_visited = set()
    # cat_label, subcat_label, cat_url = elem
    current_urls = [{"url": elem[len(elem)-1], "cat": ','.join(elem[1:-1])}]

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
                    ProxyTimeTest()
                    raw = getRawData(url_temp,proxy= proxy)
                    if "did not match any products" in raw:
                        break
                    current_soup = getSoup(raw)
                except Exception as e:
                    if count<3:
                        n = True
                        count+=1

                page_soup = get_post_soup(current_soup)
                # temp = get_subcat_urls(current_soup, url_temp)

                if page_soup:
                    if cat_temp == ','.join(elem[1:-1]):
                        cat_temp = ','.join(elem[1:-1])

                    commit_data(get_data_all(
                        scrape_data(page_soup,url_temp),
                        ','.join(elem[1:-1]),','.join(elem[1:-1])),batch_size=200)
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

get_data() #for getting category URLs

# get_data_Textfile()
# urrr = 'https://www.amazon.com/s/ref=lp_6427814011_ex_n_1?rh=n%3A468642&bbn=468642&ie=UTF8&qid=1544077115'
#
# rawda = getRawData(urrr, proxy = proxy)
# current_soup = getSoup(rawda)
# SubCat(current_soup, urrr,'Playstation 4')
# ProxyTimeTest()
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
#
# # print fuzz.ratio("ABDULLAH","abdullah")
# # print fuzz.partial_ratio("Catherine M. Gitau","Catherine Gitau")
# choices = ["Abdullah Naeem", "ABDULLAH NAEEM", "Naeem Abdullah", "NAEEM ABDULLAH", "Yasir", "Ali"]
# print process.extract("abdullahnaeem", choices, limit=6, scorer=fuzz.token_sort_ratio)