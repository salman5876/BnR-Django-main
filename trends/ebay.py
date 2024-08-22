__author__ = 'Amad'
import json
from . models import Trends
from . serializer import TrendsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status

from ebaysdk.merchandising import Connection as Merchandising
from ebaysdk import exception
import requests
import BeautifulSoup
class EbayAPI():

    def AddTrend(self,request):
        print("uddin")
        api = Merchandising(appid="huzaifaz-ERecomme-PRD-008fa563f-8f5d310e")
        try:

            api = Merchandising(appid="huzaifaz-ERecomme-PRD-008fa563f-8f5d310e")
            response = api.execute('getTopSellingProducts', {'maxResults': 10})
            # print(response.dict())
            #print(response.reply)
            dictstr=response.dict()

            for item in dictstr['productRecommendations']['product']:

                request["SNR_Title"]=item['title'];
                request["SNR_Price"]=item['priceRangeMax']['value'];
                request["SNR_ProductURL"]=( item['productURL']);
                request["SNR_Available"]="Ebay"

                request["SNR_CustomerReviews"]="0000";

                request["SNR_Available"]="Ebay"
                request["SNR_UPC"] = "00"
                request["SNR_SKU"] = "00"

                try:
                    url = item['productURL']
                    source = requests.get(url)
                    plain_text = source.text
                    # print plain_text

                    soup = BeautifulSoup(plain_text, "lxml")
                    for link in soup.findAll('img', {'id': 'icImg'}):
                        request["SNR_ImageURL"] = link.get("src")
                        print link.get("src")
                except:
                    # request["SNR_ImageURL"] = item['imageURL']


                    if 'imageURL' in item:

                        # print(item['imageURL'])
                        request["SNR_ImageURL"]=item['imageURL'];



                    else:
                        continue


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:

                 print "bad json"



        except exception as e:

            print("exception")
            print(e)
            print(e.response.dict())

