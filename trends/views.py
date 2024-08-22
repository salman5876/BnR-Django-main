from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from . models import Trends
from . serializer import TrendsSerializer
# import bestbuy
# import walmart
from django.views.decorators.csrf import ensure_csrf_cookie
# import ebay
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q



@api_view(['DELETE'])
def delete(self):

    snippet = objects.all()
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def getTrend(request):
    try:
        # Mobile_all = Mobile_DB.objects.filter(que)
        Trend = Trends.objects.all()
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass





@api_view(['GET'])
def getTrendMobile(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass








@api_view(['GET'])
def getTrendLaptop(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass





@api_view(['GET'])
def getTrendWearable(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass



@api_view(['GET'])
def getTrendmovies(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass


@api_view(['GET'])
def getTrendtoy(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass


@api_view(['GET'])
def getTrendcam(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass





@api_view(['GET'])
def getTrendaudio(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass









@api_view(['GET'])
def getTrendTV(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass








@api_view(['GET'])
def getTrendcar(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass



@api_view(['GET'])
def CountAll(request):
    try:
        que = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="car") | Q(SNR_Category__icontains="elec"))
        queL = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="laptop") )
        queM = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="mobile") )
        queW = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="wearable") )
        queA = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="audio") )
        queG = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="game") )
        queMo = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="movie") )
        queTO = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="toys") )
        queT = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="tv") )
        queC = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="cam"))
        queAp = Q(SNR_Type__icontains="Trending") & (Q(SNR_Category__icontains="appliance"))

        LaptopCount = Trends.objects.filter(queL).count()
        MobileCount = Trends.objects.filter(queM).count()
        WearableCount = Trends.objects.filter(queW).count()
        ApplincesCount = Trends.objects.filter(queAp).count()
        videogamesCount = Trends.objects.filter(queG).count()
        audioCount = Trends.objects.filter(queA).count()
        moviesCount = Trends.objects.filter(queMo).count()
        CarsElecCount = Trends.objects.filter(que).count()

        toysCount =Trends.objects.filter(queTO).count()
        TVCount = Trends.objects.filter(queT).count()
        CamsCount = Trends.objects.filter(queC).count()
        All=Trends.objects.all().count()


    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        # serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response({'laptop':LaptopCount,
                         'mobile':MobileCount,'wearable':WearableCount,'appliances':ApplincesCount,
                 'videogames':videogamesCount,'audio':audioCount,'movies':moviesCount,
                         'carselectronic':CarsElecCount,  'toys':toysCount,'tv':TVCount,
                         'cams':CamsCount,'All':All
                         })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



from django.core.cache import cache


@api_view(['GET'])
def getTrendgame(request):
    cache_key = 'trending'
    cache_time = 86200  # time to live in seconds
    result = cache.get(cache_key)

    if not result:



        try:

            # Mobile_all = Mobile_DB.objects.filter(que)
            Trend = Trends.objects.all().order_by('-SNR_Date')
            paginator = Paginator(Trend, 12)
            page = request.GET.get('page')
            try:

                users = paginator.page(page)
            except PageNotAnInteger:

                users = paginator.page(1)
            except EmptyPage:

                users = paginator.page(paginator.num_pages)

            serializer_context = {'request': request}
            serializer = TrendsSerializer(users, many=True, context=serializer_context)
            # res = serializer.data
            # res.update('pagescount:', paginator.num_pages)
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

            result = res;
            cache.set(cache_key, result, cache_time)
            print ("setting cache" + cache_key)

            return Response(res)

        except Trends.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    else:
            print ("returning from cache" + cache_key)
            return Response(result)



@api_view(['GET'])
def getTrendappliance(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass





@api_view(['GET'])
def popular(request):
    try:
        Trend = Trends.objects.all().order_by('-SNR_Date')
        paginator = Paginator(Trend, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TrendsSerializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pagescount:', paginator.num_pages)
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

    except Trends.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = TrendsSerializer(Trend, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass


@ensure_csrf_cookie
@api_view(['POST'])
def setTrend(request):

    if request.method == 'POST':

        serializer = TrendsSerializer(data=request.data)
        print(serializer)




        if serializer.is_valid():

            # print(serializer.validated_data)

           # serializer.save()

            requestdata = serializer.validated_data

            best = bestbuy.BestbuyAPI()
            best.AllCategoriesTrend(requestdata)

            wallmartapi=walmart.WallmartAPI();
            wallmartapi.trending(requestdata);


            ebaay=ebay.EbayAPI()
            ebaay.AddTrend(requestdata)







            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def setPopular(request):

    if request.method == 'POST':

        serializer = TrendsSerializer(data=request.data)
        print(serializer)




        if serializer.is_valid():

            # print(serializer.validated_data)

           # serializer.save()

            requestdata = serializer.validated_data



            best=bestbuy.BestbuyAPI()
            best.PopularMobiles(requestdata)
            best.Popularlaptops(requestdata)

            ebaay=ebay.EbayAPI()
            ebaay.AddTrend(requestdata)




        #     #query=mydata["SNR_Name"]+' '+mydata["SNR_Model"]+' '+mydata["SNR_RAM"]
        #     #
        #
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

