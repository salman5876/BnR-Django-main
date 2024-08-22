import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from bs4 import BeautifulSoup


from collections import defaultdict
import time,threading
import json


from products.serializers import AllProducts_Serializer

from wapy.api import Wapy
from mobile.serializer import Mobile_Serializer

# obj = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
obj = Wapy('m9esvpqxg8vc85g97726vdmn')
key = Wapy('26zfbnn3h5wykxcyabj9f7uh')


class Mobile:

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
            for attr in dir(Mobile):
                if not attr.startswith("__"):
                    yield attr




mobiles=defaultdict(lambda: None,Mobile)
mobileBrands=["samsung","apple","microsoft","nokia","sony","htc","motorola","lg","huawei",
              "lenovo","xiaomi","google","acer","asus","oppo","oneplus","meizu",
              "blackberry","alcatel","zte","toshiba","vodafone","gigabyte","xolo",
              "lava","micromax","blu","gionee","vivo","leeco","panasonic","hp",
              "yu","verykool","maxwest","plum"]

#Cell Phones/Unlocked Phones
#3944_542371_1073085
def mobile_Walmart(request,categoryId,nextpage=0):

    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

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

                        serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)
                        
                        if serializer.is_valid() & serializer1.is_valid():
                            print("---")
                            serializer.save()
                            serializer1.save()
                        else:
                            # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                            print("bad json")


                        mobiles[product.model_number] = Mobile("WM" + str(product.item_id), product.name,
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

                        serializer = Mobile_Serializer(data=request)
                        serializer1 = AllProducts_Serializer(data=request)
                        
                        if serializer.is_valid() & serializer1.is_valid():
                            print("---")
                            serializer.save()
                            serializer1.save()
                        else:
                            # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                            print("bad json")

                        if mobiles[product.model_number].price > product.sale_price:
                            print("same model found with lower price")
                            mobiles[product.model_number] = Mobile("WM" + str(product.item_id), product.name,
                                                                   product.model_number, product.brand_name, product.upc,
                                                                   product.sale_price, product.product_url,
                                                                   image, product.long_description)
                            print mobiles[product.model_number], mobiles[product.model_number].title, mobiles[
                                product.model_number].price, mobiles[product.model_number].productUrl

                            # for laptop in laptops:
                            # print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
            except:
                print "exception"
    else:
        # print "end"
        nextpage = None


    print len(mobiles)

    if nextpage != None:
        #for model in mobiles:
            #print mobiles[model].model, mobiles[model].title, mobiles[model].price, mobiles[model].productUrl
        time.sleep(0.15)
        mobile_Walmart(request,categoryId, nextpage)



import requests




class bestAPI():
    def getMobile(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=cell phone*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=Unlocked Cell Phones*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])

            for category in listCatagories:
                response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,customerReviewAverage,upc,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
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
                    request["SNR_Category"] = "Cell Phones"
                    request["SNR_SubCategory"] = "Cell Phones"

                 


                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)
                    
                    if  serializer1.is_valid():
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
                        request["SNR_Category"] = "Cell Phones"
                        request["SNR_SubCategory"] = "Cell Phones"

                        serializer1 = AllProducts_Serializer(data=request)
                        
                        if serializer1.is_valid():
                            print("---")
                            # serializer.save()
                            serializer1.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)



from amazonproduct import API

AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():
    def amazonMobile(self,request):

        # get all books from result set and
        # print author and title
        listCatagories = ['2335752011','2407750011','2407748011','2407749011','2407747011', '2484512011', '2407749011','2407748011','2811119011' ]

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

                    request["SNR_Category"] = "Cell Phones"
                    request["SNR_SubCategory"] = "Cell Phones"

                    # serializer = Mobile_Serializer(data=request)
                    serializer1 = AllProducts_Serializer(data=request)
                    
                    if  serializer1.is_valid():
                        print("---")
                        # serializer.save()
                        serializer1.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages

                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            except:


                print "Error"





import unicodedata

from mobile.models import Mobile_DB
class ATNT():


    def getAllMobile(self,request):
        url='https://www.att.com/shop/wireless/devices/cellphones.html'
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

        count=0
        for l in soup.findAll('div',{'class':'list-price'}):

            price=l.get_text()
            prices.append(price)
        for link in soup.findAll('a',{'class':'clickStreamSingleItem rtngURLchng'}):


            lin="https://www.att.com"+link.get('href')
            ratinglink.append(lin)


        count=0;
        for var in descriptons:
            try:


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
                request["SNR_Category"] = "Cell Phones"
                request["SNR_SubCategory"] = "Cell Phones"

                serializer1 = AllProducts_Serializer(data=request)
                
                if  serializer1.is_valid():
                    print("---")
                    # serializer.save()
                    serializer1.save()
                else:
                    print("bad json")


                count=count+1
            except:
                print "exception"

class EbayAPI():
    def ebayMobilesAll(self, request):
        listCatagories = ['9355','80077', '42428', '146492', '42428', '182073','15032', '43304', '9355', '136699']
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
                request["SNR_Category"] = "Cell Phones"
                request["SNR_SubCategory"] = "Cell Phones"

                serializer1 = AllProducts_Serializer(data=request)
                
                if  serializer1.is_valid():
                    print("---")

                    serializer1.save()
                else:
                    print("bad json")

    def ebayMobiles(self,request):
        response = requests.get("http://localhost:8000/mobile/getModels")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""

        for item in data:
            #print(item['SNR_ModelNo'])
            brand=item['SNR_Brand']
            description=item['SNR_Description']
            model=item['SNR_ModelNo']
            upc=item['SNR_UPC']
            img=item['SNR_ImageURL']




            response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+item['SNR_ModelNo']+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
            data =json.loads(response.text)
            #print(data)
            totalItems=data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
            if int(totalItems) > 0:
                #print(totalItems)
                #print(model)
                #print(item['SNR_Title'])


                for itemm in data['findItemsAdvancedResponse'][0]['searchResult'][0]['item']:
                    request["SNR_Price"]=itemm['sellingStatus'][0]['currentPrice'][0]['__value__']
                    request["SNR_Brand"]=brand
                    request["SNR_Available"]="Ebay"
                    request["SNR_Description"]=description
                    request["SNR_Title"]=itemm['title'][0]
                    request["SNR_ImageURL"] = img
                    request["SNR_ProductURL"]=itemm['viewItemURL'][0]
                    request["SNR_ModelNo"]=model
                    request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                    request["SNR_UPC"]=upc
                    request["SNR_Category"] = "Cell Phones"
                    request["SNR_SubCategory"] = "Cell Phones"

                    serializer1 = AllProducts_Serializer(data=request)
                    
                    if serializer1.is_valid():
                        print("---")
                        serializer1.save()
                    else:
                        print("bad json")
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                    # print(item['title'][0])
                    # print(item['itemId'][0])
                    # print(item['galleryURL'][0])
                    # print(item['viewItemURL'][0])
                    #
                    # print(item['sellingStatus'][0]['currentPrice'][0]['__value__'])
                    break



class GroupOnAPI():
    def groupPhones(self, request):

        flag = True
        page = 1
        while flag == True:
            time.sleep(3)
            url = 'https://www.groupon.com/goods/cell-phones-and-accessories?brand=119d26b8-2afe-4494-bbd6-702f5c7fee6c%2C14684a8d-4f36-4775-8d8d-fd04dbc952fc%2C215b2a94-2af4-487a-bb8c-c3ac8c5c1daa%2C35d18f3a-8ac7-49c7-b555-5c13181343f3%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C43f785c7-da5f-4602-b89c-53793fa22251%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C51fb58f7-c33d-4d77-96c8-c4c0dac9e4f1%2C5f6e1462-a7df-4dd5-9a62-ee1077b7ffb8%2C6262bb0d-1697-4b5a-83a7-cc0f8655fd2f%2C965b4979-61eb-4150-a63e-6a55b150c70c%2C9bd95012-195d-4fa4-a37a-bb87a93c85c0%2Ca0e35859-9583-4086-9146-cd504aab2703%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Ca8f436ea-5888-4c80-9bd6-dd35dda4d48e%2Cc1a9bca5-c09e-4555-bba6-672a22046ac1%2Cc8da91a3-e3d6-4a45-ac3e-615d12921acb%2Cd0373173-ec82-450d-ae89-2dd7b7149c0f%2Cd19ef46c-4917-453b-9378-ad3494e56b69%2Cd785b3db-ea1a-4b74-8742-8e085589e527%2Cdb89a50c-3579-4a71-91a7-c2c4daa93ecb%2Ce73aec2d-a484-4d8d-bf1a-842b694e3feb%2Cecb805e3-1ff5-4196-87ca-d33e2001e2e7%2Cf4555cbf-e4f6-411c-8475-fd85b406b302%2Cf457b68e-928e-453e-8ced-641c244dbf6d%2Cf7ab9ef7-85a1-4e47-8532-eccc7b369918&page='+str(page)
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

                    request["SNR_Price"] = price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    request["SNR_ImageURL"] ="https:"+ str(img)
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "00"
                    request["SNR_SKU"] = "00"
                    request["SNR_UPC"] = "00"
                    request["SNR_Category"] = "Cell Phones"
                    request["SNR_SubCategory"] = "Cell Phones"

                    serializer1 = AllProducts_Serializer(data=request)
                    
                    if  serializer1.is_valid():
                        print("---")
                        serializer1.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
                        print serializer.error_messages

                        print("bad json")

                    count += 1



class newEggAPI():
    def newEggMobiles(self,request):
        url = 'https://www.newegg.com/product/productlist.aspx?submit=ene&n=100167543 600025861 600025862 600025874 600025878 600025881 600551125 600025860 600025864 600025866 600025876 600025877 600025880 600025883 600025889 600025890 600077252 600078906 600095334 600476000 600482513 600484844 600547686 600551649 600415427&isnodeid=1&bop=and&pagesize=36&order=bestmatch'
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
            request["SNR_Category"] = "Cell Phones"
            request["SNR_SubCategory"] = "Cell Phones"
            serializer1 = AllProducts_Serializer(data=request)
            
            if  serializer1.is_valid():
                print("---")
                serializer1.save()
            else:
                print("bad json")

        count = 2
        while (count < 60):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/product/productlist.aspx?submit=ene&n=100167543 600025861 600025862 600025874 600025878 600025881 600551125 600025860 600025864 600025866 600025876 600025877 600025880 600025883 600025889 600025890 600077252 600078906 600095334 600476000 600482513 600484844 600547686 600551649 600415427&isnodeid=1&bop=and&Page=' + str(
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
                request["SNR_Category"] = "Cell Phones"
                request["SNR_SubCategory"] = "Cell Phones"

                serializer1 = AllProducts_Serializer(data=request)
                
                if serializer1.is_valid():
                    print("---")
                    serializer1.save()
                else:
                    print("bad json")
            count += 1


bestAPI().getMobile({})
time.sleep(30)


AmazonAPI().amazonMobile({})
time.sleep(30)


listCatagories = ['3944_542371_1163447', '3944_542371_133161', '3944_542371_1127173', '3944_542371_133261',
                  '3944_542371_1072335', '3944_542371_1073085', '3944_542371_1045119', '3944_542371_1056206',
                  ]
for category in listCatagories:
    time.sleep(30)

    mobile_Walmart({}, category)



EbayAPI().ebayMobilesAll({})



ATNT().getAllMobile({})


time.sleep(30)


from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080 # every 7 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'mobile.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"
        EbayAPI().ebayMobilesAll({})

        ATNT().getAllMobile({})

        newEggAPI().newEggMobiles({})
        GroupOnAPI().groupPhones({})
        time.sleep(30)
        ATNT().getAllMobile({})
        time.sleep(30)

        AmazonAPI().amazonMobile({})
        time.sleep(30)

        listCatagories = ['3944_542371_1163447', '3944_542371_133161', '3944_542371_1127173', '3944_542371_133261',
                          '3944_542371_1072335', '3944_542371_1073085', '3944_542371_1045119', '3944_542371_1056206',
                          ]
        for category in listCatagories:
            time.sleep(30)

            mobile_Walmart({}, category)

        bestAPI().getMobile({})
        time.sleep(30)

        pass    # do your thing here
    do(0)