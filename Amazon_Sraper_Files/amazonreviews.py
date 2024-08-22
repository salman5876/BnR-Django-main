
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()


import requests
from bs4 import BeautifulSoup
import time
from laptop.models import Laptop_DB
from mobile.models import Mobile_DB
from wearables.models import Wearable_DB

from products.models import *
from userReviews.serilizers import Vendor_Review_Serializer
from products.serializers import Product_Reviews_NoDate_Serializer

import json
from django.db import connection


class amazon_crawl():

    def AllProducts(self):
        with connection.cursor() as cursor:
            query = 'Select {0} from products_allproducts Where "SNR_Available" = %s order by id DESC offset 10 limit 5'
            Data = []
            fields = [
                "SNR_SKU", "SNR_Title",
                "SNR_ModelNo", "SNR_Brand",
                "SNR_UPC", "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description", "SNR_isShow",
                "SNR_Date", "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

            ]
            out = ['"{0}"'.format(i) for i in fields]

            query = query.format(",".join(out))
            cursor.execute(query, ['Amazon'])
            # print cursor.fetchall()
            for i in cursor.fetchall():

                # if i[5] > 0:
                current_item = {}
                for j in range(len(fields)):
                    current_item[fields[j]] = i[j]

                Data.append(current_item)
            return Data

    def alllaptop(self):
        Data = Laptop_DB.objects.filter(SNR_Available__icontains='Amazon')
        return Data

    def allMobiles(self):
        Data = Mobile_DB.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allWearable(self):
        Data = Wearable_DB.objects.filter(SNR_Available__icontains='Amazon')
        return Data



    def allAppliances(self):
        Data = Applinces.objects.filter(SNR_Available__icontains='Amazon')
        return Data




    def allTv(self):
        Data = TV.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allToys(self):
        Data = Toys.objects.filter(SNR_Available__icontains='Amazon')
        return Data




    def allGadgets(self):
        Data = ElectronicGadgets.objects.filter(SNR_Available__icontains='Amazon')
        return Data




    def allCams(self):
        Data = Cams.objects.filter(SNR_Available__icontains='Amazon')
        return Data




    def allCarsElec(self):
        Data = CarsElectronics.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allVideoGames(self):
        Data = VideoGames.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allSmarthomes(self):
        Data = SmartHomes.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allAudio(self):
        Data = Audio.objects.filter(SNR_Available__icontains='Amazon')
        return Data



    def allSoftware(self):
        Data = ComputerSoftware.objects.filter(SNR_Available__icontains='Amazon')
        return Data

    def allBooks(self):
        Data = Books.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allFurniture(self):
        Data = Furniture.objects.filter(SNR_Available__icontains='Amazon')
        return Data



    def allFlowernPlants(self):
        Data = FlowerandPlants.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allCloths(self):
        Data = Clothing.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allArts(self):
        Data = Arts.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allJewelry(self):
        Data = Jewelry.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allHomeGarden(self):
        Data = HomeandGarden.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allOffice(self):
        Data = OfficeSupply.objects.filter(SNR_Available__icontains='Amazon')
        return Data

    def allHealth(self):
        Data = HealthandFitness.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def allSports(self):
        Data = SportingGoods.objects.filter(SNR_Available__icontains='Amazon')
        return Data


    def amazonlaptop(self,request):
        titles=[]

        Data = amazon_crawl().AllProducts()
        # print Data.count(Data)
        for data in Data:
            # time.sleep(100)
            urlprod= data['SNR_ProductURL']
            upc=data['SNR_UPC']
            itemId=data['id']
            # itemId=itemId[2:]
            title=data['SNR_Title']
            # print time
            # print itemId




            source = requests.get(urlprod)
            print urlprod

            # time.sleep(30)
            plain_text = source.text
            print plain_text
            soup = BeautifulSoup(plain_text, "lxml")
            print soup
            for lin in soup.findAll('a', {'id': 'dp-summary-see-all-reviews'}):

                print "finding..."
                ref='https://www.amazon.com'+lin.get('href')
                print ref
                urlinside = ref
                sourceinside = requests.get(urlinside)
                plain_textinside = sourceinside.text
                # time.sleep(30)
                # print plain_textinside
                soupinside = BeautifulSoup(plain_textinside, "lxml")
                for link in soupinside.findAll('div', {'class': 'a-section celwidget'}):
                    print "finding..."
                    n=float(link.find('span',{'class': 'a-icon-alt'}).text[:3])
                    print type(n)
                    try:
                        request["Product"] = itemId
                        request["SNR_Review_Title"] = link.find('a',{'class': 'a-size-base a-link-normal review-title a-color-base a-text-bold'}).text
                        request["SNR_Review_Author"] = link.find('span',{'class': 'a-profile-name'}).text
                        request["SNR_Review_Body"] = link.find('span',{'class': 'a-size-base review-text'}).text
                        request["SNR_Review_Stars"] = float(link.find('span',{'class': 'a-icon-alt'}).text[:3])
                        request["SNR_Review_UP"] = 0
                        request["SNR_Review_Down"] = 0
                        request["SNR_IS_SNR"] = False

                        serializer = Product_Reviews_NoDate_Serializer(data=request)
                        print serializer
                        if serializer.is_valid():
                            print "Adding"
                            serializer.save()
                        else:
                            print("bad json")
                            print serializer.error_messages
                    except:
                        print "error..."
                        continue





    def amazonmobile(self,request):
        try:

            Data = amazon_crawl().allMobiles();
            print Data.count()
            for data in Data:
                time.sleep(100)
                urlprod= data.SNR_ProductURL
                upc=data.SNR_UPC
                itemId=data.SNR_SKU
                itemId=itemId[2:]
                title=data.SNR_Title
                print urlprod



                url = urlprod
                source = requests.get(url)
                time.sleep(30)
                plain_text = source.text
                print plain_text
                soup = BeautifulSoup(plain_text, "lxml")
                for lin in soup.findAll('a', {'id': 'dp-summary-see-all-reviews'}):

                    print "finding..."
                    ref='https://www.amazon.com'+lin.get('href')
                    print ref
                    urlinside = ref
                    sourceinside = requests.get(urlinside)
                    plain_textinside = sourceinside.text
                    time.sleep(30)
                    # print plain_textinside
                    soupinside = BeautifulSoup(plain_textinside, "lxml")
                    for link in soupinside.findAll('span', {'class': 'a-size-base review-text'}):
                        print "finding..."
                        print link.text
                        try:
                            request["SNR_Category"] = "Mobile"
                            request["SNR_ProductID"] = itemId
                            print itemId
                            request["SNR_UPC"] = upc
                            request["SNR_VendorName"] = "Amazon"
                            request["SNR_ProductTitle"] = title
                            request["SNR_StarRating"] = 0
                            request["SNR_ProductTitle"] = title
                            request["SNR_Review"] = link.text

                            serializer = Vendor_Review_Serializer(data=request)
                            # print serializer
                            if serializer.is_valid():
                                print "Adding"
                                serializer.save()
                            else:
                                print("bad json")
                                print serializer.error_messages
                        except:
                            print "Error"
                            continue
        except:
            print "Error ,...."






    def amazonwearable(self,request):
        titles=[]

        Data = amazon_crawl().allWearable();
        print Data.count()
        for data in Data:
            time.sleep(100)
            urlprod= data.SNR_ProductURL
            upc=data.SNR_UPC
            itemId=data.SNR_SKU
            itemId=itemId[2:]
            title=data.SNR_Title



            url = urlprod
            source = requests.get(url)
            time.sleep(30)
            plain_text = source.text
            # print plain_text
            soup = BeautifulSoup(plain_text, "lxml")
            for lin in soup.findAll('a', {'id': 'dp-summary-see-all-reviews'}):

                print "finding..."
                ref='https://www.amazon.com'+lin.get('href')
                print ref
                urlinside = ref
                sourceinside = requests.get(urlinside)
                plain_textinside = sourceinside.text
                time.sleep(30)
                # print plain_textinside
                soupinside = BeautifulSoup(plain_textinside, "lxml")
                for link in soupinside.findAll('span', {'class': 'a-size-base review-text'}):
                    print "finding main url..."
                    print link.text
                    try:
                        request["SNR_Category"] = "Wearable"
                        request["SNR_ProductID"] = itemId
                        print itemId
                        request["SNR_UPC"] = upc
                        request["SNR_VendorName"] = "Amazon"
                        request["SNR_ProductTitle"] = title
                        request["SNR_StarRating"] = 0
                        request["SNR_ProductTitle"] = title
                        request["SNR_Review"] = link.text
                        try:

                            serializer = Vendor_Review_Serializer(data=request)
                            print serializer
                            if serializer.is_valid():
                                print "Adding"
                                serializer.save()
                            else:
                                print("bad json")
                                print serializer.error_messages
                        except:
                            print "Bad Serilizer"
                    except:
                        continue



amazon_crawl().amazonlaptop({})
# time.sleep(300)
# amazon_crawl().amazonmobile({})
# time.sleep(300)
#
# amazon_crawl().amazonlaptop({})
