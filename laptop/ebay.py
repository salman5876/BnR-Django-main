__author__ = 'Amad'
import unicodedata


from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializers import Laptop_Serializer
from ebaysdk.finding import Connection as finding
import requests
import json

import requests
from bs4 import BeautifulSoup

class EbayAPI():


    def ebayLaptopsAll(self, request):
        listCatagories = ['58058', '111418', '179', '171957', '175672', '111422', '177', '158845', '25321', '162',
                          '86722', '171485', '3676', '67870', '175698', '175673']
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

                serializer = Laptop_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")


    def ebayLaptops(self,request):
        response = requests.get("https://djangoshopnroar.herokuapp.com/laptop/getModels")
        data =json.loads(response.text)
        for item in data:
            #print(item['SNR_ModelNo'])
            brand=unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii','ignore')
            description=item['SNR_Description']
            model=item['SNR_ModelNo']
            upc=item['SNR_UPC']
            img=item['SNR_ImageURL']




            response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+item['SNR_ModelNo']+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
            data =json.loads(response.text)
            #print(data)
            totalItems=data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
            if int(totalItems) > 0:
                # print("amad")
                # print(totalItems)
                # print(model)


                for itemm in data['findItemsAdvancedResponse'][0]['searchResult'][0]['item']:
                    request["SNR_Price"]=unicodedata.normalize('NFKD', itemm['sellingStatus'][0]['currentPrice'][0]['__value__']).encode('ascii','ignore')
                    request["SNR_Brand"]=brand
                    request["SNR_Available"]="Ebay"
                    request["SNR_Description"]=description
                    request["SNR_Title"]=unicodedata.normalize('NFKD', itemm['title'][0]).encode('ascii','ignore')

                    try:
                        url = item['viewItemURL']
                        source = requests.get(url)
                        plain_text = source.text
                        # print plain_text

                        soup = BeautifulSoup(plain_text, "lxml")
                        for link in soup.findAll('img', {'id': 'icImg'}):
                            request["SNR_ImageURL"] = link.get("src")
                            print link.get("src")
                    except:
                        request["SNR_ImageURL"] = img

                    request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                    request["SNR_ModelNo"]=model
                    request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                    request["SNR_UPC"]=upc
                    serializer = Laptop_Serializer(data=request)
                    # print("bestbuy calling")
                    # print(serializer)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print("bad json")
                    break
                else:
                    continue

                    # print(item['title'][0])
                    # print(item['itemId'][0])
                    # print(item['galleryURL'][0])
                    # print(item['viewItemURL'][0])
                    #
                    # print(item['sellingStatus'][0]['currentPrice'][0]['__value__'])
                    break


    def search(data):
        if data["company_SNR"].lower() == "lenovo" and data["series_SNR"].lower() == 'g':
            query = data["company_SNR"] + ' ' + data["series_SNR"]+data["model_SNR"]
        else:
            query = data["company_SNR"] + ' ' + data["series_SNR"] + ' ' + data["model_SNR"]

        api = finding(appid='huzaifaz-ERecomme-PRD-008fa563f-8f5d310e', debug=True)
        api.execute('findItemsAdvanced', {
                                            'keywords': query,
                                            'categoryId': ['175672','177', '111422'],
                                            'sortOrder': 'PricePlusShippingLowest',
                                            })


        #'itemFilter': [
                          #{'name': 'sortOrder', 'value': 'PricePlusShippingLowest'}
                      #],

        #'categoryId':[{'name': 'laptop & Netbooks', 'value': '175672'},
                      #{'name': 'Apple laptop', 'value': '111422'},
                      #{'name': 'PC laptop & Netbooks', 'value': '177'}],

        #CurrentPriceHighest

        dictstr = api.response.dict()
        #found = fortest.filterProducts(query,dictstr)

        if len(dictstr['searchResult']['item'])>0:

            for item in dictstr['searchResult']['item']:
                if item['condition']['conditionDisplayName'] != "For parts or not working" and query.lower() in item['title'].lower():
                    #myval=item['itemId']
                    #title=item['title']
                    #print title
                    data["price_SNR"]= item['sellingStatus']['convertedCurrentPrice']['value']
                    data["condition_SNR"]= item['condition']['conditionDisplayName']
                    data["link_SNR"]= item['viewItemURL']
                    data["CompleteName_SNR"]=item['title']
                    data["Available_SNR"]="EBAY"

                    serializer = Laptop_Serializer(data=data)

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                    break
        else:
            print "Ebay Product not found"