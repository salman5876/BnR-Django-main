import subprocess
from scrapetools import *
root_url = "http://www.kmart.com/"
start_url = "https://www.kmart.com/en_us/sitemap.html"

forb = ["deal","close","shop","gift","department","gift","sale","offer","view all"]
product_pat = "http://www.kmart.com/service/search/v2/productSearch?catgroupId={0}&levels={1}&pageNum=%s"
def get_cats_data():
    temp = False
    while not temp:
        soup = getSoup(getRawData(start_url))
        temp = soup.find("div",id="sitemap")
    cats_data = temp.select("ul.list-links li h2 a[href*=b-]")
    all_data = []

    for i in cats_data:
        cat_label = i.text.strip().capitalize()
        if not is_allowed(forb,cat_label):
            continue
        cat_url = getAbsUrl(start_url,i["href"])

        all_data.append( (cat_label,cat_url) )

    return all_data


def get_cat_soup(soup,ur):
    temp = soup.select("div.shcCatNavItem h3 a")
    if temp:
        temp = [(i.text.strip(),getAbsUrl(ur,i["href"]))  for i in temp]
    return temp


def is_post(data):

    try:
        temp = json.loads(next(
            re.finditer("catArray\s*:\s*(\[[^\]]+\]),",data)).group(1))

        return "+".join([escape(i) for i in temp])
    except:
        return False





def scrape_data(data):
    data_label, storeid,data_url = data
    is_next = True
    currentpage =1
    curl_pat = """curl 'http://www.kmart.com/service/search/price/json' -H 'Content-Type: application/json' -H 'Accept: application/json' -H $'Cookie: a=waryam' --data-binary '{"data":
%s,"storeId":"%s","zipcode":"","countryCode":"US","currencyCode":"USD"}' --compressed"""
    all_items = {}
    while is_next:
        is_next = False
        currenturl = data_url % str(currentpage)
        currentpage+=1
        a = req_session.cookies
        
        while True:
            try:
                current_data = getRawData(currenturl,json=True)["data"]["products"]
                break
            except Exception as e:
                is_next = False
                continue
            
        if current_data:
            is_next = True
        else:
            continue
        
        
        for current_item in current_data:
            request = {}
            pid = current_item["partNumber"]
            sin = current_item["sin"]
            pbType = current_item["pbType"]
            request["SNR_ModelNo"] = "00"
            
            try:
                request["SNR_UPC"] = current_item["upc"]
                if not request["SNR_UPC"]:
                    raise Exception("saas")
            except:
                request["SNR_UPC"] = "00"
            
            request["SNR_Available"] = "Kmart"
            request["SNR_Description"] = "Visit site to see description"
            request["SNR_SKU"] = "KM" + sin
            request["SNR_Title"] = current_item["name"]
            request["SNR_Category"] = data_label
            request["SNR_SubCategory"] = data_label
            request["SNR_Condition"] = "00"
            
            try:
                request["SNR_CustomerReviews"] = float(current_item["rating"])
            except:
                request["SNR_CustomerReviews"] = 0.0
            
            request["SNR_ProductURL"] =getAbsUrl(start_url,current_item["url"])
            request["SNR_ImageURL"] = current_item["image"]
            request["SNR_Brand"] = "No Brand"
            try:
                request["SNR_Brand"] = current_item["brandName"]
                if not request["SNR_Brand"]:
                    raise Exception("saas")
            except:
                request["SNR_Brand"] = "No Brand" 
                
            all_items["{0}\t{1}\t{2}".format(pid,sin,pbType)] = request
    
    
    keys = list(all_items.iterkeys())
    
    alldata = {}
    
    while keys:
        temp = keys[:10]
        keys = keys[10:]
        data = []
        for i in temp:
            pid,sin,pbType = i.split("\t")
            alldata[pid] = all_items[i]
            data.append({"pid":pid,"ssin":sin,"pidType":pbType})
        try:
            c = curl_pat %(json.dumps(data),storeid)
            p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            output = json.loads(output)
            a= list(output.iterkeys())
            allitems = []
            for id in a:
                try:
                    request = alldata[id]
                    prices_data= output[id]["priceDisplay"]["response"][0]["prices"]
                    request["SNR_Price"] = prices_data["finalPrice"]["min"]
                    try:
                        request["SNR_PriceBefore"] = prices_data["regularPrice"]["min"]
                    except:
                        request["SNR_PriceBefore"] = -1.0

                    if request["SNR_PriceBefore"] == request["SNR_Price"]:
                        request["SNR_PriceBefore"] = -1.0
                        
                    allitems.append(request)
                    
                    
                except:
                    pass

            if allitems:
                commit_data(allitems)
        except:
            pass
    
    
    
def get_data():
    cats_data = get_cats_data()
    
    all_data = []

    for cat_label, cat_url in cats_data:
        raw = getRawData(cat_url,obj=True)
        cat_url = raw.url
        raw = raw.text
        label = is_post(raw)
        data = False

        try:
            temp = cat_url.rindex("/")
            temp = cat_url[temp+1:]
            temp = temp.split("b-")[-1]
            temp2 = patSearch("""storeId\s*:\s*["'](\d+)["']""",raw).group(1)
        except Exception as e:
            continue

        if not label:
            try:

                label = getRawData(
                    "http://www.kmart.com/browse/services/v1/hierarchy/fetch-paths-by-id/%s?clientId=obusearch" % temp,obj=True).json()
                label = label["data"][0]["catgroups"][0]["namePath"].replace(" ","+")

            except Exception as e:
                continue



        if label:
            all_data.append((cat_label,temp2,product_pat.format(temp,label)))
            
    if all_data:
        with ProcessPoolExecutor(max_workers=5) as executor:
            future = executor.map(scrape_data, all_data, chunksize=4)
            executor.shutdown(wait=True)




get_data()