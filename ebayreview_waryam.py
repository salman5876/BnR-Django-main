import codecs
import os, django
import json

from django.db import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import AllProducts, Product_Reviews

from products.serializers import AllProducts_Serializer

from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

def getRawUrlData(url):
    while True:
        try:
            print "Getting Data From {0}.".format(url)
            temp = requests.get(url,timeout=30,headers=headers)
            if temp.status_code == 200:
                return temp.text
            else:
                raise KeyboardInterrupt()
        except KeyboardInterrupt as e:
            raise e
        except:
            print "Error Getting Data From {0}., Retrying".format(url)

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


def get_ebay_lower(ur):
    return getSoup(getRawUrlData(ur)).find("div",id="lowerSection")

def get_all_revs(ur):
    current_url = ur
    temp = get_ebay_lower(current_url)
    current_data = temp.find("div",id="histogramSection")
    reviews = {}
    overall_rev = int(current_data.find("meta", {"itemprop":"reviewCount"})["content"])

    if overall_rev == 0:
        return False

    overall_rating = "%0.2f"  % float(current_data.find("meta",{"itemprop":"ratingValue"})["content"])
    current_data1 = current_data.find_all("div",class_="ebay-reviews-item-href")
    overall_stars = {}

    current_data = temp
    for i in current_data1:
        temp = i.select_one("div.ebay-review-item-r span")
        counts = int( next(re.finditer("(\d+)",str(temp))).group(1) )
        i = i.find("p",class_="ebay-review-item-stars")
        count = int(i.text[0])
        overall_stars[count] = counts


    reviews["meta"] = {
        "total_review": overall_rev,
        "total_rating" : overall_rating,
        "total_starts": overall_stars
    }

    reviews["reviews"] = []


    is_next = True

    all_revs = []

    while is_next:

        all_revs.extend(
            get_single_p(soup=current_data)
        )

        is_next = False
        next_div = current_data.find("a",{"rel":"next","class":"disabled"})



        if not next_div:
            try:
                current_url = current_data.find("a",{"rel":"next","class":"spf-link"})["href"]
                if current_url:
                    is_next = True
                    current_data = get_ebay_lower(current_url)
            except:
                pass


    return all_revs



def get_single_p(url=False,soup=False):
    all_revs = []

    if not soup:
        soup = BeautifulSoup(getRawUrlData(url),"lxml")

    current_data = soup

    rev_divs = current_data.find_all("div", {
        "class": "ebay-review-section",
        "itemprop": "review"
    })

    for rev_div in rev_divs:
        current_item_data = {}
        left_data = rev_div.find("div", class_="ebay-review-section-l")
        try:
            star_div =  left_data.select_one("div.ebay-star-rating")

            try:
                t = star_div["aria-label"].split(" ")[0]
            except:
                t = star_div.select_one("meta[itemprop=ratingValue]")["content"]
            finally:
                t = t.split(".")[0]
                current_item_data["SNR_Review_Stars"] = int(t)


            current_item_data["SNR_Review_Author"] = left_data.select_one("a.review-item-author")["title"]

            try:
                rev_date = left_data.select_one("span[itemprop=datePublished]")["content"]
            except:
                pass

            right_data = rev_div.find("div", class_="ebay-review-section-r")

            try:
                tag_obj = {"itemprop": "name","class": "review-item-title"}
                current_item_data["SNR_Review_Title"] = right_data.find("he", tag_obj).text.strip()
            except:
                try:
                    current_item_data["SNR_Review_Title"] = right_data.find("p", tag_obj).text.strip()
                except:
                    current_item_data["SNR_Review_Title"] = ""

            try:
                current_item_data["SNR_Review_Body"] = right_data.find("p", {"itemprop": "reviewBody",
                                                                             "class": "review-item-content"}).text.strip()
            except:
                current_item_data["SNR_Review_Body"] = ""
            current_item_data["SNR_Review_UP"] = int(
                right_data.select_one("a.vote-up-link span.review-section-rr-txt span.positive-h-c").text.strip())
            current_item_data["SNR_Review_Down"] = int(
                right_data.select_one("a.vote-down-link span.review-section-rr-txt span.negative-h-c").text.strip())
            single_rev = Product_Reviews(
                SNR_Review_Title=current_item_data["SNR_Review_Title"],
                SNR_Review_Author=current_item_data["SNR_Review_Author"],
                SNR_Review_Body=current_item_data["SNR_Review_Body"],
                SNR_Review_Stars=current_item_data["SNR_Review_Stars"] ,
                SNR_Review_UP=current_item_data["SNR_Review_UP"],
                SNR_Review_Down=current_item_data["SNR_Review_Down"],
                Product=current_item_data
            )
            try:

                single_rev.save()
                print("----")
            except:
                print "unique constaint"

            all_revs.append(current_item_data)
        except:
            pass

    return all_revs


cr_bulk = lambda x,y: Product_Reviews.objects.bulk_create([Product_Reviews(Product=y,**i) for i in x])
def get_rev_table():
    all_rev_objects = AllProducts.objects.filter(SNR_Available__iexact="ebay",SNR_CustomerReviews__gt=0)
    for current_item in all_rev_objects:
        print "Getting Reviews For Item ID: {0} from {1}".format(current_item.SNR_SKU,current_item.SNR_ProductURL)
        rurl = rev_url(current_item.SNR_ProductURL)
        revs = get_all_revs(rurl) if rurl else get_single_p(url=current_item.SNR_ProductURL)
        if revs:
            try:
                cr_bulk(revs,current_item)
            except IntegrityError:
                pass
            except:
                print "Some Database Error"



get_rev_table()