from __future__ import absolute_import
import urllib2, urllib
import json
import re
import urlparse

walmartUrl = u"https://www.walmart.com/browse/daily-deals/0/0/?page={}"
startString = u'"preso":{"isLoading":false,"items":'
endString = u'</script>'


def extract_data(jsonData):
    data_items = []

    while jsonData:
        single_item = jsonData.pop()

        try:
            if single_item[u"department"] in [u"Gifts & Registry", u"Photo Center"]:
                raise KeyError(u"Not Needed This Item")

            primary_offer = single_item.pop(u"primaryOffer")
            item_after_price = u"{}".format(primary_offer.pop(u"offerPrice"))

            try:
                # is there before price
                item_before_price = u"{}".format(primary_offer.pop(u"listPrice"))
            except:
                # is there pickup discount
                try:
                    temp = u"{}".format(primary_offer.pop(u"pickupDiscountOfferPrice"))
                    item_after_price, item_before_price = temp, item_after_price
                except:
                    item_before_price = u"-1"

            # print(item_after_price,item_before_price)
            item_after_price = float(item_after_price)
            item_before_price = float(item_before_price)

            item_id = single_item.pop(u"productId")
            item_title = single_item.pop(u"title")
            item_url = urlparse.urljoin(
                walmartUrl, single_item.pop(u"productPageUrl"))
            item_image = single_item.pop(
                u"imageUrl").rsplit(u"?odnHeight=")[0]

            try:
                item_cat = single_item[u"seeAllName"]
            except:
                item_cat = u""

            yield {
                "SNR_SKU": item_id.encode("utf-8"),
                "SNR_Title": item_title.encode("utf-8"),
                "SNR_ProductURL": item_url.encode("utf-8"),
                "SNR_ImageURL": item_image.encode("utf-8"),
                "SNR_Category": item_cat.encode("utf-8"),
                "SNR_PriceBefore": item_before_price,
                "SNR_PriceAfter": item_after_price,
                "SNR_Available": "Walmart"
            }

        except KeyError:
            pass
        except Exception, e:
            raise e



def getJsonData(inputData):
    jsonIndex = temp = 0

    for i in inputData:
        if i == u"[":
            temp += 1
        elif i == u"]":
            temp -= 1
            if (temp == 0):
                return json.loads(inputData[:jsonIndex + 1])

        jsonIndex += 1


def getPageJs(walmartPage):
    inputData = walmartPage[walmartPage.index(startString) + len(startString):]
    inputData = inputData[:inputData.index(endString)]

    try:
        pagen = re.finditer(u'"next":{"url":"page=(\d+)', inputData).next()
        pagen = True
    except:
        pagen = False

    return (inputData, pagen)


def getDeals(totalPages=2):
    productsItems = []
    currentPage = walmartUrl
    isNext = True
    currentPage = 1

    while isNext:
        currentUrl = walmartUrl.format(currentPage)

        while True:
            try:
                urlResponse = urllib2.urlopen(currentUrl).read().decode(u"utf-8")
                break
            except:
                print u"Error Scrapping {0}, Retrying".format(currentUrl)

        print u"Scrapping {0}".format(currentUrl)
        walmartJs = getPageJs(urlResponse)

        isNext = walmartJs[1]
        # isNext = False
        currentPage += 1

        jsonResponse = getJsonData(walmartJs[0])

        # Used For Testing
        # return jsonResponse

        for i in extract_data(jsonResponse):
            yield i

