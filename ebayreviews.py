import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from laptop.models import Laptop_DB
from mobile.models import Mobile_DB
from products.models import Applinces, Books


import json
from userReviews.serilizers import Vendor_Review_Serializer
from wearables.models import Wearable_DB
from products.models import *
import requests
from bs4 import BeautifulSoup
import time
import json
from wearables.serializers import  Wearable_Serializer

class ebay_crawl():
    def ebaylaptop(self,request):
        reviewStore=""


        data =  Laptop_DB.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl







            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Laptop"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"





    def ebayMobile(self,request):
        reviewStore=""


        data =  Mobile_DB.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Mobile"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"

    def ebayWearable(self,request):
        reviewStore=""
        print "fetching.."

        data = Wearable_DB.objects.filter(SNR_Available__icontains='Ebay')

        # data = json.loads(response.text)
        # print data
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Wearable"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"





    def ebayAppliances(self,request):
        reviewStore=""

        data = Applinces.objects.filter(SNR_Available__icontains="Ebay")

        # print data
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Appliancces"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"








    def ebayBooks(self,request):
        reviewStore=""


        data = Books.objects.filter(SNR_Available__icontains='Ebay')

        # print data
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Books"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"








    def ebaySports(self,request):
        reviewStore=""

        data = SportingGoods.objects.filter(SNR_Available__icontains='Ebay')

        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl







            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Sports"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"






    def ebayOffice(self,request):
        reviewStore=""


        data = OfficeSupply.objects.filter(SNR_Available__icontains='Ebay')


        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl








            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Office"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"










    def ebayToys(self,request):
        reviewStore=""

        data = Toys.objects.filter(SNR_Available__icontains='Ebay')

        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl




            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Toys"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"







    def ebayTV(self,request):
        reviewStore=""

        data = TV.objects.filter(SNR_Available__icontains='Ebay')

        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl


            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "TV"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"






    def ebayAudio(self,request):
        reviewStore=""


        data =  Audio.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl



            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Audio"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"







    def ebayCarsElec(self,request):
        reviewStore=""


        data =  CarsElectronics.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "CarsElec"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"









    def ebayMovies(self,request):
        reviewStore=""


        data =  Movies.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Movies"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"







    def ebaySoftware(self,request):
        reviewStore=""
        data =  ComputerSoftware.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl



            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Software"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"






    def ebayCams(self,request):
        reviewStore=""


        data =  Cams.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl




            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Cams"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"






    def ebaySmarthomes(self,request):
        reviewStore=""


        data =  SmartHomes.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Smart home"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"









    def ebayVideogames(self,request):
        reviewStore=""


        data =  VideoGames.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Games"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"








    def ebayGadgets(self,request):
        reviewStore=""


        data =  ElectronicGadgets.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl



            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Gadgets"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"











    def ebayFlowers(self,request):
        reviewStore=""


        data =  FlowerandPlants.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl



            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Flowers"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"






    def ebayFurniture(self,request):
        reviewStore=""


        data =  Furniture.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Furniture"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"







    def ebayClothes(self,request):
        reviewStore=""


        data =  Clothing.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Clothes"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"








    def ebayArts(self,request):
        reviewStore=""


        data =  Arts.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl




            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Arst"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"







    def ebayJewelry(self,request):
        reviewStore=""


        data =  Jewelry.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl





            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Jewelry"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"






    def ebayHealth(self,request):
        reviewStore=""

        data =  HealthandFitness.objects.filter(SNR_Available__icontains='Ebay')
        for item in data:
            # print item
            reviewStore = " "

            upc = item.SNR_UPC
            itemId = item.SNR_SKU
            title = item.SNR_Title
            itemId=itemId[2:]
            itemurl=item.SNR_ProductURL
            print itemurl



            print "amad ud din"
            time.sleep(10)
            url = itemurl
            source = requests.get(url)
            plain_text = source.text
            # print plain_text

            try:
                soup = BeautifulSoup(plain_text, "lxml")
                for link in soup.findAll('div', {'class': 'ebay-review-section-r'}):
                    print "finding..."
                    print link.find('p', {'class':'review-item-title wrap-spaces'}).text
                    print link.find('p', {'class':'review-item-content wrap-spaces'}).text
                    reviewStore = reviewStore + "~" +link.find('p', {'class':'review-item-content wrap-spaces'}).text


                    request["SNR_Category"] = "Health"
                    request["SNR_ProductID"] = itemId

                    request["SNR_UPC"] = upc
                    request["SNR_VendorName"] = "Ebay"
                    request["SNR_ProductTitle"] = title
                    request["SNR_StarRating"] = 0
                    request["SNR_Review"] = reviewStore
                    serializer = Vendor_Review_Serializer(data=request)
                    # print serializer
                    try:
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "something went wrong in saving serilizer"
            except:
                print "error"





ebay_crawl().ebaySoftware({})
ebay_crawl().ebaySports({})
ebay_crawl().ebayVideogames({})
ebay_crawl().ebayWearable({})
ebay_crawl().ebayMobile({})
ebay_crawl().ebayAppliances({})
ebay_crawl().ebayArts({})
ebay_crawl().ebayAudio({})
ebay_crawl().ebayBooks({})
ebay_crawl().ebayCams({})
ebay_crawl().ebayCarsElec({})
ebay_crawl().ebayClothes({})
ebay_crawl().ebayFlowers({})
ebay_crawl().ebayFurniture({})
ebay_crawl().ebayGadgets({})
ebay_crawl().ebayHealth({})
ebay_crawl().ebayMovies({})
ebay_crawl().ebayJewelry({})
ebay_crawl().ebayOffice({})
ebay_crawl().ebaySmarthomes({})
ebay_crawl().ebaylaptop({})



from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'ebayreviews.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"
        ebay_crawl().ebayCams({})
        ebay_crawl().ebayCarsElec({})
        ebay_crawl().ebayClothes({})
        ebay_crawl().ebaySoftware({})
        ebay_crawl().ebayFlowers({})
        ebay_crawl().ebayFurniture({})
        ebay_crawl().ebayGadgets({})
        ebay_crawl().ebayHealth({})
        ebay_crawl().ebayMovies({})
        ebay_crawl().ebayJewelry({})
        ebay_crawl().ebayOffice({})
        ebay_crawl().ebaySmarthomes({})

        ebay_crawl().ebayWearable({})
        ebay_crawl().ebayMobile({})
        ebay_crawl().ebaylaptop({})
        ebay_crawl().ebayAppliances({})
        ebay_crawl().ebayArts({})
        ebay_crawl().ebayAudio({})
        ebay_crawl().ebayBooks({})
        ebay_crawl().ebaySports({})
        ebay_crawl().ebayVideogames({})

        time.sleep(30)
        pass    # do your thing here
    do(0)