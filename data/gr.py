from __future__ import absolute_import
import urllib2, urllib
from bs4 import BeautifulSoup
import json

def getDeals():

    grouponUrl = "https://www.groupon.com/occasion/deals-of-the-day"
    while True:
        try:
            urlResponse = urllib2.urlopen(grouponUrl).read()
            print "Scrapping {0}".format(grouponUrl)

            break
        except:
            print "Error While Scrapping {0}, Retrying.".format(grouponUrl)

    #Parse And Get Data Items
    soup = BeautifulSoup(urlResponse, 'html.parser')


    grouponItems = soup.find("div", { "id" : "result-list" })

    allItems = []
    elms = grouponItems.find_all("figure", { "class" : "card-ui"  } )

    c= 0
    for i in elms:
        parsedContents = json.loads(i["data-bhd"])
        itemTitle = parsedContents["title"]["content"]
        itemBeforePrice,itemAfterPrice = parsedContents["value"]["content"].split(" ")
        itemId = parsedContents["cardUUID"]
        itemAfterPrice = float(itemAfterPrice[1:].replace(",",""))

        if (itemBeforePrice == "undefined"):
            itemBeforePrice = -1
        else:
            itemBeforePrice = float(itemBeforePrice[1:].replace(",",""))

        temp = i.a

        try:
            imgUrl = temp.find("img",set(["class","cui-image"]))["data-original"]
        except:
            imgUrl = temp.find("img",set(["class","cui-svg-placeholder"]))["style"]
            imgUrl = imgUrl[ imgUrl.index("(//")+1 :-1]

        if (imgUrl.startswith("//")):
            imgUrl = "http:" + imgUrl
        itemUrl = temp["href"]

        if c==0:
            c+=1
        else:
            yield {
                "SNR_SKU": itemId.encode("utf-8"),
                "SNR_Title": itemTitle.encode("utf-8"),
                "SNR_ProductURL": itemUrl.encode("utf-8"),
                "SNR_ImageURL": imgUrl.encode("utf-8"),
                "SNR_Category": "Not Available".encode("utf-8"),
                "SNR_PriceBefore": itemBeforePrice,
                "SNR_PriceAfter": itemAfterPrice,
                "SNR_Available": "Groupon"
            }