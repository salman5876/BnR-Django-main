from scrapetools import *

start_url = "https://www.samsclub.com/sams/all-products/100001.cp?xid=hdr_shop1_all-departments"

forb = ["shop","club","photo","new ","gift","seasonal","member"]

def get_start_data():
    cat_data = getSoup(url=start_url).select_one("ul.subcategories").select("a[href*=.cp]")
    cats_links = [(i.text.strip(),getAbsUrl(start_url,i["href"].split(";jsess")[0]))  for i in cat_data]
    cats = [i for i in cats_links if is_allowed(forb,i[0])]
    return cats

def get_data():
    cats_data = get_start_data()

    