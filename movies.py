
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from products.serializers import *
import json
from wapy.api import Wapy
from collections import defaultdict






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
def Movies_Walmart(request,categoryId, nextpage=0):


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

                        request["SNR_Category"] = "Movies"
                        request["SNR_SubCategory"] = "Movies"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer1.errors
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
                            serializer1 = AllProducts_Serializer(data=request)
                            print(serializer)
                            if serializer.is_valid() & serializer1.is_valid():
                                print("---")
                                serializer.save()
                                serializer1.save()
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



from amazonproduct import API
from products.serializers import Audio_Serializer, CarsElec_Serializer,Software_Serializer,TV_Serializer,Movies_Serializer,Toys_Serializer,Cams_Serializer,Office_Serializer,VideoGames_Serializer,Smarthomes_Serializer,Applinces_Serializer
import time

AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():
    def amazonMovies(self, request):

        listCatagories = ['2649512011', '2649513011']

        for category in listCatagories:
            try:

                for data in api.item_search('DVD', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
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
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

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

                    request["SNR_Category"] = "Movies"
                    request["SNR_SubCategory"] = "Movies"

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
                print "Error"

        for data in api.item_search('Electronics', BrowseNode='165793011', Sort='-price',
                                    ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
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

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            request["SNR_Category"] = "Movies"
            request["SNR_SubCategory"] = "Movies"

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



    def getMovies(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=movies*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])
            for category in listCatagories:
                print category

                response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,customerReviewAverage,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
                data =response.json()
                # print(data)
                for item in data['products']:

                    request["SNR_CustomerReviews"] = item["customerReviewAverage"]

                    # print item["name"]
                    request["SNR_Price"] = item["salePrice"]

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
                    request["SNR_Category"] = "Movies"
                    request["SNR_SubCategory"] = "Movies"

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
                        request["SNR_Price"] = item["salePrice"]
                        request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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
                        request["SNR_Category"] = "Movies"
                        request["SNR_SubCategory"] = "Movies"

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


    def ebayMoviesAll(self, request):
        listCatagories = ['63821','11232','617','381','41676','132975','309','2362','2329','196']
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
                request["SNR_Category"] = "Movies"
                request["SNR_SubCategory"] = "Movies"

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

    def groupMovies(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods?category=entertainment-and-media&category2=movies-and-tv&query=movies&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    img=""
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

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

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    request["SNR_Category"] = "Movies"
                    request["SNR_SubCategory"] = "Movies"

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







EbayAPI().ebayMoviesAll({})

bestbuy().getMovies({})

listCatagories = ['1094765_133224_3214799', '1085632_1229472_1229475', '1085632_1105934', '1085632_1228561',
                  '4096']
for category in listCatagories:
    Movies_Walmart({}, category)



GroupOnAPI().groupMovies({})

AmazonAPI().amazonMovies({})


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'movie.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        GroupOnAPI().groupMovies({})

        AmazonAPI().amazonMovies({})

        EbayAPI().ebayMoviesAll({})

        bestbuy().getMovies({})

        listCatagories = ['1094765_133224_3214799', '1085632_1229472_1229475', '1085632_1105934', '1085632_1228561',
                          '4096']
        for category in listCatagories:
            Movies_Walmart({}, category)

        pass    # do your thing here
    do(0)