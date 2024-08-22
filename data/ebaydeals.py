from __future__ import absolute_import
from bs4 import BeautifulSoup
import urllib2, urllib


uiHeader = {u'User-Agent': u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
def getUrlResponse(ur):
    req = urllib2.Request(ur, data=None,headers = uiHeader)
    return urllib2.urlopen(req).read().decode(u"utf-8")


def getDeals():
    ebayUrl = u"https://www.ebay.com/deals"
    
    #Get Deal Data (Raw)
    urlResponse = getUrlResponse(ebayUrl)

    soup = BeautifulSoup(urlResponse, u'html.parser')

    getNav = soup.find(u"ul",{u"class":u"ebayui-refit-nav-ul"}).find_all(u"li")[1:-1]

    
    allItems = []
    for largeCat in getNav:
        getCat = largeCat.find(u"div").find_all(u"div")
        for i in getCat:
            catLinkTags = i.find_all(u"a",{u"class":u"navigation-desktop-flyout-link"}) 

            for eachTag in catLinkTags:
                category = eachTag.text
                ur = eachTag[u"href"]
                while True:
                    try:
                        urlResponse = getUrlResponse(ur)
                        print u"Scrapping {}".format(ur)
                        break
                    except:
                        print u"Error Occured While Getting Data From {}, Again Trying to get it".format(ur)

                soup = BeautifulSoup(urlResponse, u'html.parser')
                ebayItems = soup.find_all(u"div", { u"class" : u"col" })

                

                #traverse every single item and get its data 
                for j in ebayItems:

                    elm = j.div

                    try:
                        #get item id
                        itemId = elm[u"data-listing-id"]        

                        elmChilds = elm.children
                        

                        imgParent = elmChilds.next().div.img 

                        try:
                            imgTag = imgParent[u"data-config-src"]
                        except:
                            imgTag = imgParent[u"src"]


                        itemDetails = elmChilds.next()

                        

                        itemMetaChilds = itemDetails.children
                        temp = itemMetaChilds.next() 
                        itemTitle = temp[u"title"]
                        itemUrl = temp.a[u"href"]

                        try:

                            itemAfterPrice = float(itemMetaChilds.next().find(
                                                    itemprop=u"price").text.strip().split(u" ")[-1][1:])
                        except:
                            itemAfterPrice = -2

                        try:
                            itemBeforePrice = float(itemMetaChilds.next().span.span.text.strip().split(u" ")[-1][1:])
                        except:
                            itemBeforePrice = -1

                        #(id,imgTag,itemTitle,itemUrl,ItemAfterPrice,ItemBeforePrice)
                        yield {
                            "SNR_SKU":itemId.encode("utf-8"),
                            "SNR_Title":itemTitle.encode("utf-8"),
                            "SNR_ProductURL":itemUrl.encode("utf-8"),
                            "SNR_ImageURL":imgTag.encode("utf-8"),
                            "SNR_Category":category.encode("utf-8"),
                            "SNR_PriceBefore":itemBeforePrice,
                            "SNR_PriceAfter":itemAfterPrice,
                            "SNR_Available":"Ebay"
                        }

                    except Exception, e:
                        if e.args[0] != u"data-listing-id":
                            pass