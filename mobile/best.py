__author__ = 'Amad'


import json
# from bestbuy import BestBuyProductsAPI
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializer import Mobile_Serializer
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
                    print (it['id'])
                    listCatagories.append(it['id'])

            response = requests.get(
                "https://api.bestbuy.com/v1/categories(name=Unlocked Cell Phones*)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3&pageSize=100&show=name,id,subCategories.name,subCategories.id&format=json")
            data = response.json()
            for item in data['categories']:
                listCatagories.append(item['id'])
                for it in item['subCategories']:
                    print (it['id'])
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


                    #print(item["sku"])
                    # print(item["links"]["web"])
                    # print(item["prices"]["current"])
                    # print(item["descriptions"]["short"])
                    # print(item["images"]["standard"])
                    # print(item["names"]["title"])



                    serializer = Mobile_Serializer(data=request)
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


                        serializer = Mobile_Serializer(data=request)
                        print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            print("bad json")





        except StandardError as e:
            print(e.message)



    def search(self,request):
        query=request["SNR_Name"]+' '+request["SNR_Model"]
        query=query.replace(" ","&search=")
        bb_prod = BestBuyProductsAPI("KZf1Tiuxlc7AxMnSGbT11Xv3")
        result=bb_prod.search(query="(search="+query+")&(categoryPath.id=pcmcat209400050001)",sort="salePrice.asc", format="json", show="name,inStoreAvailability,salePrice,type,url")
        name="";
        saleprice="";
        url="";


        results = json.loads(result)
        for item in results['products']:
            name=(item["name"])
            saleprice=(item["salePrice"])
            (item["inStoreAvailability"])
            url=(item["url"])
            break;
        request["SNR_Price"]=saleprice
        request["SNR_Link"]=url
        request["SNR_Available"]="BESTBUY"
        request["SNR_CompleteName"]=name

        serializer = Mobile_Serializer(data=request)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)







