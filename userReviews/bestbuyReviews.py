
import json
from .serilizers import Vendor_Review_Serializer
import requests
import urllib
import re
import time
import requests
import unicodedata
import math
class bestbuy:
    def scrapeBestBuyProduct_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        response = requests.get("http://ns519750.ip-158-69-23.net:8005/laptop/getModels")

        data = json.loads(response.text)
        for item in data:
            # print(item['SNR_ModelNo'])
            reviewStore = " "
            upc = item['SNR_UPC']
            itemId = item['SNR_SKU']
            itemId=itemId[2:]

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""

            link = "http://bestbuy.ugc.bazaarvoice.com/3545w/"+str(itemId)+"/reviews.djs?format=embeddedhtml&page=" + str(
                page) + "&&scrollToTop=true"

            forpages = urllib.urlopen(link).read()

            totalReviews_regex = r'("numReviews":)(\d{1,3})'
            extract_regex = re.findall(totalReviews_regex, forpages, flags=0)

            totalReviews = extract_regex[0][1]

            totalPages = int(math.ceil(float(totalReviews) / 8))

            print iterator
            page=1


            while iterator != False:
                try:

                    link = "http://bestbuy.ugc.bazaarvoice.com/3545w/"+str(itemId)+"/reviews.djs?format=embeddedhtml&page=" + str(
                        page) + "&&scrollToTop=true"

                    result = urllib.urlopen(link).read()

                    regex = r'(<span class=\\"BVRRReviewText\\">)([A-Za-z0-9 \W]*?)(<\\\/span>\\n)'

                    reviewDiv = re.findall(regex, result, flags=0)

                    print page
                    print totalPages
                    print len(reviewDiv)
                    if(totalPages>5):
                        totalPages=5

                    if page <= totalPages:
                        try:
                            for review in reviewDiv:
                                reviews.append(review[1])
                                # unicode_str = review[1].decode('ascii')
                                # utf8_str = unicode_str.encode('utf-8')
                                # print review[1]
                                reviewStore=reviewStore+"~"+review[1]
                        except:
                            continue
                        page += 1

                    else:
                        iterator = False

                    time.sleep(1)
                except Exception as e:
                    iterator = False
                    print e
            try:
                request["SNR_Category"] = "Laptop"
                request["SNR_ProductID"] = itemId
                print itemId
                request["SNR_UPC"] = upc
                request["SNR_VendorName"] = "Best Buy"
                request["SNR_StarRating"] = 0
                request["SNR_Review"] = reviewStore

                serializer = Vendor_Review_Serializer(data=request)
                # print serializer
                if serializer.is_valid():
                    print "Adding"
                    serializer.save()
                else:
                    print("bad json")
                    print serializer.error_messages
            except:
                continue

        return reviews
