
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from products.serializers import *
import json
from wapy.api import Wapy
from collections import defaultdict
import time






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

#or "Electronics/Computers/Laptop Computers" in product.category_path
def Books_Walmart(request,categoryId,nextpage=0):
    products,nextpage = obj1.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            # print "path:        "+product.category_path
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
                        request["SNR_SubCategory"] = product.category_path
                        request["SNR_Description"]=product.long_description
                        request["SNR_Available"] = "Walmart"
                        request["SNR_Category"] = "Books"
                        request["SNR_SubCategory"] = "Books"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")

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

                            request["SNR_Category"] = "Books"
                            request["SNR_SubCategory"] = "Books"

                            # serializer = Mobile_Serializer(data=request)
                            serializer1 = AllProducts_Serializer(data=request)

                            if serializer1.is_valid():
                                print("---")
                                # serializer.save()
                                serializer1.save()
                            else:
                                print("bad json")

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
        Books_Walmart(request,categoryId,nextpage)








from bestbuy import BestBuyProductsAPI

import requests
class bestbuy:




    def getBooks(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=book*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])


            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=magzine*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
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
                    request["SNR_SubCategory"] = "Arts"
                    request["SNR_SKU"] = "BB" + str(item["sku"])
                    request["SNR_UPC"] = item["upc"]

                    request["SNR_Category"] = "Books"
                    request["SNR_SubCategory"] = "Books"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")

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
                        request["SNR_SubCategory"] = "Arts"
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                            # print(item["sku"])
                            # print(item["links"]["web"])
                        request["SNR_Category"] = "Books"
                        request["SNR_SubCategory"] = "Books"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)







class EbayAPI():



    def ebayBooksAll(self, request):
        listCatagories = ['267','2228','268','280','171228','11104','29792','29223','118255','118256','118257','118258','118259','162029','616','162031','162030','171210','171220','171276','279','171222']
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                request["SNR_Category"] = "Books"
                request["SNR_SubCategory"] = "Books"

                # serializer = Mobile_Serializer(data=request)
                serializer1 = AllProducts_Serializer(data=request)

                if serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")


listCatagories = ['3920_5196470_6575803', '3920']
for category in listCatagories:
    time.sleep(30)
    Books_Serializer({}, category)
time.sleep(30)

time.sleep(30)
EbayAPI().ebayBooksAll({})
time.sleep(30)


#3920

from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'book.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"
        listCatagories = ['3920_5196470_6575803', '3920']
        for category in listCatagories:
            time.sleep(30)
            Books_Serializer({}, category)
        time.sleep(30)

        time.sleep(30)
        EbayAPI().ebayBooksAll({})
        time.sleep(30)

        pass    # do your thing here
    do(0)