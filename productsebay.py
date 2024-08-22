
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import ElectronicsGadgets_Serializer, TV_Serializer,Cams_Serializer,CarsElec_Serializer,\
    Health_Serializer,VideoGames_Serializer,Toys_Serializer,Smarthomes_Serializer,Audio_Serializer,\
    Software_Serializer,Applinces_Serializer,Movies_Serializer,Office_Serializer,Books_Serializer,\
    Sports_Serializer,Furniture_Serializer,Arts_Serializer,HomeandGarden_Serializer,Jewelry_Serializer,Clothes_Serializer,Flowers_Serializer
import requests
import json
import time
import unicodedata
from rest_framework.response import Response    # to send specific response
from rest_framework import status


baseAddress = "http://localhost:8000/"

class EbayAPI():


    def ebayCarselecAll(self, request):

        listCatagories = ['3270','73335','48610','175716','32806','60207','48604','139836','156955','168105','1498','14935','168093','75390','94830','60203','75389','71530','18795','39754','39746','14936','18805','175717','79839','71527','75386','50549','85806','50550','50551','94844','50552','32810','50564','67773','64578','73348',
                          '168103','175726','73353','168104','139837','58049','73362','175712','48606','48605','149976','79834','79835']
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
                serializer = CarsElec_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    time.sleep(1)
                    serializer.save()
                else:
                    print("bad json")
                    print serializer.error_messages




    def ebaySportsAll(self, request):
        listCatagories = ['888','179767','7294','1492','15273','1513','7301','36274','310','159043','159049','159134','159136','40146','36259','73991'
            ,'97042','179792','179775','179784','177832','57262','177840','22679','177844','177831','62130','177849',
                          '158990','177862','74469','177864','2904','56185','158999','179961','62155','179978','29723','179985','159027','62143','384'
                          ,'179950','179953','159028','179973','180001','181128','181130','47323','181153','181129','630','83041','28059','158913','109130'
                          ,'28064','68816','44075','158927','28066','16059','159186','59892','23831','62214','58136','21225','36264','16059','16262','184381'
                          '106460','62229','159135','62166','13340','178886','31680','20835','79786','16034','30105','184355','159045','159048','11330','3153',
                          '36275','21567','165938','79777','97072','36276','36252','71110','73937','36271','177880','73943']
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                serializer = Sports_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages





    def ebayAudioAll(self, request):
        listCatagories = ['15052','112529','73839','3281','15053','15054','15056','96954','109256','48626','163769','73834','168093','111694','56172','56170','73835','124270','118261','73836','173632','122654','131093','48680','79877','168096']
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
                serializer = Audio_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages







    def ebaySmartHomeAll(self, request):
        listCatagories = ['50582','14948','50583','50584','94879','14953','175724','75395','48636','163825','88754','75397']
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
                serializer = Smarthomes_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    time.sleep(1)

                    serializer.save()
                else:
                    print("bad json")
                    print serializer.error_messages




    def ebaySoftwareAll(self, request):
        listCatagories = ['175689','158911','3783','80015','41859','3768','11226','182','158906','80356','185','18793','175689','158911','80015','3783','11226','185','80356','158906','182']
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
                serializer = Software_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    time.sleep(1)

                    serializer.save()
                else:
                    print("bad json")
                    print serializer.error_messages





    def ebayToysAll(self, request):
        listCatagories = ['175692','158666','158671','158672','175693','175694','158679','49018','175691','348','754','83732','75708','49019','18992','73248','21254','19013','180018','180019','28811','52338','19015','52339','180020','145844','19014','19018','152912','19026','2664','2536','222','145930','177915','11733','166796','11735','2518','123829','145935','19071','2550','180350','55415','234','2543','180250','19169','11743','1188','436','717','2631','436','19192','2562']
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
                serializer = Toys_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    time.sleep(1)

                    serializer.save()
                else:
                    print("bad json")
                    print serializer.error_messages






    def ebayTVAll(self, request):
        listCatagories = ['32852','39804','175711','11725','14990','22610','14981','72406','168058','163829','96969','11071']
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
                serializer = TV_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages





    def ebayGadgetsAll(self, request):
        listCatagories = ['14948','182099','11711','94861','50608','14954','73340','163824','14955','175745','3314','175744','38331','163827','178894','175743','163826','62041','48623']
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
                serializer = ElectronicsGadgets_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    time.sleep(1)

                    serializer.save()
                else:
                    print("bad json")
                    print serializer.error_messages



    def ebayBooksAll(self, request):
        listCatagories = ['267','2228','268','280','171228','11104','29792','29223','118255','118256','118257','118258','118259','162029','616','162031','162030','171210','171220','171276','279','171222']
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                serializer = Books_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages







    def ebayHomeGradenAll(self, request):
        listCatagories = ['11700','26677','20444','14308','178069','3197','16086','38227','10033','159907','299','176988','20625','20697'
                          ,'20710','181076','20571','631','11827','31605','63514','159912']
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                serializer = HomeandGarden_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages









    def ebayFlowersAll(self, request):
        listCatagories = ['160667','16491','16494','16493','160648','183166','160704','160734','160828','178069','177757','178070','178072','183349','183354','183353','20938','160895','34130','13','165720','117419','181003','19617','181019','119688','20520','40609','181052','66794','65203']
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                serializer = Flowers_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages

                def ebayHomeJewelryAll(self, request):
                    listCatagories = ['84605', '91427', '11312', '10968', '4196', '110633', '10321', '164352', '179264',
                                      '491', '10290', '98863', '48579', '14324', '40131']
                    for category in listCatagories:
                        response = requests.get(
                            "http://svcs.ebay.com/MerchandisingService?OPERATION-NAME=getRelatedCategoryItems&SERVICE-NAME=MerchandisingService&SERVICE-VERSION=1.1.0&CONSUMER-ID=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&maxResults=100000&categoryId=" + category)
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
                            request["SNR_SubCategory"] = item['primaryCategoryName']
                            request["SNR_ImageURL"] = item['imageURL']
                            request["SNR_ProductURL"] = item['viewItemURL']
                            request["SNR_ModelNo"] = "00"
                            request["SNR_SKU"] = "EB" + str(item['itemId'])
                            request["SNR_UPC"] = "00"
                            serializer = Flowers_Serializer(data=request)
                            # print("bestbuy calling")
                            print(serializer)
                            if serializer.is_valid():
                                serializer.save()
                                time.sleep(1)

                            else:
                                print("bad json")
                                print serializer.error_messages





                                #can add more categories
    def ebayHomeClothingAll(self, request):
        listCatagories = ['3082','163147','155240','112425','171146','137085','63862','63861','11524','11514','11554','3009','169001','172378','84275','15691','11507','15687','15690'
            ,'4250','1059','93427','28015','155184','175759','3259','41964','4251','15724','169291','3034','314','63863','11555','63864','63865','63866','63869','53159','15775',
                          '155183','11484','3001','11511','11510','15689','57989','11483','57991','57988','57990','3002']
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                serializer = Clothes_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages




    def ebayFurnitureAll(self, request):
        listCatagories = []
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                serializer = Furniture_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages





    def ebayArtsAll(self, request):
        listCatagories = ['550','552','2211','28009','360','553','357','554','20158','551','156196']
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
                request["SNR_SubCategory"] = item['primaryCategoryName']
                request["SNR_ImageURL"] = item['imageURL']
                request["SNR_ProductURL"] = item['viewItemURL']
                request["SNR_ModelNo"] = "00"
                request["SNR_SKU"] = "EB" + str(item['itemId'])
                request["SNR_UPC"] = "00"
                serializer = Arts_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages




    def ebayGamesAll(self, request):
        listCatagories = ['139973','38583','139971','54968','156597','182175','182174','1249','182174','182175','187','156597','171833','156595','139971','38583','139973','48749']
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
                serializer = VideoGames_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages



    def ebayMoviesAll(self, request):
        listCatagories = ['63821','11232','617','381','41676','132975','309','2362','2329','196']
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
                serializer = Movies_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages



    def ebayCamsAll(self, request):
        listCatagories = ['11724','31388','179697','625','28179','15200','182969','179697','4684','31388','150044','69323','78997','27432','182074','21162','30090','30078']
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
                serializer = Cams_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages





    def ebayHealthAll(self, request):
        listCatagories = ['11838','67588','36447','180959','11863','26395','1277','177731','31772','180959','11863','31762','177731','31769','67659','36447','31786','180345']
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
                serializer = Health_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages






    def ebayAppliancesAll(self, request):
        listCatagories = ['116026','116023','150138','159903','20715','43563','71258','42231']
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
                serializer = Applinces_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    time.sleep(1)

                else:
                    print("bad json")
                    print serializer.error_messages





    def ebayHealth(self,request):
        response = requests.get(baseAddress+"products/health/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems=data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems=0

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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Health_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
                            serializer.save()
                            time.sleep(1)

                        else:
                            print("bad json")
                            # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

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










    def ebayToys(self,request):
        response = requests.get(baseAddress+"products/toys/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems=data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems=0

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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Toys_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
                            serializer.save()
                            time.sleep(1)

                        else:
                            print("bad json")
                            # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

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




    def ebayAudio(self,request):
        response = requests.get(baseAddress+"products/audio/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"

            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Audio_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
                            time.sleep(1)

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




    def ebayApplinces(self,request):
        response = requests.get(baseAddress+"products/applinces/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"

            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Applinces_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
                            time.sleep(1)

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




    def ebayMovies(self,request):
        response = requests.get(baseAddress+"products/movies/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"


            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems=0

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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Movies_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebayOffice(self,request):
        response = requests.get(baseAddress+"products/office/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"




            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Office_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebaySoftware(self,request):
        response = requests.get(baseAddress+"products/software/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"




            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)

                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems = 0
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Software_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebayVideo(self,request):
        response = requests.get(baseAddress+"products/video/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand']!= None:
                brand=unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii','ignore')
            else:
                brand="Brand Not Available"
            if item['SNR_Description'] !=None:
                description=item['SNR_Description']
            else:
                description=" Not Available"

            if item['SNR_ModelNo']!=None:

                model=item['SNR_ModelNo']
            else:
                model=" "
            if item['SNR_UPC']!=None:
                upc=item['SNR_UPC']
            else:
                upc="Not Available"
            if item['SNR_ImageURL'] !=None:

                img=item['SNR_ImageURL']
            else:
                img="Not Available"


            try:




                if model !=None:
                    response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                    data =json.loads(response.text)
                    #print(data)

                    if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                        totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                    else:
                        totalItems = 0

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
                            if img !=None:
                                request["SNR_ImageURL"] = img
                            else:
                                request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                            request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                            request["SNR_ModelNo"]=model
                            if itemm['itemId'][0]!=None:
                                request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                            if upc !=None:
                                request["SNR_UPC"]=upc
                            else:
                                request["SNR_UPC"] = "0000"
                            serializer = VideoGames_Serializer(data=request)
                            # print("bestbuy calling")
                            print(serializer)
                            if serializer.is_valid():
                                print "------"
                                serializer.save()
                            else:
                                print("bad json")
                                #return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

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
            except:
                print "exception"




    def ebaySmarthome(self,request):
        response = requests.get(baseAddress+"products/smarthome/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"


            try:


                if model !=None:
                    response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                            if img !=None:
                                request["SNR_ImageURL"] = img
                            else:
                                request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                            request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                            request["SNR_ModelNo"]=model
                            if itemm['itemId'][0]!=None:
                                request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                            if upc !=None:
                                request["SNR_UPC"]=upc
                            else:
                                request["SNR_UPC"] = "0000"
                            serializer = Smarthomes_Serializer(data=request)
                            # print("bestbuy calling")
                            # print(serializer)
                            if serializer.is_valid():
                                print "------"
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
            except:
                print "Pagination Error"




    def ebayCars(self,request):
        response = requests.get(baseAddress+"products/cars/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"




            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                # print(data)
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = CarsElec_Serializer(data=request)

                        # print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print "------"
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






    def ebayCams(self,request):
        response = requests.get(baseAddress+"products/cams/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems = 0


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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Cams_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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






    def ebayTV(self,request):
        response = requests.get(baseAddress+"products/tv/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand']!= None:
                brand=unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii','ignore')
            else:
                brand="Brand Not Available"
            if item['SNR_Description'] !=None:
                description=item['SNR_Description']
            else:
                description=" Not Available"

            if item['SNR_ModelNo']!=None:

                model=item['SNR_ModelNo']
            else:
                model=" "
            if item['SNR_UPC']!=None:
                upc=item['SNR_UPC']
            else:
                upc="Not Available"
            if item['SNR_ImageURL'] !=None:

                img=item['SNR_ImageURL']
            else:
                img="Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = TV_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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





from products.serializers import ElectronicsGadgets_Serializer, TV_Serializer,Cams_Serializer,CarsElec_Serializer,\
    Health_Serializer,VideoGames_Serializer,Toys_Serializer,Smarthomes_Serializer,Audio_Serializer,\
    Software_Serializer,Applinces_Serializer,Movies_Serializer,Office_Serializer,Books_Serializer,\
    Sports_Serializer,Furniture_Serializer,Arts_Serializer,HomeandGarden_Serializer,Jewelry_Serializer,Clothes_Serializer,Flowers_Serializer


Ebay=EbayAPI()
Ebay.ebayGadgetsAll({})
Ebay.ebayFurnitureAll({})
Ebay.ebayGamesAll({})
Ebay.ebayHomeClothingAll({})
Ebay.ebaySmartHomeAll({})
Ebay.ebayFlowersAll({})
Ebay.ebayMoviesAll({})
Ebay.ebayOffice({})
Ebay.ebayToysAll({})
Ebay.ebayTVAll({})
Ebay.ebaySoftwareAll({})
Ebay.ebayAppliancesAll({})
Ebay.ebayAppliancesAll({})
Ebay.ebayHomeGradenAll({})
Ebay.ebayHomeClothingAll({})
Ebay.ebayAudioAll({})
Ebay.ebayArtsAll({})
Ebay.ebayFlowersAll({})
Ebay.ebaySportsAll({})
Ebay.ebayBooksAll({})
Ebay.ebayCamsAll({})
Ebay.ebayCarselecAll({})
