from attr import attrs
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import urllib
from urlparse import urljoin
import re
#

my_url="https://www.bestbuy.com/site/home-appliances"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
r=requests.get(my_url,headers=agent)
html=r.text
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())
#all_cats=soup.findAll(class_="column-wrap")
#print(all_cats)

#print(len(all_cats))
# all_cats_links=[]
# for cat in all_cats:
#     for href in cat.findAll("li"):
#         #print(href.find("a")["href"])
#         all_cats_links.append(href.find("a")["href"])#all categories links stored in list


cat_mapping = {
    "TV & Home Theater".capitalize(): "TV, Audio & Surveillance".capitalize(),
    "Computers & Tablets".capitalize() : "Computers & Tablets".capitalize(),
    "Cameras & Camcorders".capitalize() : "Cameras & Photo".capitalize(),
    "Cell Phones".capitalize() : "Cellphones & Accessories".capitalize(),
    "Audio": "TV, Audio & Surveillance".capitalize(),
    "Video Games".capitalize() : "Video Games & Consoles".capitalize(),
    "Movies & Music".capitalize() : "Videos, Movies & TV".capitalize(),
    "Car Electronics & GPS".capitalize() : "Vehicle Electronics & GPS".capitalize(),
    "Wearable Technology".capitalize() : "Wearable Tech".capitalize(),
    "Health, Fitness & Beauty".capitalize(): "Health, Fitness & Beauty".capitalize(),
    "Home, Garage & Office".capitalize() : "Home & Garden".capitalize(),
    "Smart Home, Security & Wi-Fi".capitalize() : "Smart Home".capitalize(),
    "Drones, Toys & Collectibles".capitalize() :"Toys, Kids and Baby".capitalize().capitalize()
}

from scrapetools import *

def get_url2(url2,category,sub_cat_name):
    new_url2 = requests.get(url2, headers=agent)
    new_html2 = new_url2.text
    soup3= BeautifulSoup(new_html2,"lxml")
    containers= soup3.find_all("div",{"class":"list-item"})
    cat_name= category
    sub_cat_title=sub_cat_name[:13]


    for container in containers:
        item_title = container.find("div", {"class": "sku-title"}).text
        # item_title.append(container.find("div", {"class": "sku-title"}).text)

        print("product main category:"+cat_name)
        print("product sub category: "+sub_cat_title[:13])
        print("product name :" + item_title)
        try:
            url = container.find('a',{"data-rank":"pdp"})
            item_url = urljoin("https://www.bestbuy.com",str(url.attrs['href']))
            print("product url: " + item_url)
        except:
            pass
        try:
            # item_price.append(container.find("div", {"class": "pb-hero-price"}))
            item_price = container.find("div", {"class": "pb-hero-price"}).text[1:].replace(',','')
            print("product price :" + item_price)
        except:
            pass

        try:
          item_review = container.find("span", {"class": "c-review-average"}).text
          print("item_review: " + item_review)
        except:
            pass
        try:
            rating=container.find("div",{"class":"customer-rating"})
            customer_rating=rating.find("meta",{"itemprop":"reviewCount"})['content']
            print("customer -rating: "+customer_rating)
        except:
            pass
        try:
          product_id=container.find("li",{"class":"sku-id"})
          pd_id=product_id.find("span",{"class":"sku-value"}).text
          print("product id: "+pd_id)
        except:
            pass
        try:
            product_model=container.find("li",{"class":"model-number"})
            pd_model=product_model.find("span",{"class":"sku-value"}).text
            print("product model: "+pd_model)
        except:
            pass
        try:
            image=container.find("div",{"class":"thumb"})
            image_url=image.find("img")["src"]
            print("product image: " +image_url)
        except:
            pass
        cat_name = map_data(cat_mapping,cat_name.capitalize())
        sub_cat_title = sub_cat_title.capitalize()
        data={
            "SNR_Title":item_title,
            "SNR_Category":cat_name,
            "SNR_SubCategory":sub_cat_title,
            "SNR_ProductURL":item_url,
            "SNR_ImageURL":image_url,
            "SNR_Price":float(item_price.replace(",","")),
            #"pd_review":customer_rating,item_review
            "SNR_CustomerReviews":float(item_review),
            "SNR_SKU":"BB{0}".format(pd_id),
            "SNR_ModelNo":pd_model,
            "SNR_Brand" : "No Brand",
            "SNR_PriceBefore" : -1.0,
            "SNR_Condition" : "00",
            "SNR_Description" : "Visit site to see description",
            "SNR_Available" : "BestBuy",
            "SNR_UPC" : "00"
        }

        yield data


    next_pg_url=soup3.find("li",{"class":"pager-next"})
    next_url=next_pg_url.find("a")["href"]
    try:
        if next_url is not None:
            print("going to next page")
            for i in get_url2(next_url,cat_name,sub_cat_title):
                yield i

    except:
        print("no next page")
        pass


sub_urls=[] # all
def no_sub_cat():
  print("no sub categories")



def get_url(link,cat_title):
    #print(link)
    new_url=requests.get(link,headers=agent)
    new_html=new_url.text
    soup2=BeautifulSoup(new_html,"lxml")
    sub_category_title=soup2.find("title").text
    #print("sub categories in "+soup2.find("title").text)
    containers = soup2.select(".flex-copy-wrapper")
    try:
      for sub_cat in containers:
          #print(sub_cat.find("a").text)
          temp=sub_cat.find("a")["href"]
          url_title=sub_cat.find("a").text
          #print(temp)
          try:
           if temp is not None:
              url2=urljoin("https://www.bestbuy.com",str(temp))
              sub_urls.append(url2)
              #print("sub category is: "+url_title)
              print("getting :" +url2)
              for i in get_url2(url2,cat_title,sub_category_title):
                  yield i
          except:
              for i in get_url2(new_url,cat_title,sub_category_title):
                  yield i
    except:
        pass



#print(all_cats_links[50])
# print("total categories in Best Buy "+str(len(all_cats_links)))
all_main_cats=soup.findAll("h2")
#print(all_main_cats)

def get_main_url(main_cat_url,cat_Name):
    sub_url=requests.get(main_cat_url,headers=agent)
    new_html5=sub_url.text
    soup5=BeautifulSoup(new_html5,"lxml")
    #name=soup5.find("title").text
    # print("getting: "+name)
    all_sub_cats=soup5.findAll("div",{"class":"list col-xs-6"})
    for cat in all_sub_cats:
        lists=cat.findAll("li")
        for links in lists:
            #print(links.find("a").text)
            category_url=urljoin("https://www.bestbuy.com",links.find("a")["href"])
            print("getting: "+category_url)
            for i in get_url(category_url,cat_Name):
                yield i


for head in all_main_cats:
    try:
        main_cat_url=head.find("a")["href"]
        #print(main_cat_url)
        main_cat_name=head.find("a").text
        #print(main_cat_name)
        temp = main_cat_name.lower()
        if "outlet" not in temp:
            commit_data(get_main_url(main_cat_url,main_cat_name))

    except:
        pass




