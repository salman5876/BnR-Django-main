# __author__ = 'Amad'
# import requests
# from . serializers import Wearable_Serializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response    # to send specific response
# from rest_framework import status
# import exceptions
#
# class BestbuyAPI():
#
#     def Wearables(self,request):
#         try:
#             listCatagories = []
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=action*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=activity*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=watch*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=fitness*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=headphones*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=pet tracking*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=smart sports*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=smart tracker*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=smart watches*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             response = requests.get(
#                 "https://api.bestbuy.com/v1/categories(name=virtual*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
#             data = response.json()
#             # print(data)
#             for item in data['categories']:
#                 for it in item['subCategories']:
#                     # print it['id']
#                     listCatagories.append(it['id'])
#
#             for category in listCatagories:
#                 print category
#
#                 response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,name,customerReviewAverage,sku,modelNumber,upc,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100")
#                 data =response.json()
#                 print(data)
#                 for item in data['products']:
#
#                     # print item["name"]
#                     try:
#                         request["SNR_CustomerReviews"] = item["customerReviewAverage"]
#
#                         request["SNR_Title"] = item["name"].encode("utf-8")
#
#                         request["SNR_Price"] = item["salePrice"];
#                         request["SNR_ProductURL"] = item["url"];
#                         request["SNR_Available"] = "Best Buy"
#                         request["SNR_ImageURL"] = item["image"]
#                         request["SNR_Brand"] = item["manufacturer"]
#                         request["SNR_ModelNo"] = item["modelNumber"];
#                         request["SNR_UPC"] = item["upc"]
#                         request["SNR_SKU"] = "BB" + str(item["sku"])
#                         request["SNR_Description"] = item["longDescription"].encode("utf-8")
#
#                         # print(item["sku"])
#                         # print(item["links"]["web"])
#                         # print(item["prices"]["current"])
#                         # print(item["descriptions"]["short"])
#                         # print(item["images"]["standard"])
#                         # print(item["names"]["title"])
#
#
#                         serializer = Wearable_Serializer(data=request)
#                         if serializer.is_valid():
#
#                             serializer.save()
#                         else:
#
#                             print "bad json"
#                             print serializer.errors
#                             print serializer.error_messages
#                     except:
#                         print "error"
#
#
#                 totalPages = data["totalPages"]
#                 count=2
#                 print totalPages
#                 while(count<=int(totalPages)):
#                     print "amad"
#
#                     count+=1
#
#                     response = requests.get("https://api.bestbuy.com/v1/products((categoryPath.id="+category+"))?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&show=description,customerReviewAverage,name,sku,modelNumber,upc,image,url,manufacturer,salePrice,longDescription&format=json&pageSize=100&page="+str(count))
#                     data = response.json()
#                     # print(data)
#                     for item in data['products']:
#
#                         # print (item["name"])
#                         try:
#                             request["SNR_CustomerReviews"] = item["customerReviewAverage"]
#
#                             request["SNR_Title"] = item["name"].encode("utf-8")
#                             request["SNR_Price"] = item["salePrice"];
#                             request["SNR_ProductURL"] = item["url"];
#                             request["SNR_Available"] = "Best Buy"
#                             request["SNR_ImageURL"] = item["image"]
#                             request["SNR_Brand"] = item["manufacturer"]
#                             request["SNR_ModelNo"] = item["modelNumber"];
#                             request["SNR_UPC"] = "00"
#                             request["SNR_SKU"] = "BB" + str(item["sku"])
#                             request["SNR_Description"] = item["longDescription"].encode("utf-8")
#
#                             # print(item["sku"])
#                                 # print(item["links"]["web"])
#                                 # print(item["prices"]["current"])
#                                 # print(item["descriptions"]["short"])
#                                 # print(item["images"]["standard"])
#                                 # print(item["names"]["title"])
#
#
#                             serializer = Wearable_Serializer(data=request)
#                             if serializer.is_valid():
#
#                                 serializer.save()
#                             else:
#
#                                 print "bad json"
#                                 print serializer.errors
#                                 print serializer.error_messages
#                         except:
#                             print "error"
#
#
#
#
#
#
#         except StandardError as e:
#             print(e.message)
#
#
#
#         def MobileTrend(self,request):
#             try:
#
#
#                 response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat209400050001)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
#                 data =response.json()
#                 print(data)
#                 for item in data['results']:
#
#                     request["SNR_Title"]=item["names"]["title"];
#                     request["SNR_PriceMin"]="0";
#                     request["SNR_PriceMax"]=item["prices"]["current"];
#                     request["SNR_ProductURL"]=item["links"]["web"];
#                     request["SNR_AvailableAt"]="Best Buy"
#                     request["SNR_ImageURL"]=item["images"]["standard"];
#
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
#                     serializer = Wearable_Serializer(data=request)
#                     if serializer.is_valid():
#                         serializer.save()
#                     else:
#                         return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
#
#             except StandardError as e:
#                 print(e.message)
#                 print serializer.errors
#                 print serializer.error_messages
#
#     def LaptopTrend(self,request):
#         try:
#
#
#             response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0502000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
#             data =response.json()
#             print(data)
#             for item in data['results']:
#
#                 request["SNR_Title"]=item["names"]["title"];
#                 request["SNR_PriceMin"]="0";
#                 request["SNR_PriceMax"]=item["prices"]["current"];
#                 request["SNR_ProductURL"]=item["links"]["web"];
#                 request["SNR_AvailableAt"]="Best Buy"
#                 request["SNR_ImageURL"]=item["images"]["standard"];
#
#
#
#                 #print(item["sku"])
#                 # print(item["links"]["web"])
#                 # print(item["prices"]["current"])
#                 # print(item["descriptions"]["short"])
#                 # print(item["images"]["standard"])
#                 # print(item["names"]["title"])
#
#
#                 serializer = Wearable_Serializer(data=request)
#                 if serializer.is_valid():
#                     serializer.save()
#                 else:
#                     return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
#
#         except StandardError as e:
#             print(e.message)
#
