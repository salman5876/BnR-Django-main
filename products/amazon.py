
from amazon import API
import lxml.etree
import unicodedata
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializers import Audio_Serializer, CarsElec_Serializer,Software_Serializer,TV_Serializer,Movies_Serializer,Toys_Serializer,Cams_Serializer,Office_Serializer,VideoGames_Serializer,Smarthomes_Serializer,Applinces_Serializer
from ebaysdk.finding import Connection as finding
from lxml import objectify
import time


AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():

    def amazonAppliances(self,request):
        listCatagories = ['3737671', '267554011', '2632820011', '2242350011', '2686378011', '2686328011', '495362',
                          '678542011', '3741261', '3741271', '3737601', '3741331', '680343011', '267555011',
                          '2399939011', '510240', '510240', '289935', '3741181', '3741441', '3741411', '3741361',
                          '289913', '510182', '3741451', '510106', '3741481', '2399955011', '2383576011', '3741521']
        for category in listCatagories:
            try:

                for data in api.item_search('Electronics', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

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

                    serializer = Applinces_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"




    def amazonAudio(self,request):

        listCatagories = ['172563','322215011','3236443011','172550','172552','667846011','13308581','3236449011']
        for category in listCatagories:
            try:

                for data in api.item_search('Electronics', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = Audio_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"



                # get all books from result set and
        # print author and title












    def amazonCarsElectronics(self,request):

        listCatagories = ['15710351','2204830011','15857501','15706941','15857511','15706571','2230642011','1077068','15684181','2204830011','15718271','2230642011','15857511','15857501','346333011','15718791','15709231','15710351','15719731','2258019011','15706941','15706571']
        for category in listCatagories:
            try:

                for data in api.item_search('Automotive', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = CarsElec_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"



    def amazonSoftware(self,request):


        # get all books from result set and
        # print author and title

        listCatagories = ['497022','497026','229534','229535','229677','229548','229563','1294826011','229637','229653','497024','229672','229545','229667','229614','229540','283891','229536','229537','15699371','229546','229636','229538','229541','229542','283013','229543','229544','229678','229547','229549','229556','229558','229559','229560','229552','229557','229592','2251985011','2251987011','2251986011','2251988011','2251989011','229565','229567','229566','229568','229569','229634','229570','497644','229571','229564','229572','229573','229574','229625','229628','229626','229627','229629','283896','108156011','16415711','491974','491972','289976','15699271','491968','491966','289979','491970','15699261','289977','289980','300249','229661','229655','281440','229657','277268011','2234513011','229662','283016','283015','229668','229669','229670','229671','229545','229638','229640','289972','229641','289974','289973','289975','283903','290542','567574','567576','567580','567566','229673','283898','229675','283904','283901','229674','600526','283900','229615','229617','15699351','229621','229623']
        for category in listCatagories:
            try:

                for data in api.item_search('Software', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = Software_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"



    def amazonTV(self,request):

        # get all books from result set and
        # print author and title
        listCatagories = ['1266092011','3213034011','172669','172659','578960','3230976011','400080','1288718011','1286610011','281056','352696011','3213035011','3213027011','3213025011','6459738011','3213034011','578960','3230976011','400080','3213028011','1065854','400082','3213025011','352697011','3213026011','979935011','3213027011','172514','886258','281056','3025451','3213035011','1286610011','1288718011','172669']
        for category in listCatagories:
            try:

                for data in api.item_search('Electronics', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = TV_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"




    def amazonToys(self,request):

        listCatagories = ['166508011','166118011','166316011','166309011','166164011','166220011','165993011','3226142011','276729011','165993011','166210011','166269011','166326011','166027011','1266203011','166333011','166359011','166092011','166461011','166420011','256994011','166310011','166224011','196601011','166057011','165993011','165793011']
        for category in listCatagories:
            try:

                for data in api.item_search('Toys', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = Toys_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"


        # get all books from result set and
        # print author and title








    def amazonMovies(self,request):

        listCatagories = ['2649512011','2649513011']

        for category in listCatagories:
            try:

                for data in api.item_search('DVD', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:



                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:

                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = Movies_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"







        for data in api.item_search('Electronics', BrowseNode='165793011', Sort='-price',ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
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

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Movies_Serializer(data=request)
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





    def amazonCams(self,request):

        listCatagories = ['2649512011','2649513011','14015121','698234','3109899011','3348501','172426','3346200','2686483011','505106','14015081','172840','3345831','3345801','13535371','502394','330405011','2476681011','3017941','2476680011','502394','14015021','754486','51547011','291226','499108','172441','3017961','3017971','172444','172427','562261011','3350181','3350211','3350171','3350301','3426471','14241441','14241151','14241331','525464','3348211','14015071','3349781','196569011','3443921','172450','3346261','3117830011','3347871','3349701','525898','699138011','172447','3346401','499262','4993282','281063','3168051','499170','297842','499158']
        for category in listCatagories:
            try:

                for data in api.item_search('Photo', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = Cams_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"



    def amazonOffice(self,request):

        # get all books from result set and
        # print author and title

        for data in api.item_search('OfficeProducts', BrowseNode='172574',ResponseGroup='ItemAttributes,Images,Large', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
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

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

            except:

                try:
                    request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                except:

                    try:
                        request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                    except:
                        request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"





            serializer = Office_Serializer(data=request)
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
        for data in api.item_search('OfficeProducts', BrowseNode='1069102', ResponseGroup='ItemAttributes,Images,Large',
                                    limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

            except:

                try:
                    request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                except:

                    try:
                        request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                    except:
                        request["SNR_Price"] = str(0)



            request["SNR_Available"] = "Amazon"

            serializer = Office_Serializer(data=request)
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

        for data in api.item_search('OfficeProducts', BrowseNode='1069242', ResponseGroup='ItemAttributes,Images,Large',
                                    limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

            except:

                try:
                    request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                except:

                    try:
                        request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                    except:
                        request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"

            serializer = Office_Serializer(data=request)
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

    def amazonVideoGames(self,request):

        listCatagories = ['229575','6427814011','14220161','6469269011','229647','294940','2622269011','14218901','229575','14210751','6427814011','11075221','3010556011','11075831','6469269011','14220161','265748','10987771','10987781','724106011','4924889011','2242427011','265754','265753','265752','10988221','6427871011','6427815011','14210861','14211021','14210671','14210761','724114011','14211101','360238011','14211281','14210961','6469295011','14220171','14220321','4924903011','14112941','14220361','14220431','360241011','14220371']
        for category in listCatagories:
            try:

                for data in api.item_search('VideoGames', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = VideoGames_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"




        listCatagories = ['1294478011','1294221011','14220161','6469269011']
        for category in listCatagories:
            try:

                for data in api.item_search('Software', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images,Large', limit=1000,
                                            AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        request["SNR_Price"] = str(data.OfferSummary.LowestNewPrice.Amount)

                    except:

                        try:
                            request["SNR_Price"] = data.ItemAttributes.ListPrice.Amount

                        except:

                            try:
                                request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount))
                            except:
                                request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = VideoGames_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"


