import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from amazonproduct import API

from wapy.api import Wapy
from laptop.serializers import Laptop_Serializer
from products.serializers import AllProducts_Serializer
from products.models import AllProducts
import math
from collections import defaultdict
import time,threading





obj = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
# obj = Wapy('26zfbnn3h5wykxcyabj9f7uh')
key = Wapy('26zfbnn3h5wykxcyabj9f7uh')

class Laptop:

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
            for attr in dir(Laptop):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,Laptop)
laptopBrands=["apple","hp","dell","asus","acer","lenovo","samsung"]

#or "Electronics/Computers/Laptop Computers" in product.category_path


#3944_3951_132960
def laptop_Walmart(request,categoryId,nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    # time.sleep(5)
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
                        laptops[product.model_number] = Laptop("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
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

                        request["SNR_Category"] = "Computer & Laptops"
                        request["SNR_SubCategory"] = "Computer & Laptops"

                        # serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)

                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")
                            print serializer1.errors
                    elif product.model_number != None and laptops[product.model_number] != None:
                        if laptops[product.model_number].price > product.sale_price:
                            print("same model found with lower price")
                            laptops[product.model_number]=Laptop("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                            print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl
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

                            request["SNR_Category"] = "Computer & Laptops"
                            request["SNR_SubCategory"] = "Computer & Laptops"

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
        laptop_Walmart(request,categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()


import requests

class bestbuy:
    def getLaptops(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=laptop*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=computer*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            print(data)
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])


            for category in listCatagories:

                print category

                response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,customerReviewAverage,sku,modelNumber,upc,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
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

                    request["SNR_Category"] = "Computer & Laptops"
                    request["SNR_SubCategory"] = "Computer & Laptops"

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

                    response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100&page="+str(count))
                    data = response.json()
                    # print(data)
                    for item in data['products']:

                        # print (item["name"])
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

                        request["SNR_Category"] = "Computer & Laptops"
                        request["SNR_SubCategory"] = "Computer & Laptops"

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

from bs4 import BeautifulSoup
import json
class EbayAPI():


    def ebayLaptopsAll(self, request):
        listCatagories = ['179','31530','177','171485','176970','86722', '171485', '3676', '67870', '175698', '175673','58058', '111418', '179', '171957', '175672', '111422', '177', '158845', '25321', '162'
                          ]
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
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"

                try:
                    url =  item['viewItemURL']
                    source = requests.get(url)
                    plain_text = source.text
                    # print plain_text

                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('img', {'id': 'icImg'}):
                        request["SNR_ImageURL"]=link.get("src")
                        print link.get("src")
                except:
                    request["SNR_ImageURL"] = item['imageURL']

                request["SNR_Category"] = "Computer & Laptops"
                request["SNR_SubCategory"] = "Computer & Laptops"

                # serializer = Mobile_Serializer(data=request)
                serializer1 = AllProducts_Serializer(data=request)

                if serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")
                    print serializer1.errors
import unicodedata

class ATNT():

    def getLaptops(self,request):
        url='https://www.att.com/shop/wireless/devices/tablets.html'
        source=requests.get(url)
        plain_text=source.text
        soup= BeautifulSoup(plain_text,"lxml")
        titles=[]
        images=[]
        prooductlinks=[]
        prices=[]
        sku=[]
        descriptons=[]
        ratinglink=[]

        for link in soup.findAll('a',{'class':'titleURLchng'}):


            lin="https://www.att.com"+link.get('href')
            prooductlinks.append(lin)
            title= link.string
            SKU=link.get('data-cskuid')
            sku.append(SKU)

            titles.append(title)

        for link in soup.findAll('img',{'class':'inStockOpacity'}  ):

            img=link.get('src')

            images.append(img)

        for link in soup.findAll('div',{'class':'list-description'}  ):

            des=link.get_text()
            descriptons.append(des)

        for l in soup.findAll('div',{'class':'list-priceInfo'}):

            price=l.get_text()
            # print price
            prices.append(price)

        for link in soup.findAll('a',{'class':'clickStreamSingleItem rtngURLchng'}):


            lin="https://www.att.com"+link.get('href')
            ratinglink.append(lin)


        count=0;
        for var in titles:
        # print(titles[count]+"   "+str(sku[count]))
            print(sku[count])
            for ex in soup.findAll('img',{'id':'image-'+str(sku[count])}  ):

                img=ex.get('src')

                images.append(img)

                print(img)

        for var in descriptons:


            desc=unicodedata.normalize('NFKD', var).encode('ascii','ignore')
            desc=desc.strip()
            title=unicodedata.normalize('NFKD', titles[count]).encode('ascii','ignore')
          #  skuu=unicodedata.normalize('NFKD', sku[count]).encode('ascii','ignore')
            prc=unicodedata.normalize('NFKD', prices[count]).encode('ascii','ignore')

            #print(desc)

            title=title.strip()
            prc=prc.strip()

            #print(title)




            # print titles[count]
            #
            # print(titles[count]+"   "+str(sku[count]))
            # cell = unicode(descriptons[count]).replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
            #
            #
            # print(str(cell))
            prc=prc.strip()
            print(prc)
            # print(images[count])
            request["SNR_Price"]=prc[1:-4]

            request["SNR_Brand"]="00"
            request["SNR_Available"]="AT&T"
            request["SNR_Description"]=desc
            request["SNR_Title"]=title
            request["SNR_ImageURL"]=images[count]
            request["SNR_ProductURL"]=prooductlinks[count]
            request["SNR_ModelNo"]=title
            request["SNR_SKU"]="AT"+str(sku[count])
            request["SNR_UPC"]="00"
            # request["SNR_ReviewLink"]=requests[count]

            request["SNR_Category"] = "Computer & Laptops"
            request["SNR_SubCategory"] = "Computer & Laptops"

            # serializer = Mobile_Serializer(data=request)
            serializer1 = AllProducts_Serializer(data=request)

            if serializer1.is_valid():
                print("---")
                # serializer.save()
                serializer1.save()
            else:
                print("bad json")
                print serializer1.errors

            count=count+1




AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():
    def amazonLaptops(self,request):

        # get all books from result set and
        # print author and title
        listCatagories = ['3012292011','565098','1292108011','193870011','172504','541966', '541966', '565108' ]
        for category in listCatagories:
            try:




                for data in api.item_search('Electronics', BrowseNode=category, Sort='-price',ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
                    time.sleep(2)


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

                    request["SNR_Category"] = "Computer & Laptops"
                    request["SNR_SubCategory"] = "Computer & Laptops"

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
            except:


                print "Error"




class GroupOnAPI():
    def groupLaptop(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/computers-and-tablets?brand=109e8002-7631-45e8-a2cb-9b497d982571%2C14684a8d-4f36-4775-8d8d-fd04dbc952fc%2C1f27b9c3-dfb0-46c7-8c80-a6c38b8a4dfe%2C23d34b72-ea5b-464e-b1c9-092611f27b78%2C26acd6be-3782-439d-9ab5-0a1e770b4070%2C3d942c1c-a47b-412d-a46c-45c9f191e401%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C4af0d9e3-6b81-4467-847a-bc85eee9359e%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C7ac9c33c-07b3-475b-a36e-26097e70da9b%2C8528a092-0c2b-4f78-82e0-e9fa740885b7%2C890d12bc-9970-4023-b5cf-44568da216f5%2C8efa5611-0f81-4233-93f1-e922c8f6dc73%2C96280a34-9ba8-485a-bf0a-c6563199be44%2C97e52463-e2eb-4f60-9ab2-384e15051e5b%2C9bd95012-195d-4fa4-a37a-bb87a93c85c0%2Ca093638f-2739-42d2-a6d2-7f5777cda678%2Ca09a53e3-8818-4c8c-a862-04813f925f8a%2Ca4726dc4-c43c-4c4d-89cd-82321f943ff3%2Ca8f436ea-5888-4c80-9bd6-dd35dda4d48e%2Cc8da91a3-e3d6-4a45-ac3e-615d12921acb%2Ccffbd974-dd3d-45dc-ae3c-38effb51e828%2Cd2993075-4ae9-435b-bcc5-4fcd450254d4%2Ce5d7ebec-6220-45e4-b78d-97ead81cd6be%2Cf457b68e-928e-453e-8ced-641c244dbf6d&page='+str(page)
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
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] = price[1:]

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
                    request["SNR_Category"] = "Computer & Laptops"
                    request["SNR_SubCategory"] = "Computer & Laptops"

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
    def newEggLaptops(self,request):
        url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&IsNodeId=1&N=100006740%2050001146%2050001186%2050001315%2050001759%2050010418%2050010772'
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
            request["SNR_Category"] = "Computer & Laptops"
            request["SNR_SubCategory"] = "Computer & Laptops"

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
        while (count < 100):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006740%2050001146%2050001186%2050001315%2050001759%2050010418%2050010772&IsNodeId=1&bop=And&Page='+str(count)+'&PageSize=36&order=BESTMATCH'
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
                request["SNR_Category"] = "Computer & Laptops"
                request["SNR_SubCategory"] = "Computer & Laptops"

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



# listCatagories = []
listCatagories = [ '3944_3951_132960','3944_3951_132982', '3944_3951_1089430','3944_3951_1073804','3944_3951_1230331',  '3944_3951_7052607','3944_3951', '3944_3951_132960', '3944_3951_132959']
for category in listCatagories:
    time.sleep(30)

    laptop_Walmart({}, category)

AmazonAPI().amazonLaptops({})
bestbuy().getLaptops({});

EbayAPI().ebayLaptopsAll({})
GroupOnAPI().groupLaptop({})


newEggAPI().newEggLaptops({})

ATNT().getLaptops({})





from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'laptop.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        EbayAPI().ebayLaptopsAll({})
        bestbuy().getLaptops({});

        AmazonAPI().amazonLaptops({})
        ATNT().getLaptops({})

        newEggAPI().newEggLaptops({})

        GroupOnAPI().groupLaptop({})

        listCatagories = ['3944_3951_132960']
        # listCatagories = [ '3944_3951_132982', '3944_3951_1089430','3944_3951_1073804','3944_3951_1230331',  '3944_3951_7052607','3944_3951', '3944_3951_132960', '3944_3951_132959']
        for category in listCatagories:
            time.sleep(30)

            laptop_Walmart({}, category)

        pass    # do your thing here
    do(0)