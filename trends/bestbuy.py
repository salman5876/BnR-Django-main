__author__ = 'Amad'
import requests
from . serializer import TrendsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status

class BestbuyAPI():

    def PopularMobiles(self,request):
        try:


            response = requests.get("https://api.bestbuy.com/beta/products/mostViewed(categoryId=pcmcat209400050001)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    print "-----"
                    serializer.save()
                else:
                    print "bad json"
                    # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        except StandardError as e:
            print(e.message)

    def Popularlaptops(self,request):
        try:


            response = requests.get("https://api.bestbuy.com/beta/products/mostViewed(categoryId=abcat0502000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"


                #print(item["sku"])
                # print(item["links"]["web"])
                # print(item["prices"]["current"])
                # print(item["descriptions"]["short"])
                # print(item["images"]["standard"])
                # print(item["names"]["title"])


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    print "-----"
                    serializer.save()
                else:
                    print "bad json"
                    # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        except StandardError as e:
            print(e.message)



    def AllCategoriesTrend(self,request):
        try:
            print "amad"


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat209400050001)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print serializer.error_messages

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0401000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.error_messages)
        except StandardError as e:
            print(e.message)
        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0501000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            print(data)
            for item in data['results']:
                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)


        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat209400050001)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)
        except StandardError as e:
            print(e.message)


        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat254000050002)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat209000050006)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0502000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat232900050000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat295700050012)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0502000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:
                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0904000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"
                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except:
            print(serializer.error_messages)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat242800050021)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0901000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:
                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0912000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:
                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"
                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0101000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=abcat0910000)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"

                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)



        try:


            response = requests.get("https://api.bestbuy.com/beta/products/trendingViewed(categoryId=pcmcat300300050002)?apiKey=KZf1Tiuxlc7AxMnSGbT11Xv3")
            data =response.json()
            # print(data)
            for item in data['results']:

                request["SNR_Title"]=item["names"]["title"];
                request["SNR_CustomerReviews"]=item["customerReviews"]["averageScore"];

                request["SNR_Price"]=item["prices"]["current"];
                request["SNR_ProductURL"]=item["links"]["web"];
                request["SNR_Available"]="Best Buy"
                request["SNR_ImageURL"]=item["images"]["standard"];
                request["SNR_Description"] = item["descriptions"]["short"];
                request["SNR_SKU"] = "BB" + str(item["sku"])
                request["SNR_UPC"] = "00"
                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print "bad json"

        except StandardError as e:
            print(e.message)


