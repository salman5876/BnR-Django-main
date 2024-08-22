
import os, django
import json

import math

from requests import Timeout, ConnectionError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import AllProducts, Product_Reviews

from products.serializers import AllProducts_Serializer, Product_Reviews_Serializer

from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

def getRawUrlData(url):
    while True:
        try:
            print ("Getting Data From {0}.".format(url))
            temp = requests.get(url,timeout=30,headers=headers)
            if temp.status_code == 200:
                return temp.text
            else:
                raise KeyboardInterrupt()
        except KeyboardInterrupt as e:
            raise e
        except:
            print ("Error Getting Data From {0}., Retrying".format(url))

def getSoup(data):
    return BeautifulSoup(data,"lxml")

def rev_url(url):
    try:
        current_item_rev_url = getSoup(
            getRawUrlData(url)
        ).find("a", class_="see--all--reviews-link")["href"]

        if current_item_rev_url:
            return current_item_rev_url
    except:
        return False



def getJsonData(inputData,st=u"[",en=u"]"):
    jsonIndex = temp = 0

    for i in inputData:
        if i == st:
            temp += 1
        elif i == en:
            temp -= 1
            if (temp == 0):
                return json.loads(inputData[:jsonIndex + 1])

        jsonIndex += 1


def get_all_review(itemid,pagescount,current_item):
    d = '{"itemId":"%s","paginationContext":{"page":%s,"sort":"relevancy","filters":[],"limit":20}}' % (itemid,"%s")
    headers = {
        'content-type': 'application/json',
        'wm_mart_id': 0,
        'user-agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        'wm_channel_id': 0,
        'wm_bu_id': 0 ,
        'wm_locale_id': 'en_US'
    }

    u = "https://www.walmart.com/terra-firma/fetch?rgs=REVIEWS_MAP"
    revs_all = []
    for i in range(1,pagescount+1):
        while True:
            try:
                temp = d % str(i)
                data =  requests.post(u,headers=headers,data=temp,timeout=60)

                if data.status_code==200:
                    try:
                        data = data.json()["payload"]
                        data = data["reviews"]
                    except Exception as e:
                        break;

                    for j in data.iterkeys():
                        temp = data[j]["customerReviews"]
                        for rev in temp:
                            try:
                                rev_author = rev["userNickname"]
                            except:
                                rev_author = ""

                            rev_up = int( rev["positiveFeedback"] )
                            rev_down = int( rev["negativeFeedback"] )
                            rev_star = int( rev["rating"] )

                            try:
                                rev_title = rev["reviewTitle"]
                            except:
                                rev_title = ""

                            try:
                                rev_body = rev["reviewText"]
                            except:
                                rev_body = ""


                            single_rev = Product_Reviews(
                                SNR_Review_Title = rev_title,
                                SNR_Review_Author = rev_author,
                                SNR_Review_Body = rev_body,
                                SNR_Review_Stars = rev_star,
                                SNR_Review_UP = rev_up,
                                SNR_Review_Down = rev_down,
                                Product = current_item
                            )
                            try:

                                single_rev.save()
                                print("----")
                            except:
                                print "unique constaint"


                            # request={}
                            # request["SNR_Review_Title"]=rev_title;
                            # request["SNR_Review_Author"]=rev_author;
                            # request["SNR_Review_Body"]=rev_body;
                            # request["SNR_Review_Stars"]=rev_star;
                            # request["SNR_Review_UP"]=rev_up;
                            # request["SNR_Review_Down"]=rev_down;
                            # request["Product"]=current_item;
                            #
                            # serializer1 = Product_Reviews_Serializer(data=request)
                            # print serializer1
                            #
                            # if serializer1.is_valid():
                            #     print("---")
                            #     # serializer.save()
                            #     serializer1.save()
                            # else:
                            #     print serializer1.error_messages

                            revs_all.append(single_rev)

                    return revs_all
                else:
                    break

            except Timeout:
                pass
            except ConnectionError:
                pass

def get_all_revs(ur,current_item):

        try:
            rev_soup = getSoup(getRawUrlData(ur)).find("div",class_="ReviewsHeader-container")
        except:
            return []

        try:
            data = rev_soup.find("a",class_="ReviewsHeader-seeAll")["href"]
        except:
            return []

        product_id = next(re.finditer("product.(\d+)/?$",data)).group(1)
        rating_div = rev_soup.select_one("div[itemprop=aggregateRating]")

        rev_count = int(rating_div.find("meta",{"itemprop":"reviewCount"})["content"])
        overall_stars = float(rating_div.find("meta",{"itemprop":"ratingValue"})["content"])

        pages = int(math.ceil(rev_count/20.0))

        return get_all_review(product_id,pages,current_item)




def get_table_walmart_revs():
    all_rev_objects = AllProducts.objects.filter(SNR_Available__iexact="Walmart",SNR_CustomerReviews__gt=0).values_list("id")

    a = set([i[0] for i in all_rev_objects])
    for current_item in a:
        current_item = AllProducts.objects.get(id=current_item)
        print ("Getting Reviews from {0}".format(current_item))
        revs = get_all_revs(current_item.SNR_ProductURL,current_item)

        if revs:
            try:
                Product_Reviews.objects.bulk_create(revs)
            except:
                pass

get_table_walmart_revs();