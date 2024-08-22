#
# import os, django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
# django.setup()
#
# from products.serializers import *
# import json
# from wapy.api import Wapy
# from collections import defaultdict
#
#
#
#
#
#
# obj1 = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
# obj = Wapy('m9esvpqxg8vc85g97726vdmn')
# key = Wapy('26zfbnn3h5wykxcyabj9f7uh')
#
#
# class Offce:
#
#     def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
#         self.sku = sku
#         self.title = title
#         self.model = model
#         self.brand = brand
#         self.upc = upc
#         self.price = price
#         self.available="Walmart"
#         self.productUrl = url
#         self.imageUrl = imgUrl
#         self.description = desc
#
#
#     class __metaclass__(type):
#         def __iter__(self):
#             for attr in dir(Offce):
#                 if not attr.startswith("__"):
#                     yield attr
#
#
#
#
#
#
# laptops=defaultdict(lambda: None,Offce)
#
#
#
# class Health:
#
#     def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
#         self.sku = sku
#         self.title = title
#         self.model = model
#         self.brand = brand
#         self.upc = upc
#         self.price = price
#         self.available="Walmart"
#         self.productUrl = url
#         self.imageUrl = imgUrl
#         self.description = desc
#
#
#     class __metaclass__(type):
#         def __iter__(self):
#             for attr in dir(Offce):
#                 if not attr.startswith("__"):
#                     yield attr
#
#
#
#
#
#
# laptops=defaultdict(lambda: None,Health)
#
# #or "Electronics/Computers/Laptop Computers" in product.category_path
# #
# #3944_1229875_4214212
# def Health_Walmart(request,categoryId,nextpage=0):
#     products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
#     print products
#     if len(products)>0:
#         for product in products:
#             if product.brand_name != None:
#                 brand=product.brand_name
#             if product.available_online == None:
#                 product.available_online=False
#
#             if product.large_image != None:
#                 image = product.large_image
#             elif product.medium_image != None:
#                 image = product.medium_image
#             else:
#                 image = product.thumbnail_image
#
#             try:
#
#
#                 if (product.available_online == True) and (product.sale_price != None):
#                     # print product.available_online
#                     if product.model_number != None and laptops[product.model_number] == None:
#
#                         request["SNR_ImageURL"] = image
#                         request["SNR_Brand"] = brand
#                         request["SNR_SKU"] = "WM"+str(product.item_id)
#                         request["SNR_Title"] = product.name
#                         request["SNR_UPC"] = product.upc
#                         request["SNR_ModelNo"] =product.model_number
#                         request["SNR_Price"] =product.sale_price
#                         request["SNR_ProductURL"] =product.product_url
#                         request["SNR_Description"]=product.long_description
#                         request["SNR_Available"] = "Walmart"
#
#                         request["SNR_Category"] = "Health & Fitness"
#                         request["SNR_SubCategory"] = "Health & Fitness"
#
#                         # serializer = Mobile_Serializer(data=request)
#                         serializer1 = AllProducts_Serializer(data=request)
#
#                         if serializer1.is_valid():
#                             print("---")
#                             # serializer.save()
#                             serializer1.save()
#                         else:
#                             print("bad json")
#                             print serializer1.errors
#
#                         laptops[product.model_number] = Offce("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
#                     elif product.model_number != None and laptops[product.model_number] != None:
#                         if laptops[product.model_number].price > product.sale_price:
#                             request["SNR_ImageURL"] = image
#                             request["SNR_Brand"] = brand
#                             request["SNR_SKU"] = "WM" + str(product.item_id)
#                             request["SNR_Title"] = product.name
#                             request["SNR_UPC"] = product.upc
#                             request["SNR_ModelNo"] = product.model_number
#                             request["SNR_Price"] = product.sale_price
#                             request["SNR_ProductURL"] = product.product_url
#                             request["SNR_Description"] = product.long_description
#                             request["SNR_Available"] = "Walmart"
#
#                             serializer = Health_Serializer(data=request)
#                             print("calling ")
#                             serializer1 = AllProducts_Serializer(data=request)
#                             print(serializer)
#                             if serializer.is_valid() & serializer1.is_valid():
#                                 print("---")
#                                 serializer.save()
#                                 serializer1.save()
#                             else:
#                                 # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
#
#                                 print("bad json")
#
#             except:
#                 print "exception"
#
#         #for laptop in laptops:
#             #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
#     else:
#         #print "end"
#         nextpage=None
#
#
#     print len(laptops)
#
#     if nextpage!=None:
#
#         time.sleep(0.15)
#         Health_Walmart(request,categoryId,nextpage)
#
#
#
#
#
# from amazonproduct import API
# from products.serializers import Audio_Serializer, CarsElec_Serializer,Software_Serializer,TV_Serializer,Movies_Serializer,Toys_Serializer,Cams_Serializer,Office_Serializer,VideoGames_Serializer,Smarthomes_Serializer,Applinces_Serializer
# import time
#
# AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
# SECRET_KEY = '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'
#
# api = API(AWS_KEY, SECRET_KEY, 'us')
#
# class AmazonAPI():
#
#
#     def amazonSoftware(self,request):
#
#
#         # get all books from result set and
#         # print author and title
#
#         listCatagories = ['497022','497026','229534','229535','229677','229548','229563','1294826011','229637','229653','497024','229672','229545','229667','229614','229540','283891','229536','229537','15699371','229546','229636','229538','229541','229542','283013','229543','229544','229678','229547','229549','229556','229558','229559','229560','229552','229557','229592','2251985011','2251987011','2251986011','2251988011','2251989011','229565','229567','229566','229568','229569','229634','229570','497644','229571','229564','229572','229573','229574','229625','229628','229626','229627','229629','283896','108156011','16415711','491974','491972','289976','15699271','491968','491966','289979','491970','15699261','289977','289980','300249','229661','229655','281440','229657','277268011','2234513011','229662','283016','283015','229668','229669','229670','229671','229545','229638','229640','289972','229641','289974','289973','289975','283903','290542','567574','567576','567580','567566','229673','283898','229675','283904','283901','229674','600526','283900','229615','229617','15699351','229621','229623']
#         for category in listCatagories:
#             try:
#
#                 for data in api.item_search('Software', BrowseNode=category, Sort='-price',
#                                             ResponseGroup='ItemAttributes,Images,Large', limit=1000,
#                                             AssociateTag='bpl001-20'):
#                     time.sleep(3)
#
#                     # print(objectify.dump(data))
#                     request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
#                     try:
#                         request["SNR_Title"] = str(data.ItemAttributes.Title)
#                     except:
#                         request["SNR_Title"] = "No Title"
#
#                     try:
#
#                         request["SNR_ModelNo"] = str(data.ItemAttributes.Model)
#
#                     except:
#                         request["SNR_ModelNo"] = "00"
#
#                     try:
#
#                         request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)
#
#                     except:
#                         request["SNR_SKU"] = "00"
#
#                     try:
#
#                         request["SNR_Description"] = str(data.ItemAttributes.Feature)
#
#                     except:
#                         request["SNR_Description"] = "Please visit site to see description"
#
#                     try:
#                         request["SNR_Brand"] = str(data.ItemAttributes.Brand)
#
#                     except:
#                         request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
#
#                     try:
#
#                         request["SNR_ImageURL"] = str(data.LargeImage.URL)
#
#                     except:
#
#                         try:
#                             request["SNR_ImageURL"] = str(data.MediumImage.URL)
#                         except:
#                             try:
#                                 request["SNR_ImageURL"] = str(data.SmallImage.URL)
#                             except:
#                                 request["SNR_ImageURL"] = None
#
#                     try:
#
#                         request["SNR_UPC"] = str(data.ItemAttributes.UPC)
#
#                     except:
#                         request["SNR_UPC"] = "000"
#
#                     try:
#
#                         request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)
#
#                     except:
#
#                         try:
#                             request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount
#
#                         except:
#
#                             try:
#                                 request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
#                             except:
#                                 request["SNR_Price"] = str(0)
#
#                     request["SNR_Available"] = "Amazon"
#                     request["SNR_Category"] = "Health & Fitness"
#                     request["SNR_SubCategory"] = "Health & Fitness"
#
#                     # serializer = Mobile_Serializer(data=request)
#                     serializer1 = AllProducts_Serializer(data=request)
#
#                     if serializer1.is_valid():
#                         print("---")
#                         # serializer.save()
#                         serializer1.save()
#                     else:
#                         print("bad json")
#                         print serializer1.errors
#             except:
#                 print "Error"
#
#
#
#
# from bestbuy import BestBuyProductsAPI
#
# import requests
# class bestbuy:
#
#
#
#     def getHealth(self,request):
#         try:
#
#             listCatagories = []
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=beauty*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 listCatagories.append(item['id'])
#                 for it in item['subCategories']:
#                     print it['id']
#                     listCatagories.append(it['id'])
#
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=health*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 listCatagories.append(item['id'])
#                 for it in item['subCategories']:
#                     print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=fitness*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 listCatagories.append(item['id'])
#                 for it in item['subCategories']:
#                     print it['id']
#                     listCatagories.append(it['id'])
#
#
#             for category in listCatagories:
#                 print category
#
#                 response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,customerReviewAverage,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
#                 data =response.json()
#                 # print(data)
#                 for item in data['products']:
#
#
#                     # print item["name"]
#                     request["SNR_Price"] = item["salePrice"]
#                     request["SNR_CustomerReviews"] = item["customerReviewAverage"]
#
#                     request["SNR_Brand"] = item["manufacturer"]
#                     request["SNR_Available"] = "Best Buy"
#                     if item["longDescription"]==None:
#
#                         request["SNR_Description"] = "No Description"
#                     else:
#                         request["SNR_Description"] = item["longDescription"]
#
#                     request["SNR_Title"] = (item["name"])
#                     if item["image"] ==None:
#                         request["SNR_ImageURL"] ="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
#                     else:
#                         request["SNR_ImageURL"] = (item["image"])
#                     request["SNR_ProductURL"] = item["url"]
#                     request["SNR_ModelNo"] = item["modelNumber"]
#                     request["SNR_SKU"] = "BB" + str(item["sku"])
#                     request["SNR_UPC"] = item["upc"]
#
#
#                     #print(item["sku"])
#                     # print(item["links"]["web"])
#                     # print(item["prices"]["current"])
#                     # print(item["descriptions"]["short"])
#                     # print(item["images"]["standard"])
#                     # print(item["names"]["title"])
#
#
#
#                     request["SNR_Category"] = "Health & Fitness"
#                     request["SNR_SubCategory"] = "Health & Fitness"
#
#                     # serializer = Mobile_Serializer(data=request)
#                     serializer1 = AllProducts_Serializer(data=request)
#
#                     if serializer1.is_valid():
#                         print("---")
#                         # serializer.save()
#                         serializer1.save()
#                     else:
#                         print("bad json")
#                         print serializer1.errors
#
#                 totalPages = data["totalPages"]
#                 count=2
#                 # print totalPages
#                 while(count<=int(totalPages)):
#                     # print "amad"
#
#                     count+=1
#
#                     response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,sku,modelNumber,upc,customerReviewAverage,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100&page="+str(count))
#                     data = response.json()
#                     # print(data)
#                     for item in data['products']:
#
#                         # print (item["name"])
#                         request["SNR_CustomerReviews"] = item["customerReviewAverage"]
#
#                         request["SNR_Price"] = item["salePrice"]
#                         request["SNR_Brand"] = item["manufacturer"]
#                         request["SNR_Available"] = "Best Buy"
#                         request["SNR_Description"] = item["longDescription"]
#                         request["SNR_Title"] = (item["name"])
#                         request["SNR_ImageURL"] = (item["image"])
#                         request["SNR_ProductURL"] = item["url"]
#                         request["SNR_ModelNo"] = item["modelNumber"]
#                         request["SNR_SKU"] = "BB" + str(item["sku"])
#                         request["SNR_UPC"] = item["upc"]
#                             # print(item["sku"])
#                             # print(item["links"]["web"])
#                             # print(item["prices"]["current"])
#                             # print(item["descriptions"]["short"])
#                             # print(item["images"]["standard"])
#                             # print(item["names"]["title"])
#
#                         request["SNR_Category"] = "Health & Fitness"
#                         request["SNR_SubCategory"] = "Health & Fitness"
#
#                         # serializer = Mobile_Serializer(data=request)
#                         serializer1 = AllProducts_Serializer(data=request)
#
#                         if serializer1.is_valid():
#                             print("---")
#                             # serializer.save()
#                             serializer1.save()
#                         else:
#                             print("bad json")
#                             print serializer1.errors
#
#
#
#
#         except StandardError as e:
#             print(e.message)
#
#
#
# class EbayAPI():
#
#     def ebayHealthAll(self, request):
#         listCatagories = ['11838','67588','36447','180959','11863','26395','1277','177731','31772','180959','11863','31762','177731','31769','67659','36447','31786','180345']
#         for category in listCatagories:
#             response = requests.get(
#                 "http://svcs.ebay.com/MerchandisingService?OPERATION-NAME=getRelatedCategoryItems&SERVICE-NAME=MerchandisingService&SERVICE-VERSION=1.1.0&CONSUMER-ID=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&maxResults=100000&categoryId="+category)
#             data = json.loads(response.text)
#             print(data)
#             totalItems = data['getRelatedCategoryItemsResponse']['itemRecommendations']['item']
#             # print totalItems
#             for item in totalItems:
#                 # print item['itemId']
#                 # print item['title']
#                 # print item['viewItemURL']
#                 # print item['imageURL']
#                 # print item['buyItNowPrice']['__value__']
#
#                 request["SNR_Price"] = item['buyItNowPrice']['__value__']
#                 request["SNR_Brand"] = "No Brand"
#                 request["SNR_Available"] = "Ebay"
#                 request["SNR_Description"] = "Visit site to see description"
#                 request["SNR_Title"] = item['title']
#                 request["SNR_ImageURL"] = item['imageURL']
#                 request["SNR_ProductURL"] = item['viewItemURL']
#                 request["SNR_ModelNo"] = "00"
#                 request["SNR_SKU"] = "EB" + str(item['itemId'])
#                 request["SNR_UPC"] = "00"
#                 request["SNR_Category"] = "Health & Fitness"
#                 request["SNR_SubCategory"] = "Health & Fitness"
#
#                 # serializer = Mobile_Serializer(data=request)
#                 serializer1 = AllProducts_Serializer(data=request)
#
#                 if serializer1.is_valid():
#                     print("---")
#                     # serializer.save()
#                     serializer1.save()
#                 else:
#                     print("bad json")
#                     print serializer1.errors
#
#
#
#
# from bs4 import BeautifulSoup
#
# baseAddress = "http://localhost:8000/"
# img=""
#
# class GroupOnAPI():
#
#
#
#
#     def groupHome(self, request):
#
#         flag = True
#         page = 1
#         while flag == True:
#
#             url = 'https://www.groupon.com/goods?category=for-the-home&category2=art-and-home-decor&page='+str(page)
#             source = requests.get(url)
#             plain_text = source.text
#             if "Oops" in plain_text:
#                 print "OOPPPS"
#                 flag = False
#             else:
#                 page += 1
#
#                 soup = BeautifulSoup(plain_text, "lxml")
#
#
#                 images = []
#                 prices = []
#                 titles = []
#
#                 for link in soup.findAll('figure', {'class': 'card-ui'}):
#                     img=""
#                     for li in link.findAll('img', {'class': 'cui-image'}):
#                         # print li
#                         img = li.get('data-high-quality')
#                         # print img
#
#                     for li in link.findAll('span', {'class': 'cui-price-discount'}):
#                         price = li.text.strip()
#                         # prices.append(price)
#                         # print "price "+li.text.strip()
#
#                     for li in link.findAll('div', {'class': 'cui-udc-title'}):
#                         title = li.text.strip()
#                         # titles.append(title)
#                         # print "Title "+li.text.strip()
#
#                     for addr in link.findAll('a', {'ontouchstart': ""}):
#
#                         address = addr.get("href")
#
#                         # print address
#                         inside_url = address
#                         inside_source = requests.get(inside_url)
#                         inside_plain_text = inside_source.text
#                         inside_soup = BeautifulSoup(inside_plain_text, "lxml")
#                         for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
#                             description=lin.text.strip()
#
#                     count = 0
#
#                     request["SNR_Price"] =price[1:]
#
#                     request["SNR_Brand"] = "Visit site to see Brand"
#                     request["SNR_Available"] = "Groupon "
#
#                     request["SNR_Description"] = description
#
#                     request["SNR_Title"] = title
#
#                     if img !=None:
#
#                         request["SNR_ImageURL"] ="https:"+ img
#                     else:
#                         request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
#                     request["SNR_ProductURL"] = address
#                     request["SNR_ModelNo"] = "Visit site to see "
#                     request["SNR_SKU"] = "Visit site to see "
#                     request["SNR_UPC"] = "Visit site to see "
#                     request["SNR_Category"] = "Health & Fitness"
#                     request["SNR_SubCategory"] = "Health & Fitness"
#
#                     # serializer = Mobile_Serializer(data=request)
#                     serializer1 = AllProducts_Serializer(data=request)
#
#                     if serializer1.is_valid():
#                         print("---")
#                         # serializer.save()
#                         serializer1.save()
#                     else:
#                         print("bad json")
#                         print serializer1.errors
#
#                     count += 1
#
#
#
# class newEggAPI():
#
#
#     def newEggHealth(self, request):
#         url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&Category=665&N=100199234&IsNodeId=1'
#         source = requests.get(url)
#         plain_text = source.text
#         # print plain_text
#
#
#
#
#         soup = BeautifulSoup(plain_text, "lxml")
#         for link in soup.findAll('div', {'class': 'item-container'}):
#             request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
#             request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
#             # for li in link.findAll('img'):
#             #     print "https:"+li.get("src") #warranty and image
#
#             x = link.find('a', {'class': 'item-img'})  # product image
#             request["SNR_ImageURL"] = "https:" + x.find('img').get("src")
#             try:
#                 x = link.find('a', {'class': 'item-brand'})  # product url
#                 request["SNR_Brand"] = "https:" + x.find('img').get("src")
#             except:
#                 request["SNR_Brand"] = "No Brand"
#
#             try:
#                 x = link.find('li', {'class': 'price-current'})
#                 request["SNR_Price"] = x.find('strong').text
#             except:
#                 request["SNR_Price"] = "00"
#
#             try:
#                 x = link.find('ul', {'class': 'item-features'})
#                 for feature in x.findAll('li'):
#                     if ("Model #" in feature.text):
#                         request["SNR_ModelNo"] = feature.text
#                     if ("Item #" in feature.text):
#                         request["SNR_SKU"] = feature.text
#             except:
#                 request["SNR_SKU"] = "00"
#                 request["SNR_ModelNo"] = "00"
#
#             request["SNR_Available"] = "Newegg"
#             request["SNR_Description"] = "Visit site to see description"
#             request["SNR_UPC"] = "00"
#             request["SNR_Category"] = "Health & Fitness"
#             request["SNR_SubCategory"] = "Health & Fitness"
#
#             # serializer = Mobile_Serializer(data=request)
#             serializer1 = AllProducts_Serializer(data=request)
#
#             if serializer1.is_valid():
#                 print("---")
#                 # serializer.save()
#                 serializer1.save()
#             else:
#                 print("bad json")
#                 print serializer1.errors
#
#         count = 2
#         while (count < 60):
#             time.sleep(count + 4)
#             url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100199234&IsNodeId=1&bop=And&Page=' + str(
#                 count) + '&pagesize=36&order=bestmatch'
#             source = requests.get(url)
#             plain_text = source.text
#             # print plain_text
#             soup = BeautifulSoup(plain_text, "lxml")
#             for link in soup.findAll('div', {'class': 'item-container'}):
#                 request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
#                 request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
#                 # for li in link.findAll('img'):
#                 #     print "https:"+li.get("src") #warranty and image
#
#                 x = link.find('a', {'class': 'item-img'})  # product image
#                 request["SNR_ImageURL"] = "https:" + x.find('img').get("src")
#                 try:
#                     x = link.find('a', {'class': 'item-brand'})  # product url
#                     request["SNR_Brand"] = "https:" + x.find('img').get("src")
#                 except:
#                     request["SNR_Brand"] = "No Brand"
#
#                 try:
#                     x = link.find('li', {'class': 'price-current'})
#                     request["SNR_Price"] = x.find('strong').text
#                 except:
#                     request["SNR_Price"] = "00"
#
#                 try:
#                     x = link.find('ul', {'class': 'item-features'})
#                     for feature in x.findAll('li'):
#                         if ("Model #" in feature.text):
#                             request["SNR_ModelNo"] = feature.text
#                         if ("Item #" in feature.text):
#                             request["SNR_SKU"] = feature.text
#                 except:
#                     request["SNR_SKU"] = "00"
#                     request["SNR_ModelNo"] = "00"
#
#                 request["SNR_Available"] = "Newegg"
#                 request["SNR_Description"] = "Visit site to see description"
#                 request["SNR_UPC"] = "00"
#                 request["SNR_Category"] = "Health & Fitness"
#                 request["SNR_SubCategory"] = "Health & Fitness"
#
#                 # serializer = Mobile_Serializer(data=request)
#                 serializer1 = AllProducts_Serializer(data=request)
#
#                 if serializer1.is_valid():
#                     print("---")
#                     # serializer.save()
#                     serializer1.save()
#                 else:
#                     print("bad json")
#                     print serializer1.errors
#
#             count += 1
#
#
# # AmazonAPI().amazonSoftware({})
# # time.sleep(30)
#
# newEggAPI().newEggHealth({})
# EbayAPI().ebayHealthAll({})
# time.sleep(30)
#
# listCatagories = ['3944_1229875_4214212', '3920_7415838', '5427_1224874', '4125_4134', '976760_36290',
#                   '1094765_133224_3214799']
# for category in listCatagories:
#     time.sleep(30)
#
#     Health_Walmart({}, category)
#
# bestbuy().getHealth({})
# time.sleep(30)
#
# from django_cron import CronJobBase, Schedule
#
# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 10080 # every 7 days
#
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'healths.my_cron_job'    # a unique code
#
#     def do(self):
#         print "amad ud din"
#         newEggAPI().newEggHealth({})
#         EbayAPI().ebayHealthAll({})
#         time.sleep(30)
#
#         listCatagories = ['3944_1229875_4214212', '3920_7415838', '5427_1224874', '4125_4134', '976760_36290',
#                           '1094765_133224_3214799']
#         for category in listCatagories:
#             time.sleep(30)
#
#             Health_Walmart({}, category)
#
#         bestbuy().getHealth({})
#         time.sleep(30)
#         # 1094765_133224_3214799
#
#         pass    # do your thing here
#     do(0)
#
# print 'amad'
# from autocorrect import spell
# print 'amad'
# print spell('Dall latitude')
#

from yboss import YBoss
boss = YBoss(key='dj0yJmk9UEY5eGV2Z1BqWlBLJmQ9WVdrOVZUWldTRWhETXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hZQ--', secret='81d7500ed987f13f8f29716ed330992df01af319')
results = boss.search("Solar Filter")
print 'amm'
print results
for result in results:
    print result
