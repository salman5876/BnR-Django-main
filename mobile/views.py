from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from . models import Mobile_DB
from . serializer import Mobile_Serializer
from . import best
from django.views.decorators.csrf import ensure_csrf_cookie
from . import ebay, ATnT, walmart, groupon, newegg
# import ebay
# import ATnT
# import walmart
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import groupon
# import amazon
# import newegg
def index(request):
    return HttpResponse("<h1>Something NOT WELL</h1>")




#######################Filter Mobiles

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




       products = Mobile_DB.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Mobile_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterAllProductsASC(request,query,price1,price2,brand,merchant):



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




       products = Mobile_DB.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Mobile_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


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




       products = Mobile_DB.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Mobile_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['DELETE'])
def deleteAmazon(self):

    snippet = Mobile_DB.objects.all()
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def Filter_Mobiles(request,query):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que)
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass



@api_view(['GET'])
def Filter_Mobileswithprice(request,query,price1,price2):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)
       que &= Q(SNR_Price__range=(price1, price2))

       Mobile_all = Mobile_DB.objects.filter(que)
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator.num_pages
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass




@api_view(['GET'])
def Filter_Mobilesbybrands(request,query):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que |= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_Brand__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que)
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass




@api_view(['GET'])
def Filter_MobilesbybrandsASC(request,query):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que |= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_Brand__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass




@api_view(['GET'])
def Filter_MobilesbybrandsDESC(request,query):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que |= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_Brand__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass






@api_view(['GET'])
def Mobilesbyrange(request,p1,p2):

   try:
       que = Q()
       que = Q(SNR_Price__range=(p1,p2))
       Mobile_all = Mobile_DB.objects.filter(que)
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass







@api_view(['GET'])
def MobilesbyrangeASC(request,p1,p2):

   try:
       que = Q()
       que = Q(SNR_Price__range=(p1,p2))
       Mobile_all = Mobile_DB.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass



@api_view(['GET'])
def MobilesbyrangeDESC(request,p1,p2):

   try:
       que = Q()
       que = Q(SNR_Price__range=(p1,p2))
       Mobile_all = Mobile_DB.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass


#######################Filter Mobiles
@api_view(['GET'])
def Filter_MobilesDESC(request,query):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass



#######################Filter Mobiles
@api_view(['GET'])
def Filter_MobilesDESCwithprice(request,query,price1,price2):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)
       que &= Q(SNR_Price__range=(price1, price2))

       Mobile_all = Mobile_DB.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass



#######################Filter Mobiles
@api_view(['GET'])
def Filter_MobilesASC(request,query):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass

#######################Filter Mobiles
@api_view(['GET'])
def Filter_MobilesASCwithprice(request,query,price1,price2):

   print(query)
   try:
       que = Q()
       for word in query.split():
           que &= Q(SNR_Title__icontains=word)

       que |=  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)
       que &= Q(SNR_Price__range=(price1, price2))

       Mobile_all = Mobile_DB.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator.num_pages
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass


#######################View all mobiles
@api_view(['GET'])
@permission_classes([AllowAny])
def getAll_Mobiles(request):
    try:

        Mobile_all = Mobile_DB.objects.all()
        paginator = Paginator(Mobile_all, 21)

        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
            users = paginator.page(paginator.num_pages)
        serializer_context = {'request': request}
        serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def getAll_MobilesASC(request):
    try:

        Mobile_all = Mobile_DB.objects.all().order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 21)

        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
            users = paginator.page(paginator.num_pages)
        serializer_context = {'request': request}
        serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator._count
        pages=paginator._get_num_pages()
        res={
    'totalItems':items,
    'totalPages':pages,
    'results': serializer.data
}

        return Response(res)

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getAll_MobilesDESC(request):
    try:

        Mobile_all = Mobile_DB.objects.all().order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 21)

        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
            users = paginator.page(paginator.num_pages)
        serializer_context = {'request': request}
        serializer = Mobile_Serializer(users,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator._count
        pages=paginator._get_num_pages()
        res={
    'totalItems':items,
    'totalPages':pages,
    'results': serializer.data
}

        return Response(res)

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


#######################View all mobiles
@api_view(['GET'])
def getModels(request):
    try:


        Mobile_all = Mobile_DB.objects.filter(SNR_Available__icontains="Best Buy")

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

######### Adding new Mobiles

@ensure_csrf_cookie
@api_view(['POST'])
def add_Mobiles(request):

    if request.method == 'POST':

        serializer = Mobile_Serializer(data=request.data)
        print(serializer)


        if serializer.is_valid():
            print("inserilier")

            #serializer.save()
            requestdata = serializer.validated_data

            #
            listCatagories = ['3944_542371_1127173','3944_542371_1073085','3944_542371_1045119','3944_542371_1056206','3944_542371_133261','3944_542371_1072335','3944_542371_1163447','3944_542371_133161']
            for category in listCatagories:
                walmart.mobile_Walmart(requestdata,category)


            # bestapi.search(requestdata)

            # amz = amazon.AmazonAPI()
            # amz.amazonMobile(requestdata)
            #
            ebay.EbayAPI.ebayMobilesAll(requestdata)

            bestapi = best.bestAPI()
            bestapi.getMobile(requestdata)

            atnt= ATnT.ATNT()
            atnt.getAllMobile(requestdata)
            # #
            neww=newegg.newEggAPI()
            neww.newEggMobiles(requestdata)

            group= groupon.GroupOnAPI()
            group.groupPhones(requestdata)

            ebay.EbayAPI.ebayMobiles(requestdata)




            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getModelsebay(request):

    Laptop_all = Mobile_DB.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Mobile_Serializer(data, many=True, context=serializer_context)
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
def getModelsebestbuy(request):

    Laptop_all = Mobile_DB.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Mobile_Serializer(data, many=True, context=serializer_context)
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

    Laptop_all = Mobile_DB.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Mobile_Serializer(data, many=True, context=serializer_context)
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
