from scrapetools import *

start_url = "http://store.hp.com"

forb = ["offer","support"]

api_url = "http://store.hp.com/api/es/product/v2/search?aggregates%5Bprice%5D=1&filters%5Bcat%5D={0}&from=0&size=10000&sort%5Brank.default%5D=asc"
def get_cat():
    soup = getSoup(url=start_url).select("div.hf_top_menu ul li a[class*=level1-]")
    a =[i["href"] for i in soup]
    print ""


def scrape_bus(ur):
    pass