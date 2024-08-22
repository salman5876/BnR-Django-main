
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from products.serializers import *
import json
from wapy.api import Wapy
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


def Clothes_Walmart(request, categoryId, nextpage=0):
    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    print products
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
                    # print product.available_online
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

                        request["SNR_Category"] = "Clothes"
                        request["SNR_SubCategory"] = "Clothes"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer1.errors
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

                            request["SNR_Category"] = "Clothes"
                            request["SNR_SubCategory"] = "Clothes"

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

                # for laptop in laptops:
                # print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # print "end"
        nextpage = None

    print len(laptops)

    if nextpage != None:
        time.sleep(0.15)
        Clothes_Walmart(request, categoryId, nextpage)





import requests
class bestbuy:




    def getClothes(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=clothe*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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

                    request["SNR_Category"] = "Clothes"
                    request["SNR_SubCategory"] = "Clothes"

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
                        request["SNR_SubCategory"] = "Arts"
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                            # print(item["sku"])
                            # print(item["links"]["web"])
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])

                        request["SNR_Category"] = "Clothes"
                        request["SNR_SubCategory"] = "Clothes"

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


                                #can add more categories
    def ebayHomeClothingAll(self, request):
        listCatagories = ['3082','163147','155240','112425','171146','137085','63862','63861','11524','11514','11554','3009','169001','172378','84275','15691','11507','15687','15690'
            ,'4250','1059','93427','28015','155184','175759','3259','41964','4251','15724','169291','3034','314','63863','11555','63864','63865','63866','63869','53159','15775',
                          '155183','11484','3001','11511','11510','15689','57989','11483','57991','57988','57990','3002']
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
                request["SNR_Category"] = "Clothes"
                request["SNR_SubCategory"] = "Clothes"

                # serializer = Mobile_Serializer(data=request)
                serializer1 = AllProducts_Serializer(data=request)

                if serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")
                    print serializer1.error_messages


#3920
bestbuy().getClothes({})

listCatagories = ['5438_1228424']
for category in listCatagories:
    time.sleep(30)
    Clothes_Walmart({}, category)
time.sleep(30)

time.sleep(30)
EbayAPI().ebayHomeClothingAll({})
time.sleep(30)


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'clothes.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        bestbuy().getClothes({})
        EbayAPI().ebayHomeClothingAll({})

        listCatagories = ['5438_1228424']
        for category in listCatagories:
            time.sleep(30)
            Clothes_Walmart({}, category)
        time.sleep(30)

        time.sleep(30)
        time.sleep(30)
        pass    # do your thing here
    do(0)