
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from products.serializers import Books_Serializer,TV_Serializer,Cams_Serializer,CarsElec_Serializer,VideoGames_Serializer,\
    Toys_Serializer,Smarthomes_Serializer,Audio_Serializer,Software_Serializer,Applinces_Serializer,Movies_Serializer,\
    Office_Serializer,Health_Serializer,Furniture_Serializer,Arts_Serializer,HomeandGarden_Serializer,Jewelry_Serializer,Clothes_Serializer,Flowers_Serializer
import requests
import json
from rest_framework.response import Response    # to send specific response
from rest_framework import status
#


from products.models import Cams,OfficeSupply,TV,VideoGames,Applinces,Audio,ComputerSoftware,HealthandFitness,Books,Furniture
from wapy.api import Wapy
from products.serializers import Cams_Serializer
import math
from collections import defaultdict
import time,threading





baseAddress = "http://localhost:8000/"


obj1 = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
obj = Wapy('m9esvpqxg8vc85g97726vdmn')
key = Wapy('26zfbnn3h5wykxcyabj9f7uh')


class Offce:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,Offce)




def Office_Walmart(request,categoryId="1229749_1046059",nextpage=0):

    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:


                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM"+str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] =product.model_number
                        request["SNR_Price"] =product.sale_price
                        request["SNR_ProductURL"] =product.product_url
                        request["SNR_Description"]=product.long_description
                        request["SNR_Available"] = "Walmart"
                        serializer = Office_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)


                        laptops[product.model_number] = Offce("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"

                            serializer = Office_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                                time.sleep(1)


            except:
                print ""

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Office_Walmart(request,categoryId,nextpage)


def Arts_Walmart(request, categoryId="1229749_1046059", nextpage=0):
    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:

                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"
                        request["SNR_SubCategory"] = product.category_path

                        serializer = Arts_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number] = Offce("WM" + str(product.item_id), product.name,
                                                              product.model_number, product.brand_name, product.upc,
                                                              product.sale_price, product.product_url, image,
                                                              product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"
                            request["SNR_SubCategory"] = product.category_path

                            serializer = Arts_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                            else:
                                print ""
                                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                                #print("bad json")

            except:
                print ""
    else:
        # #print "end"
        nextpage = None

    #print len(laptops)

    if nextpage != None:
        time.sleep(0.15)
        Arts_Walmart(request, categoryId, nextpage)















def HomeandGradden_Walmart(request, categoryId="1072864", nextpage=0):
    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:

                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"
                        request["SNR_SubCategory"] = product.category_path

                        serializer = HomeandGarden_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number] = Offce("WM" + str(product.item_id), product.name,
                                                              product.model_number, product.brand_name, product.upc,
                                                              product.sale_price, product.product_url, image,
                                                              product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"
                            request["SNR_SubCategory"] = product.category_path

                            serializer = HomeandGarden_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                            else:

                                print ""

                                #print("bad json")

            except:
                print ""

                # for laptop in laptops:
                # #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # #print "end"
        nextpage = None

    #print len(laptops)

    if nextpage != None:
        time.sleep(0.15)
        HomeandGarden_Serializer(request, categoryId, nextpage)












def Jewelry_Walmart(request, categoryId="3891", nextpage=0):
    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:

                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"
                        request["SNR_SubCategory"] = product.category_path

                        serializer = Jewelry_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number] = Offce("WM" + str(product.item_id), product.name,
                                                              product.model_number, product.brand_name, product.upc,
                                                              product.sale_price, product.product_url, image,
                                                              product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"
                            request["SNR_SubCategory"] = product.category_path

                            serializer = Jewelry_Walmart(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                            else:
                                print ""

                                #print("bad json")

            except:
                print ""

                # for laptop in laptops:
                # #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # #print "end"
        nextpage = None

    #print len(laptops)

    if nextpage != None:
        time.sleep(0.15)
        Jewelry_Walmart(request, categoryId, nextpage)












def Flowers_Walmart(request, categoryId="4044_133012", nextpage=0):
    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:

                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"
                        request["SNR_SubCategory"] = product.category_path

                        serializer = Jewelry_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number] = Offce("WM" + str(product.item_id), product.name,
                                                              product.model_number, product.brand_name, product.upc,
                                                              product.sale_price, product.product_url, image,
                                                              product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"
                            request["SNR_SubCategory"] = product.category_path

                            serializer = Flowers_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                                time.sleep(1)

                            else:
                                print ""

                                #print("bad json")

            except:
                print ""

                # for laptop in laptops:
                # #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # #print "end"
        nextpage = None

    #print len(laptops)

    if nextpage != None:
        time.sleep(0.15)
        Flowers_Walmart(request, categoryId, nextpage)











def Clothes_Walmart(request, categoryId="5438_1228424", nextpage=0):
    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:

                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"
                        request["SNR_SubCategory"] = product.category_path

                        serializer = Clothes_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            time.sleep(1)

                            serializer.save()
                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number] = Offce("WM" + str(product.item_id), product.name,
                                                              product.model_number, product.brand_name, product.upc,
                                                              product.sale_price, product.product_url, image,
                                                              product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"
                            request["SNR_SubCategory"] = product.category_path

                            serializer = Clothes_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                            else:
                                print ""

                                #print("bad json")

            except:
                print ""

                # for laptop in laptops:
                # #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # #print "end"
        nextpage = None

    #print len(laptops)

    if nextpage != None:
        time.sleep(0.15)
        Clothes_Serializer(request, categoryId, nextpage)


#4044_539095_5547362
def Furniture_Walmart(request, categoryId="4044_539095_5547362", nextpage=0):
    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:

                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"
                        request["SNR_SubCategory"] = product.category_path

                        serializer = Furniture_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            time.sleep(1)

                            serializer.save()
                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number] = Offce("WM" + str(product.item_id), product.name,
                                                              product.model_number, product.brand_name, product.upc,
                                                              product.sale_price, product.product_url, image,
                                                              product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"

                            request["SNR_SubCategory"] = product.category_path
                            serializer = Furniture_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                time.sleep(1)

                                serializer.save()
                            else:
                                print ""

                                #print("bad json")

            except:
                print ""

                # for laptop in laptops:
                # #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # #print "end"
        nextpage = None

    #print len(laptops)

    if nextpage != None:
        time.sleep(0.15)
        Office_Walmart(request, categoryId, nextpage)


#3920
def Books_Walmart(request,categoryId="3920_5196470_6575803",nextpage=0):
    products,nextpage = obj1.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            # #print "path:        "+product.category_path
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:


                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM"+str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] =product.model_number
                        request["SNR_Price"] =product.sale_price
                        request["SNR_ProductURL"] =product.product_url
                        request["SNR_SubCategory"] = product.category_path
                        request["SNR_Description"]=product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Books_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            time.sleep(1)

                            serializer.save()
                        else:
                            print ""

                            #print("bad json")


                        laptops[product.model_number] = Offce("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_SubCategory"] = product.category_path
                            request["SNR_Available"] = "Walmart"

                            serializer = Books_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                            else:
                                print ""

                                #print("bad json")

            except:
                print ""

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Books_Walmart(request,categoryId,nextpage)






class Health:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,Health)

#or "Electronics/Computers/Laptop Computers" in product.category_path
#
#1094765_133224_3214799
#976760_36290
#4125_4134
#5427_1224874
#3920_7415838
#3944_1229875_4214212
def Health_Walmart(request,categoryId="3944_1229875_4214212",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            try:


                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM"+str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] =product.model_number
                        request["SNR_Price"] =product.sale_price
                        request["SNR_ProductURL"] =product.product_url
                        request["SNR_Description"]=product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Health_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            time.sleep(1)

                            serializer.save()
                        else:
                            print ""

                            #print("bad json")


                        laptops[product.model_number] = Offce("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand
                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"

                            serializer = Health_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                serializer.save()
                                time.sleep(1)

                            else:
                                print ""

                                #print("bad json")

            except:
                print ""

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Health_Walmart(request,categoryId,nextpage)








class Movies:
    def __init__(self, sku, title, model, brand, upc, price, url, imgUrl, desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available = "Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc

    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr


laptops = defaultdict(lambda: None, Movies)


# or "Electronics/Computers/Laptop Computers" in product.category_path
#
# 1094765_133224_3214799
#1085632_1229472_1229475
#1085632_1105934
#1085632_1228561
def Movies_Walmart(request,categoryId="4096", nextpage=0):


    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
                request["SNR_Brand"]=brand
            if product.available_online == None:
                product.available_online=False


            if product.large_image != None:
                image = product.large_image
                request["SNR_ImageURL"]=image

            elif product.medium_image != None:
                image = product.medium_image
                request["SNR_ImageURL"] = image
            else:
                image = product.thumbnail_image
                request["SNR_ImageURL"] = image

            try:


                if (product.available_online == True) and (product.sale_price != None):
                    # #print product.available_online
                    if product.model_number != None and laptops[product.model_number] == None:

                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand
                        request["SNR_SKU"] = "WM"+str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] =product.model_number
                        request["SNR_Price"] =product.sale_price
                        request["SNR_ProductURL"] =product.product_url
                        request["SNR_Description"]=product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Movies_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            time.sleep(1)

                            serializer.save()
                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number] = Movies("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            request["SNR_ImageURL"] = image
                            request["SNR_Brand"] = brand

                            request["SNR_SKU"] = "WM" + str(product.item_id)
                            request["SNR_Title"] = product.name
                            request["SNR_UPC"] = product.upc
                            request["SNR_ModelNo"] = product.model_number
                            request["SNR_Price"] = product.sale_price
                            request["SNR_ProductURL"] = product.product_url
                            request["SNR_Description"] = product.long_description
                            request["SNR_Available"] = "Walmart"

                            serializer = Movies_Serializer(data=request)
                            #print("calling ")
                            #print(serializer)
                            if serializer.is_valid():
                                #print("---")
                                time.sleep(1)

                                serializer.save()
                            else:
                                print ""

                                #print("bad json")

                            #print("same model found with lower price")
                            laptops[product.model_number]=Movies("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                            #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl
            except:
                print ""

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None
    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Movies_Walmart(request,categoryId,nextpage)


class Cam:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Cam):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,Cam)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def Cams_Walmart(request,categoryId="3944_133277",nextpage=0):
    products,nextpage = key.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):

                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = Cams_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        serializer.save()
                        time.sleep(1)

                    else:
                        print ""

                        #print("bad json")

                    laptops[product.model_number] = Cam("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        laptops[product.model_number]=Cam("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

    else:
        ##print "end"
        nextpage=None

    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Cams_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()



class software:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,software)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def software_Walmart(request,categoryId="3944_3951_443023",nextpage=0):
    products,nextpage = key.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online

                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = Software_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        serializer.save()
                        time.sleep(1)

                    else:
                        print ""

                        #print("bad json")

                    laptops[product.model_number] = software("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Software_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number]=software("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        software_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()


class WalmartTV:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,WalmartTV)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def TV_Walmart(request,categoryId="3944_1060825_447913",nextpage=0):

    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)

    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = TV_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        serializer.save()
                        time.sleep(1)

                    else:
                        print ""

                        #print("bad json")

                    laptops[product.model_number] = WalmartTV("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = TV_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number]=WalmartTV("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None

    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        TV_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()





class appliances:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,appliances)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def appliances_Walmart(request,categoryId="3944_1229875",nextpage=0):
    products,nextpage = obj1.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = Applinces_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        serializer.save()
                        time.sleep(1)

                    else:
                        print ""

                        #print("bad json")

                    laptops[product.model_number] = appliances("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Applinces_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                        else:
                            print ""

                            #print("bad json")

                        #print("same model found with lower price")
                        laptops[product.model_number]=appliances("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None

    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        appliances_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()



class audio:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,audio)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def audio_Walmart(request,categoryId="3944_133251",nextpage=0):
    products,nextpage = obj1.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = Audio_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        time.sleep(1)

                        serializer.save()
                    else:
                        print ""

                        #print("bad json")

                    laptops[product.model_number] = audio("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Audio_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number]=audio("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None
    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        audio_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()







class games:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,games)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def games_Walmart(request,categoryId="2636",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = VideoGames_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        serializer.save()
                        time.sleep(1)

                    else:
                        print ""

                        #print("bad json")

                    laptops[product.model_number] = games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = VideoGames_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                        else:
                            print ""

                            #print("bad json")

                        laptops[product.model_number]=games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        games_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()




def toys_Walmart(request,categoryId="5427",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = Toys_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        serializer.save()
                        time.sleep(1)

                    else:
                        print ""

                        print("bad json")

                    # laptops[product.model_number] = games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Toys_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                        else:
                            print ""

                            #print("bad json")

                        # laptops[product.model_number]=games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        # #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        toys_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()





def toys_Walmart(request,categoryId="5427",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:


                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = Toys_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        time.sleep(1)

                        serializer.save()
                    else:
                        print ""

                        print("bad json")

                    # laptops[product.model_number] = games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Toys_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                        else:
                            print ""

                            #print("bad json")

                        # laptops[product.model_number]=games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        # #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        toys_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()




def cars_Walmart(request,categoryId="3944_538883",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = CarsElec_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        time.sleep(1)

                        serializer.save()
                    else:
                        print ""

                        print("bad json")

                    # laptops[product.model_number] = games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = CarsElec_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                        else:
                            print ""

                            #print("bad json")

                        # laptops[product.model_number]=games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        # #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        cars_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()







def smarthome_Walmart(request,categoryId="1072864_1229875",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    #print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                #print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    serializer = Smarthomes_Serializer(data=request)
                    #print("calling ")
                    #print(serializer)
                    if serializer.is_valid():
                        #print("---")
                        serializer.save()
                        time.sleep(1)

                    else:
                        print ""

                        print("bad json")

                    # laptops[product.model_number] = games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        #print("same model found with lower price")
                        request["SNR_ImageURL"] = image
                        request["SNR_Brand"] = brand

                        request["SNR_SKU"] = "WM" + str(product.item_id)
                        request["SNR_Title"] = product.name
                        request["SNR_UPC"] = product.upc
                        request["SNR_ModelNo"] = product.model_number
                        request["SNR_Price"] = product.sale_price
                        request["SNR_ProductURL"] = product.product_url
                        request["SNR_Description"] = product.long_description
                        request["SNR_Available"] = "Walmart"

                        serializer = Smarthomes_Serializer(data=request)
                        #print("calling ")
                        #print(serializer)
                        if serializer.is_valid():
                            #print("---")
                            serializer.save()
                            time.sleep(1)

                            time.sleep(1)
                        else:
                            print ""

                            #print("bad json")

                        # laptops[product.model_number]=games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        # #print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            ##print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        ##print "end"
        nextpage=None


    #print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        smarthome_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()











Movies_Walmart({})

Furniture_Walmart({})
time.sleep(5)
HomeandGradden_Walmart({})
time.sleep(5)
Clothes_Walmart({})
time.sleep(5)
Flowers_Walmart({})
time.sleep(5)
time.sleep(5)
Jewelry_Walmart({})
time.sleep(5)
Arts_Walmart({})
time.sleep(5)
software_Walmart({})
time.sleep(5)
smarthome_Walmart({})
time.sleep(5)
cars_Walmart({})
time.sleep(5)
audio_Walmart({})
Office_Walmart({})
appliances_Walmart({})
time.sleep(5)
Cams_Walmart({})
time.sleep(5)
toys_Walmart({})
time.sleep(5)
TV_Walmart({})
time.sleep(5)

Health_Walmart({})
time.sleep(5)

Books_Walmart({})
time.sleep(5)

games_Walmart({})
time.sleep(5)

from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'produc.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        Movies_Walmart({})

        Furniture_Walmart({})
        time.sleep(5)
        HomeandGradden_Walmart({})
        time.sleep(5)
        Clothes_Walmart({})
        time.sleep(5)
        Flowers_Walmart({})
        time.sleep(5)
        time.sleep(5)
        Jewelry_Walmart({})
        time.sleep(5)
        Arts_Walmart({})
        time.sleep(5)
        software_Walmart({})
        time.sleep(5)
        smarthome_Walmart({})
        time.sleep(5)
        cars_Walmart({})
        time.sleep(5)
        audio_Walmart({})
        Office_Walmart({})
        appliances_Walmart({})
        time.sleep(5)
        Cams_Walmart({})
        time.sleep(5)
        toys_Walmart({})
        time.sleep(5)
        TV_Walmart({})
        time.sleep(5)

        Health_Walmart({})
        time.sleep(5)

        Books_Walmart({})
        time.sleep(5)

        games_Walmart({})
        time.sleep(5)

        pass    # do your thing here
    do(0)