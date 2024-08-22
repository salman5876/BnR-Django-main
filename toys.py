
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


def toys_Walmart(request,categoryId,nextpage=0):
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

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    request["SNR_ImageURL"] = image
                    try:
                        request["SNR_Brand"] = brand
                    except:
                        request["SNR_Brand"]="No brand"

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    request["SNR_Category"] = "Toys"
                    request["SNR_SubCategory"] = "Toys"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                        print serializer1.error_messages

                        # laptops[product.model_number] = games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
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
                        request["SNR_Category"] = "Toys"
                        request["SNR_SubCategory"] = "Toys"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer1.error_messages

                            # laptops[product.model_number]=games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        # print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None


    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        toys_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()




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

    def amazonToys(self,request):

        listCatagories = ['166508011','166118011','166316011','166309011','166164011','166220011','165993011','3226142011','276729011','165993011','166210011','166269011','166326011','166027011','1266203011','166333011','166359011','166092011','166461011','166420011','256994011','166310011','166224011','196601011','166057011','165993011','165793011']
        for category in listCatagories:
            try:

                for data in api.item_search('Toys', BrowseNode=category, Sort='-price',
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
                    request["SNR_Category"] = "Toys"
                    request["SNR_SubCategory"] = "Toys"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                        print serializer1.error_messages
            except:
                print "Error"


        # get all books from result set and
        # print author and title




from bestbuy import BestBuyProductsAPI

import requests
class bestbuy:

    def getToys(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=drone*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            print(data)
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=toy*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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
                    request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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

                    request["SNR_Category"] = "Toys"
                    request["SNR_SubCategory"] = "Toys"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                        print serializer1.error_messages

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


                        request["SNR_Category"] = "Toys"
                        request["SNR_SubCategory"] = "Toys"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer1.error_messages





        except StandardError as e:
            print(e.message)



class EbayAPI():



    def ebayToysAll(self, request):
        listCatagories = ['175692','158666','158671','158672','175693','175694','158679','49018','175691','348','754','83732','75708','49019','18992','73248','21254','19013','180018','180019','28811','52338','19015','52339','180020','145844','19014','19018','152912','19026','2664','2536','222','145930','177915','11733','166796','11735','2518','123829','145935','19071','2550','180350','55415','234','2543','180250','19169','11743','1188','436','717','2631','436','19192','2562']
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
                request["SNR_Category"] = "Toys"
                request["SNR_SubCategory"] = "Toys"

                # serializer = Mobile_Serializer(data=request)
                serializer1 = AllProducts_Serializer(data=request)

                if serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")
                    print serializer1.error_messages


from bs4 import BeautifulSoup

baseAddress = "http://localhost:8000/"
img=""

class GroupOnAPI():



    def groupToys(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods?category=baby-kids-and-toys&category2=toys&page='+str(page)
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
                    request["SNR_Category"] = "Toys"
                    request["SNR_SubCategory"] = "Toys"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)

                    if serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print("bad json")
                        print serializer1.error_messages

                    count += 1



class newEggAPI():

    def newEggTV(self, request):
        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&Category=31&N=100198692%2050008957%2050010405%2050011043%2050011059%2050087708%2050091965&IsNodeId=1'
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
            request["SNR_Category"] = "Toys"
            request["SNR_SubCategory"] = "Toys"

            # serializer = Mobile_Serializer(data=request)
            serializer1 = AllProducts_Serializer(data=request)

            if serializer1.is_valid():
                print("---")
                # serializer.save()
                serializer1.save()
            else:
                print("bad json")
                print serializer1.error_messages

        count = 2
        while (count < 5):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100198692%2050008957%2050010405%2050011043%2050011059%2050087708%2050091965&IsNodeId=1&bop=And&Page=' + str(
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
                request["SNR_Category"] = "Toys"
                request["SNR_SubCategory"] = "Toys"

                # serializer = Mobile_Serializer(data=request)
                serializer1 = AllProducts_Serializer(data=request)

                if serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")
                    print serializer1.error_messages
            count += 1



EbayAPI().ebayToysAll({})
time.sleep(30)

bestbuy().getToys({})

listCatagories = ['5427']
for category in listCatagories:
    time.sleep(30)

    toys_Walmart({}, category)

time.sleep(30)

AmazonAPI().amazonToys({})
time.sleep(30)

GroupOnAPI().groupToys({})
time.sleep(30)

from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'toy.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        listCatagories = ['5427']
        for category in listCatagories:
            time.sleep(30)

            toys_Walmart({}, category)

        AmazonAPI().amazonToys({})
        time.sleep(30)

        GroupOnAPI().groupToys({})
        time.sleep(30)

        EbayAPI().ebayToysAll({})
        time.sleep(30)

        bestbuy().getToys({})
        time.sleep(30)
        pass    # do your thing here
    do(0)