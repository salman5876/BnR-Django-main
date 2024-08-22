__author__ = 'Amad'

import json
from bestbuy import BestBuyProductsAPI
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializers import Laptop_Serializer

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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Laptop_Serializer(data=request)
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


                        serializer = Laptop_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)


def search(data):
    if data["company_SNR"].lower() == "lenovo" and data["series_SNR"].lower() == 'g':
        query = data["company_SNR"] + ' ' + data["series_SNR"]+data["model_SNR"]
    else:
        query = data["company_SNR"] + ' ' + data["series_SNR"] + ' ' + data["model_SNR"]

    searchquery=query.replace(" ","&search=")

    bb_prod = BestBuyProductsAPI("KZf1Tiuxlc7AxMnSGbT11Xv3")

    result=bb_prod.search(query="(search="+searchquery+")&(categoryPath.id=pcmcat138500050001)",sort="salePrice.asc", format="json", show="name,inStoreAvailability,salePrice,type,url")



    results = json.loads(result)
    #print results

    if len(results['products']) > 0:
        for item in results['products']:
            if item["inStoreAvailability"] == True:
                name = item["name"]
                name = name.replace(" - ", " ")
                if query.lower() in name.lower():
                    if "refurbished" in item["name"].lower():
                        data["condition_SNR"] = "Refurbished"
                    else:
                        data["condition_SNR"] = "New"

                    data["price_SNR"] = item["salePrice"]
                    data["link_SNR"] = item["url"]
                    data["CompleteName_SNR"]=(item["name"])
                    data["Available_SNR"]="BESTBUY"

                    serializer = Laptop_Serializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                    break

    else:
        print "BestBuy Product not found"








