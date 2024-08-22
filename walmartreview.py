import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

import requests
from bs4 import BeautifulSoup
import time
import json

from userReviews.serilizers import Vendor_Review_Serializer

class walmart_crawl():

    def walmartlaptop(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/laptop/getModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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


    def walmartMobile(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/mobile/getModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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



    def walmartwearable(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/wearable/getModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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



    def walmartAppliances(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getAppliancesModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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





    def walmartBooks(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getBooksModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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





    def walmartHealth(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getHealthModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartJewelry(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getJewelryModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartArts(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getArtsModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartClothes(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getClothesModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartFurniture(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getFurnitureModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartFlowers(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getFlowerModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartGadgets(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getGadgetsModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartGames(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getgamesModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartSmarthome(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getSmarthomeModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartCams(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getCamsModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartSoftware(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getSoftwareModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartMovies(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getMoviesModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartCarselec(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getCarselecModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartAudio(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getAudioModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartTV(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getTvModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartToys(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getToyModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartOffice(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getOfficeModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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




    def walmartSports(self,request):
        page=1
        flag=True
        while flag==True:


            response = requests.get("http://ns519750.ip-158-69-23.net:8005/products/getSportsModelswalmart?page="+str(page))

            data = json.loads(response.text)
            # print data

            totalpages=data['totalPages']
            if(page>=totalpages):
                flag=False
            else:
                page=page+1;
            for item in data['results']:
                # print item
                reviewStore = " "

                upc = item['SNR_UPC']
                itemId = item['SNR_SKU']
                title = item['SNR_Title']
                itemId=itemId[2:]
                print itemId
                itemurl=item['SNR_ProductURL']
                print itemurl





                print "amad ud din"
                time.sleep(10)
                url ='https://www.walmart.com/reviews/product/'+itemId
                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)

                source = requests.get(url)
                plain_text = source.text
                time.sleep(5)
                try:
                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('div', {'class': 'zeus-collapsable clearfix'}):
                        print link.text
                        reviewStore = reviewStore + "~" + link.text

                        request["SNR_Category"] = "Laptop"
                        request["SNR_ProductID"] = itemId

                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Walmart"
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
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






walmart_crawl().walmartCams({})
walmart_crawl().walmartCarselec({})
walmart_crawl().walmartClothes({})
walmart_crawl().walmartFlowers({})
walmart_crawl().walmartFurniture({})
walmart_crawl().walmartlaptop({})
walmart_crawl().walmartMobile({})
walmart_crawl().walmartwearable({})
walmart_crawl().walmartGadgets({})
walmart_crawl().walmartHealth({})
walmart_crawl().walmartMovies({})
walmart_crawl().walmartJewelry({})
walmart_crawl().walmartOffice({})
walmart_crawl().walmartSmarthome({})
walmart_crawl().walmartSoftware({})
walmart_crawl().walmartSports({})
walmart_crawl().walmartGames({})
walmart_crawl().walmartAppliances({})

walmart_crawl().walmartArts({})
walmart_crawl().walmartAudio({})
walmart_crawl().walmartBooks({})

from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'walmartreviews.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        walmart_crawl().walmartlaptop({})
        time.sleep(30)
        walmart_crawl().walmartMobile({})
        time.sleep(30)
        walmart_crawl().walmartwearable({})


        time.sleep(30)
        walmart_crawl().walmartAppliances({})
        time.sleep(30)
        walmart_crawl().walmartArts({})
        time.sleep(30)
        walmart_crawl().walmartAudio({})

        time.sleep(30)
        walmart_crawl().walmartBooks({})
        time.sleep(30)
        walmart_crawl().walmartCams({})

        time.sleep(30)
        time.sleep(30)
        walmart_crawl().walmartCarselec({})
        time.sleep(30)
        walmart_crawl().walmartClothes({})
        time.sleep(30)
        walmart_crawl().walmartFlowers({})
        time.sleep(30)
        walmart_crawl().walmartFurniture({})
        walmart_crawl().walmartGadgets({})
        time.sleep(30)

        time.sleep(30)
        walmart_crawl().walmartHealth({})
        time.sleep(30)
        walmart_crawl().walmartMovies({})
        walmart_crawl().walmartJewelry({})
        time.sleep(30)
        walmart_crawl().walmartOffice({})
        time.sleep(30)
        walmart_crawl().walmartSmarthome({})


        time.sleep(30)
        walmart_crawl().walmartSoftware({})
        walmart_crawl().walmartSports({})
        walmart_crawl().walmartGames({})

        time.sleep(30)
        pass    # do your thing here
    do(0)