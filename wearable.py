
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()


from wapy.api import Wapy
from wearables.serializers import Wearable_Serializer
import time
from collections import defaultdict
from wearables.models import Wearable_DB
from products.serializers import AllProducts_Serializer

obj1 = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
obj = Wapy('m9esvpqxg8vc85g97726vdmn')


class Wearable:

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
            for attr in dir(Wearable):
                if not attr.startswith("__"):
                    yield attr





wearables=defaultdict(lambda: None,Wearable)
Accessories=["tempered glass","screen protector","protective case",
                 "protective holder","silicone replacement","wrist band",
                 "bracelet strap","watch case","band strap",
                 "sports band","sports bracelet","replacement silicone",
                 "sports strap","watch band","dock charger","watch charging",
                 "wireless charger","dock station","wrist strap","wrap",
                 "skin decal","replacement","accessory","accessory band",
                 "replace","loop band","woven nylon","sport nylon","nylon band",
                 "leather loop","stand","ipm","sport bands","cable","battery","band"]


accessoryFound = False
appleAccessoryFound = False
#3944_1086506_1089150
#3944_1229723
#Wearable
def wearable_Walmart(request,categoryId,nextpage=0):

    products, nextpage = obj1.pagination(categoryId=categoryId, nextpage=nextpage)
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

                if  (product.available_online == True) and ( product.sale_price != None) :
                    print product.available_online
                    if product.model_number != None and mobiles[product.model_number] == None:
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

                        request["SNR_Category"] = "Wearables"
                        request["SNR_SubCategory"] = "Wearables"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")

                        wearables[product.model_number] = wearables("WM" + str(product.item_id), product.name,
                                                               product.model_number, product.brand_name, product.upc,
                                                               product.sale_price, product.product_url,
                                                               image, product.long_description)
                    else:
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

                        request["SNR_Category"] = "Wearables"
                        request["SNR_SubCategory"] = "Wearables"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")

                        if wearables[product.model_number].price > product.sale_price:
                            print("same model found with lower price")
                            wearables[product.model_number] = wearables("WM" + str(product.item_id), product.name,
                                                                   product.model_number, product.brand_name, product.upc,
                                                                   product.sale_price, product.product_url,
                                                                   image, product.long_description)
                            print wearables[product.model_number], wearables[product.model_number].title, wearables[
                                product.model_number].price, wearables[product.model_number].productUrl

                            # for laptop in laptops:
                            # print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
            except:
                print "exception"
    else:
        # print "end"
        nextpage = None



    if nextpage != None:
        #for model in mobiles:
            #print mobiles[model].model, mobiles[model].title, mobiles[model].price, mobiles[model].productUrl
        time.sleep(0.15)
        wearable_Walmart(request,categoryId, nextpage)



from wearables.serializers import Wearable_Serializer
from ebaysdk.finding import Connection as finding
import requests
import time
import json
class EbayAPI():
    def ebayWearableAll(self, request):
        listCatagories = ['178893','31387','173695','3937','31387','98624']
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
                try:

                    request["SNR_Price"] = item['buyItNowPrice']['__value__']
                    request["SNR_Brand"] = "No Brand"
                    request["SNR_Available"] = "Ebay"
                    request["SNR_Description"] = "Visit site to see description"
                    request["SNR_Title"] = item['title'].encode("utf-8")
                    request["SNR_ImageURL"] = item['imageURL']
                    request["SNR_ProductURL"] = item['viewItemURL']
                    request["SNR_ModelNo"] = "00"
                    request["SNR_SKU"] = "EB" + str(item['itemId'])
                    request["SNR_UPC"] = "00"
                    request["SNR_Category"] = "Wearables"
                    request["SNR_SubCategory"] = "Wearables"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                except:
                    print "error"



import requests
from wearables.serializers import Wearable_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
import exceptions

class BestbuyAPI():

    def Wearables(self,request):
        try:
            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=action*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=activity*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=watch*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=fitness*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=headphones*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=pet tracking*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=smart sports*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=smart tracker*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=smart watches*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=virtual*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    # print it['id']
                    listCatagories.append(it['id'])

            for category in listCatagories:
                print category

                response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,customerReviewAverage,sku,modelNumber,upc,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
                data =response.json()
                print(data)
                for item in data['products']:

                    # print item["name"]
                    try:
                        request["SNR_CustomerReviews"] = item["customerReviewAverage"]

                        request["SNR_Title"] = item["name"].encode("utf-8")
                        request["SNR_Price"] = item["salePrice"];
                        request["SNR_ProductURL"] = item["url"];
                        request["SNR_Available"] = "Best Buy"
                        request["SNR_ImageURL"] = item["image"]
                        request["SNR_Brand"] = item["manufacturer"]
                        request["SNR_ModelNo"] = item["modelNumber"];
                        request["SNR_UPC"] = item["upc"]
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_Description"] = item["longDescription"].encode("utf-8")

                        request["SNR_Category"] = "Wearables"
                        request["SNR_SubCategory"] = "Wearables"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer.errors
                            print serializer.error_messages
                    except:
                        print "error"


                totalPages = data["totalPages"]
                count=2
                print totalPages
                while(count<=int(totalPages)):
                    print "amad"

                    count+=1

                    response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,customerReviewAverage,name,sku,modelNumber,upc,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100&page="+str(count))
                    data = response.json()
                    # print(data)
                    for item in data['products']:

                        # print (item["name"])
                        try:
                            request["SNR_CustomerReviews"] = item["customerReviewAverage"]

                            request["SNR_Title"] = item["name"].encode("utf-8")
                            request["SNR_Price"] = item["salePrice"];
                            request["SNR_ProductURL"] = item["url"];
                            request["SNR_Available"] = "Best Buy"
                            request["SNR_ImageURL"] = item["image"]
                            request["SNR_Brand"] = item["manufacturer"]
                            request["SNR_ModelNo"] = item["modelNumber"];
                            request["SNR_UPC"] = item["upc"]
                            request["SNR_SKU"] = "BB" + str(item["sku"])
                            request["SNR_Description"] = item["longDescription"].encode("utf-8")
                            request["SNR_Category"] = "Wearables"
                            request["SNR_SubCategory"] = "Wearables"

                            # serializer = Mobile_Serializer(data=request)
                            serializer1 = AllProducts_Serializer(data=request)

                            if serializer1.is_valid():
                                print("---")
                                # serializer.save()
                                serializer1.save()
                            else:
                                print("bad json")
                                print serializer.errors
                                print serializer.error_messages
                        except:
                            print "error"






        except StandardError as e:
            print(e.message)




from bs4 import BeautifulSoup
import time
baseAddress = "http://localhost:8000/"


class GroupOnAPI():
    def groupWearable(self, request):

        flag = True
        page = 1
        while flag == True:
            time.sleep(3)
            url = 'https://www.groupon.com/goods/wearable-technology?brand=119d26b8-2afe-4494-bbd6-702f5c7fee6c%2C298dfbcc-9737-42a1-b79e-b8820ad55737%2C2badc5e4-b30d-4ef2-8510-5777a95b40b1%2C32f7210d-2ea7-498d-a2a9-5716a8e83ce2%2C4be23845-9268-48ac-809f-fc1324f36a8f%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C6a886149-f219-4423-9978-79d9a274088e%2C8c08fd0c-e9b5-4900-9878-a3d53cfb5bf8%2C9a2a5ef7-a244-4851-8960-e36246e38eea%2C9bd95012-195d-4fa4-a37a-bb87a93c85c0%2C9e1e4822-b9a6-4367-a947-1f6afa68dc21%2Ca1957946-766d-4cf5-b446-af7476ed302a%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Ca6a8b9e2-f1a4-42a6-8151-0ca80f8e85b7%2Ca77185b5-b78c-423a-be8a-0fb4545a1e64%2Ca8789205-ee9d-46f2-9922-817e547d56ff%2Cb1ccee99-5a63-4dfc-81cf-6044bdabbd19%2Ccee45173-df2a-4f4d-a1f2-bd868cc9572c%2Cd19b8561-fc62-4a04-b797-e29be85c9c0c%2Cd6c85834-4d68-49bb-9934-b0170d779787%2Ce16da45a-8423-47f0-9278-dd863904a3ae%2Cec03289e-2556-4d42-b8b9-9eb395757c34%2Cf31f1916-1668-405c-bf1f-dcd04acc674e%2Cfd768008-970f-4dd1-bb48-b171429c1d1b&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            # print plain_text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []
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
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0
                    try:

                        request["SNR_Price"] = price[1:]

                        request["SNR_Brand"] = "Visit site to see Brand"
                        request["SNR_Available"] = "Groupon "

                        request["SNR_Description"] = description.decode('unicode_escape').encode('ascii', 'ignore')

                        request["SNR_Title"] = title.decode('unicode_escape').encode('ascii', 'ignore')

                        request["SNR_ImageURL"] ="https:"+ str(img)
                        request["SNR_ProductURL"] = address
                        request["SNR_ModelNo"] = "00"
                        request["SNR_SKU"] = "00"
                        request["SNR_UPC"] = "00"
                        request["SNR_Category"] = "Wearables"
                        request["SNR_SubCategory"] = "Wearables"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer.error_messages

                            print("bad json")
                    except:
                        print "error"

                    count += 1




from amazonproduct import API
import lxml.etree
import unicodedata
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from wearables.serializers import Wearable_Serializer
from ebaysdk.finding import Connection as finding
from lxml import objectify
import time


AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():
    def amazonWatches(self,request):
        listCatagories = ['378516011', '10103533031', '10103532031','10103534031','10103530031','10103539031','10103538031','10103540031','10103543031','10103542031','10103541031','10103529031','10103536031','10103535031','10103537031' ]
        for category in listCatagories:
            try:




                for data in api.item_search('Electronics', BrowseNode=category, Sort='-price',ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
                    time.sleep(2)


                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title).encode("utf-8")
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

                        request["SNR_Description"]  = str(data.ItemAttributes.Feature).encode("utf-8")

                    except:
                        request["SNR_Description"] ="Please visit site to see description"




                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



                    try:

                        request["SNR_ImageURL"]=str(data.LargeImage.URL)

                    except :


                        try:
                            request["SNR_ImageURL"]= str(data.MediumImage.URL)
                        except:
                                # print
                                request["SNR_ImageURL"]=str(data.SmallImage.URL)

                    try:

                        request["SNR_UPC"] =str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"]= str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except :

                            try:
                                request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    request["SNR_Category"] = "Wearables"
                    request["SNR_SubCategory"] = "Wearables"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                        print serializer.error_messages

                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            except:


                print "Error"



listCatagories = ['3944_1086506_1089150', '3944_1229723', '4125_4134_1229723']
for category in listCatagories:
    wearable_Walmart({}, category)

AmazonAPI().amazonWatches({})

BestbuyAPI().Wearables({})

EbayAPI().ebayWearableAll({})



GroupOnAPI().groupWearable({})

GroupOnAPI().groupWearable({})

listCatagories = ['3944_1086506_1089150', '3944_1229723', '4125_4134_1229723']
for category in listCatagories:
    wearable_Walmart({}, category)


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'wearable.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        GroupOnAPI().groupWearable({})
        AmazonAPI().amazonWatches({})

        BestbuyAPI().Wearables({})

        EbayAPI().ebayWearableAll({})

        listCatagories = ['3944_1086506_1089150', '3944_1229723', '4125_4134_1229723']
        for category in listCatagories:
            wearable_Walmart({}, category)
        pass    # do your thing here
    do(0)