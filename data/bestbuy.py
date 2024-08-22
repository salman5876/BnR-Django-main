from __future__ import absolute_import
import urllib2, urllib
from bs4 import BeautifulSoup
import urlparse
def getDeals():
    bestbuyUrl = u"https://www.bestbuy.com/site/clp/sale-page/pcmcat185700050011.c?id=pcmcat185700050011"
    while True:
        try:
            urlResponse = urllib2.urlopen(bestbuyUrl).read()
            print u"Scrapping {0}".format(bestbuyUrl)

            break
        except:
            print u"Error While Scrapping {0}, Retrying.".format(bestbuyUrl)

    #Parse And Get Data Items
    soup = BeautifulSoup(urlResponse, u'html.parser')

    fullWidgetContainers = soup.find_all(u"div", { u"class" : u"widget-feature" })

    allItems = []
    for currentCat in fullWidgetContainers:
        currentCat = currentCat.div
        try:
            category = currentCat.find(u"div",set([u"class",u"feature-header"])).h2.text
            elms = currentCat.find_all(u"div", { u"class" : u"offer-column" })
            

        except Exception, e:
            continue

        

        for i in elms:
            itemData = i.div
            try:
                
                productOffer = i.find(u"div",{u"class":u"product-offer"})
                
                priceData = productOffer.find(u"div",set([u"class",u"pb-price"])) 

                afterPrice = float(priceData.find(u"div",{u"class":u"pb-hero-price"}).span[u"aria-label"].rsplit(u" ",1)[-1][1:])

                beforePrice = priceData.find(u"div",set([u"class",u"pb-regular-price"]))

                infoData = productOffer.find(u"div",set([u"class",u"info-block"])).h3.a

                itemLink = urlparse.urljoin(bestbuyUrl,infoData[u"href"])
                itemTitle = infoData.text
                itemId = itemLink.rsplit(u"skuId=",1)[-1]

                if beforePrice:
                    beforePrice = float(beforePrice[u"aria-label"].rsplit(u" ",1)[-1][1:])
                else:
                    beforePrice = -1

                itemImage = i.find(
                    u"div",{u"class":u"image-shell-wrapper"}
                    ).a.span.img[u"data-src"].split(u";maxHeight",1)[0]


                current_item =  {
                    "SNR_SKU": itemId.encode("utf-8"),
                    "SNR_Title": itemTitle.encode("utf-8"),
                    "SNR_ProductURL": itemLink.encode("utf-8"),
                    "SNR_ImageURL": itemImage.encode("utf-8"),
                    "SNR_Category": category.encode("utf-8"),
                    "SNR_PriceBefore": beforePrice,
                    "SNR_PriceAfter": afterPrice,
                    "SNR_Available": "BestBuy"
                }
                print current_item

                yield current_item
                
                
            except Exception,e:
                print e.message

