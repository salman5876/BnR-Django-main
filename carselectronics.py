
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


def cars_Walmart(request,categoryId,nextpage=0):
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
                    request["SNR_Brand"] = brand

                    request["SNR_SKU"] = "WM" + str(product.item_id)
                    request["SNR_Title"] = product.name
                    request["SNR_UPC"] = product.upc
                    request["SNR_ModelNo"] = product.model_number
                    request["SNR_Price"] = product.sale_price
                    request["SNR_ProductURL"] = product.product_url
                    request["SNR_Description"] = product.long_description
                    request["SNR_Available"] = "Walmart"

                    request["SNR_Category"] = "Cars Electronics"
                    request["SNR_SubCategory"] = "Cars Electronics"

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
                        request["SNR_Category"] = "Cars Electronics"
                        request["SNR_SubCategory"] = "Cars Electronics"

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
        cars_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()




from amazonproduct import API
from products.serializers import Audio_Serializer, CarsElec_Serializer,Software_Serializer,TV_Serializer,Movies_Serializer,Toys_Serializer,CarsElec_Serializer,Office_Serializer,VideoGames_Serializer,Smarthomes_Serializer,Applinces_Serializer
import time

AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():



    def amazonCarsElectronics(self,request):

        listCatagories = ['15710351','2204830011','15857501','15706941','15857511','15706571','2230642011','1077068','15684181','2204830011','15718271','2230642011','15857511','15857501','346333011','15718791','15709231','15710351','15719731','2258019011','15706941','15706571']
        for category in listCatagories:
            try:

                for data in api.item_search('Automotive', BrowseNode=category, Sort='-price',
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
                    request["SNR_Category"] = "Cars Electronics"
                    request["SNR_SubCategory"] = "Cars Electronics"

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






import requests
class bestbuy:



    def getCarsElect(self, request):
        try:
            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=gps*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            print(data)
            for item in data['categories']:
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])

            for category in listCatagories:
                print category

                response = requests.get(
                    "https://api.bestbuy.com/v1/products((categoryPath.id=" + category + "))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,customerReviewAverage,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
                data = response.json()
                # print(data)
                for item in data['products']:

                    # print item["name"]
                    request["SNR_Price"] = item["salePrice"]
                    request["SNR_CustomerReviews"] = item["customerReviewAverage"]


                    request["SNR_Brand"] = item["manufacturer"]
                    request["SNR_Available"] = "Best Buy"
                    if item["longDescription"] == None:

                        request["SNR_Description"] = "No Description"
                    else:
                        request["SNR_Description"] = item["longDescription"]

                        request["SNR_Title"] = (item["name"])
                    if item["image"] == None:
                            request[
                                "SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    else:
                        request["SNR_ImageURL"] = (item["image"])
                        request["SNR_ProductURL"] = item["url"]
                        request["SNR_ModelNo"] = item["modelNumber"]
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                        request["SNR_Category"] = "Cars Electronics"
                        request["SNR_SubCategory"] = "Cars Electronics"

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
                    count = 2
                    # print totalPages
                    while (count <= int(totalPages)):
                        # print "amad"

                        count += 1

                        response = requests.get(
                            "https://api.bestbuy.com/v1/products((categoryPath.id=" + category + "))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,customerReviewAverage,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100&page=" + str(
                                count))
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
                            # print(item["links"]["web"])
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                            request["SNR_Category"] = "Cars Electronics"
                            request["SNR_SubCategory"] = "Cars Electronics"

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


    def ebayCarselecAll(self, request):
        listCatagories = ['3270','73335','48610','175716','32806','60207','48604','139836','156955','168105','1498','14935','168093','75390','94830','60203','75389','71530','18795','39754','39746','14936','18805','175717','79839','71527','75386','50549','85806','50550','50551','94844','50552','32810','50564','67773','64578','73348',
                          '168103','175726','73353','168104','139837','58049','73362','175712','48606','48605','149976','79834','79835']
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
                request["SNR_Category"] = "Cars Electronics"
                request["SNR_SubCategory"] = "Cars Electronics"

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


    def groupCarsElectronics(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/car-electronics-and-gps?brand=085b8ef1-6195-4936-9a78-0ab6409a4af2%2C0cad1ce7-60fe-453f-9640-cc29f4cfdd0b%2C119d26b8-2afe-4494-bbd6-702f5c7fee6c%2C3061f93c-4a05-4c3a-8bab-65618ecd042b%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C434bb387-8e82-446f-9d25-c0578ab24600%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C50e5275a-2712-4653-91f8-410197177d7a%2C5a443675-0b42-441e-8d60-378f8fd6ba62%2C5f6e1462-a7df-4dd5-9a62-ee1077b7ffb8%2C5fca46bd-c4e3-4eb3-a329-333cca916127%2C904231b9-f837-4dab-8f5f-ad3dc9acd3ad%2C965b4979-61eb-4150-a63e-6a55b150c70c%2C990dc215-e0fe-4b04-97e6-81d10e80de31%2Ca093638f-2739-42d2-a6d2-7f5777cda678%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Cc756c723-9cbf-4d2c-bb4c-3a7d53fa3357%2Cdb89a50c-3579-4a71-91a7-c2c4daa93ecb%2Cdb92452b-396b-4e7a-932d-ee6bdcea71d9%2Cf457b68e-928e-453e-8ced-641c244dbf6d&page=' + str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")



                for link in soup.findAll('figure', {'class': 'card-ui'}):
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

                    request["SNR_ImageURL"] ="https:"+ img
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    request["SNR_Category"] = "Cars Electronics"
                    request["SNR_SubCategory"] = "Cars Electronics"

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
            request["SNR_Category"] = "Cars Electronics"
            request["SNR_SubCategory"] = "Cars Electronics"

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
                request["SNR_Category"] = "Cars Electronics"
                request["SNR_SubCategory"] = "Cars Electronics"

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
listCatagories = ['3944_538883']
for category in listCatagories:
    cars_Walmart({}, category)

AmazonAPI().amazonCarsElectronics({})
GroupOnAPI().groupCarsElectronics({})

bestbuy().getCarsElect({})

EbayAPI().ebayCarselecAll({})




from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cars.my_cron_job'    # a unique code

    def do(self):
        listCatagories = ['3944_538883']
        for category in listCatagories:
            cars_Walmart({}, category)

        AmazonAPI().amazonCarsElectronics({})
        GroupOnAPI().groupCarsElectronics({})

        bestbuy().getCarsElect({})

        EbayAPI().ebayCarselecAll({})

        pass    # do your thing here
    do(0)