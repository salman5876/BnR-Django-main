__author__ = 'Amad'

from wapy.api import Wapy
from . serializer import TrendsSerializer
from rest_framework.response import Response    # to send specific response
from rest_framework import status

class WallmartAPI():
    def trending(slef,request):
        try:


            print "Walmant Api Called"
            # obj = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
            obj = Wapy('26zfbnn3h5wykxcyabj9f7uh')
            products = obj.trending_products()
            print (len(products))

            if len(products) > 0:

                for product in products:

                    if product.large_image != None:
                        image = product.large_image
                    elif product.medium_image != None:
                        image = product.medium_image
                    else:
                        image = product.thumbnail_image


                    request["SNR_ImageURL"]=image

                    request["SNR_Title"] = product.name;
                    request["SNR_Price"] =product.sale_price;
                    request["SNR_ProductURL"] = product.product_url;
                    request["SNR_Available"] = "Walmart"

                    print("before serilizer")
                    # print((image))
                    # print((product.product_url))
                    # print((product.name))




                    serializer = TrendsSerializer(data=request)
                    print serializer
                    if serializer.is_valid():

                        serializer.save()
                    else:

                        print "bad json"

                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




                    #print product.category_path
                    # print product.name
                    # print product.sale_price
                    # print product.product_url
                    # print product.thumbnail_image


            else:
                print "no products found"
        except StandardError as e:
            print(e.message);


