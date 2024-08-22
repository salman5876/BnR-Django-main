
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from products.serializers import *
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

#or "Electronics/Computers/Laptop Computers" in product.category_path
#
#1094765_133224_3214799
def Office_Walmart(request,categoryId="1229749_1046059",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
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
                    # print product.available_online
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

                        request["SNR_Category"] = "Office Supplies"
                        request["SNR_SubCategory"] = "Office Supplies"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer1.errors

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

                            request["SNR_Category"] = "Office Supplies"
                            request["SNR_SubCategory"] = "Office Supplies"

                            # serializer = Mobile_Serializer(data=request)
                            serializer1 = AllProducts_Serializer(data=request)

                            if serializer1.is_valid():
                                print("---")
                                # serializer.save()
                                serializer1.save()
                            else:
                                print("bad json")
                                print serializer1.errors
            except:
                print "exception"

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None


    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Office_Walmart(request,categoryId,nextpage)


from amazonproduct import API
import lxml.etree
import unicodedata
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from products.serializers import Audio_Serializer, CarsElec_Serializer,Software_Serializer,TV_Serializer,Movies_Serializer,Toys_Serializer,Cams_Serializer,Office_Serializer,VideoGames_Serializer,Smarthomes_Serializer,Applinces_Serializer
from ebaysdk.finding import Connection as finding
from lxml import objectify
import time

AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():

    def amazonOffice(self,request):

        # get all books from result set and
        # print author and title

        for data in api.item_search('OfficeProducts', BrowseNode='172574',ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

            except:

                try:
                    request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                except:

                    try:
                        request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                    except:
                        request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            request["SNR_Category"] = "Office Supplies"
            request["SNR_SubCategory"] = "Office Supplies"

            # serializer = Mobile_Serializer(data=request)
            serializer1 = AllProducts_Serializer(data=request)

            if serializer1.is_valid():
                print("---")
                # serializer.save()
                serializer1.save()
            else:
                print("bad json")
                print serializer1.errors
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        for data in api.item_search('OfficeProducts', BrowseNode='1069102', ResponseGroup='ItemAttributes,Images,Large',
                                    limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

            except:

                try:
                    request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                except:

                    try:
                        request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                    except:
                        request["SNR_Price"] = str(0)



            request["SNR_Available"] = "Amazon"

            request["SNR_Category"] = "Office Supplies"
            request["SNR_SubCategory"] = "Office Supplies"

            # serializer = Mobile_Serializer(data=request)
            serializer1 = AllProducts_Serializer(data=request)

            if serializer1.is_valid():
                print("---")
                # serializer.save()
                serializer1.save()
            else:
                print("bad json")
                print serializer1.errors
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('OfficeProducts', BrowseNode='1069242', ResponseGroup='ItemAttributes,Images,Large',
                                    limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

            except:

                try:
                    request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                except:

                    try:
                        request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                    except:
                        request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"

            request["SNR_Category"] = "Office Supplies"
            request["SNR_SubCategory"] = "Office Supplies"

            # serializer = Mobile_Serializer(data=request)
            serializer1 = AllProducts_Serializer(data=request)

            if serializer1.is_valid():
                print("---")
                # serializer.save()
                serializer1.save()
            else:
                print("bad json")
                print serializer1.errors
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




from bestbuy import BestBuyProductsAPI

import requests
class bestbuy:





    def getOfficeSupply(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=office*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            print(data)
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])

            for category in listCatagories:
                print category

                response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,customerReviewAverage,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
                data =response.json()
                # print(data)
                for item in data['products']:


                    # print item["name"]
                    request["SNR_Price"] = item["salePrice"]
                    request["SNR_CustomerReviews"] = item["customerReviewAverage"]

                    request["SNR_Brand"] = item["manufacturer"]
                    request["SNR_Available"] = "Best Buy"
                    if item["longDescription"]==None:

                        request["SNR_Description"] = "No Description"
                    else:
                        request["SNR_Description"] = item["longDescription"]

                    request["SNR_Title"] = (item["name"])
                    if item["image"] ==None:
                        request["SNR_ImageURL"] ="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    else:
                        request["SNR_ImageURL"] = (item["image"])
                    request["SNR_ProductURL"] = item["url"]
                    request["SNR_ModelNo"] = item["modelNumber"]
                    request["SNR_SKU"] = "BB" + str(item["sku"])
                    request["SNR_UPC"] = item["upc"]


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    request["SNR_Category"] = "Office Supplies"
                    request["SNR_SubCategory"] = "Office Supplies"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                        print serializer1.errors
                        
                totalPages = data["totalPages"]
                count=2
                # print totalPages
                while(count<=int(totalPages)):
                    # print "amad"

                    count+=1

                    response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,customerReviewAverage,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100&page="+str(count))
                    data = response.json()
                    # print(data)
                    for item in data['products']:

                        # print (item["name"])
                        request["SNR_CustomerReviews"] = item["customerReviewAverage"]

                        request["SNR_Price"] = item["salePrice"]
                        request["SNR_Brand"] = item["manufacturer"]
                        request["SNR_Available"] = "Best Buy"
                        request["SNR_Description"] = item["longDescription"]
                        request["SNR_Title"] = (item["name"])
                        request["SNR_ImageURL"] = (item["image"])
                        request["SNR_ProductURL"] = item["url"]
                        request["SNR_ModelNo"] = item["modelNumber"]
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                            # print(item["sku"])
                            # print(item["links"]["web"])
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])

                        request["SNR_Category"] = "Office Supplies"
                        request["SNR_SubCategory"] = "Office Supplies"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer1.errors
        except StandardError as e:
            print(e.message)



class EbayAPI():




    def ebayOfficeAll(self, request):
        listCatagories = ['11828','3300','58271','25298']
        for category in listCatagories:
            response = requests.get(
                "http://svcs.ebay.com/MerchandisingService?OPERATION-NAME=getRelatedCategoryItems&SERVICE-NAME=MerchandisingService&SERVICE-VERSION=1.1.0&CONSUMER-ID=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&maxResults=100000&categoryId="+category)
            data = json.loads(response.text)
            print(data)
            totalItems = data['getRelatedCategoryItemsResponse']['itemRecommendations']['item']
            # print totalItems
            for item in totalItems:
                # print item['itemId']
                # print item['title']
                # print item['viewItemURL']
                # print item['imageURL']
                # print item['buyItNowPrice']['__value__']

                request["SNR_Price"] = item['buyItNowPrice']['__value__']
                request["SNR_Brand"] = "No Brand"
                request["SNR_Available"] = "Ebay"
                request["SNR_Description"] = "Visit site to see description"
                request["SNR_Title"] = item['title']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                request["SNR_Category"] = "Office Supplies"
                request["SNR_SubCategory"] = "Office Supplies"

                # serializer = Mobile_Serializer(data=request)
                serializer1 = AllProducts_Serializer(data=request)

                if serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")
                    print serializer1.errors



from bs4 import BeautifulSoup

baseAddress = "http://localhost:8000/"
img=""

class GroupOnAPI():



    def groupOffice(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/office-and-school-supplies?brand=1cdf8c46-f6d5-43aa-a048-2a88f15f5f35%2C1f07e9cf-f406-4b9c-98b7-f1cfa8a695d5%2C23d34b72-ea5b-464e-b1c9-092611f27b78%2C2489602b-5757-4165-bca3-11d34167f053%2C2a5b42cd-3c7a-4799-a1a1-77bca921865e%2C3350ca50-e4d5-477f-a623-1a7ef4f56fce%2C3ffae6d6-2994-43e8-ae31-d564124ebb4a%2C41f7972b-117b-46e3-8b02-17aa2d2873f9%2C47ab2b5c-dfbd-45cf-b051-bbeb0ae5c553%2C4bf4d230-1f7e-426e-a095-e126c1469a28%2C51198fdc-779e-4881-bc41-129ef8f11600%2C7c2226ea-8563-4e5e-bbc3-6e8b4a3e2b6c%2C8efa5611-0f81-4233-93f1-e922c8f6dc73%2Ca7ad779a-8137-4e93-8592-ea6dd9ef6088%2Cb1ccee99-5a63-4dfc-81cf-6044bdabbd19%2Cec3dbb6d-8c0f-4904-b213-527843f3dc49&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                img=""

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        try:
                            img = li.get('data-high-quality')
                            # print img
                        except:
                            img="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        try:
                            for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                                description=lin.text.strip()
                        except:
                            description="No Description"

                    count = 0

                    request["SNR_Price"] = price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "
                    try:

                        request["SNR_Description"] = description
                    except:
                        request["SNR_Description"] = 'No Description'


                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    request["SNR_Category"] = "Office Supplies"
                    request["SNR_SubCategory"] = "Office Supplies"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                        print serializer1.errors
                    count += 1







class newEggAPI():


    def newEggOffice(self,request):
        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&Category=125&N=100201438%2050001009%2050001467%2050081237%2050093636%2050097055%2050129358&IsNodeId=1'
        source = requests.get(url)
        plain_text = source.text
        # print plain_text




        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('div', {'class': 'item-container'}):
            request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
            request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
            # for li in link.findAll('img'):
            #     print "https:"+li.get("src") #warranty and image

            x = link.find('a', {'class': 'item-img'})  # product image
            request["SNR_ImageURL"]= "https:" + x.find('img').get("src")
            try:
                x = link.find('a', {'class': 'item-brand'})  # product url
                request["SNR_Brand"] = "https:" + x.find('img').get("src")
            except:
                request["SNR_Brand"] = "No Brand"

            try:
                x = link.find('li', {'class': 'price-current'})
                request["SNR_Price"] = x.find('strong').text
            except:
                request["SNR_Price"] = "00"

            try:
                x = link.find('ul', {'class': 'item-features'})
                for feature in x.findAll('li'):
                    if ("Model #" in feature.text):
                        request["SNR_ModelNo"] = feature.text
                    if ("Item #" in feature.text):
                        request["SNR_SKU"] =  feature.text
            except:
                request["SNR_SKU"] ="00"
                request["SNR_ModelNo"] ="00"

            request["SNR_Available"] = "Newegg"
            request["SNR_Description"] = "Visit site to see description"
            request["SNR_UPC"] ="00"
            request["SNR_Category"] = "Office Supplies"
            request["SNR_SubCategory"] = "Office Supplies"

            # serializer = Mobile_Serializer(data=request)
            serializer1 = AllProducts_Serializer(data=request)

            if serializer1.is_valid():
                print("---")
                # serializer.save()
                serializer1.save()
            else:
                print("bad json")
                print serializer1.errors
        count = 2
        while (count < 5):
            time.sleep(count + 40)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100201438%2050001009%2050001467%2050081237%2050093636%2050097055%2050129358&IsNodeId=1&bop=And&Page=' + str(
                count) + '&pagesize=36&order=bestmatch'
            source = requests.get(url)
            plain_text = source.text
            # print plain_text
            soup = BeautifulSoup(plain_text, "lxml")
            for link in soup.findAll('div', {'class': 'item-container'}):
                request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
                request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
                # for li in link.findAll('img'):
                #     print "https:"+li.get("src") #warranty and image

                x = link.find('a', {'class': 'item-img'})  # product image
                request["SNR_ImageURL"] = "https:" + x.find('img').get("src")
                try:
                    x = link.find('a', {'class': 'item-brand'})  # product url
                    request["SNR_Brand"] = "https:" + x.find('img').get("src")
                except:
                    request["SNR_Brand"] = "No Brand"

                try:
                    x = link.find('li', {'class': 'price-current'})
                    request["SNR_Price"] = x.find('strong').text
                except:
                    request["SNR_Price"] = "00"

                try:
                    x = link.find('ul', {'class': 'item-features'})
                    for feature in x.findAll('li'):
                        if ("Model #" in feature.text):
                            request["SNR_ModelNo"] = feature.text
                        if ("Item #" in feature.text):
                            request["SNR_SKU"] = feature.text
                except:
                    request["SNR_SKU"] = "00"
                    request["SNR_ModelNo"] = "00"

                request["SNR_Available"] = "Newegg"
                request["SNR_Description"] = "Visit site to see description"
                request["SNR_UPC"] = "00"
                request["SNR_Category"] = "Office Supplies"
                request["SNR_SubCategory"] = "Office Supplies"

                # serializer = Mobile_Serializer(data=request)
                serializer1 = AllProducts_Serializer(data=request)

                if serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")
                    print serializer1.errors
            count += 1



bestbuy().getOfficeSupply({})
time.sleep(30)

AmazonAPI().amazonOffice({})
time.sleep(30)

GroupOnAPI().groupOffice({})
time.sleep(30)
newEggAPI().newEggOffice({})

listCatagories = ['1229749_1046059']
for category in listCatagories:
    time.sleep(100)

    Office_Walmart({}, category)

EbayAPI().ebayOfficeAll({})
time.sleep(30)


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'office.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        GroupOnAPI().groupOffice({})
        time.sleep(30)
        newEggAPI().newEggOffice({})

        listCatagories = ['1229749_1046059']
        for category in listCatagories:
            time.sleep(100)

            Office_Walmart({}, category)

        EbayAPI().ebayOfficeAll({})
        time.sleep(30)

        bestbuy().getOfficeSupply({})
        time.sleep(30)

        AmazonAPI().amazonOffice({})
        time.sleep(30)

        pass    # do your thing here
    do(0)