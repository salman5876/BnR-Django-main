from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .models import Wearable_DB
from .serializers import Wearable_Serializer
from . import ebay
from . import walmart
from . import best
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# import groupon
# import amazon
# Create your views here.



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




       products = Wearable_DB.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Wearable_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Wearable_Serializer.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

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




       products = Wearable_DB.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Wearable_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Wearable_Serializer.DoesNotExist:

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




       products = Wearable_DB.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Wearable_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Wearable_Serializer.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['DELETE'])
def deleteAmazon(self):

    snippet = Wearable_DB.objects.all()
    # snippet = Wearable_DB.objects.filter(SNR_Available__icontains='Best Buy')
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



from django.db.models import F, Func, Value




@api_view(['GET'])
def filterWearables(request,query):
    try:

        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que)
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass



@api_view(['GET'])
def filterWearableswithprice(request,query,price1,price2):
    try:

        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        wearabledata_all = Wearable_DB.objects.filter(que)
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator.num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass






@api_view(['GET'])
def filterWearablesbybrands(request,query):
    try:

        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que)
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass




@api_view(['GET'])
def Wearablesbyprice(request,p1,p2):
    try:

        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        wearabledata_all = Wearable_DB.objects.filter(que)
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass






@api_view(['GET'])
def WearablesbypriceASC(request,p1,p2):
    try:

        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        wearabledata_all = Wearable_DB.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass



@api_view(['GET'])
def WearablesbypriceDESC(request,p1,p2):
    try:

        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        wearabledata_all = Wearable_DB.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass



@api_view(['GET'])
def filterWearablesDESC(request,query):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que).order_by("-SNR_Date","-SNR_Price")
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass



@api_view(['GET'])
def filterWearablesDESCwithprice(request,query,price1,price2):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        wearabledata_all = Wearable_DB.objects.filter(que).order_by("-SNR_Date","-SNR_Price")
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass


@api_view(['GET'])
def filterWearablesASC(request,query):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass





@api_view(['GET'])
def filterWearablesASCwithprice(request,query,price1,price2):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        wearabledata_all = Wearable_DB.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass











@api_view(['GET'])
def filterWearablesbybrandsDESC(request,query):
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que).order_by("-SNR_Price")
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    pass


@api_view(['GET'])
def filterWearablesbybrandsASC(request,query):
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass







@api_view(['GET'])
def getAllWearablesModels(request):
    try:
        Wearable_DB.objects.filter(SNR_Title__icontains='?').update(
            description=Func(
                F('SNR_Title'),
                Value('?'), Value(''),
                function='replace',
            )
        )

        wearabledata_all = Wearable_DB.objects.exclude(SNR_Available__icontains="Ebay")

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Wearable_Serializer(wearabledata_all,
                                         many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getAll_Wearables(request):
    try:
        wearabledata_all = Wearable_DB.objects.all()
        paginator = Paginator(wearabledata_all, 21)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator.count()
        pages = paginator.num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

@api_view(['GET'])
def getAll_WearablesDESC(request):
    try:
        wearabledata_all = Wearable_DB.objects.all().order_by('-SNR_Price')
        paginator = Paginator(wearabledata_all, 21)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

@api_view(['GET'])
def getAll_WearablesASC(request):
    try:
        wearabledata_all = Wearable_DB.objects.all().order_by('SNR_Price')
        paginator = Paginator(wearabledata_all, 21)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

######################################333
from django.conf import settings
# client = settings.ES_CLIENT
import json
from django.http import HttpResponse

@ensure_csrf_cookie
@api_view(['POST'])
def add_Wearables(request):
    print (request.data)

    if request.method == 'POST':

        serializer = Wearable_Serializer(data=request.data)
        #print(serializer)


        if serializer.is_valid():
            print("inserilier")


            #serializer.save()
            requestdata = serializer.validated_data


            walmart.wearable_Walmart(requestdata)
            bestapi=best.BestbuyAPI()
            bestapi.Wearables(requestdata)
            #
            group=groupon.GroupOnAPI()
            group.groupWearable(requestdata)
            #


            ebayapi = ebay.EbayAPI()
            ebayapi.ebayWearables(requestdata)

            ebayapi.ebayWearableAll(requestdata)

            amz=amazon.AmazonAPI()
            amz.amazonWatches(requestdata)




            #
            #
            #

            # walmart.wearable_Walmart(requestdata)



            #
            # bestapi.search(requestdata)
            # walmart.wearable_Walmart()
            # wallapi=wallmart.WallmartAPI()
            # wallapi.search(requestdata)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def getModelsBestbuy(request):

    Laptop_all = Wearable_DB.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Wearable_Serializer(data, many=True, context=serializer_context)
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

    Laptop_all = Wearable_DB.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Wearable_Serializer(data, many=True, context=serializer_context)
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

    Laptop_all = Wearable_DB.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 20000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Wearable_Serializer(data, many=True, context=serializer_context)
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
