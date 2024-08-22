import json
from bestbuy import BestBuyProductsAPI
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializers import TV_Serializer,Cams_Serializer,CarsElec_Serializer,VideoGames_Serializer,Toys_Serializer,Smarthomes_Serializer,\
    Audio_Serializer,Software_Serializer,Applinces_Serializer,Movies_Serializer,Office_Serializer,Health_Serializer,Clothes_Serializer,Sports_Serializer,\
    Flowers_Serializer,Arts_Serializer,HomeandGarden_Serializer,Jewelry_Serializer,Furniture_Serializer,Books_Serializer



import requests
class bestbuy:



    def getHealth(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=beauty*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])


            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=health*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            # print(data)
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print it['id']
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=fitness*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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
                    request["SNR_SKU"] = "BB" + str(item["sku"])
                    request["SNR_UPC"] = item["upc"]


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Health_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                            # print(item["sku"])
                            # print(item["links"]["web"])
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Health_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)




    def getArts(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=arts*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Arts_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Arts_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)








    def getHomeandGarden(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=kitchen*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Arts_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Arts_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)




    def getflowers(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=flower*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Flowers_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Flowers_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)





    def getJewelry(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=jewelry*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Jewelry_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Jewelry_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)




    def getSports(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=sports*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Sports_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Sports_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)









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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Clothes_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Clothes_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)







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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Books_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Books_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)





    def getFurniture(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=furniture*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Furniture_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Furniture_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)





    def getOfficeSupply(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=office*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Office_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                            # print(item["sku"])
                            # print(item["links"]["web"])
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Office_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)






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



                    serializer = Movies_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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


                        serializer = Movies_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)






    def getApplinces(self,request):

        print "amad"
        try:

            listCatagories = ['abcat0912025','abcat0912024','pcmcat158500050031','pcmcat158500050033','pcmcat158500050046','pcmcat158500050035','pcmcat158500050036','pcmcat158500050034','pcmcat158500050037','pcmcat158500050032','abcat0912027','pcmcat194000050030','pcmcat194000050031','pcmcat309100050005','abcat0912015','pcmcat194000050034','pcmcat194000050039','pcmcat194000050035','abcat0912019','pcmcat194000050032','pcmcat194000050038','pcmcat262100050013','pcmcat244600050019','abcat0912017','pcmcat253000050002','pcmcat282400050017','pcmcat321600050000','pcmcat334100050003','pcmcat374900050006','pcmcat1485889868233','pcmcat242200050001','pcmcat242200050002','pcmcat242200050005','pcmcat242200050003','pcmcat242200050004','pcmcat242200050006','pcmcat242200050007','pcmcat143000050068','pcmcat143000050069','pcmcat748300604159','pcmcat748300604266','pcmcat748300604280','pcmcat748302046004','pcmcat748302046006','pcmcat748302046008','pcmcat748302031267','pcmcat748302046004','pcmcat748302047069','pcmcat77600050007','pcmcat1489177306197','pcmcat1496258950325','pcmcat1496259045057','pcmcat1496259212489','pcmcat1496259324873','pcmcat1496259425517','pcmcat1496259530557','pcmcat1496259631131','pcmcat242100050024','pcmcat134800050009','pcmcat1484172586229','pcmcat1485889868233','pcmcat1494947523982','pcmcat1494947903603','pcmcat1494948033899','pcmcat1490202108030','pcmcat161300050013','pcmcat261500050000','pcmcat1484596902850','pcmcat133000050035','pcmcat134800050005','pcmcat134800050006','pcmcat134800050007','pcmcat134800050008','abcat0901002','pcmcat194000050021','abcat0912018','abcat0912028','abcat0912020','abcat0912021','abcat0912012','pcmcat194000050022','abcat0912022','abcat0912023','pcmcat367400050002','pcmcat328000050021','abcat0912010','pcmcat748301695371','abcat0912013','abcat0912014','pcmcat169000050017','pcmcat748301695489','pcmcat159400050007','pcmcat180100050007','abcat0909000','pcmcat374900050006','pcmcat748302046387','pcmcat748301695363','abcat0912011','pcmcat194000050020','abcat0900000','abcat0905000','pcmcat249000050000','abcat0906000','pcmcat321600050000','abcat0912001','abcat0907000','abcat0908000','pcmcat177200050009','abcat0912000','abcat0910000','pcmcat303000050004','pcmcat305400050001','abcat0911000','pcmcat302300050021','pcmcat179100050006','abcat0916000','abcat0901000','abcat0904000','abcat0904002','abcat0903000','abcat0901007','abcat0902000','pcmcat302600050005'];
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
                    request["SNR_SKU"] = "BB" + str(item["sku"])
                    request["SNR_UPC"] = item["upc"]


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Applinces_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        print("bad json")
                        print serializer.errors
                        print serializer.error_messages

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
                        request["SNR_Brand"] = item["manufacturer"]
                        request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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


                        serializer = Applinces_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)







    def getsoftware(self,request):
        try:

            listCatagories = ['abcat0508000'];
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
                    request["SNR_SKU"] = "BB" + str(item["sku"])
                    request["SNR_UPC"] = item["upc"]


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Software_Serializer(data=request)
                    print("bestbuy calling software..")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                            # print(item["sku"])
                            # print(item["links"]["web"])
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Software_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)





    def getAudios(self,request):
        try:

            # listCatagories = ['abcat0201000','abcat0208007','pcmcat241600050001','abcat0202000','abcat0204000','abcat0302019','pcmcat156500050009','abcat0302000','abcat0302038','pcmcat156300050010','pcmcat152100050020','pcmcat138100050024','pcmcat253300050003','abcat0208000','pcmcat185200050009','pcmcat310200050004','pcmcat344200050005','abcat0208015','abcat0107045','pcmcat253300050003','abcat0107039','abcat0107035','abcat0107015','abcat0106008','pcmcat332100050015','abcat0515001','abcat0106010','abcat0302012','abcat0302005','abcat0302034','abcat0302001','abcat0302011','abcat0307011','abcat0302019','pcmcat1493671011172','pcmcat59600050005','pcmcat331600050007','pcmcat1479753593119','pcmcat1481836436024','pcmcat1491427134658','pcmcat1492540301090','pcmcat1494863753799','pcmcat1494863977108','pcmcat1496259728030','pcmcat1496259850379','pcmcat1496260004835','pcmcat1496260127778','pcmcat1496260216336','pcmcat1496260216336','pcmcat172100050000','pcmcat304800050036','pcmcat304800050037','pcmcat150300050005','pcmcat254100050011','pcmcat150300050006','pcmcat216400050015','pcmcat304800050038','pcmcat343700050004','pcmcat150300050002','pcmcat150300050003','pcmcat150300050004','pcmcat151900050009','pcmcat216400050014','pcmcat150300050001','pcmcat218300050014','pcmcat218300050016','pcmcat748302045995','pcmcat748302045996','pcmcat152100050022','pcmcat152100050023','pcmcat156300050010','pcmcat156300050013','pcmcat156300050014','pcmcat156500050035','pcmcat156300050012','pcmcat231000050008','pcmcat156300050009','pcmcat175600050012','abcat0201000','abcat0203000','pcmcat309300050002','abcat0208000','pcmcat748302046691','abcat0205007','pcmcat309300050003','pcmcat186600050004','abcat0207000','pcmcat156300050010','abcat0302000','pcmcat175600050013','pcmcat175600050014','pcmcat185200050009','pcmcat188000050000','pcmcat188000050002','pcmcat188000050003','pcmcat188000050004','pcmcat309300050004'];
            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=audio*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Audio_Serializer(data=request)
                    print("bestbuy calling")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                        request["SNR_Price"] = item["salePrice"]
                        request["SNR_Brand"] = item["manufacturer"]
                        request["SNR_Available"] = "Best Buy"
                        request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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


                        serializer = Audio_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)


    def getSmartHomes(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=smart home*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Smarthomes_Serializer(data=request)
                    print("bestbuy calling")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                        request["SNR_Price"] = item["salePrice"]
                        request["SNR_Brand"] = item["manufacturer"]
                        request["SNR_Available"] = "Best Buy"
                        request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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


                        serializer = Smarthomes_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)

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



                    serializer = Toys_Serializer(data=request)
                    print("bestbuy calling")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                        request["SNR_SKU"] = "BB" + str(item["sku"])
                        request["SNR_UPC"] = item["upc"]
                            # print(item["sku"])
                            # print(item["links"]["web"])
                            # print(item["prices"]["current"])
                            # print(item["descriptions"]["short"])
                            # print(item["images"]["standard"])
                            # print(item["names"]["title"])


                        serializer = Toys_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)



    def getVideoGames(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=game*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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



                    serializer = VideoGames_Serializer(data=request)
                    print("bestbuy calling")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
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
                        request["SNR_Price"] = item["salePrice"]
                        request["SNR_Brand"] = item["manufacturer"]
                        request["SNR_Available"] = "Best Buy"
                        request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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


                        serializer = VideoGames_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)


    def getTVS(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=tv*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                        #print(item["sku"])
                        # print(item["links"]["web"])
                        # print(item["prices"]["current"])
                        # print(item["descriptions"]["short"])
                        # print(item["images"]["standard"])
                        # print(item["names"]["title"])



                        serializer = TV_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
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
                            request["SNR_Price"] = item["salePrice"]
                            request["SNR_Brand"] = item["manufacturer"]
                            request["SNR_Available"] = "Best Buy"
                            request["SNR_Description"] = item["longDescription"]
                            request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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


                            serializer = TV_Serializer(data=request)
                            print("bestbuy calling")
                            print(serializer)
                            if serializer.is_valid():
                                print("---")
                                serializer.save()
                            else:
                                print("bad json")





        except StandardError as e:
            print(e.message)





    def getCams(self,request):
        try:

            listCatagories = []

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=camera*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
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


                        #print(item["sku"])
                        # print(item["links"]["web"])
                        # print(item["prices"]["current"])
                        # print(item["descriptions"]["short"])
                        # print(item["images"]["standard"])
                        # print(item["names"]["title"])



                        serializer = Cams_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
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
                            request["SNR_Price"] = item["salePrice"]
                            request["SNR_Brand"] = item["manufacturer"]
                            request["SNR_CustomerReviews"] = item["customerReviewAverage"]

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


                            serializer = Cams_Serializer(data=request)
                            print("bestbuy calling")
                            print(serializer)
                            if serializer.is_valid():
                                print("---")
                                serializer.save()
                            else:
                                print("bad json")





        except StandardError as e:
            print(e.message)







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

                        # print(item["sku"])
                        # print(item["links"]["web"])
                        # print(item["prices"]["current"])
                        # print(item["descriptions"]["short"])
                        # print(item["images"]["standard"])
                        # print(item["names"]["title"])



                        serializer = CarsElec_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")

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


                            serializer = CarsElec_Serializer(data=request)
                            print("bestbuy calling")
                            print(serializer)
                            if serializer.is_valid():
                                print("---")
                                serializer.save()
                            else:
                                print("bad json")





        except StandardError as e:
            print(e.message)
