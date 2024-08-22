
from amazonproduct import API
import lxml.etree
import unicodedata
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializers import Wearable_Serializer
from ebaysdk.finding import Connection as finding
from lxml import objectify
import time


AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():
    def amazonWatches(self,request):
        listCatagories = ['378516011', '10103533031', '10103532031','10103534031','10103530031','10103539031','10103538031','10103540031','10103543031','10103542031','10103541031','10103529031','10103536031','10103535031','10103537031' ]
        for category in listCatagories:
            try:




                for data in api.item_search('Electronics', BrowseNode=category, Sort='-price',ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
                    time.sleep(2)


                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title).encode("utf-8")
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

                        request["SNR_Description"]  = str(data.ItemAttributes.Feature).encode("utf-8")

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





                    serializer = Wearable_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"


                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages

                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            except:


                print "Error"
