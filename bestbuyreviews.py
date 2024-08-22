
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

import json
from userReviews.serilizers import Vendor_Review_Serializer
import requests
import urllib
import re
import time
import requests
import unicodedata
import math
from products.models import *
from laptop.models import *
from mobile.models import *
from wearables.models import *
class bestbuy:

    def scrapeBestBuyProduct_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Laptop_DB.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews





    def scrapeBestBuyMobile_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Mobile_DB.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Mobile"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews






    def scrapeBestBuyWearable_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Wearable_DB.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Wearable"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews








    def scrapeBestBuyHealth_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = HealthandFitness.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Health"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyJewelry_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Jewelry.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Jewelry"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyArts_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Arts.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Arts"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyClothes_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Clothing.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Clothes"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyfurniture_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Furniture.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Furniture"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyFlowers_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = FlowerandPlants.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Flowers"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyGadgets_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = ElectronicGadgets.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Gadgets"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyGames_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = VideoGames.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Games"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuySmarthome_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = SmartHomes.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Smart home"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyCams_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Cams.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Wearable"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuySoftware_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = ComputerSoftware.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Software"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyMovies_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Movies.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Movies"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyCarsElec_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = CarsElectronics.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "CarsElec"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyAudio_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Audio.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Audio"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyTV_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = TV.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "TV"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyToys_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Toys.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Toys"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyOffice_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = OfficeSupply.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Office"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuySports_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = SportingGoods.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Wearable"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews




    def scrapeBestBuyBooks_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Books.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Books"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews



    def scrapeBestBuyAppliances_Reviews(self,request):
        page = 1
        reviews = []
        iterator = True
        reviewStore=""
        data = Applinces.objects.filter(SNR_Available__icontains='Best Buy')

        # data = json.loads(response.text)
        # print data
        for item in data:
            print item
            # print(item['SNR_ModelNo'])
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL

            iterator=True
            page = 1
            reviews = []
            iterator = True
            reviewStore = ""
            try:

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
                    request["SNR_Category"] = "Appliances"
                    request["SNR_ProductID"] = itemId
                    print itemId
                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Best Buy"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_ProductTitle"] = title
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
            except:
                print "error"

        return reviews




bestbuy().scrapeBestBuyMovies_Reviews({})
bestbuy().scrapeBestBuyOffice_Reviews({})
bestbuy().scrapeBestBuySmarthome_Reviews({})
bestbuy().scrapeBestBuySoftware_Reviews({})
bestbuy().scrapeBestBuyWearable_Reviews({})
bestbuy().scrapeBestBuyMobile_Reviews({})

bestbuy().scrapeBestBuyProduct_Reviews({})

bestbuy().scrapeBestBuyAppliances_Reviews({})
bestbuy().scrapeBestBuyArts_Reviews({})
bestbuy().scrapeBestBuyAudio_Reviews({})
bestbuy().scrapeBestBuyBooks_Reviews({})
bestbuy().scrapeBestBuyCams_Reviews({})
bestbuy().scrapeBestBuyCarsElec_Reviews({})
bestbuy().scrapeBestBuyClothes_Reviews({})
bestbuy().scrapeBestBuyFlowers_Reviews({})
bestbuy().scrapeBestBuyfurniture_Reviews({})
bestbuy().scrapeBestBuyGadgets_Reviews({})
bestbuy().scrapeBestBuyHealth_Reviews({})
bestbuy().scrapeBestBuyJewelry_Reviews({})
bestbuy().scrapeBestBuySports_Reviews({})
bestbuy().scrapeBestBuyTV_Reviews({})
bestbuy().scrapeBestBuyToys_Reviews({})
bestbuy().scrapeBestBuyGames_Reviews({})


from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'reviews.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        bestbuy().scrapeBestBuyProduct_Reviews({})
        bestbuy().scrapeBestBuyMobile_Reviews({})
        bestbuy().scrapeBestBuyWearable_Reviews({})


        bestbuy().scrapeBestBuyWearable_Reviews({})
        bestbuy().scrapeBestBuyMobile_Reviews({})
        bestbuy().scrapeBestBuyProduct_Reviews({})
        time.sleep(30)

        bestbuy().scrapeBestBuyAppliances_Reviews({})
        bestbuy().scrapeBestBuyArts_Reviews({})
        bestbuy().scrapeBestBuyAudio_Reviews({})
        bestbuy().scrapeBestBuyBooks_Reviews({})
        time.sleep(30)

        bestbuy().scrapeBestBuyCams_Reviews({})
        bestbuy().scrapeBestBuyCarsElec_Reviews({})
        bestbuy().scrapeBestBuyClothes_Reviews({})
        bestbuy().scrapeBestBuyFlowers_Reviews({})
        time.sleep(30)

        bestbuy().scrapeBestBuyfurniture_Reviews({})
        bestbuy().scrapeBestBuyGadgets_Reviews({})
        bestbuy().scrapeBestBuyHealth_Reviews({})
        bestbuy().scrapeBestBuyJewelry_Reviews({})
        time.sleep(30)

        bestbuy().scrapeBestBuyMovies_Reviews({})
        bestbuy().scrapeBestBuyOffice_Reviews({})
        time.sleep(30)

        bestbuy().scrapeBestBuySmarthome_Reviews({})
        bestbuy().scrapeBestBuySoftware_Reviews({})
        bestbuy().scrapeBestBuySports_Reviews({})
        bestbuy().scrapeBestBuyTV_Reviews({})
        bestbuy().scrapeBestBuyToys_Reviews({})
        bestbuy().scrapeBestBuyGames_Reviews({})

        time.sleep(30)
        pass    # do your thing here
    do(0)