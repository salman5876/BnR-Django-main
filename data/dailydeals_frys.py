import requests
import urllib
from bs4 import BeautifulSoup
from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlsplit


def get_deals():
    my_url="https://www.frys.com/"
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    r = requests.get(my_url, headers=agent)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find("title").text)
    all_products=soup.findAll("div",{"id":"computerdeals-1"})
    for product in all_products:
        try:
            product_name=product.find("b").text[7:]
            if not product_name:
                continue
        except:
            continue

        product_price1 = -1.0

        try:
            product_price2=product.find("div",{"id":"did_price2valuediv"}).text[2:]
        except:
            try:
                product_price2=product.find("div",{"id":"did_price1valuediv"}).text[2:]
            except:
                continue

        product_price2 = float(product_price2.strip())

        try:
            product_url=urljoin("https://www.frys.com/",product.find("a")["href"])
        except Exception as e:
            continue
        finally:
            product_id = urlparse(product_url).path.split('/')[-1]

        try:
            product_image = product.select_one("a[href*=product/] img")["src"]

        except:
            continue



        temp = {
            "SNR_SKU": "FR"+product_id,
            "SNR_Title": product_name,
            "SNR_ProductURL": product_url,
            "SNR_ImageURL": product_image,
            "SNR_Category": "Not Available",
            "SNR_PriceBefore": -1.0,
            "SNR_PriceAfter": product_price2,
            "SNR_Available": "FRYS"
        }

        yield temp




