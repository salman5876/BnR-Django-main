__author__ = 'Amad'


from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializer import Mobile_Serializer
from ebaysdk.finding import Connection as finding
import requests
import time
import json
class EbayAPI():
    def ebayMobilesAll(self, request):
        listCatagories = ['15032', '43304', '9355', '136699', '42428', '146492', '42428', '182073']
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
                serializer = Mobile_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
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
                    serializer = Mobile_Serializer(data=request)
                    #print("bestbuy calling")
                    print(serializer)
                    if serializer.is_valid():
                        serializer.save()
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


    def search(self,request):

        query=request["SNR_Name"]+' '+request["SNR_Model"]+' '+request["SNR_RAM"]

        api = finding(appid='huzaifaz-ERecomme-PRD-008fa563f-8f5d310e', debug=True)

        api.execute('findItemsByKeywords', {
            'keywords': query,
            'sortOrder':' PricePlusShippingLowest',
            'itemFilter': [
                {'name': 'Condition', 'value': 'New'},
                {'name':'sortOrder', 'value':'PricePlusShippingLowest'}
            ],
            'paginationInput': {
                'entriesPerPage': '25',
                'pageNumber': '1'
            },
            'sortOrder': 'CurrentPriceLowest'
            })


        dictstr = api.response.dict()

        price=""
        link=""
        completeName=""
        for item in dictstr['searchResult']['item']:
            myval=item['itemId']
            price=(item['sellingStatus']['convertedCurrentPrice']['value'])
            link=( item['viewItemURL'])
            completeName=item['title'];

        request["SNR_Price"]=price
        request["SNR_Link"]=link
        request["SNR_Available"]="EBAY"

        request["SNR_CompleteName"]=completeName

        serializer = Mobile_Serializer(data=request)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

