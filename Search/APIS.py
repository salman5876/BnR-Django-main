import random
import string
import time
from urllib.request import urlopen

from django.db.models.functions import Greatest
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
import random
from threading import Thread
import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from products.serializers import *


from laptop.models import Laptop_DB
from laptop.serializers import Laptop_Serializer,Laptop_SerializerTitle
from mobile.models import Mobile_DB
from mobile.serializer import Mobile_Serializer,Mobile_SerializerTitle
from wearables.models import Wearable_DB
from wearables.serializers import Wearable_Serializer,Wearable_SerializerTitle
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity
from itertools import chain

# Create your views here.
from django.db.models import Q, Max,Case, When, IntegerField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
import re

from django.core.cache import cache


def open_website(url):
    return urlopen(url)

def save_products(url,request):
    # # # printsaving"
    # # print(request)
    header = {'Content-Type': 'application/json'}
    return requests.put(url, headers=header, data=json.dumps(request))

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getAll_CatsQueries(request):
    try:

        data_all = AllProducts.objects.values('SNR_Category').distinct()
        # data_all = DailyDeals.objects.values('SNR_Category').annotate(the_count=Count('SNR_Category'))
        # # print data_all
        paginator = Paginator(data_all, 100)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = AllProducts_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator.count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except AllProducts.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def CountQueryAll(request,query):
    try:
        que = Q()
        for word in query.split():
           que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)

        LaptopCount = Laptop_DB.objects.filter(que).count()
        MobileCount = Mobile_DB.objects.filter(que).count()
        WearableCount = Wearable_DB.objects.filter(que).count()
        ApplincesCount = Applinces.objects.filter(que).count()
        softwareCount = ComputerSoftware.objects.filter(que).count()
        smarthomesCount = SmartHomes.objects.filter(que).count()
        videogamesCount = VideoGames.objects.filter(que).count()
        audioCount = Audio.objects.filter(que).count()
        moviesCount = Movies.objects.filter(que).count()
        CarsElecCount = CarsElectronics.objects.filter(que).count()
        OfficeCount = OfficeSupply.objects.filter(que).count()
        toysCount = Toys.objects.filter(que).count()
        TVCount = TV.objects.filter(que).count()
        CamsCount = Cams.objects.filter(que).count()
        healthCount=HealthandFitness.objects.filter(que).count()
        bookCount=Books.objects.filter(que).count()
        ArtsCount=Arts.objects.filter(que).count()
        furnitureCount=Furniture.objects.filter(que).count()
        sportsCount=SportingGoods.objects.filter(que).count()
        homeandgardenCount=HomeandGarden.objects.filter(que).count()
        jewelryCount=Jewelry.objects.filter(que).count()
        ClotheCount=Clothing.objects.filter(que).count()
        FlowerCount=FlowerandPlants.objects.filter(que).count()
        GadgetsCount=ElectronicGadgets.objects.filter(que).count()



    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method == 'GET':
        # serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response({'laptop':LaptopCount,
                         'mobile':MobileCount,'wearable':WearableCount,'software':softwareCount,'appliances':ApplincesCount,
                         'smarthome':smarthomesCount,'videogames':videogamesCount,'audio':audioCount,'movies':moviesCount,
                         'carselectronic':CarsElecCount, 'office':OfficeCount, 'toys':toysCount,'tv':TVCount,
                         'cams':CamsCount,
                         'arts':ArtsCount,
                         'books':bookCount,
                         'furniture':furnitureCount,
                         'sports':sportsCount,
                         'homegarden':homeandgardenCount,
                         'jewelry':jewelryCount,
                         'clothes':ClotheCount,
                         'gadgets':GadgetsCount,
                         'flowers':FlowerCount,
                         'Health':healthCount})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def CountAll(request):
    try:
        LaptopCount = Laptop_DB.objects.all().count()
        MobileCount = Mobile_DB.objects.all().count()
        WearableCount = Wearable_DB.objects.all().count()
        ApplincesCount = Applinces.objects.all().count()
        softwareCount = ComputerSoftware.objects.all().count()
        smarthomesCount = SmartHomes.objects.all().count()
        videogamesCount = VideoGames.objects.all().count()
        audioCount = Audio.objects.all().count()
        moviesCount = Movies.objects.all().count()
        CarsElecCount = CarsElectronics.objects.all().count()
        OfficeCount = OfficeSupply.objects.all().count()
        toysCount = Toys.objects.all().count()
        TVCount = TV.objects.all().count()
        CamsCount = Cams.objects.all().count()
        healthCount=HealthandFitness.objects.all().count()
        # bookCount=Books.objects.all().count()
        # ArtsCount=Arts.objects.all().count()
        # furnitureCount=Furniture.objects.all().count()
        # sportsCount=SportingGoods.objects.all().count()
        # homeandgardenCount=HomeandGarden.objects.all().count()
        # jewelryCount=Jewelry.objects.all().count()
        # ClotheCount=Clothing.objects.all().count()
        # FlowerCount=FlowerandPlants.objects.all().count()


    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method == 'GET':
        # serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response({'laptop':LaptopCount,
                         'mobile':MobileCount,'wearable':WearableCount,'software':softwareCount,'appliances':ApplincesCount,
                         'smarthome':smarthomesCount,'videogames':videogamesCount,'audio':audioCount,'movies':moviesCount,
                         'carselectronic':CarsElecCount, 'office':OfficeCount, 'toys':toysCount,'tv':TVCount,
                         'cams':CamsCount,
                         'Health':healthCount})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def FilterGroupon(request,query):

   ### print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_UPC__icontains=query)

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)



   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass

@api_view(['GET'])
def FilterGrouponASC(request,query):

   ### print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=   Q(SNR_UPC__icontains=query)

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)


   pass


@api_view(['GET'])
def FilterGrouponDESC(request,query):

   ### print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass

@api_view(['GET'])
def FilterProductsbyModelUPC(request,query):

   ### print(query)
   try:
       que =  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)
       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass


@api_view(['GET'])
def FilterProductsbyModelUPCDESC(request,query):

   try:
       que =  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)

       products = AllProducts.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass


@api_view(['GET'])
def FilterProductsbyModelUPCASC(request,query):

   ### print(query)
   try:
       que =  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)

       products = AllProducts.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)



   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:


       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass


from django.db import connection
from django.apps import apps

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterProductsbyCat(request):
    table_info = []
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)
    for model in apps.get_models():
        if model._meta.proxy:
            continue

        table = model._meta.db_table
        ### print table
        if table not in tables:
            continue

        columns = [field.column for field in model._meta.fields]
        table_info.append((table, columns))

    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def FilterProducts(request,query):


   ### print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)


       products = AllProducts.objects.filter(que)



       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except AllProducts.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)


   pass

empty_response = {"totalItems":0,"totalPages":0,"results":[]}
empty_brands = {"brands":[]}
from scrapetools import *


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_Ilike(request, query, price1, price2, brand, merchant, category):
    # # print query
    query = query.lower()
    query = query.replace('(', '\(')
    query = query.replace(')', '\)')

    query=query.replace('(','\(')
    query=query.replace("'","''")


    # # print query;
    query = query.encode('utf-8').strip()

    try:
        entry_per_page = int(request.GET.get('count'))
    except:
        entry_per_page = 18

    count_q = 'explain Select * from products_allproducts Where {0}'

    temp = []

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)


    # temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)

    is_c = False
    for i in re.split("\W+",query):
        if i:
            temp.append('"SNR_Title" ~* \'%s\'' % i)

    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)


    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory","SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = []
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select *{0} from products_allproducts Where {1}' % (",".join(
        out
    ))

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count = cursor.fetchone()[0]
            # print(query_count)
            ## print(query_cat)
            query_count=patSearch('rows=(\d+)',query_count).group(1)
            query_count=int(query_count)
            # print(query_count)


            # temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)
            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            q = q.format(""",similarity('%s',"SNR_Title") > 0""" % (query),temp) + offset+") AS rankTable"
            # # print q
            # # print q
            # # print query
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp


            return Response(res)

    except Exception as e:
        # # print e
        return Response(empty_response)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Count(request, query, price1, price2, brand, merchant, category):

    query = query.lower()
    query = query.replace("'", "''")
    query = query.replace("+", "\+")

    query = "".join(i for i in query if ord(i) < 128)

    query = re.sub('[^A-Za-z0-9]+', ' ', query)

    # # print query;

    query = query.encode('utf-8').strip()

    try:
        entry_per_page = int(request.GET.get('count'))
    except:
        entry_per_page = 36

    count_q = 'Select count(*) from products_allproducts Where {0}'

    temp = []

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    is_c = False
    Q_parts = query.split(" ");
    #
    # for part in Q_parts:
    #     part = ps.stem(part)
    #     # # print(part)
    #     temp.append('"SNR_Title" ~* \'%s\'' % part)

    temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)


    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)


    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select *{0} from products_allproducts Where {1} ORDER BY rank DESC' % (",".join(
        out
    ))

    f_count = len(fields)

    # # # printbefore try"
    try:
        with connection.cursor() as cursor:
            # # print count_q
            cursor.execute(count_q, [query])
            query_count = cursor.fetchone()[0]
            # print(query_count)
            ## print(query_cat)
            # print(query_count)

            # query_count=patSearch('rows=(\d+)',query_count).group(1)
            # query_count=int(query_count)


            # temp.append('"SNR_Category" = \'%s\'' % query_cat)
            # temp = " AND ".join(temp)
            # if query_count == 0:
            #     return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount
            return Response(res)


    except Exception as e:
        # # print e
        return Response(empty_response)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_tsv(request, query, price1, price2, brand, merchant, category):
    query_without_space = query.replace(" ", "")
    cache_key = '_search_exact__' + query_without_space + str(request.GET.get('page'))+str(price1)+str(price2)+str(category.replace(" ",""))+str(merchant.replace(" ",""))+str(brand.replace(" ",""))
    cache_time = 86200  # time to live in seconds
    result = cache.get(cache_key)

    if not result:

        brand = brand.replace("'", "''")
        merchant = merchant.replace("'", "''")


        query=query.replace("'","''")
        query=query.replace("(","\(")
        query=query.replace(")","\)")
        query=query.replace("+","\+")

        query = query.lower()

        query = "".join(i for i in query if ord(i) < 128)

        # query = re.sub('[^A-Za-z0-9]+', ' ', query)
        # # print query;

        query = query.encode('utf-8').strip()

        try:
            entry_per_page = int(request.GET.get('count'))
        except:
            entry_per_page = 36


        count_q = 'explain Select * from products_allproductspartition Where {0}'

        temp = []
        tsvquery='';

        if (query == '-1'):
            query = " "

        if (price1 != '-1' and price2 != '-1'):
            # # print 'added price'
            temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

        if (brand != '-1'):
            # # print 'added brand'
            brand = brand.lower()
            temp.append('"SNR_Brand" ~* \'%s\'' % brand)

        if (merchant != '-1'):
            merchant = merchant.lower()
            # # print 'added merchant'
            temp.append('"SNR_Available" ~* \'%s\'' % merchant)

        is_c = False
        # for i in re.split("\W+",query):
        #     if i:
        #
        #         temp.append('"SNR_Title" ~* \'%s\'' % i)
        #


        if (category != '-1'):
            # # # printcategory add"
            category = category.lower()
            is_c = True
            temp.append('"SNR_Category" ~* \'%s\'' % category)

        # tsvquery=query.replace(' ',' & ')
        # # print tsvquery

        # temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)

        temp.append('"SNR_Title" ~* \'%s\'' % query)


        temp2 = " AND ".join(temp)

        # if is_c:
        #     temp.pop()


        res = {}
        count_q = count_q.format(temp2)

        offset = ' LIMIT {0}'.format(entry_per_page)

        fields = ["id",
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition", "SNR_SubCategory","SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        q = 'Select %s  from products_allproductspartition Where {0} ' % (",".join(
            out
        ))

        # q='select %s from products_allproducts where "tsv_title" @@ to_tsquery(\'{0}\') Limit 50' % (",".join(out))

        # q=q.format(tsvquery)
        # # print q

        f_count = len(fields)

        try:
            with connection.cursor() as cursor:
                cursor.execute(count_q, [query])
                query_count = cursor.fetchone()[0]
                # print(query_count)
                ## print(query_cat)
                query_count=patSearch('rows=(\d+)',query_count).group(1)
                query_count=int(query_count)
                # print(query_count)


                # temp.append('"SNR_Category" = \'%s\'' % query_cat)
                temp = " AND ".join(temp)

                if query_count == 0:
                    return Response(empty_response)

                pageCount = int(math.ceil(query_count / float(entry_per_page)))
                res['totalItems'] = query_count
                res['totalPages'] = pageCount

                try:
                    page = int(request.GET.get('page'))
                except:
                    page = 1

                if page > pageCount:
                    page = pageCount
                # # print 'count...'

                if page > 0:
                    offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))
                # # print offset

                # # print temp
                # # # printamad"
                q = q.format(temp) + offset
                # # print q
                # # print q
                cursor.execute(q)
                temp = []
                for i in cursor.fetchall():
                    # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

                res["results"] = temp

                result = res;
                cache.set(cache_key, result, cache_time)
                # # # printsetting cache" + cache_key

                ##########
                return Response(res)

        except Exception as e:
            # # print e
            return Response(empty_response)

    else:
        # # # printreturning from cache"+cache_key
        return Response(result)




# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
# ps = PorterStemmer()
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_tsv_new(request, query, price1, price2, brand, merchant, category):
    # # print query

    query_without_space = query.replace(" ", "")
    cache_key = '_search__' + query_without_space + str(request.GET.get('page')) + str(price1) + str(price2) + str(category.replace(" ","")) + str(merchant.replace(" ","")) + str(brand.replace(" ",""))
    cache_time = 86200  # time to live in seconds
    result = cache.get(cache_key)

    if not result:

        brand=brand.replace("'","''")
        merchant=merchant.replace("'","''")

        query = query.lower()
        query=query.replace("'","''")
        query=query.replace("+","\+")


        query= "".join(i for i in query if ord(i) < 128)

        # query=re.sub('[^A-Za-z0-9]+', ' ', query)

        # # print query;

        query = query.strip()

        try:
            # entry_per_page = 3
            entry_per_page = int(request.GET.get('count'))
        except:
            entry_per_page = 36


        count_q = 'explain Select * from products_allproductspartition Where {0}'

        temp = []
        tsvquery='';

        if (query == '-1'):
            query = " "

        if (price1 != '-1' and price2 != '-1'):
            # # print 'added price'
            temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

        if (brand != '-1'):
            # # print 'added brand'
            brand = brand.lower()
            temp.append('"SNR_Brand" ~* \'%s\'' % brand)

        if (merchant != '-1'):
            merchant = merchant.lower()
            # # print 'added merchant'
            temp.append('"SNR_Available" ~* \'%s\'' % merchant)

        is_c = False
        # for i in re.split("\W+",query):
        #     if i:
        #
        #         temp.append('"SNR_Title" ~* \'%s\'' % i)
        #


        if (category != '-1'):
            # # # printcategory add"
            category = category.lower()
            is_c = True
            temp.append('"SNR_Category" ILIKE \'%s\'' % category)

        # tsvquery=query.replace(' ',' & ')
        # # print tsvquery

        # output = [w for w in query if not w in nltk_words]
        #
        # # print output
        Q_parts=query.split(" ")

        # for part in Q_parts:
        #     part=ps.stem(part)
        #     # # print(part)
        #     temp.append('"SNR_Title" ~* \'%s\'' % part)

            # temp.append('"SNR_Title" ~* \'%s\'' % query)

        temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)

        temp2 = " AND ".join(temp)


        res = {}
        count_q = count_q.format(temp2)

        offset = ' LIMIT {0}'.format(entry_per_page)

        fields = [
            "id",
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition", "SNR_SubCategory","SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        q = 'Select %s  from products_allproductspartition Where {0} ' % (",".join(
            out
        ))

        # q='select %s from products_allproducts where "tsv_title" @@ to_tsquery(\'{0}\') Limit 50' % (",".join(out))

        # q=q.format(tsvquery)
        # # print q

        f_count = len(fields)

        try:
            with connection.cursor() as cursor:
                query_count=1
                temp = " AND ".join(temp)

                if query_count == 0:
                    return Response(empty_response)

                pageCount = int(math.ceil(query_count / float(entry_per_page)))
                res['totalItems'] = query_count
                res['totalPages'] = pageCount

                try:
                    page = int(request.GET.get('page'))
                except:
                    page = 1

                if page > pageCount:
                    page = pageCount
                # # print 'count...'

                if page > 0:
                    offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))
                # # print offset

                # # print temp
                # # # printamad"
                q = q.format(temp) + offset
                # # print q
                # # print q
                cursor.execute(q)
                temp = []
                for i in cursor.fetchall():
                    # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

                res["results"] = temp
                result = res;
                cache.set(cache_key, result, cache_time)
                # # # printsetting cache" + cache_key

                ##########
                return Response(res)

        except Exception as e:
            # # print e
            return Response(empty_response)

    else:
        # # # printreturning from cache" + cache_key
        return Response(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_tsv_new_vector(request, query, price1, price2, brand, merchant, category):
    # # print query
    query = query.lower()
    query=query.replace('(','\(')
    query=query.replace(')','\)')
    query=query.replace("'","''")
    query=query.replace("$","\$")

    # # print query;

    query = query.encode('utf-8').strip()

    try:
        entry_per_page = int(request.GET.get('count'))
    except:
        entry_per_page = 36


    count_q = 'explain Select * from products_allproducts Where {0}'

    temp = []
    tsvquery='';

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    is_c = False
    # for i in re.split("\W+",query):
    #     if i:
    #
    #         temp.append('"SNR_Title" ~* \'%s\'' % i)
    #


    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)

    # tsvquery=query.replace(' ',' & ')
    # # print tsvquery

    temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)
    # Q_parts=query.split(" ");
    #
    # for part in Q_parts:
    #     temp.append('"SNR_Title" ~* \'%s\'' % part)
    #     # temp.append('"SNR_Title" ~* \'%s\'' % query)


    temp2 = " AND ".join(temp)

    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory","SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = []
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s  from products_allproducts Where {0} ' % (",".join(
        out
    ))

    # q='select %s from products_allproducts where "tsv_title" @@ to_tsquery(\'{0}\') Limit 50' % (",".join(out))

    # q=q.format(tsvquery)
    # # print q

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count = cursor.fetchone()[0]
            # print(query_count)
            ## print(query_cat)
            query_count=patSearch('rows=(\d+)',query_count).group(1)
            query_count=int(query_count)
            # print(query_count)


            # temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)

            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount
            # # print 'count...'

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))
            # # print offset

            # # print temp
            # # # printamad"
            q = q.format(temp) + offset
            # # print q
            # # print q
            cursor.execute(q)
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except Exception as e:
        # # print e
        return Response(empty_response)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_tsv_ASC(request, query, price1, price2, brand, merchant, category):


    query_without_space = query.replace(" ", "")
    cache_key = 'searchasc' + query_without_space + str(request.GET.get('page')) + str(price1) + str(price2) + str(
        category.replace(" ","")) + str(merchant.replace(" ","")) + str(brand.replace(" ",""))
    cache_time = 86200  # time to live in seconds
    result = cache.get(cache_key)

    if not result:



        # # print query
        query = query.lower()
        query=query.replace('(','\(')
        query=query.replace(')','\)')
        query=query.replace("'","''")

        # # print query;

        query = query.encode('utf-8').strip()

        try:
            entry_per_page = int(request.GET.get('count'))
        except:
            entry_per_page = 36

        count_q = 'explain Select * from products_allproducts Where {0}'

        temp = []
        tsvquery='';

        if (query == '-1'):
            query = " "

        if (price1 != '-1' and price2 != '-1'):
            # # print 'added price'
            temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

        if (brand != '-1'):
            # # print 'added brand'
            brand = brand.lower()
            temp.append('"SNR_Brand" ~* \'%s\'' % brand)

        if (merchant != '-1'):
            merchant = merchant.lower()
            # # print 'added merchant'
            temp.append('"SNR_Available" ~* \'%s\'' % merchant)

        is_c = False
        # for i in re.split("\W+",query):
        #     if i:
        #
        #         temp.append('"SNR_Title" ~* \'%s\'' % i)
        #


        if (category != '-1'):
            # # # printcategory add"
            category = category.lower()
            is_c = True
            temp.append('"SNR_Category" ILIKE \'%s\'' % category)

        # tsvquery=query.replace(' ',' & ')
        # # print tsvquery

        # temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)
        temp.append('"SNR_Title" ~* \'%s\'' % query)


        temp2 = " AND ".join(temp)

        if is_c:
            temp.pop()


        res = {}
        count_q = count_q.format(temp2)

        offset = ' LIMIT {0}'.format(entry_per_page)

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition", "SNR_SubCategory","SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        q = 'Select %s  from products_allproducts Where {0} order by "SNR_Price" ASC ' % (",".join(
            out
        ))

        # q='select %s from products_allproducts where "tsv_title" @@ to_tsquery(\'{0}\') Limit 50' % (",".join(out))

        # q=q.format(tsvquery)
        # # print q

        f_count = len(fields)

        try:
            with connection.cursor() as cursor:
                cursor.execute(count_q, [query])
                query_count = cursor.fetchone()[0]
                # print(query_count)
                ## print(query_cat)
                query_count=patSearch('rows=(\d+)',query_count).group(1)
                query_count=int(query_count)
                # print(query_count)


                # temp.append('"SNR_Category" = \'%s\'' % query_cat)
                temp = " AND ".join(temp)

                if query_count == 0:
                    return Response(empty_response)

                pageCount = int(math.ceil(query_count / float(entry_per_page)))
                res['totalItems'] = query_count
                res['totalPages'] = pageCount

                try:
                    page = int(request.GET.get('page'))
                except:
                    page = 1

                if page > pageCount:
                    page = pageCount
                # # print 'count...'

                if page > 0:
                    offset = '{0} OFFSET {1}'.format(offset, entry_per_page * (page - 1))
                # # print offset
                # 
                # # print temp
                # # # printamad"
                q = q.format(temp) + offset
                # # print q
                # # print q
                cursor.execute(q)
                temp = []
                for i in cursor.fetchall():
                    # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

                res["results"] = temp
                result = res;
                cache.set(cache_key, result, cache_time)
                # # # printsetting cache" + cache_key

                ##########
                return Response(res)

        except Exception as e:
            # # print e
            return Response(empty_response)

    else:
        # # # printreturning from cache" + cache_key
        return Response(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_tsv_DESC(request, query, price1, price2, brand, merchant, category):
    # # print query

    query_without_space = query.replace(" ", "")
    cache_key = 'searchdesc' + query_without_space + str(request.GET.get('page')) + str(price1) + str(price2) + str(
        category.replace(" ","")) + str(merchant.replace(" ","")) + str(brand.replace(" ",""))
    cache_time = 86200  # time to live in seconds
    result = cache.get(cache_key)

    if not result:


        query = query.lower()
        query=query.replace('(','\(')
        query=query.replace(')','\)')
        query=query.replace("'","''")

        # # print query;

        query = query.encode('utf-8').strip()

        try:
            entry_per_page = int(request.GET.get('count'))
        except:
            entry_per_page = 36

        count_q = 'explain Select * from products_allproducts Where {0}'

        temp = []
        tsvquery='';

        if (query == '-1'):
            query = " "

        if (price1 != '-1' and price2 != '-1'):
            # # print 'added price'
            temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

        if (brand != '-1'):
            # # print 'added brand'
            brand = brand.lower()
            temp.append('"SNR_Brand" ~* \'%s\'' % brand)

        if (merchant != '-1'):
            merchant = merchant.lower()
            # # print 'added merchant'
            temp.append('"SNR_Available" ~* \'%s\'' % merchant)

        is_c = False
        # for i in re.split("\W+",query):
        #     if i:
        #
        #         temp.append('"SNR_Title" ~* \'%s\'' % i)
        #


        if (category != '-1'):
            # # # printcategory add"
            category = category.lower()
            is_c = True
            temp.append('"SNR_Category" ILIKE \'%s\'' % category)

        # tsvquery=query.replace(' ',' & ')
        # # print tsvquery

        # temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)
        temp.append('"SNR_Title" ~* \'%s\'' % query)


        temp2 = " AND ".join(temp)

        if is_c:
            temp.pop()


        res = {}
        count_q = count_q.format(temp2)

        offset = ' LIMIT {0}'.format(entry_per_page)

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition", "SNR_SubCategory","SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        q = 'Select %s  from products_allproducts Where {0} order by "SNR_Price" DESC ' % (",".join(
            out
        ))

        # q='select %s from products_allproducts where "tsv_title" @@ to_tsquery(\'{0}\') Limit 50' % (",".join(out))

        # q=q.format(tsvquery)
        # # print q

        f_count = len(fields)

        try:
            with connection.cursor() as cursor:
                cursor.execute(count_q, [query])
                query_count = cursor.fetchone()[0]
                # print(query_count)
                ## print(query_cat)
                query_count=patSearch('rows=(\d+)',query_count).group(1)
                query_count=int(query_count)
                # print(query_count)


                # temp.append('"SNR_Category" = \'%s\'' % query_cat)
                temp = " AND ".join(temp)

                if query_count == 0:
                    return Response(empty_response)

                pageCount = int(math.ceil(query_count / float(entry_per_page)))
                res['totalItems'] = query_count
                res['totalPages'] = pageCount

                try:
                    page = int(request.GET.get('page'))
                except:
                    page = 1

                if page > pageCount:
                    page = pageCount
                # # print 'count...'

                if page > 0:
                    offset = '{0} OFFSET {1}'.format(offset, entry_per_page * (page - 1))
                # # print offset
                # 
                # # print temp
                # # # printamad"
                q = q.format(temp) + offset
                # # print q
                # # print q
                cursor.execute(q)
                temp = []
                for i in cursor.fetchall():
                    # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

                res["results"] = temp
                result = res;
                cache.set(cache_key, result, cache_time)
                # # # printsetting cache" + cache_key

                ##########
                return Response(res)

        except Exception as e:
            # # print e
            return Response(empty_response)

    else:
        # # # printreturning from cache" + cache_key
        return Response(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_tsvtri(request, query, price1, price2, brand, merchant, category):
    # # print query
    query = query.lower()
    query = query.encode('utf-8').strip()

    entry_per_page = 36

    count_q = 'explain Select * from products_allproducts Where {0}'

    temp = []
    tsvquery='';

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    is_c = False
    # for i in re.split("\W+",query):
    #     if i:
    #
    #         temp.append('"SNR_Title" ~* \'%s\'' % i)
    #


    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)

    tsvquery=query.replace(' ',' & ')
    # # print tsvquery

    temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % tsvquery)


    temp2 = " AND ".join(temp)

    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    # q = 'Select %s from (Select *{0} from products_allproducts Where {1} ORDER BY rank DESC' % (",".join(
    #     out
    # ))

    q='select %s , similarity("SNR_Title",\'{0}\') AS sml from products_allproducts where "tsv_title" @@ to_tsquery(\'{1}\') ORDER BY sml DESC Limit 50' % (",".join(out))

    q=q.format(query,tsvquery)
    # # print q

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count = cursor.fetchone()[0]
            # print(query_count)
            ## print(query_cat)
            query_count=patSearch('rows=(\d+)',query_count).group(1)
            query_count=int(query_count)
            # print(query_count)


            # temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)

            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount
            # # print 'count...'

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))
            # # print offset
            # 
            # # print temp
            # q = q.format(""",similarity('%s',"SNR_Title") as rank""" % (query), temp) + offset + ") AS rankTable"

            # # print q
            # # print q
            cursor.execute(q)
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except Exception as e:
        # # print e
        return Response(empty_response)


@api_view(['GET'])
def FilterAllProducts_Search_Similar_Ilike_without_count(request, query, price1, price2, brand, merchant, category):
    # # print query
    query = query.lower()
    query = query.encode('utf-8').strip()

    entry_per_page = 36

    count_q = 'explain Select * from products_allproducts Where {0}'

    temp = []

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    is_c = False
    for i in re.split("\W+",query):
        if i:
            temp.append('"SNR_Title" ~* \'%s\'' % i)

    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)


    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select *{0} from products_allproducts Where {1} ORDER BY rank DESC' % (",".join(
        out
    ))

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:
            # cursor.execute(count_q, [query])
            # query_count = cursor.fetchone()[0]
            query_count=100;

            # print(query_count)
            ## print(query_cat)
            # query_count=patSearch('rows=(\d+)',query_count).group(1)
            # query_count=int(query_count)
            # # print(query_count)


            # temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)
            if query_count == 0:
                return Response(empty_response)

            # pageCount = int(math.ceil(query_count / float(entry_per_page)))
            pageCount = 100
            res['totalItems'] = 100
            res['totalPages'] = 100

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            q = q.format(""",similarity('%s',"SNR_Title") as rank""" % (query),temp) + offset+") AS rankTable"
            # # print q
            # # print q
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                # # print i
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except Exception as e:
        # # print e
        return Response(empty_response)

@api_view(['GET'])
def Product_Detail_Similaritytemp(request, query):
    # # print query
    query = query.lower()
    query = query.encode('utf-8').strip()

    entry_per_page = 36

    count_q = 'explain Select * from products_allproducts Where {0}'

    temp = []

    if (query == '-1'):
        query = " "

    is_c = False
    length=len(query)
    count=0;
    for i in re.split("\W+",query):
        if count<4:
            if i:
                temp.append('"SNR_Title" ~* \'%s\'' % i)
                count=count+1;



    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT 100'

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory","SNR_Price"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as numeric)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select *{0} from products_allproducts Where {1} ORDER BY rank DESC' % (",".join(
        out
    ))

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:

            # temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)

            pageCount = 100;
            res['totalItems'] = 100
            res['totalPages'] = 100

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0}".format(offset, entry_per_page * (page - 1))

            q = q.format(""",similarity('%s',"SNR_Title") as rank""" % (query),temp) + offset+') AS rankTable order by "SNR_Price" ASC'
            # # print q
            # # print q
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except Exception as e:
        # # print e
        return Response(empty_response)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def mainsearchvector(request, query,totalResult):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    results = AllProducts.objects.annotate(search=SearchVector('SNR_Title')).filter(
        search=str(query)).values()[offset:limit]
    return Response({'results': results}, status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def mainsearch_slides(request,query):
    cats=[]
    query = "'" + query + "'"
    query_data1 = 'SELECT DISTINCT "SNR_Available" from public.products_allproducts  where  "tsv_title" @@ plainto_tsquery('+str(query)+') AND "SNR_Available" IS NOT NULL ORDER BY "SNR_Available" ASC'
    query_data = 'SELECT COUNT(*),MIN("SNR_Price"),MAX("SNR_Price") from public.products_allproducts  where  "tsv_title" @@ plainto_tsquery(' + str(
        query) + ')'

    with connection.cursor() as cursor:
        cursor.execute(query_data)
        dic={}
        for i in cursor.fetchall():
            dic={'count':i[0],'MinPrice':i[1],'Maxprice':i[2]}
            # dic+=dic
    with connection.cursor() as cursor:
        cursor.execute(query_data1)
        for i in cursor.fetchall():
            cats.append(i[0])
        print(cats)
    res = {
                "result":dic,
                "other":cats
            }
    return Response(res,status.HTTP_200_OK)
# res={
#             "result":dic
#         }

@api_view(['POST','GET'])
@permission_classes((permissions.AllowAny,))
def xxmainsearch(request,que,items):
    if request.method == 'GET':
        # try:
        #     query = "".join(i for i in que if ord(i) < 128)
        #     query = que.replace(" ", "+")
        #     try:
        #         if  int(request.GET.get('low'))!=-1 & int(request.GET.get('high'))!=-1 :
        #             minprice=int(request.GET.get('low'))
        #             maxprice=int(request.GET.get('high'))
        #             url = 'https://www.ebay.com/sch/i.html?_nkw=' + query +'&&_udlo='+str(minprice)+'&_udhi='+str(maxprice)
        #         else:
        #             url = 'https://www.ebay.com/sch/i.html?_nkw=' + query
        # 
        #     except:
        #         minprice=-1
        #         maxprice=-1
        #         url = 'https://www.ebay.com/sch/i.html?_nkw=' + query
        # 
        #     try:
        #         source = requests.get(url)
        #         plain_text = source.text
        #         soup = BeautifulSoup(plain_text, "html.parser")
        # 
        #         itemss = []
        # 
        #         cat = soup.find('ul', {'class': 'srp-refine__category__list'})
        #         for link in soup.findAll('li', {'class': 's-item'}):
        #             # # print link
        #             request = {}
        #             try:
        #                 request["SNR_ProductURL"] = link.find('a', {'class': 's-item__link'}).get('href')
        #                 request["SNR_Title"] = link.find('h3', {'class': 's-item__title'}).text
        #                 request["SNR_Description"] = "Visit site to see description"
        #                 request["SNR_Price"] = float(link.find('span', {'class': 's-item__price'}).text[1:])
        #                 request["SNR_CustomerReviews"] = 0.0
        #                 request["SNR_PriceBefore"] = -1
        # 
        #                 request["SNR_Category"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
        #                 request["SNR_Available"] = "Ebay"
        # 
        #                 request["SNR_ModelNo"] = "00"
        #                 request["SNR_UPC"] = "00"
        # 
        #                 request["SNR_SubCategory"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
        #                 request["SNR_Condition"] = "00"
        #                 img = link.find('img').get('src')
        #                 if 'gif' in img:
        #                     img = link.find('img').get('data-src')
        # 
        #                 request["SNR_ImageURL"] = img
        # 
        # 
        #                 itemss.append(request)
        # 
        #             except:
        #                 continue
        # 
        #         res = {"data": itemss, "status": True}
        # 
        # 
        #         # # printsetting cache for " + cache_key
        # 
        #         return Response(res)
        #     except:
        #         pass
        # except:
            try:
                page = int(request.GET.get('page'))
                if page < 1:
                    page = 1

            except:
                page = 1
            limit = page * int(items)
            offset = (page - 1) * int(items)
            query = str(que).replace("\'", "")
            query = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in query.split("\n")]
            print('>>>>>>>>>>>>>>>>>>>>>>>', query)
            temp=[]
            try:
                if  int(request.GET.get('low'))!=-1 & int(request.GET.get('high'))!=-1 :
                    minprice=int(request.GET.get('low'))
                    maxprice=int(request.GET.get('high'))
                    main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(\'' + str(
                        query[0]) + '\') AND "SNR_Price" BETWEEN '+str(minprice)+' AND '+str(maxprice)+' OFFSET ' + str(
                        offset) + ' LIMIT ' + str(limit)
                    print('in')
        #             url = 'https://www.ebay.com/sch/i.html?_nkw=' + query +'&&_udlo='+str(minprice)+'&_udhi='+str(maxprice)
                else:
                    main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(\'' + str(
                        query[0]) + '\') OFFSET ' + str(
                        offset) + ' LIMIT ' + str(limit)
        #
            except:
                minprice=-1
                maxprice=-1
                main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(\''+str(query[0])+'\') OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
            fields = ["id",
                      "SNR_Title", "SNR_Brand", "SNR_Available",
                      "SNR_ProductURL", "SNR_ImageURL",
                      "SNR_Description",
                      "SNR_Condition", "SNR_Price", "SNR_PriceBefore", "SNR_CustomerReviews"

                      ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out))
            f_count = len(fields)
            count=0
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]
                        current_item['index']=count
                    count=count+1
                    temp.append(current_item)
            connection.close()
            if len(temp) == 0:
                print(query)
                try:
                    if  int(request.GET.get('low'))!=-1 & int(request.GET.get('high'))!=-1 :
                        minprice=int(request.GET.get('low'))
                        maxprice=int(request.GET.get('high'))
                        url = 'https://www.ebay.com/sch/i.html?_nkw=' + query[0] +'&&_udlo='+str(minprice)+'&_udhi='+str(maxprice)
                    else:
                        url = 'https://www.ebay.com/sch/i.html?_nkw=' + query[0]

                except:
                    minprice=-1
                    maxprice=-1
                    url = 'https://www.ebay.com/sch/i.html?_nkw=' + query[0]

                try:
                    source = requests.get(url)
                    plain_text = source.text
                    soup = BeautifulSoup(plain_text, "html.parser")

                    itemss = []
                    count=0
                    cat = soup.find('ul', {'class': 'srp-refine__category__list'})
                    for link in soup.findAll('li', {'class': 's-item'}):
                        # # print link
                        request = {}
                        try:
                            request["SNR_ProductURL"] = link.find('a', {'class': 's-item__link'}).get('href')
                            request["SNR_Title"] = link.find('h3', {'class': 's-item__title'}).text
                            request["SNR_Description"] = "Visit site to see description"
                            request["SNR_Price"] = float(link.find('span', {'class': 's-item__price'}).text[1:])
                            request["SNR_CustomerReviews"] = 0.0
                            request["SNR_PriceBefore"] = -1

                            request["SNR_Category"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                            request["SNR_Available"] = "ebay"

                            request["SNR_ModelNo"] = "00"
                            request["SNR_UPC"] = "00"

                            request["SNR_SubCategory"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                            request["SNR_Condition"] = "00"
                            img = link.find('img').get('src')
                            if 'gif' in img:
                                img = link.find('img').get('data-src')

                            request["SNR_ImageURL"] = img
                            request["index"]=count

                            itemss.append(request)
                        except:
                            continue
                        count = count + 1

                    res = {"data": itemss, "status": True}
                    return Response(res, status.HTTP_200_OK)
                except:
                    pass
            res = {
                'data': temp,
            }

            return Response(res, status.HTTP_200_OK)
            # print('in')
            # return Response(status.HTTP_200_OK)

    if request.method == 'POST':
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        limit = page * int(items)
        offset = (page - 1) * int(items)
        query=str(que).replace("\'","")
        print('>>>>>>>>>>>>>>>>>>>>>>>',query)
        query="'"+query+"'"
        ls=''
        dic=request.data
        if dic['minprice'] != -1 and dic['maxprice'] != -1:
            ls = ls + ' AND "SNR_Price" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                request.data['maxprice'])
        if dic['merchant'] != 'undefine':
            ls =ls +' And "SNR_Available"=\'' +str(request.data['merchant'])+'\''
        if dic['sort'] !='undefine':
            if dic['sort'] =='ASC':
                ls = ls + ' ORDER by "SNR_Price" ASC'
            elif dic['sort'] =='DESC':
                ls = ls + ' ORDER by "SNR_Price" DESC'
        main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery({1}) {2} OFFSET '+str(offset)+' LIMIT '+str(limit)
        fields = ["id",
                  "SNR_Title","SNR_Brand","SNR_Available",
                  "SNR_ProductURL", "SNR_ImageURL",
                  "SNR_Description",
                  "SNR_Condition","SNR_Price", "SNR_PriceBefore", "SNR_CustomerReviews"

                  ]
        out = ['"{0}"'.format(i) for i in fields]
        print("out", out)
        temp = []
        extra_fields = []
        fields.extend(extra_fields)
        print("extra fields", extra_fields)
        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])
        # te=' AND "SNR_Price" BETWEEN 0 AND 100'
        data_query = main_data_query.format(",".join(out), query,ls)
        print(data_query)
        f_count = len(fields)
        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)
        connection.close()
        # cats = []
        # query_data1 = 'SELECT DISTINCT "SNR_Available" from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(' + str(
        #     query) + ') AND "SNR_Available" IS NOT NULL ORDER BY "SNR_Available" ASC'
        # query_data = 'SELECT COUNT(*),MIN("SNR_Price"),MAX("SNR_Price") from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(' + str(
        #     query) + ')'
        #
        # with connection.cursor() as cursor:
        #     cursor.execute(query_data)
        #     dic = {}
        #     for i in cursor.fetchall():
        #         dic = {'count': i[0], 'MinPrice': i[1], 'Maxprice': i[2]}
        #         # dic+=dic
        # with connection.cursor() as cursor:
        #     cursor.execute(query_data1)
        #     for i in cursor.fetchall():
        #         cats.append(i[0])
        #     print(cats)
        res = {
            # "result": dic,
            # "other": cats,
            'data':temp
        }

        return Response(res,status.HTTP_200_OK)


@api_view(['POST','GET'])
@permission_classes((permissions.AllowAny,))
def mainsearch1(request,que,items):
    if request.method =='GET':
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        limit = page * int(items)
        offset = (page - 1) * int(items)
        query = str(que).replace("\'", "")
        print('>>>>>>>>>>>>>>>>>>>>>>>', query)
        query = "'" + query + "'"
        results = AllProductsPartition.objects.annotate(search=SearchVector('SNR_Title')).filter(
                Q(search=query))[offset:limit]
        if len(results) == 0:
            print('sim')
            results = AllProductsPartition.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(Q(similarity__gte=0.2))[offset:limit]

        res = {
            "result": results.values(),
            # "other": cats,
            # 'data': temp
        }
        return Response(res, status.HTTP_200_OK)
    if request.method == 'POST':
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        limit = page * int(items)
        offset = (page - 1) * int(items)
        query=str(que).replace("\'","")
        print('>>>>>>>>>>>>>>>>>>>>>>>',query)
        query="'"+query+"'"
        que =Q()
        dic = request.data
        if dic['minprice'] != -1 and dic['maxprice'] != -1:
            que &=Q(SNR_Price__range=[str(request.data['minprice']),str(request.data['maxprice'])])
            # que &= Q(SNR_Price__range=[request.data['minprice'], datetime_object2.date()])
        if dic['merchant'] != 'undefine':
            que &=Q(SNR_Available=str(request.data['merchant']))
        if dic['sort'] != 'undefine':
            if dic['sort'] == 'ASC':
                results = AllProductsPartition.objects.annotate(search=SearchVector('SNR_Title')).filter(Q(search=query) & que).order_by('SNR_Price')[offset:limit]
            elif dic['sort'] == 'DESC':
                results = AllProductsPartition.objects.annotate(search=SearchVector('SNR_Title')).filter(Q(search=query) & que).order_by('-SNR_Price')[offset:limit]
        else:
            print('in')
            results = AllProductsPartition.objects.annotate(search=SearchVector('SNR_Title')).filter(
                Q(search=query) & que)[offset:limit]
        if len(results) == 0:
            print('sim')
            results = AllProductsPartition.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(
                Q(similarity__gte=0.2) & que)[offset:limit]

        res = {
                  "result": results.values(),
                  # "other": cats,
                  # 'data': temp
              }
        return Response(res, status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def mainsearchincat(request,cat,query):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    limit = page * int(10)
    offset = (page - 1) * int(10)
    query="'"+query+"'"
    main_data_query = 'Select {0} from public.products_allproducts  where "SNR_CatID" = '+str(cat)+' AND "tsv_title" @@ plainto_tsquery({1}) OFFSET '+str(offset)+' LIMIT '+str(limit)
    fields = ["id",
              "SNR_SKU", "SNR_Title",
              "SNR_ModelNo", "SNR_Brand",
              "SNR_UPC", "SNR_Available",
              "SNR_ProductURL", "SNR_ImageURL",
              "SNR_Description", "SNR_isShow",
              "SNR_Date", "SNR_Category",
              "SNR_Condition", "SNR_SubCategory", "SNR_Price", "SNR_PriceBefore", "SNR_CustomerReviews"

              ]
    out = ['"{0}"'.format(i) for i in fields]
    print("out", out)

    temp = []
    extra_fields = []
    fields.extend(extra_fields)
    print("extra fields", extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    data_query = main_data_query.format(",".join(out), query)
    print(data_query)
    f_count = len(fields)

    with connection.cursor() as cursor:
        cursor.execute(data_query)

        for i in cursor.fetchall():

            # if i[5] > 0:
            # print (i)
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = i[j]

            temp.append(current_item)
    # main_data_query ='Select COUNT(*) from public.products_allproducts  where  "tsv_title" @@ plainto_tsquery('+query+')'
    # print("with count", main_data_query)
    # re = connection.cursor()
    # re.execute(main_data_query)
    # row = re.fetchall()
    # row = [i[0] for i in row]
    # print("value", row[0])
    return Response(temp,status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Product_Detail_Similarity_test1(request, query):

    # # print query


    query_without_space = query.replace(" ", "")


    query=query.replace("'","''")
    query= "".join(i for i in query if ord(i) < 128)

    query = query.strip()

    entry_per_page = 50

    count_q = 'explain Select * from products_allproductspartition Where {0}'

    temp = []

    if (query == '-1'):
        query = " "

    is_c = False
    length=len(query)
    count=0;
    tempQ=""
    for i in re.split("\W+",query):
        if count<4:
            if i:
                # temp.append('"SNR_Title" ~* \'%s\'' % i)
                tempQ=tempQ+" "+i

                count=count+1;
    print(tempQ)
    temp.append("tsv_title @@ plainto_tsquery('%s')" % tempQ)
    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT 20'

    fields = ["id",
        "SNR_SKU", "SNR_Title",
        "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description",
        "SNR_Price","SNR_PriceBefore", "SNR_CustomerReviews"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = []
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as numeric)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select * from products_allproductspartition Where {0} ' % (",".join(
        out
    ))

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:

            # temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)

            pageCount = 100;
            res['totalItems'] = 100
            res['totalPages'] = 100

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0}".format(offset, 10 * (page - 1))

            q = q.format(temp) + offset+') AS rankTable order by "SNR_Price" ASC'
            # # print q
            print('qwfaf',q)

            # print(q.count())
            cursor.execute(q, [query])
            print('kjjfaklf',cursor.execute(q, [query]))
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            result = res;
            print(query)
            ##########
            return Response(res)

    except Exception as e:
        # # print e
        return Response(empty_response)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Product_Detail_Similarity_test(request, query):
    query = "".join(i for i in query if ord(i) < 128)
    query = query.strip()
    if (query == '-1'):
        query = " "

    is_c = False
    length = len(query)
    count = 0
    tempQ = ""
    query= query.replace("'","")
    query= query.replace('"',"")

    for i in re.split("\W+", query):
        if count < 4:
            if i:
                # temp.append('"SNR_Title" ~* \'%s\'' % i)
                tempQ = tempQ + " " + i
                count = count + 1

    print(tempQ)
    tempQ="'"+tempQ+"'"
    main_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(' + str(tempQ) + ') and "SNR_Title"!=\''+str(query)+'\' limit 20'
    print(main_query)
    fields = ["id",
              "SNR_Title",
              "SNR_Available",
              "SNR_ProductURL", "SNR_ImageURL",
              "SNR_Description",
              "SNR_Price", "SNR_PriceBefore", "SNR_CustomerReviews"

              ]
    temp=[]
    out = ['"{0}"'.format(i) for i in fields]
    data_query = main_query.format(",".join(out))
    f_count = len(fields)
    with connection.cursor() as cursor:
        cursor.execute(data_query)
        for i in cursor.fetchall():
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = i[j]
            temp.append(current_item)
    connection.close()
    res={
        # "items":totalitems[0],
        # "pages":totalpages,
        "results":temp
    }
    return Response(res,status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def filter_deal_comparison(request, query):
    # try:
    #     page = int(request.GET.get('page'))
    #     if page < 1:
    #         page = 1
    #
    # except:
    #     page = 1
    # limit = page * 10
    # offset = (page - 1) * 10
    # query = query.replace("'", "''")
    # query = "".join(i for i in query if ord(i) < 128)
    # query = query.strip()
    # if (query == '-1'):
    #     query = " "
    #
    # is_c = False
    # length = len(query)
    # count = 0;
    # tempQ = ""
    # for i in re.split("\W+", query):
    #     if count < 4:
    #         if i:
    #             # temp.append('"SNR_Title" ~* \'%s\'' % i)
    #             tempQ = tempQ + " " + i
    #             count = count + 1;
    # tempQ="'"+tempQ+"'"
    # print('in')
    # main_query = 'Select {0} from public.products_active_dailydeals  where  "tsv_title" @@ plainto_tsquery(' + str(tempQ) + ') AND "SNR_Active"=True offset 0 limit 20'
    # fields = ["id",
    #           "SNR_Title",
    #           "SNR_Available",
    #           "SNR_ProductURL", "SNR_ImageURL",
    #           "SNR_PriceAfter", "SNR_PriceBefore","SNR_Description","SNR_Customer_Rating"
    #
    #           ]
    # temp = []
    # out = ['"{0}"'.format(i) for i in fields]
    # data_query = main_query.format(",".join(out))
    # f_count = len(fields)
    # with connection.cursor() as cursor:
    #     cursor.execute(data_query)
    #
    #     for i in cursor.fetchall():
    #         current_item = {}
    #         for j in range(f_count):
    #             current_item[fields[j]] = i[j]
    #
    #         temp.append(current_item)
    # connection.close()
    # if temp:
    #     print('ist')
    #     res = {
    #         # "items":totalitems[0],
    #         # "pages":totalpages,
    #         "results": temp
    #     }
    #     return Response(res, status.HTTP_200_OK)
    # # results = Active_DailyDeals.objects.annotate(
    # #     search=SearchVector('SNR_Title')).filter(
    # #     Q(search=tempQ)).filter(SNR_Active=True).values()[:5]
    # else:
    # main_query = 'select * from public."products_active_dailydeals"  where(similarity("SNR_Title",\''+str(query.strip())+'\')) > 0.5 AND "SNR_Active" = True limit 20'
    # fields = ["id",
    #           "SNR_Title",
    #           "SNR_Available",
    #           "SNR_ProductURL", "SNR_ImageURL",
    #           "SNR_PriceAfter", "SNR_PriceBefore","SNR_Description","SNR_Customer_Rating"
    #
    #           ]
    # results = []
    # out = ['"{0}"'.format(i) for i in fields]
    # data_query = main_query.format(",".join(out))
    # f_count = len(fields)
    # print(data_query)
    # with connection.cursor() as cursor:
    #     cursor.execute(data_query)
    #
    #     for i in cursor.fetchall():
    #         current_item = {}
    #         for j in range(f_count):
    #             current_item[fields[j]] = i[j]
    #
    #         results.append(current_item)
    results = Active_DailyDeals.objects.annotate(
        similarity=TrigramSimilarity('SNR_Title', query)).filter(
        Q(similarity__gte=0.6)).filter(SNR_Active=True).exclude(SNR_Title=str(query)).values()[:20]
    res={
        # "items":totalitems[0],
        # "pages":totalpages,
        "results":results
    }
    return Response(res,status.HTTP_200_OK)


from django.db import models

class filter_deal_comparison_test_backup(APIView):

    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # def get(self, request, query):
    def get(self, request, id):
        # from django.db.models.functions import Greatest
        # >> > Facility.objects.annotate(match=Greatest(Similarity("facility__street", models.Value(query)),Similarity("facility__city", models.Value(query)))).filter(match__gt=0.2)

        # query = request.GET.get('category') # params
        # query = request.data()   # body/json
        # query = request.data()   # body/json

        print('id: ', id)
        # print('query: ', query)
        # print('category: ', category)
        print('request: ', request.data)
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(Q(similarity__gte=0.6)).filter(SNR_Active=True).exclude(SNR_Title=str(query)).values()[:20]
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query))
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query))
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(similarity__gt=0.6).filter(SNR_Active=True).values()[:20]
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(SNR_Active=True).values()[:20]
        # results = Active_DailyDeals.objects.annotate(similarity=Greatest(Max(TrigramSimilarity('SNR_Title', query))).filter(similarity__gte=0.6).order_by('-similarity')).values()[0:10]
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query) + \
        #                                                         TrigramSimilarity(' ', query)) \
        #               .filter(similarity__gte=0.6).filter(SNR_Active=True).order_by('-similarity').values(
        #     'SNR_Title', 'SNR_ProductURL')[0:10]
        #             Max(TrigramSimilarity('SNR_Title', query)))\
        #
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Category', query))\
        # .filter(similarity__gte=0.6).filter(SNR_Active=True).order_by('-similarity').exclude(SNR_Title=str(query)).values(
        #     'SNR_Title', 'SNR_ProductURL')[0:10]

        # product = Active_DailyDeals.objects.filter(SNR_Category__icontains=category, SNR_Active=True).values('SNR_Title', 'SNR_ProductURL')[0:10]



        # snr_category = Active_DailyDeals.objects.filter(id=id, SNR_Active=True).values('SNR_Category')
        # print('snr_category: ', snr_category)
        #
        results = Active_DailyDeals.objects.filter(SNR_Category__icontains=snr_category, SNR_Active=True).values()[0:10]
        # results = Active_DailyDeals.objects.filter(SNR_Category__icontains=category, SNR_Active=True).values()[0:20]
        # print(results)

        # if not results:
        #     results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(
        #         Q(similarity__gte=0.6)).filter(SNR_Active=True).exclude(SNR_Title=str(query)).values()[:20]

        # from django.db.models import Q
        # from myapp.models import Product
        #
        # def search_similar_products(request, title):
        #     threshold = 3  # define the Levenshtein distance threshold
        #     products = Product.objects.filter(
        #         Q(title__icontains=title) | Q(title__levenshtein_distance=title) <= threshold)
        #     similar_products = [{'title': product.title, 'description': product.description, 'price': product.price,
        #                          'image_url': product.image_url} for product in products]
        #     return similar_products

        res = {
            # "results": 'Everything is good'
                "results": results
        }

        return Response(res, status.HTTP_200_OK)

        # field_name = 'SNR_Title'
        # search_term = query
        # similarity_name = 'SNR_Title' + '_similarity'
        # strict_matching_name = 'SNR_Title' + '_strict_matching'
        # similarity = 0.2
        #
        # qs = Active_DailyDeals.objects.annotate(
        #     **{
        #         strict_matching_name: Case(
        #             When(**{field_name + '__iexact': search_term, 'then': 3}),
        #             When(**{field_name + '__istartswith': search_term, 'then': 2}),
        #             When(**{field_name + '__icontains': search_term, 'then': 1}),
        #             output_field=IntegerField(),
        #             default=0
        #         )
        #     }
        # )
        # print(qs)
        # print(qs.value())

        # qs = qs.annotate(**{similarity_name: TrigramSimilarity(field_name, search_term)})
        #
        # qs = qs.filter(
        #     Q(**{similarity_name + '__gt': similarity}) |
        #     # following line is required if column's max length is big,
        #     # because in this case similarity can be less
        #     # than minimum similarity, but strict match exists
        #     Q(**{strict_matching_name + '__gt': 0})
        # )
        #
        # results = qs.order_by(
        #     '-' + strict_matching_name)

        # res = {
        #     "results": 'Everything is good'
        # #     "results": results
        # }
        #
        # return Response(res, status.HTTP_200_OK)


class filter_deal_comparison_test(APIView):

    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    def get(self, request,typ, id):
        print('id: ', id)
        print('type: ', typ)
        t = typ
        # print(type(typ))
        # print('query: ', query)
        # print('category: ', category)
        print('request: ', request.data)

        if typ == 'vendor':
            print('true')
            snr_category = AllProducts.objects.using('newdb').filter(id=id, SNR_isShow=True).values('SNR_Category')
            print('snr_category: ', snr_category)
            results = AllProducts.objects.using('newdb').filter(SNR_Category__icontains=snr_category, SNR_isShow=True).values()[0:10]
        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(Q(similarity__gte=0.6)).filter(SNR_Active=True).exclude(SNR_Title=str(query)).values()[:20]

        # results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query) + \
        #                                                         TrigramSimilarity(' ', query)) \
        #               .filter(similarity__gte=0.6).filter(SNR_Active=True).order_by('-similarity').values(
        #     'SNR_Title', 'SNR_ProductURL')[0:10]
        #             Max(TrigramSimilarity('SNR_Title', query)))

        else:
            snr_category = Active_DailyDeals.objects.filter(id=id, SNR_Active=True).values('SNR_Category')
            print('snr_category: ', snr_category)
            results = Active_DailyDeals.objects.filter(SNR_Category__icontains=snr_category, SNR_Active=True).values()[0:10]

        # if not results:
        #     results = Active_DailyDeals.objects.annotate(similarity=TrigramSimilarity('SNR_Title', query)).filter(
        #         Q(similarity__gte=0.6)).filter(SNR_Active=True).exclude(SNR_Title=str(query)).values()[:20]

        # from django.db.models import Q
        # from myapp.models import Product
        #
        # def search_similar_products(request, title):
        #     threshold = 3  # define the Levenshtein distance threshold
        #     products = Product.objects.filter(
        #         Q(title__icontains=title) | Q(title__levenshtein_distance=title) <= threshold)
        #     similar_products = [{'title': product.title, 'description': product.description, 'price': product.price,
        #                          'image_url': product.image_url} for product in products]
        #     return similar_products

        res = {
            # "results": 'Everything is good'
                "results": results
        }

        return Response(res, status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def vocation_comparison(request,query):
    result = Active_Vocation.objects.annotate(
        similarity=TrigramSimilarity('SNR_Title',query)).filter(
            Q(similarity__gte=0.5)).filter(SNR_Active=True).exclude(SNR_Title=str(query)).values()[:20]


    res = {
        "result" : result
    }
    return Response (res,status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def sim_test(request, query):
    if request.method == 'GET':
        main_query = 'select * from public."products_active_dailydeals"  where(similarity("SNR_Title",\'' + str(
            query.strip()) + '\')) > 0.5 AND "SNR_Active" = True limit 20'
        fields = ["id",
                  "SNR_Title",
                  "SNR_Available",
                  "SNR_ProductURL", "SNR_ImageURL",
                  "SNR_PriceAfter", "SNR_PriceBefore","SNR_Description","SNR_Customer_Rating"

                  ]
        results = []
        out = ['"{0}"'.format(i) for i in fields]
        data_query = main_query.format(",".join(out))
        f_count = len(fields)
        print(data_query)
        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                results.append(current_item)
        res = {
            # "items":totalitems[0],
            # "pages":totalpages,
            "results": results
        }
        return Response(res, status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Product_Detail_Similarity_mobile(request, query):
    query_without_space = query.replace(" ", "")
    cache_key = 'comparison_search__' + query_without_space
    cache_time = 86200  # time to live in seconds
    result = cache.get(cache_key)
    print(query_without_space)
    if not result:

        query = query.replace("'", "''")
        query = "".join(i for i in query if ord(i) < 128)

        # query=re.sub('[^A-Za-z0-9]+', ' ', query)

        # print query;

        query = query.strip()

        entry_per_page = 50

        count_q = 'explain Select * from products_allproducts Where {0}'

        temp = []

        if (query == '-1'):
            query = " "

        is_c = False
        length = len(query)
        count = 0;
        tempQ = ""
        for i in re.split("\W+", query):
            if count < 4:
                if i:
                    # temp.append('"SNR_Title" ~* \'%s\'' % i)
                    tempQ = tempQ + " " + i

                    count = count + 1;

        # temp.append('"SNR_Title" ~* \'%s\'' % tempQ)
        # query=query.split()
        # query=query[0:4]
        temp.append("tsv_title @@ plainto_tsquery('%s')" % tempQ)
        temp2 = " AND ".join(temp)
        if is_c:
            temp.pop()

        res = {}
        count_q = count_q.format(temp2)

        offset = ' LIMIT 60'

        fields = ["id",
                  "SNR_SKU", "SNR_Title",
                  "SNR_ModelNo", "SNR_Brand",
                  "SNR_UPC", "SNR_Available",
                  "SNR_ProductURL", "SNR_ImageURL",
                  "SNR_Description", "SNR_isShow",
                  "SNR_Date", "SNR_Category",
                  "SNR_Condition", "SNR_SubCategory", "SNR_Price", "SNR_PriceBefore", "SNR_CustomerReviews"

                  ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as numeric)'.format(i) for i in extra_fields])

        q = 'Select %s from (Select * from products_allproducts Where {0} ' % (",".join(
            out
        ))

        f_count = len(fields)

        try:
            with connection.cursor() as cursor:

                # temp.append('"SNR_Category" = \'%s\'' % query_cat)
                temp = " AND ".join(temp)

                pageCount = 100;
                res['totalItems'] = 100
                res['totalPages'] = 100

                try:
                    page = int(request.GET.get('page'))
                except:
                    page = 1

                if page > pageCount:
                    page = pageCount

                if page > 0:
                    offset = "{0}".format(offset, entry_per_page * (page - 1))

                q = q.format(temp) + offset + ') AS rankTable order by "SNR_Price" ASC LIMIT 5'
                # # print q
                print('qwfaf', q)

                # print(q.count())
                cursor.execute(q, [query])
                print('kjjfaklf', cursor.execute(q, [query]))
                temp = []
                for i in cursor.fetchall():
                    # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

                res["results"] = temp

                result = res;
                # cache.set(cache_key, result, cache_time)
                # # # printsetting cache" + cache_key
                print(query)
                ##########
                return Response(res)

        except Exception as e:
            # # print e
            return Response(empty_response)

    else:
        # # # printreturning from cache" + cache_key
        return Response(result)

@api_view(['GET'])
def Product_Detail_Similarity_mobile_extra(request, query):

    # # print query


    # query_without_space = query.replace(" ", "")
    # cache_key = 'comparison_search__' + query_without_space
    # cache_time = 86200  # time to live in seconds
    # result = cache.get(cache_key)

    # if not result:

    query=query.replace("'","")
    query= "".join(i for i in query if ord(i) < 128)

    # query=re.sub('[^A-Za-z0-9]+', ' ', query)


    query = query.strip()
    print(query)
    #
    # entry_per_page = 5
    #
    # count_q = 'explain Select * from products_allproducts Where {0}'
    #
    # temp = []
    #
    # if (query == '-1'):
    #     query = " "
    #
    # is_c = False
    # length=len(query)
    # count=0;
    # tempQ=""
    # for i in re.split("\W+",query):
    #     if count<4:
    #         if i:
    #             # temp.append('"SNR_Title" ~* \'%s\'' % i)
    #             tempQ=tempQ+" "+i
    #
    #             count=count+1;
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    # re = connection.cursor()
    # re.execute('Select count(*) from public.products_allproducts  where  "tsv_title" @@ plainto_tsquery({1})')
    # row = re.fetchall()
    # row = [i[0] for i in row]
    # print("value", row[0])
    # count = int(row[0])
    # print(count)
    items = page * 5
    offset = (page - 1) * 5
    main_data_query = 'Select {0} from public.products_allproducts  where  "tsv_title" @@ plainto_tsquery({1}) order by "SNR_Price" ASC offset '+str(0)+' LIMIT '+str(50)

    fields = ["id",
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition", "SNR_SubCategory","SNR_Price","SNR_PriceBefore", "SNR_CustomerReviews"

    ]
    out = ['"{0}"'.format(i) for i in fields]
    temp = []
    extra_fields = []
    fields.extend(extra_fields)
    print("extra fields", extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    data_query = main_data_query.format(",".join(out), "'"+query+"'")
    print(data_query)
    f_count = len(fields)

    with connection.cursor() as cursor:
        cursor.execute(data_query)

        for i in cursor.fetchall():

            # if i[5] > 0:
            # print (i)
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = i[j]

            temp.append(current_item)
    print(len(temp))

    return Response(temp,status.HTTP_200_OK)
    # temp.append('"SNR_Title" ~* \'%s\'' % tempQ)
    # query=query.split()
    # query=query[0:4]
    # temp.append("tsv_title @@ plainto_tsquery('%s')" % tempQ)
    # temp2 = " AND ".join(temp)
    # if is_c:
    #     temp.pop()
    #
    #
    # res = {}
    # count_q = count_q.format(temp2)
    #
    # offset = offset = ' LIMIT {0}'.format(5)
    #
    # fields = ["id",
    #     "SNR_SKU", "SNR_Title",
    #     "SNR_ModelNo", "SNR_Brand",
    #     "SNR_UPC", "SNR_Available",
    #     "SNR_ProductURL", "SNR_ImageURL",
    #     "SNR_Description", "SNR_isShow",
    #     "SNR_Date", "SNR_Category",
    #     "SNR_Condition", "SNR_SubCategory","SNR_Price","SNR_PriceBefore", "SNR_CustomerReviews"
    #
    # ]
    # out = ['"{0}"'.format(i) for i in fields]
    #
    # extra_fields = []
    # fields.extend(extra_fields)
    #
    # out.extend(['cast("{0}" as numeric)'.format(i) for i in extra_fields])
    #
    # q = 'Select %s from (Select * from products_allproducts Where {0} ' % (",".join(
    #     out
    # ))
    # count_query = q.format("*")
    # f_count = len(fields)
    #
    # try:
    #     with connection.cursor() as cursor:
    #         cursor.execute(count_query, [query])
    #         # print count_query
    #         query_count = cursor.fetchone()[0]
    #         # temp.append('"SNR_Category" = \'%s\'' % query_cat)
    #         temp = " AND ".join(temp)
    #         query_count = patSearch('rows=(\d+)', query_count).group(1)
    #         query_count = int(query_count)
    #
    #         pageCount = int(math.ceil(query_count / float(5)))
    #         res['totalItems'] = query_count
    #         res['totalPages'] = pageCount
    #
    #         try:
    #             page = int(request.GET.get('page'))
    #         except:
    #             page = 1
    #
    #         if page > pageCount:
    #             page = pageCount
    #
    #         if page > 0:
    #             offset = "{0}".format(offset, entry_per_page * (page - 1))
    #
    #         q = q.format(temp) + offset+') AS rankTable order by "SNR_Price" ASC'
    #         # # print q
    #         # # print q
    #         cursor.execute(q+offset, [query])
    #         temp = []
    #         for i in cursor.fetchall():
    #             # if i[5] > 0:
    #             current_item = {}
    #             for j in range(f_count):
    #                 current_item[fields[j]] = i[j]
    #
    #             temp.append(current_item)
    #
    #         res["results"] = temp
    #
    #         result = res;
    #         # cache.set(cache_key, result, cache_time)
    #         # # # printsetting cache" + cache_key
    #
    #         ##########
    #         return Response(res)
    #
    # except Exception as e:
    #     # # print e
    #     return Response(empty_response)

    # else:
    #     print('ok')
    #     # # # printreturning from cache" + cache_key
    #     return Response(result)


@api_view(['GET'])
def FilterAllProducts_Search_Similar_Ilike_Faster(request, query, price1, price2, brand, merchant, category):
    # # print query
    query = query.lower()
    query = query.encode('utf-8').strip()

    entry_per_page = 36

    count_q = 'Select count(*),"SNR_Category" from products_allproducts Where {0} GROUP BY "SNR_Category" ORDER BY count("SNR_Category") DESC limit 1'

    temp = []

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    is_c = False
    for i in re.split("\W+", query):
        if i:
            temp.append('"SNR_Title" ~* \'%s\'' % i)

    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)

    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()

    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select *{0} from products_allproducts Where {1} ORDER BY rank DESC' % (",".join(
        out
    ))

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count, query_cat = cursor.fetchone()
            # # print(count_q)
            # # print(query_cat)
            temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)
            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            q = q.format(""",similarity('%s',"SNR_Title") as rank""" % (query), temp) + offset + ") AS rankTable"
            # # print q
            # # print q
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except:
        return Response(empty_response)


@api_view(['GET'])
def FilterAllProducts_Search_Similar_S(request, query, price1, price2, brand, merchant, category):
    # # print query
    query = query.lower()
    query = query.encode('utf-8').strip()

    entry_per_page = 36

    count_q = 'Select count(*),"SNR_Category" from products_allproducts Where {0} GROUP BY "SNR_Category" ORDER BY count("SNR_Category") DESC limit 1'

    temp = []

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    is_c = False
    temp.append('similarity("SNR_Title",%s)')
    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)


    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select *{0} from products_allproducts Where {1} ORDER BY rank DESC' % (",".join(
        out
    ))

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count,query_cat = cursor.fetchone()
            ## print(count_q)
            ## print(query_cat)
            temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)
            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            q = q.format(""",similarity("SNR_Title",'%s') as rank""" % (query),temp) + offset+") AS rankTable"
            # # print q
            # # print q
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except:
        return Response(empty_response)




@api_view(['GET'])
def FilterAllProducts_Search_Similar(request, query, price1, price2, brand, merchant, category):
    # # print query
    query = query.lower()
    query = query.encode('utf-8').strip()

    entry_per_page = 36

    count_q = 'Select count(*),"SNR_Category" from products_allproducts Where {0} GROUP BY "SNR_Category" ORDER BY count("SNR_Category") DESC limit 1'

    temp = []

    if (query == '-1'):
        query = " "

    if (price1 != '-1' and price2 != '-1'):
        # # print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        # # print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        # # print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    is_c = False
    temp.append('tsv_title @@ plainto_tsquery(%s)')
    if (category != '-1'):
        # # # printcategory add"
        category = category.lower()
        is_c = True
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)


    temp2 = " AND ".join(temp)
    if is_c:
        temp.pop()


    res = {}
    count_q = count_q.format(temp2)

    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from (Select *{0} from products_allproducts Where {1} ORDER BY rank DESC' % (",".join(
        out
    ))

    f_count = len(fields)

    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count,query_cat = cursor.fetchone()
            ## print(count_q)
            ## print(query_cat)
            temp.append('"SNR_Category" = \'%s\'' % query_cat)
            temp = " AND ".join(temp)
            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            q = q.format(""",similarity('%s',"SNR_Title") as rank""" % (query),temp) + offset+") AS rankTable"
            # # print q
            # # print q
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except:
        return Response(empty_response)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search(request,query,price1,price2,brand,merchant,category):
    ## print query
    query=query.lower()
    query=query.encode('utf-8').strip()

    entry_per_page = 36

    count_q = 'Select count(*) from products_allproducts Where {0}'

    temp = []

    if (query == '-1'):
        query=" "

    if (price1 != '-1' and price2 != '-1'):
        ## print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        ## print 'added brand'
        brand=brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant=merchant.lower()
        ## print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    if (category!='-1'):
        ## # printcategory add"
        category=category.lower()
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)


    temp.append('tsv_title @@ plainto_tsquery(%s)')
    temp = " AND ".join(temp)

    res = {}
    count_q = count_q.format(temp)




    offset = ' ORDER BY "SNR_Date" DESC LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC","SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
         "SNR_Condition","SNR_SubCategory"


    ]
    out = ['"{0}"'.format(i) for i in fields]
    
    extra_fields = ["SNR_PriceBefore","SNR_CustomerReviews","SNR_Price"]
    fields.extend(extra_fields)
    
    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from products_allproducts Where {0}' % (",".join(
        out
    ))


    f_count = len(fields)

    with connection.cursor() as cursor:
        cursor.execute(count_q,[query])
        query_count = cursor.fetchone()[0]
        if query_count ==0:
            return Response(status=status.HTTP_204_NO_CONTENT)

        pageCount = int(math.ceil( query_count/float(entry_per_page)))
        res['totalItems'] = query_count
        res['totalPages'] = pageCount

        try:
            page = int(request.GET.get('page'))
        except:
            page = 1

        if page>pageCount:
            page = pageCount

        if page>0:
            offset = "{0} OFFSET {1}".format(offset,entry_per_page*(page-1))

        q = q.format(temp) + offset
        ## print q
        cursor.execute(q, [query])
        temp = []
        for i in cursor.fetchall():
            # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

        res["results"] = temp

        return Response(res)


@api_view(['GET'])
def FilterAllProductsASC_Search(request, query, price1, price2, brand, merchant, category):
    ## print query
    query = query.lower()
    query = query.replace('(', '\(')
    query = query.replace(')', '\)')

    query=query.encode('utf-8').strip()


    entry_per_page = 36

    count_q = 'Select count(*) from products_allproducts Where {0}'

    temp = []

    if (price1 != '-1' and price2 != '-1'):
        ## print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        ## print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        ## print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    if (category != '-1'):
        ## # printcategory add"
        category = category.lower()
        temp.append('"SNR_Category" ~* \'%s\'' % category)


    temp.append('tsv_title @@ plainto_tsquery(%s)')
    temp = " AND ".join(temp)

    res = {}
    count_q = count_q.format(temp)

    offset = ' ORDER BY "SNR_Price" LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from products_allproducts Where {0}' % (",".join(
        out
    ))

    f_count = len(fields)
    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count = cursor.fetchone()[0]
            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            q = q.format(temp) + offset
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except:
        return Response(empty_response)


@api_view(['GET'])
def CountQueryAll_new(request,query):
    q = 'Select "SNR_Category" ,count(*) from products_allproducts Where tsv_title @@ plainto_tsquery(%s) GROUP BY "SNR_Category"'

    cats = {}
    with connection.cursor() as cursor:
        cursor.execute(q,[query])
        data = {str(i[0]).title():i[1] for i in cursor.fetchall()}
    return Response(data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CountQueryAll_new_count(request,query):
    query = query.replace('(', '\(')
    query = query.replace(')', '\)')

    q = 'Select "SNR_Category" ,count(*) from products_allproducts where {0} GROUP BY "SNR_Category";'

    subque='';
    temp = []
    # for word in query.split():
    #     temp.append('"SNR_Title" ~* \'%s\'' % word)

    # tsvquery = query.replace(' ', ' & ')
    # # print tsvquery
    #
    temp.append('tsv_title @@ plainto_tsquery(\'%s\')' % query)

    temp2 = " AND ".join(temp)
    q=q.format(temp2)
    # # print q
    # # print q
    with connection.cursor() as cursor:
        # # print q
        cursor.execute(q,[query])
        # # print cursor.fetchall()
        data = {str(i[0]).title():i[1] for i in cursor.fetchall()}
    return Response(data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CountQueryAll_new(request,query):
    q = 'Select "SNR_Category" ,count(*) from products_allproducts Where tsv_title @@ plainto_tsquery(%s) GROUP BY "SNR_Category"'

    cats = {}
    with connection.cursor() as cursor:
        cursor.execute(q,[query])
        data = {str(i[0]).title():i[1] for i in cursor.fetchall()}
    return Response(data)


@api_view(['GET'])
def FilterAllProductsDESC_Search(request,query,price1,price2,brand,merchant,category):
    ## print query
    query = query.lower()
    query = query.replace('(', '\(')
    query = query.replace(')', '\)')

    query=query.encode('utf-8').strip()


    entry_per_page = 36

    count_q = 'Select count(*) from products_allproducts Where {0}'

    temp = []

    if (price1 != '-1' and price2 != '-1'):
        ## print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        ## print 'added brand'
        brand = brand.lower()
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        merchant = merchant.lower()
        ## print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)

    if (category != '-1'):
        ## # printcategory add"
        category = category.lower()
        temp.append('"SNR_Category" ~* \'%s\'' % category)


    temp.append('tsv_title @@ plainto_tsquery(%s)')
    temp = " AND ".join(temp)

    res = {}
    count_q = count_q.format(temp)




    offset = ' ORDER BY "SNR_Price" DESC LIMIT {0}'.format(entry_per_page)

    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews", "SNR_Price"]
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    q = 'Select %s from products_allproducts Where {0}' % (",".join(
        out
    ))
    f_count = len(fields)
    try:
        with connection.cursor() as cursor:
            cursor.execute(count_q, [query])
            query_count = cursor.fetchone()[0]
            if query_count == 0:
                return Response(empty_response)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            q = q.format(temp) + offset
            cursor.execute(q, [query])
            temp = []
            for i in cursor.fetchall():
                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp

            return Response(res)

    except:
        return Response(empty_response)


# Create your tests here.
@api_view(['GET'])
def FilterAllProducts(request,query,price1,price2,brand,merchant):


   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_UPC__icontains=query)



       if(price1!='-1' and price2!='-1'):
           ## print 'added price'
           que &= Q(SNR_Price__range=(price1, price2))

       if( brand!='-1'):
           ## print 'added brand'

           que &= Q(SNR_Brand__icontains=brand)


       if( merchant!='-1'):
           ## print 'added merchant'

           que &= Q(SNR_Available__icontains=merchant)

       products = AllProducts.objects.filter(que).order_by("-SNR_Date")

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data,
        }
       return Response(res)


   except AllProducts.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)


   pass

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CountBrandMerchantsAllProducts_Search(request,query,price1,price2,brand,merchant,category):
    query = query.lower()

    query = "".join(i for i in query if ord(i) < 128)

    query = re.sub('[^A-Za-z0-9]+', ' ', query)

    # # print query;

    query = query.encode('utf-8').strip()
    q = 'Select Distinct "SNR_Available","SNR_Brand" from products_allproducts Where {0}'

    temp = []

    if (price1 != '-1' and price2 != '-1'):
        ## print 'added price'
        temp.append('"SNR_Price" BETWEEN %s AND %s' % (price1, price2))

    if (brand != '-1'):
        ## print 'added brand'
        temp.append('"SNR_Brand" ~* \'%s\'' % brand)

    if (merchant != '-1'):
        ## print 'added merchant'
        temp.append('"SNR_Available" ~* \'%s\'' % merchant)
    if (category!='-1'):
        ## # printcategory add"
        category=category.lower()
        temp.append('"SNR_Category" ILIKE \'%s\'' % category)

    Q_parts = query.split(" ");

    # for part in Q_parts:
    #     part = ps.stem(part)
    #     # # print(part)
    #     temp.append('"SNR_Title" ~* \'%s\'' % part)
    #
    temp.append('tsv_title @@ plainto_tsquery(%s)')
    temp = " AND ".join(temp)

    q = q.format(temp)

    data = ['merchants', 'brands']
    data1 = ['SNR_Available', 'SNR_Brand']

    mappings = [set(), set()]
    try:

        with connection.cursor() as cursor:
            cursor.execute(q,[query])
            temp = cursor.fetchall()
            if not temp:
                return Response(empty_brands)
            # out[ mappings[i] ] = [{i:j[0]} for j in cursor.fetchall()]
            for i in temp:
                if i[0]:
                    mappings[0].add(i[0])

                if i[1]:
                    mappings[1].add(i[1])

        out = {}
        for i in range(2):
            out[data[i]] = [{data1[i]: j} for j in mappings[i]]


        return Response(out)
    except:
        return Response(empty_brands)

from django.db import connections

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def findcredential(request):
    if request.method =='GET':
        db_host = connections['default'].settings_dict['HOST']
        db_name = connections['default'].settings_dict['NAME']
        db_port = connections['default'].settings_dict['PORT']
        db_pass = connections['default'].settings_dict['PASSWORD']
        db_engine = connections['default'].settings_dict['ENGINE']
        db_user = connections['default'].settings_dict['USER']
        dic={
            'Host':db_host,
            'Name':db_name,
            'Port':db_port,
            'password':db_pass,
            'engine':db_engine,
            'user':db_user
        }
        return Response(dic)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def findtitlefromUPC(request,upc):
        try:
            url = 'https://www.upcitemdb.com/upc/'+upc
            source = requests.get(url)
            plain_text = source.text
            # # print plain_text
            soup = BeautifulSoup(plain_text, "lxml")

            count = 0;
            for link in soup.findAll('p', {'class': 'detailtitle'}):
                # # # print link
                title=link.find('b').text
                firstpart, secondpart = title[:len(title) / 2], title[len(title) / 2:]


            res={"Title":firstpart,
                             "FullText":title}
            result = res;
            # cache.set(cache_key, result, cache_time)
            # # printsetting cache for "+cache_key

            return Response(res)
        except:
            res={"Error":True,
                             "Status":"UPC Not found"}
            result = res;
            # cache.set(cache_key, result, cache_time)
            # # printsetting cache for "+cache_key

            return Response(res)




@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterProductsRevsebay(request,query):
    # # printaamad"
    if request.method == 'GET':
        # try:
        query = query.replace(" ", "+")
        url = 'https://www.ebay.com/sch/i.html?_nkw=' + query
        source = requests.get(url)
        plain_text = source.text
        soup = BeautifulSoup(plain_text, "lxml")
        newlink=""
        for link in soup.findAll('li', {'class': 's-item'}):
            newlink=link.find('a', {'class': 's-item__link'}).get('href')
            break

        # print newlink
        found=""
        m = re.search('/itm/(.+?)/?&hash', newlink)
        if m:
            found = m.group(1)

        # # printfound   "+found
        title = found.split("/")
        # print title[0]
        id = title[1].split("?")
        # print id[0]
        prodid = id[1].split("=")
        # print prodid[1].split("&")[0]
        nlink = 'https://www.ebay.com/urw/' + title[0] + '/product-reviews/' + prodid[1].split("&")[
            0] + '?_itm=' + str(id[0])


        # # printnew lnk"
        # print nlink
        source = requests.get(nlink)
        plain_text = source.text
        soup = BeautifulSoup(plain_text, "lxml")

        items = []

        # # print soup.body

        for rev in soup.findAll('div', {'class': ' ebay-review-section'}):

            Reviews = {};
            Reviews["SNR_Review_Title"] = rev.find('h3', {'class': 'review-item-title rvw-nowrap-spaces'}).text
            Reviews["SNR_Review_Author"] = rev.find("a", class_="review-item-author").text
            try:
                Reviews["SNR_Review_Body"] = rev.find('p', {'class': 'review-item-content rvw-wrap-spaces'}).text
            except:
                Reviews["SNR_Review_Body"] =""

            Reviews["SNR_Review_Stars"] = int(rev.find("span", class_="star-rating").get('aria-label').split(" ")[0])
            Reviews["SNR_Review_UP"] = 1
            Reviews["SNR_Review_Down"] = 1
            Reviews["SNR_IS_SNR"] = True

            items.append(Reviews)

        result = {"Reviews": items}
        res= {"results": result}
        return Response(res)
        # except:
        #     return Response({
        #         "Error": "Please provide URL"
        #     })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def findproductsfromebay(request,query):
    query = "".join(i for i in query if ord(i) < 128)
    items=[]
    query=query.replace(" ","+")
    url = 'https://www.ebay.com/sch/i.html?_nkw=' + query

    cache_key = url+str(query.encode('utf-8'))
    cache_time = 60500  # time to live in seconds
    result = cache.get(cache_key)

    if not result:



        try:
            source = requests.get(url)
            plain_text = source.text
            soup = BeautifulSoup(plain_text, "html.parser")

            items = []

            cat = soup.find('ul', {'class': 'srp-refine__category__list'})
            for link in soup.findAll('li', {'class': 's-item'}):
                # # print link
                request = {}
                try:
                    request["SNR_ProductURL"] = link.find('a', {'class': 's-item__link'}).get('href')
                    request["SNR_Title"] = link.find('h3', {'class': 's-item__title'}).text
                    request["SNR_Description"] = "Visit site to see description"
                    request["SNR_Price"] =float (link.find('span', {'class': 's-item__price'}).text[1:])
                    request["SNR_CustomerReviews"] = 0.0
                    request["SNR_PriceBefore"] = -1

                    request["SNR_Category"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                    request["SNR_Available"] = "ebay"

                    request["SNR_ModelNo"] = "00"
                    request["SNR_UPC"] = "00"

                    request["SNR_SubCategory"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                    request["SNR_Condition"] = "00"
                    img = link.find('img').get('src')
                    if 'gif' in img:
                        img = link.find('img').get('data-src')

                    request["SNR_ImageURL"] = img

                    request["SNR_SKU"] = "EB" + str(random.randint(1, 1111111))

                    url = "http://54.39.28.217:9000/products/InsertProduct/"
                    header = {'Content-Type': 'application/json'}
                    Thread(target=save_products, args=[url, request]).start()

                    items.append(request)

                except:
                    continue

            res = {"results": items,"status":True}
            result = res;
            cache.set(cache_key, result, cache_time)
            # # printsetting cache for " + cache_key

            return Response(res)

        except:
            res = {"results": items,"error":True}
            result = res;
            # cache.set(cache_key, result, cache_time)
            # # printsetting cache for " + cache_key

            return Response(res)



    else:
        # # printreturning from cache " + cache_key

        return Response(result)



# import bottlenose
import json
# import xmltodict

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def findproductsfromamazon(request,query):
    query = "".join(i for i in query if ord(i) < 128)

    query_cache = query.replace(" ", "+")

    items=[]

    cache_key = "amazon_search_apixxxx"+str(query_cache)
    cache_time = 60500  # time to live in seconds
    result = cache.get(cache_key)


    query=query.replace("'","")
    query=query.replace("(","")
    query=query.replace(")","")
    query=query.replace("#","")
    query=query.replace("^","")
    query=query.replace("*","")
    if not result:
        # try:




            # print(query)
            # amazon = bottlenose.Amazon('AKIAJYH5LPTVAMBU6NOQ', 'DfGaLxsy9ftS/672f0VxCWgoXecj3LRxNoqLMNPA',
            #                            'mobilea0fe6ba-20')
            # response = amazon.ItemSearch(Keywords=query, SearchIndex="All",ResponseGroup='ItemAttributes,Images,Large', limit=100, )
            #
            #
            # response = json.dumps(xmltodict.parse(response), indent=4)
            response = json.loads(response)
            items=[]
            # print response['ItemLookupResponse']['Items']['Item']
            try:
                for item in response['ItemSearchResponse']['Items']['Item']:
                    request={}

                    request["SNR_Title"] = (item['ItemAttributes']['Title'])

                    try:
                        request["SNR_Price"] = (item['ItemAttributes']['ListPrice']['FormattedPrice'][1:])
                    except:
                        request["SNR_Price"] = 00;
                    request["SNR_CustomerReviews"] = 0.0
                    request["SNR_PriceBefore"] = -1

                    try:
                        request["SNR_Category"] = (item['ItemAttributes']['Binding'])
                    except:
                        request["SNR_Category"] ="Uncategorized"

                    request["SNR_Available"] = "Amazon"

                    try:
                        request["SNR_SubCategory"] = (item['ItemAttributes']['Binding'])
                    except:
                        request["SNR_SubCategory"] ="Uncategorized"

                    request["SNR_Condition"] = "Brand New"





                    try:
                        pass
                        # print(item['ItemAttributes']['Brand'])
                    except:
                        pass
                        # # printNo Brand"
                    try:
                        request["SNR_ModelNo"]=(item['ItemAttributes']['Model'])
                    except:
                        request["SNR_ModelNo"]="0000"

                    try:
                        request["SNR_UPC"] = (item['ItemAttributes']['UPC'])
                    except:
                        request["SNR_UPC"] = "0000"

                    try:
                        request["SNR_Description"]=(item['ItemAttributes']['Feature'][0])

                    except:
                        request["SNR_Description"]="Visit site to see description"

                    request["SNR_ProductURL"]=(item['DetailPageURL'])
                    request["SNR_SKU"]=(item['ASIN'])

                    try:
                        request["SNR_ImageURL"]=['MediumImage']['URL']
                    except:
                        try:
                            for img in (item['ImageSets']['ImageSet']):
                                request["SNR_ImageURL"]= img['MediumImage']['URL']
                                break
                        except:
                            request["SNR_ImageURL"]= item['ImageSets']['ImageSet']['MediumImage']['URL']

                    # # print(request)
                    url = "http://54.39.28.217:9000/products/InsertProduct/"
                    header = {'Content-Type': 'application/json'}
                    # requests.put(url, headers=header, data=json.dumps(request))
                    Thread(target=save_products, args=[url,request]).start()


                    items.append(request)
            except:
                res = {"results": items}
                result = res;
                cache.set(cache_key, result, cache_time)
                # # printsetting cache for " + cache_key

                return Response(res)


            #
            # url = "http://127.0.0.1:8000/search/insertsearchedproducts_ebay/"+query

            res = {"results": items}
            result = res;
            # cache.set(cache_key, result, cache_time)
            # # printsetting cache for " + cache_key

            return Response(res)

        # except:
        #     res = {"results": items,"exception-occered":True}
        #     result = res;
        #     cache.set(cache_key, result, cache_time)
        #     # # printsetting cache for " + cache_key
        #
        #     return Response(res)



    else:
        # # printreturning from cache " + cache_key

        return Response(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def insertproductsfromebay(request,query):
    query = "".join(i for i in query if ord(i) < 128)
    query = query.replace(" ", "+")
    items=[]
    url = 'https://www.ebay.com/sch/i.html?_nkw=' + query

    cache_key = 'cache_for_ebaysearch_'+str(query)
    cache_time = 60500  # time to live in seconds
    result = cache.get(cache_key)

    if not result:



        try:
            source = requests.get(url)
            plain_text = source.text
            soup = BeautifulSoup(plain_text, "lxml")

            items = []

            cat = soup.find('ul', {'class': 'srp-refine__category__list'})
            for link in soup.findAll('li', {'class': 's-item'}):
                # # print link
                request = {}
                try:
                    request["SNR_ProductURL"] = link.find('a', {'class': 's-item__link'}).get('href')
                    request["SNR_Title"] = link.find('h3', {'class': 's-item__title'}).text
                    request["SNR_Description"] = "Visit site to see description"
                    request["SNR_Price"] =float (link.find('span', {'class': 's-item__price'}).text[1:])
                    request["SNR_CustomerReviews"] = 0.0
                    request["SNR_PriceBefore"] = -1

                    request["SNR_Category"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                    request["SNR_Available"] = "Ebay"

                    request["SNR_ModelNo"] = "00"
                    request["SNR_UPC"] = "00"

                    request["SNR_SubCategory"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                    request["SNR_Condition"] = "00"
                    img = link.find('img').get('src')
                    if 'gif' in img:
                        img = link.find('img').get('data-src')

                    request["SNR_ImageURL"] = img

                    request["SNR_SKU"] = "EB" + str(random.randint(1, 1111111))

                    url = "https://backend.shopnroar.com/products/InsertProduct/"
                    header = {'Content-Type': 'application/json'}
                    requests.put(url, headers=header, data=json.dumps(request))

                    items.append(request)

                except:
                    continue


            res = {"results": items}
            result = res;
            # cache.set(cache_key, result, cache_time)
            # # printsetting cache for " + cache_key

            return Response(res)

        except:
            res = {"results": items}
            result = res;
            # cache.set(cache_key, result, cache_time)
            # # printsetting cache for " + cache_key

            return Response(res)



    else:
        # # printreturning from cache " + cache_key

        return Response(result)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterAllProducts_Search_Similar_Ilike_nazir(request, query):
    query_one = query
    query_two = ''
    query = query.split()
    if len(query) > 2:
        query_one = ' '.join(query[0:2])
        query_two = ' '.join(query[-len(query)+2:])

        dub_q = "SELECT " + '"SNR_Title"' + " FROM (SELECT *, similarity('{query_one}'," + '"SNR_Title"' + ") FROM products_allproducts Where " + '"SNR_Title"' + " ~ '{first}' AND " + '"SNR_Title"' + " ~ '{last}') as search_result where similarity('{query_two}', " + '"SNR_Title"' + ") > 0;"
    dub_q = dub_q.format(query_one=query_one, first=query[0], last=query[1], query_two=query_two)
    # print dub_q
    with connection.cursor() as cursor:
        cursor.execute(dub_q)
        row = cursor.fetchone()
        # print list(row)
        return Response({"MSG":list(row)}, status=status.HTTP_200_OK)




# Create your tests here.
@api_view(['GET'])
def CountBrandMerchantsAllProducts(request,query,price1,price2,brand,merchant):


   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_UPC__icontains=query)



       if(price1!='-1' and price2!='-1'):
           ## print 'added price'
           que &= Q(SNR_Price__range=(price1, price2))

       if( brand!='-1'):
           ## print 'added brand'

           que &= Q(SNR_Brand__icontains=brand)


       if( merchant!='-1'):
           ## print 'added merchant'

           que &= Q(SNR_Available__icontains=merchant)




       products = AllProducts.objects.filter(que)
       merchants= products.values('SNR_Available').distinct()
       brands= products.values('SNR_Brand').distinct()


       serializer_context = {'request': request}
       merchant_serilizer = AllProductsFilterStores_Serializer(merchants, many=True, context=serializer_context)
       brand_serilizer = AllProductsFilterBrands_Serializer(brands, many=True, context=serializer_context)

       res={
       'merchants': merchant_serilizer.data,
       'brands': brand_serilizer.data
        }
       return Response(res)


   except AllProducts.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)


   pass


"""
@api_view(['GET'])
def GetDistinctCategories(request):
    query = 'Select "SNR_Category" from products_allproducts Group By "SNR_Category"'

    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()


        try:
            All_Cats = set(str(i[0]).title() for i in data if i[0])

            return Response({"Categories":list(All_Cats)})
        except AllProducts.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
"""

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def GetDistinctShops(request):
    query = 'Select distinct "SNR_Available" from products_allproducts'

    with connection.cursor() as cursor:
        cursor.execute(query)

        try:
            All_Cats = set(i[0].capitalize() for i in cursor.fetchall() if i[0])

            return Response({"Shops":list(All_Cats)})
        except AllProducts.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def FilterAllProductsASC(request,query,price1,price2,brand,merchant):
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_UPC__icontains=query)



       if(price1!='-1' and price2!='-1'):
           ## print 'added price'
           que &= Q(SNR_Price__range=(price1, price2))

       if( brand!='-1'):
           ## print 'added brand'

           que &= Q(SNR_Brand__icontains=brand)


       if( merchant!='-1'):
           ## print 'added merchant'

           que &= Q(SNR_Available__icontains=merchant)

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)

       page = request.GET.get('page')
       try:

           data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items = paginator.count
       pages = paginator.num_pages
       res = {
           'totalItems': items,
           'totalPages': pages,
           'results': product_serilizer.data,
       }
       return Response(res)


   except AllProducts.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)


   pass

# Create your tests here.
@api_view(['GET'])
def FilterAllProductsDESC(request,query,price1,price2,brand,merchant):


   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_UPC__icontains=query)



       if(price1!='-1' and price2!='-1'):
           ## print 'added price'
           que &= Q(SNR_Price__range=(price1, price2))

       if( brand!='-1'):
           ## print 'added brand'

           que &= Q(SNR_Brand__icontains=brand)


       if( merchant!='-1'):
           ## print 'added merchant'

           que &= Q(SNR_Available__icontains=merchant)

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)

       page = request.GET.get('page')
       try:

           data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items = paginator.count
       pages = paginator.num_pages
       res = {
           'totalItems': items,
           'totalPages': pages,
           'results': product_serilizer.data,
       }
       return Response(res)


   except AllProducts.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)


   pass



# Create your tests here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def GetDistinctCategories(request):
    cache_key = 'getCategories'
    cache_time = 43200  # time to live in seconds
    result = cache.get(cache_key)

    if not result:

        query = 'Select DISTINCT "SNR_Category" from products_categorytable'

        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            try:

                cats=list(set((i[0]) for i in data))
                cats.sort()

                res={
                    "Categories": cats
                }
                result = res;
                cache.set(cache_key, result, cache_time)
                # # printsetting cache" + cache_key
                return Response(res)
            except AllProducts.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        # # printreturning from cache" + cache_key
        return Response(result)







@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterProductsbyprice(request,query,price1, price2):

   # ### print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=Q(SNR_UPC__icontains=query)
       que &= Q(SNR_Price__range=(price1, price2))

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)



   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterProductsbypriceASC(request, query, price1, price2):
    ### print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |=  Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        products = AllProducts.objects.filter(que).order_by('SNR_Price')

        paginator = Paginator(products, 36)

        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

        items = paginator.count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': product_serilizer.data
        }
        return Response(res)



    except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

        return Response(status=status.HTTP_204_NO_CONTENT)

    #
    # if request.method == 'GET':
    #
    #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterProductsbypriceDESC(request, query, price1, price2):
    ### print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))
        products = AllProducts.objects.filter(que)

        paginator = Paginator(products, 36)

        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

        items = paginator.count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': product_serilizer.data
        }
        return Response(res)




    except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

        return Response(status=status.HTTP_204_NO_CONTENT)

    #
    # if request.method == 'GET':
    #
    #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def FilterProductsDESC(request,query):

   ### print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)

       products = AllProducts.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)
   except AllProducts.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)

   pass


@api_view(['GET'])
def FilterProductsASC(request,query):

   ### print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)

       products = AllProducts.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)

   except AllProducts.DoesNotExist:


       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass




@api_view(['GET'])
def FilterbyURL(request,query):

   ### print(query)
   try:
       que = Q()

       que = Q(SNR_ProductURL__icontains=query)

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)



   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:


       return Response(status=status.HTTP_204_NO_CONTENT)


   pass








@api_view(['GET'])
def FilterbyURLASC(request,query):

   ### print(query)
   try:
       que = Q()

       que = Q(SNR_ProductURL__icontains=query)

       products = AllProducts.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)



   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:


       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass




@api_view(['GET'])
def FilterbyURLDESC(request,query):

   ### print(query)
   try:
       que = Q()

       que = Q(SNR_ProductURL__icontains=query)

       products = AllProducts.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)



   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:


       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass








@api_view(['GET'])
def Filterbyprice(request,p1,p2):

   try:

       que = Q()
       que = Q(SNR_Price__range=(p1, p2))

       products = AllProducts.objects.filter(que)

       paginator = Paginator(products, 36)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)



   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:


       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def AutoComplete(request,query):
    res = {}

    query = query.replace('(', '\(')
    query = query.replace(')', '\)')
    query = query.replace("'", "''")

    # print query;

    query=query+'%'

    entry_count = 10
    fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL", "id",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition", "SNR_PriceBefore",
            "SNR_CustomerReviews", "SNR_Price",
            "SNR_SubCategory"

    ]

    q = 'Select {0} from products_allproductspartition Where "SNR_Title" ilike (%s) limit {1}'.format(",".join(
        ['"{0}"'.format(i) for i in fields]
    ),entry_count)

    f_count = len(fields)

    with connection.cursor() as cursor:
        cursor.execute(q, [query])

        # print q

        res['totalItems'] = 0
        res['totalPages'] = 0
        temp = []
        for i in cursor.fetchall():
            # if i[5]>0:
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)

        if temp:
            res["results"] = temp
            return Response(res)
        return  Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def AutoComplete1(request,query):
    res = {}
    temp=[]
    query = query.replace('(', '\(')
    query = query.replace(')', '\)')
    query = query.replace("'", "''")
    main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(\''+str(query)+'\') limit 10'
    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL", "id",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition", "SNR_PriceBefore",
        "SNR_CustomerReviews", "SNR_Price",
        "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]
    data_query = main_data_query.format(",".join(out))
    f_count = len(fields)
    with connection.cursor() as cursor:
        cursor.execute(data_query)
        for i in cursor.fetchall():
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = i[j]
            temp.append(current_item)
    connection.close()
    res = {
        'results': temp,
    }
    return Response(res, status.HTTP_200_OK)

"""
@api_view(['GET'])
def AutoComplete(request,query):

   try:
       # que = Q()
       # for word in query.split():
       #     que &= Q(SNR_Title__icontains=word)
       #

       products = AllProducts.objects.filter(SNR_Title__icontains=query)

       paginator = Paginator(products, 15)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       Products_Serializer = AllProducts_Serializer(data, many=True, context=serializer_context)

       items = paginator.count
       pages = paginator.num_pages
       res = {
           'totalItems': items,
           'totalPages': pages,
           'results': Products_Serializer.data
       }

       return Response(res)

   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

       return Response(status=status.HTTP_204_NO_CONTENT)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass

"""
############################################################################################
@api_view(['POST','GET'])
@permission_classes((permissions.AllowAny,))
def xxtestsearch(request,que,items):
    if request.method == 'GET':
        # try:
        #     query = "".join(i for i in que if ord(i) < 128)
        #     query = que.replace(" ", "+")
        #     try:
        #         if  int(request.GET.get('low'))!=-1 & int(request.GET.get('high'))!=-1 :
        #             minprice=int(request.GET.get('low'))
        #             maxprice=int(request.GET.get('high'))
        #             url = 'https://www.ebay.com/sch/i.html?_nkw=' + query +'&&_udlo='+str(minprice)+'&_udhi='+str(maxprice)
        #         else:
        #             url = 'https://www.ebay.com/sch/i.html?_nkw=' + query
        #
        #     except:
        #         minprice=-1
        #         maxprice=-1
        #         url = 'https://www.ebay.com/sch/i.html?_nkw=' + query
        #
        #     try:
        #         source = requests.get(url)
        #         plain_text = source.text
        #         soup = BeautifulSoup(plain_text, "html.parser")
        #
        #         itemss = []
        #
        #         cat = soup.find('ul', {'class': 'srp-refine__category__list'})
        #         for link in soup.findAll('li', {'class': 's-item'}):
        #             # # print link
        #             request = {}
        #             try:
        #                 request["SNR_ProductURL"] = link.find('a', {'class': 's-item__link'}).get('href')
        #                 request["SNR_Title"] = link.find('h3', {'class': 's-item__title'}).text
        #                 request["SNR_Description"] = "Visit site to see description"
        #                 request["SNR_Price"] = float(link.find('span', {'class': 's-item__price'}).text[1:])
        #                 request["SNR_CustomerReviews"] = 0.0
        #                 request["SNR_PriceBefore"] = -1
        #
        #                 request["SNR_Category"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
        #                 request["SNR_Available"] = "Ebay"
        #
        #                 request["SNR_ModelNo"] = "00"
        #                 request["SNR_UPC"] = "00"
        #
        #                 request["SNR_SubCategory"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
        #                 request["SNR_Condition"] = "00"
        #                 img = link.find('img').get('src')
        #                 if 'gif' in img:
        #                     img = link.find('img').get('data-src')
        #
        #                 request["SNR_ImageURL"] = img
        #
        #
        #                 itemss.append(request)
        #
        #             except:
        #                 continue
        #
        #         res = {"data": itemss, "status": True}
        #
        #
        #         # # printsetting cache for " + cache_key
        #
        #         return Response(res)
        #     except:
        #         pass
        # except:
            try:
                page = int(request.GET.get('page'))
                if page < 1:
                    page = 1

            except:
                page = 1
            limit = page * int(items)
            offset = (page - 1) * int(items)
            query = str(que).replace("\'", "")
            query = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in query.split("\n")]
            print('>>>>>>>>>>>>>>>>>>>>>>>', query)
            temp=[]
            try:
                if  int(request.GET.get('low'))!=-1 & int(request.GET.get('high'))!=-1 :
                    minprice=int(request.GET.get('low'))
                    maxprice=int(request.GET.get('high'))
                    main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(\'' + str(
                        query[0]) + '\') AND "SNR_Price" BETWEEN '+str(minprice)+' AND '+str(maxprice)+' OFFSET ' + str(
                        offset) + ' LIMIT ' + str(limit)
                    print('in')
        #             url = 'https://www.ebay.com/sch/i.html?_nkw=' + query +'&&_udlo='+str(minprice)+'&_udhi='+str(maxprice)
                else:
                    main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(\'' + str(
                        query[0]) + '\') OFFSET ' + str(
                        offset) + ' LIMIT ' + str(limit)
        #
            except:
                minprice=-1
                maxprice=-1
                main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(\''+str(query[0])+'\') OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
            fields = ["id",
                      "SNR_Title", "SNR_Brand", "SNR_Available",
                      "SNR_ProductURL", "SNR_ImageURL",
                      "SNR_Description",
                      "SNR_Condition", "SNR_Price", "SNR_PriceBefore", "SNR_CustomerReviews"

                      ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out))
            f_count = len(fields)
            count=0
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]
                        current_item['index']=count
                    count=count+1
                    temp.append(current_item)
            connection.close()
            if len(temp) == 0:
                print(query)
                try:
                    if  int(request.GET.get('low'))!=-1 & int(request.GET.get('high'))!=-1 :
                        minprice=int(request.GET.get('low'))
                        maxprice=int(request.GET.get('high'))
                        url = 'https://www.ebay.com/sch/i.html?_nkw=' + query[0] +'&&_udlo='+str(minprice)+'&_udhi='+str(maxprice)
                    else:
                        url = 'https://www.ebay.com/sch/i.html?_nkw=' + query[0]

                except:
                    minprice=-1
                    maxprice=-1
                    url = 'https://www.ebay.com/sch/i.html?_nkw=' + query[0]

                try:
                    source = requests.get(url)
                    plain_text = source.text
                    soup = BeautifulSoup(plain_text, "html.parser")
                    print(soup)
                    itemss = []
                    count=0
                    cat = soup.find('ul', {'class': 'srp-refine__category__list'})
                    for link in soup.findAll('li', {'class': 's-item'}):
                        # # print link
                        request = {}
                        try:
                            request["SNR_ProductURL"] = link.find('a', {'class': 's-item__link'}).get('href')
                            request["SNR_Title"] = link.find('h3', {'class': 's-item__title'}).text
                            request["SNR_Description"] = "Visit site to see description"
                            request["SNR_Price"] = float(link.find('span', {'class': 's-item__price'}).text[1:])
                            request["SNR_CustomerReviews"] = 0.0
                            request["SNR_PriceBefore"] = -1

                            request["SNR_Category"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                            request["SNR_Available"] = "ebay"

                            request["SNR_ModelNo"] = "00"
                            request["SNR_UPC"] = "00"

                            request["SNR_SubCategory"] = cat.findNext('li', {'class': 'srp-refine__category__item'}).text[15:50]
                            request["SNR_Condition"] = "00"
                            img = link.find('img').get('src')
                            if 'gif' in img:
                                img = link.find('img').get('data-src')

                            request["SNR_ImageURL"] = img
                            request["index"]=count

                            itemss.append(request)
                        except:
                            continue
                        count = count + 1

                    res = {"data1": itemss, "statuss": True,"soup":soup.text}
                    return Response(res, status.HTTP_200_OK)
                except:
                    pass
            res = {
                'data': temp,
            }

            return Response(res, status.HTTP_200_OK)
            # print('in')
            # return Response(status.HTTP_200_OK)

    if request.method == 'POST':
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        limit = page * int(items)
        offset = (page - 1) * int(items)
        query=str(que).replace("\'","")
        print('>>>>>>>>>>>>>>>>>>>>>>>',query)
        query="'"+query+"'"
        ls=''
        dic=request.data
        if dic['minprice'] != -1 and dic['maxprice'] != -1:
            ls = ls + ' AND "SNR_Price" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                request.data['maxprice'])
        if dic['merchant'] != 'undefine':
            ls =ls +' And "SNR_Available"=\'' +str(request.data['merchant'])+'\''
        if dic['sort'] !='undefine':
            if dic['sort'] =='ASC':
                ls = ls + ' ORDER by "SNR_Price" ASC'
            elif dic['sort'] =='DESC':
                ls = ls + ' ORDER by "SNR_Price" DESC'
        main_data_query = 'Select {0} from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery({1}) {2} OFFSET '+str(offset)+' LIMIT '+str(limit)
        fields = ["id",
                  "SNR_Title","SNR_Brand","SNR_Available",
                  "SNR_ProductURL", "SNR_ImageURL",
                  "SNR_Description",
                  "SNR_Condition","SNR_Price", "SNR_PriceBefore", "SNR_CustomerReviews"

                  ]
        out = ['"{0}"'.format(i) for i in fields]
        print("out", out)
        temp = []
        extra_fields = []
        fields.extend(extra_fields)
        print("extra fields", extra_fields)
        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])
        # te=' AND "SNR_Price" BETWEEN 0 AND 100'
        data_query = main_data_query.format(",".join(out), query,ls)
        print(data_query)
        f_count = len(fields)
        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)
        connection.close()
        # cats = []
        # query_data1 = 'SELECT DISTINCT "SNR_Available" from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(' + str(
        #     query) + ') AND "SNR_Available" IS NOT NULL ORDER BY "SNR_Available" ASC'
        # query_data = 'SELECT COUNT(*),MIN("SNR_Price"),MAX("SNR_Price") from public.products_allproductspartition  where  "tsv_title" @@ plainto_tsquery(' + str(
        #     query) + ')'
        #
        # with connection.cursor() as cursor:
        #     cursor.execute(query_data)
        #     dic = {}
        #     for i in cursor.fetchall():
        #         dic = {'count': i[0], 'MinPrice': i[1], 'Maxprice': i[2]}
        #         # dic+=dic
        # with connection.cursor() as cursor:
        #     cursor.execute(query_data1)
        #     for i in cursor.fetchall():
        #         cats.append(i[0])
        #     print(cats)
        res = {
            # "result": dic,
            # "other": cats,
            'data':temp
        }

        return Response(res,status.HTTP_200_OK)


