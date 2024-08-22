import requests
import urllib
from bs4 import BeautifulSoup
from urlparse import urljoin
from urlparse import urlsplit
j=0
def get_url_iter(i):
    my_url="https://www.samsclub.com/sams/instant-savings-book/6930116.cp?pageView=grid&searchCategoryId=6930116&xid=hdr_shop1_instant-savings&totalLimit=48&offset="+str(i)+"&navigate=1&recordType=all"
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    r = requests.get(my_url, headers=agent)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find("title").text)
    all_deals= soup.findAll("div",{"class":"products-card"})
    for deals in all_deals:
        produt_url= urljoin("https://www.samsclub.com/",deals.find("a")["href"])
        print("product url "+produt_url)
        product_title=deals.find(class_="img-text").text
        print("product title: "+product_title)
        try:
           product_img=deals.find(class_="cardProdImg")["data-src"]
           print("product image :"+urljoin("https://www.samsclub.com",product_img))
        except:
           pass
        try:
           bef_price=deals.find(class_="strike-price").text[1:]
           print("product Before price: "+bef_price)
        except:
           pass
        try:
           after_price=deals.find(class_="sc-dollars-v2").text+"."+deals.find(class_="sc-cents-v2").text
           print("after price: "+after_price)
        except:
           pass
        try:
            prod_id=deals["data-item-number"]
            print("product id: "+prod_id)
        except:
            pass

for i in range(9):
    j=j+48
    get_url_iter(j)
