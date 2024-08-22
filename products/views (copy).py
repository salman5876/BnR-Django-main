from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response  # to send specific response
from rest_framework import status
from .models import TV, Cams, CarsElectronics, VideoGames, Toys, SmartHomes, Audio, \
    Books, ComputerSoftware, Applinces, Movies, OfficeSupply, HealthandFitness, ElectronicGadgets, SportingGoods, \
    Furniture, Jewelry, HomeandGarden, FlowerandPlants, \
    Clothing, Arts, AllProducts, DailyDeals, Product_Reviews

from .serializers import TV_Serializer, Cams_Serializer, CarsElec_Serializer, VideoGames_Serializer, \
    Toys_Serializer, Smarthomes_Serializer, Audio_Serializer, Software_Serializer, Applinces_Serializer, \
    Movies_Serializer, Office_Serializer, Health_Serializer, ElectronicsGadgets_Serializer, Books_Serializer, \
    Sports_Serializer, Furniture_Serializer, \
    Jewelry_Serializer, HomeandGarden_Serializer, Flowers_Serializer, Clothes_Serializer, Arts_Serializer, \
    AllProducts_Serializer, DailyDeals_Serializer, DailyDealsCategories_Serializer, DailyDealsBrands_Serializer, \
    ProductReview_Serializer
import walmart
import ebay
import best
import groupon
import math
from django.db import connection
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import amazon
import newsegg


@api_view(['DELETE'])
def deleteAmazon(self):
    snippet = DailyDeals.objects.all()
    snippet.delete()
    #
    # snippet = TV.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    #
    # snippet = SmartHomes.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = HealthandFitness.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = OfficeSupply.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = Applinces.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = VideoGames.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = ComputerSoftware.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    #
    # snippet = Cams.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = CarsElectronics.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = Toys.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    # snippet = Audio.objects.filter(SNR_Available__icontains="Amazon")
    # snippet.delete()
    #
    #




    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def deleteGame(self):
    snippet = VideoGames.objects.filter(SNR_Available__icontains="Best Buy")
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def Filter_Appliences(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Applinces.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Applienceswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Applinces.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Appliencesbybyrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Applinces.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesbyrangeDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Applinces.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesbyrangeASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Applinces.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Appliencesbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Applinces.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def TVbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = TV.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Gadgetsbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = ElectronicGadgets.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Smarthomebyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = SmartHomes.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Booksbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Books.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Jewelrybyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Jewelry.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Healthbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = HealthandFitness.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Officebyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = OfficeSupply.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Sportsbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = SportingGoods.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Homeandgardenbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = HomeandGarden.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Artsbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Arts.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Clothesbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Clothing.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Flowersbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = FlowerandPlants.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Furniturebyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Furniture.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Moviesbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Movies.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Softwarebyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = ComputerSoftware.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Audiobyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Audio.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Toysbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Toys.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def videogamesbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = VideoGames.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Carsbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = CarsElectronics.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Camsbyrange(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Cams.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def AppliencesbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Applinces.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def TVbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = TV.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def GadgetsbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = ElectronicGadgets.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def SmarthomebyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = SmartHomes.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def BooksbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Books.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def JewelrybyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Jewelry.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def HealthbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = HealthandFitness.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def OfficebyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = OfficeSupply.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def SportsbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = SportingGoods.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def HomeandgardenbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = HomeandGarden.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ArtsbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Arts.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ClothesbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Clothing.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def FlowersbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def FurniturebyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Furniture.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def MoviesbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Movies.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def SoftwarebyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = ComputerSoftware.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def AudiobyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Audio.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ToysbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Toys.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def videogamesbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = VideoGames.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def CarsbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = CarsElectronics.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def CamsbyrangeASC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Cams.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def AppliencesbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Applinces.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def TVbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = TV.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def GadgetsbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = ElectronicGadgets.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def SmarthomebyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = SmartHomes.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def BooksbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Books.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def JewelrybyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Jewelry.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def HealthbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = HealthandFitness.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def OfficebyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = OfficeSupply.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def SportsbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = SportingGoods.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def HomeandgardenbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = HomeandGarden.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ArtsbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Arts.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ClothesbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Clothing.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def FlowersbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def FurniturebyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Furniture.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def MoviesbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Movies.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def SoftwarebyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = ComputerSoftware.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def AudiobyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Audio.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ToysbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Toys.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def videogamesbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = VideoGames.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def CarsbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = CarsElectronics.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def CamsbyrangeDESC(request, p1, p2):
    try:
        que = Q()
        que = Q(SNR_Price__range=(p1, p2))

        Mobile_all = Cams.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Books(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Books.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Bookswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Books.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_BooksBYbrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Books.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Sports(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = SportingGoods.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Sportswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = SportingGoods.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Sportsbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = SportingGoods.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Furniture(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Furniture.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Furniturewithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Furniture.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Furniturebybrad(request, query):
    print(query)
    try:
        que = Q()

        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        Mobile_all = Furniture.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Arts(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Arts.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Artswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Arts.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Artsbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Arts.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Flowerbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = FlowerandPlants.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Flower(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = FlowerandPlants.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Flowerwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = FlowerandPlants.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Clothewithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Clothing.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Clothe(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Clothing.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Clothebybrand(request, query):
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Clothing.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGarden(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = HomeandGarden.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = HomeandGarden.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = HomeandGarden.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Jewelry(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Jewelry.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Jewelrywithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Jewelry.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Jewelrybybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        Mobile_all = Jewelry.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_BooksDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Books.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_BooksDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Books.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_BooksbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Books.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_SportsDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = SportingGoods.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_SportsDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = SportingGoods.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_SportsbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = SportingGoods.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FurnitureDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Furniture.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FurnitureDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Furniture.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FurniturebybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Furniture.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ArtsDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Arts.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ArtsDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Arts.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ArtsbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Arts.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FlowerDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FlowerDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FlowerbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ClotheDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Clothing.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ClotheDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Clothing.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ClothebybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Clothing.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = HomeandGarden.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = HomeandGarden.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = HomeandGarden.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_JewelryDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Jewelry.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_JewelryDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Jewelry.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_JewelrybybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Jewelry.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_BooksASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Books.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_BooksASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Books.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_BooksbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Books.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_SportsASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = SportingGoods.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_SportsASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = SportingGoods.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_SportsbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = SportingGoods.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FurnitureASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Furniture.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FurnitureASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Furniture.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FurniturebybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Furniture.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ArtsASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Arts.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ArtsASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Arts.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ArtsbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Arts.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FlowerASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FlowerASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_FlowerbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = FlowerandPlants.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ClotheASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Clothing.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ClotheASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Clothing.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_ClothebybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Clothing.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = HomeandGarden.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = HomeandGarden.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HomeandGardenbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = HomeandGarden.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_JewelryASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = Jewelry.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_JewelryASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Jewelry.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_JewelrybybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Jewelry.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Health(request, query):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        Mobile_all = HealthandFitness.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Healthwithprice(request, query, price1, price2):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = HealthandFitness.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Healthbybrand(request, query):
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = HealthandFitness.objects.filter(que)
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HealthASC(request, query):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        Mobile_all = HealthandFitness.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HealthASCwithprice(request, query, price1, price2):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = HealthandFitness.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HealthbybrandASC(request, query):
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = HealthandFitness.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesASC(request, query):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        Mobile_all = Applinces.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesASCwithprice(request, query, price1, price2):
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Applinces.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesbybrandASC(request, query):
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        Mobile_all = Applinces.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_GadgetsbybrandASC(request, query):
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = ElectronicGadgets.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        Mobile_all = Applinces.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = Applinces.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HealthDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        Mobile_all = HealthandFitness.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HealthDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = HealthandFitness.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_HealthbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        Mobile_all = HealthandFitness.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(record, many=True, context=serializer_context)
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


    except HealthandFitness.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogames(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = VideoGames.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogameswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = VideoGames.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = VideoGames.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = VideoGames.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = VideoGames.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = VideoGames.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = VideoGames.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = VideoGames.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_GadgetsDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = ElectronicGadgets.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_GadgetsbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = ElectronicGadgets.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audio(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Audio.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audiowithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = Audio.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audiobybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = Audio.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audioASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Audio.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audioASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = Audio.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audiobybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = Audio.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audiobybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = Audio.objects.filter(que).order_by('-SNR_Price', "-SNR_Date")
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audioDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        data = Audio.objects.filter(que).order_by('-SNR_Price', "-SNR_Date")
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_cams(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Cams.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = Cams.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camsbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = Cams.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camsASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Cams.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camsbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = Cams.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camsDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Cams.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camsbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = Cams.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthome(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = SmartHomes.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomewithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = SmartHomes.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomebybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = SmartHomes.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomeASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = SmartHomes.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomeASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = SmartHomes.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomebybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = SmartHomes.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomeDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = SmartHomes.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomebybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = SmartHomes.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronics(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = CarsElectronics.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = CarsElectronics.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicsbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)

        data = CarsElectronics.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicsASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = CarsElectronics.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicsbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = CarsElectronics.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicsDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = CarsElectronics.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camsASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = Cams.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_moviesASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))
        data = Movies.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Applinces.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicsASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = CarsElectronics.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = VideoGames.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_AppliencesDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        Mobile_all = Applinces.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(record, many=True, context=serializer_context)
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


    except Applinces.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_videogamesDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = VideoGames.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(record, many=True, context=serializer_context)
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


    except VideoGames.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_audioDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        data = Audio.objects.filter(que).order_by('-SNR_Price', "-SNR_Date")
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(record, many=True, context=serializer_context)
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


    except Audio.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = TV.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toysDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = Toys.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwareDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = ComputerSoftware.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officeDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = OfficeSupply.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_smarthomeDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = SmartHomes.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
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


    except SmartHomes.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_camsDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = Cams.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(record, many=True, context=serializer_context)
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


    except Cams.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_moviesDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = Movies.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicsDESCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = CarsElectronics.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_carselectronicsbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = CarsElectronics.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(record, many=True, context=serializer_context)
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


    except CarsElectronics.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_movies(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Movies.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_movieswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = Movies.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_moviesbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = Movies.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_moviesASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Movies.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_moviesbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = Movies.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_moviesDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Movies.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_moviesbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = Movies.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(record, many=True, context=serializer_context)
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


    except Movies.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_software(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = ComputerSoftware.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwarewithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = ComputerSoftware.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwarebybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = ComputerSoftware.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwareASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = ComputerSoftware.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwareASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = ComputerSoftware.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwarebybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = ComputerSoftware.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwareDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = ComputerSoftware.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_softwarebybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = ComputerSoftware.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(record, many=True, context=serializer_context)
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


    except ComputerSoftware.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_office(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = OfficeSupply.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officewithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = OfficeSupply.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officebybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = OfficeSupply.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officeASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = OfficeSupply.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officeASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = OfficeSupply.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officebybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = OfficeSupply.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officeDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = OfficeSupply.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_officebybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = OfficeSupply.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(record, many=True, context=serializer_context)
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


    except OfficeSupply.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toyswithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = Toys.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toys(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        data = Toys.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toysbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = Toys.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toysASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Toys.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toysASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = Toys.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toysbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = Toys.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toysDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = Toys.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_toysbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = Toys.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(record, many=True, context=serializer_context)
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


    except Toys.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tv(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = TV.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

        que &= Q(SNR_Price__range=(price1, price2))

        data = TV.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = TV.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Gadgets(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = ElectronicGadgets.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except ElectronicGadgets.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Gadgetsbybrand(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = ElectronicGadgets.objects.filter(que)
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(record, many=True, context=serializer_context)
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


    except ElectronicGadgets.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = TV.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvASCwithprice(request, query, price1, price2):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        que &= Q(SNR_Price__range=(price1, price2))

        data = TV.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvbybrandASC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = TV.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que &= Q(SNR_Title__icontains=word)

        que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
        data = TV.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_tvbybrandDESC(request, query):
    print(query)
    try:
        que = Q()
        for word in query.split():
            que |= Q(SNR_Title__icontains=word)

        que |= Q(SNR_Brand__icontains=query)
        data = TV.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(data, 12)
        page = request.GET.get('page')
        try:

            record = paginator.page(page)
        except PageNotAnInteger:

            record = paginator.page(1)
        except EmptyPage:

            record = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(record, many=True, context=serializer_context)
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


    except TV.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getModelsOffice(request):
    try:

        data = OfficeSupply.objects.exclude(SNR_Available__icontains="Ebay")
    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Office_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsHealth(request):
    try:

        data = HealthandFitness.objects.exclude(SNR_Available__icontains="Ebay")
    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Health_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsApplinces(request):
    try:

        data = Applinces.objects.filter(SNR_Available__icontains="Best Buy")
    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Applinces_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsSoftware(request):
    try:

        data = ComputerSoftware.objects.filter(SNR_Available__icontains="Best Buy")
    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Software_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsSmarthome(request):
    try:

        data = SmartHomes.objects.exclude(SNR_Available__icontains="Ebay")
    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Smarthomes_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsToys(request):
    try:

        data = Toys.objects.exclude(SNR_Available__icontains="Ebay")
    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Toys_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsTV(request):
    try:

        data = TV.objects.filter(SNR_Available__icontains="Best Buy")
    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TV_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsCams(request):
    try:

        data = Cams.objects.filter(SNR_Available__icontains="Best Buy")
    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Cams_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsCarElec(request):
    try:

        data = CarsElectronics.objects.filter(SNR_Available__icontains="Best Buy")
    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarsElec_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsAudio(request):
    try:

        data = Audio.objects.filter(SNR_Available__icontains="Best Buy")
    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Applinces_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsMovies(request):
    try:

        data = Movies.objects.filter(SNR_Available__icontains="Best Buy")
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Movies_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsGames(request):
    try:

        data = VideoGames.objects.exclude(SNR_Available__icontains="Ebay")
    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoGames_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getAll_ArstASC(request):
    try:

        data_all = Arts.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ArstDESC(request):
    try:

        data_all = Arts.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Arst(request):
    try:

        data_all = Arts.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Arts_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Applinces(request):
    try:

        data_all = Applinces.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ClothesASC(request):
    try:

        data_all = Clothing.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ClothesDESC(request):
    try:

        data_all = Clothing.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Clothes(request):
    try:

        data_all = Clothing.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Clothes_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Flowers(request):
    try:

        data_all = FlowerandPlants.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_HomeandGraden(request):
    try:

        data_all = HomeandGarden.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Jewelry(request):
    try:

        data_all = Jewelry.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Furniture(request):
    try:

        data_all = Furniture.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_FlowersASC(request):
    try:

        data_all = FlowerandPlants.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_HomeandGradenASC(request):
    try:

        data_all = HomeandGarden.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_JewelryASC(request):
    try:

        data_all = Jewelry.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_FurnitureASC(request):
    try:

        data_all = Furniture.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_FlowersDESC(request):
    try:

        data_all = FlowerandPlants.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Flowers_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_HomeandGradenDESC(request):
    try:

        data_all = HomeandGarden.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = HomeandGarden_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_JewelryDESC(request):
    try:

        data_all = Jewelry.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Jewelry_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_FurnitureDESC(request):
    try:

        data_all = Furniture.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Furniture_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Sports(request):
    try:

        data_all = SportingGoods.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_SportsASC(request):
    try:

        data_all = SportingGoods.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_SportsDESC(request):
    try:

        data_all = SportingGoods.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Sports_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Health(request):
    try:

        data_all = HealthandFitness.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except HealthandFitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_OfficeItems(request):
    try:

        data_all = OfficeSupply.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Books(request):
    try:

        data_all = Books.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_BooksDESC(request):
    try:

        data_all = Books.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_BooksASC(request):
    try:

        data_all = Books.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Books_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Movies(request):
    try:

        data_all = Movies.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_software(request):
    try:

        data_all = ComputerSoftware.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Toys(request):
    try:

        data_all = Toys.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Audio(request):
    try:

        data_all = Audio.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Gadgets(request):
    try:

        data_all = ElectronicGadgets.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_SmartHomes(request):
    try:

        data_all = SmartHomes.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_CarsElectronics(request):
    try:

        data_all = CarsElectronics.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Cams(request):
    try:

        data_all = Cams.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_videoGames(request):
    try:

        data_all = VideoGames.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_TV(request):
    try:

        laptopdata_all = TV.objects.all()
        paginator = Paginator(laptopdata_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ApplincesASC(request):
    try:

        data_all = Applinces.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_OfficeItemsASC(request):
    try:

        data_all = OfficeSupply.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_HealthDESC(request):
    try:

        data_all = HealthandFitness.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except HealthandFitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_HealthASC(request):
    try:

        data_all = HealthandFitness.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except HealthandFitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_MoviesASC(request):
    try:

        data_all = Movies.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_softwareASC(request):
    try:

        data_all = ComputerSoftware.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ToysASC(request):
    try:

        data_all = Toys.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_AudioASC(request):
    try:

        data_all = Audio.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_SmartHomesASC(request):
    try:

        data_all = SmartHomes.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_GadgetsASC(request):
    try:

        data_all = ElectronicGadgets.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_CarsElectronicsASC(request):
    try:

        data_all = CarsElectronics.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_CamsASC(request):
    try:

        data_all = Cams.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_videoGamesASC(request):
    try:

        data_all = VideoGames.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_TVASC(request):
    try:

        laptopdata_all = TV.objects.all().order_by('SNR_Price')
        paginator = Paginator(laptopdata_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Products(request):
    try:

        laptopdata_all = AllProducts.objects.all().order_by("-SNR_Date")
        paginator = Paginator(laptopdata_all, 21)
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
        return Response(status=status.HTTP_404_NOT_FOUND)


import datetime


@api_view(['GET'])
def getAll_TodayDeals(request):
    try:

        data_all = DailyDeals.objects.filter(SNR_Date__date=datetime.date.today())
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = DailyDeals_Serializer(data, many=True, context=serializer_context)
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
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def filter_TodayDeals(request,query):
    try:
        que = Q()


        que &= Q(SNR_Date__date=datetime.date.today()) & Q(SNR_Category__icontains=query)

        data_all = DailyDeals.objects.filter(que)
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = DailyDeals_Serializer(data, many=True, context=serializer_context)
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
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def filter_TodayDeals(request,query):
    try:
        que = Q()


        que &= Q(SNR_Date__date=datetime.date.today()) & Q(SNR_Available__icontains=query)

        data_all = DailyDeals.objects.filter(que)
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = DailyDeals_Serializer(data, many=True, context=serializer_context)
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
        return Response(status=status.HTTP_404_NOT_FOUND)







@api_view(['GET'])
def FilterALLAppliencesASC(request,query,price1,price2,brand,merchant):

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




       products = Applinces.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Applinces_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLSportsASC(request,query,price1,price2,brand,merchant):

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




       products = SportingGoods.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Sports_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLHomeGardenASC(request,query,price1,price2,brand,merchant):

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




       products = HomeandGarden.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = HomeandGarden_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLJewelryASC(request,query,price1,price2,brand,merchant):

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




       products = Jewelry.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Jewelry_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLArtsASC(request,query,price1,price2,brand,merchant):

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




       products = Arts.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Arts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLClothesASC(request,query,price1,price2,brand,merchant):

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




       products = Clothing.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Clothes_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLFlowerASC(request,query,price1,price2,brand,merchant):

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




       products = FlowerandPlants.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Flowers_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLFurnitureASC(request,query,price1,price2,brand,merchant):

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




       products = Furniture.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Furniture_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLBooksASC(request,query,price1,price2,brand,merchant):

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




       products = Books.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Books_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLMoviesASC(request,query,price1,price2,brand,merchant):

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




       products = Movies.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Movies_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLSoftwareASC(request,query,price1,price2,brand,merchant):

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




       products = ComputerSoftware.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Software_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

@api_view(['GET'])
def FilterALLAudioASC(request,query,price1,price2,brand,merchant):

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




       products = Audio.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Audio_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLSmartHomeASC(request,query,price1,price2,brand,merchant):

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




       products = SmartHomes.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Smarthomes_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLToysASC(request,query,price1,price2,brand,merchant):

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




       products = Toys.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Toys_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLCarsElecASC(request,query,price1,price2,brand,merchant):

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




       products = CarsElectronics.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = CarsElec_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterCamsASC(request,query,price1,price2,brand,merchant):

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




       products = Cams.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Cams_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLGadgetsASC(request,query,price1,price2,brand,merchant):

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




       products = ElectronicGadgets.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLTVASC(request,query,price1,price2,brand,merchant):

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




       products = TV.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = TV_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLOfficeASC(request,query,price1,price2,brand,merchant):

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




       products = OfficeSupply.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Office_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass





@api_view(['GET'])
def FilterALLAppliences(request,query,price1,price2,brand,merchant):

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




       products = Applinces.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Applinces_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLSports(request,query,price1,price2,brand,merchant):

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




       products = SportingGoods.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Sports_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLHomeGarden(request,query,price1,price2,brand,merchant):

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




       products = HomeandGarden.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = HomeandGarden_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLJewelry(request,query,price1,price2,brand,merchant):

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




       products = Jewelry.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Jewelry_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLArts(request,query,price1,price2,brand,merchant):

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




       products = Arts.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Arts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLClothes(request,query,price1,price2,brand,merchant):

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




       products = Clothing.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Clothes_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLFlower(request,query,price1,price2,brand,merchant):

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




       products = FlowerandPlants.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Flowers_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLFurniture(request,query,price1,price2,brand,merchant):

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




       products = Furniture.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Furniture_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLBooks(request,query,price1,price2,brand,merchant):

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




       products = Books.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Books_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLMovies(request,query,price1,price2,brand,merchant):

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




       products = Movies.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Movies_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLSoftware(request,query,price1,price2,brand,merchant):

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




       products = ComputerSoftware.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Software_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

@api_view(['GET'])
def FilterALLAudio(request,query,price1,price2,brand,merchant):

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




       products = Audio.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Audio_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLSmartHome(request,query,price1,price2,brand,merchant):

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




       products = SmartHomes.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Smarthomes_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLToys(request,query,price1,price2,brand,merchant):

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




       products = Toys.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Toys_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLCarsElec(request,query,price1,price2,brand,merchant):

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




       products = CarsElectronics.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = CarsElec_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterCams(request,query,price1,price2,brand,merchant):

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




       products = Cams.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Cams_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLGadgets(request,query,price1,price2,brand,merchant):

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




       products = ElectronicGadgets.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLTV(request,query,price1,price2,brand,merchant):

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




       products = TV.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = TV_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLOffice(request,query,price1,price2,brand,merchant):

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




       products = OfficeSupply.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Office_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass








@api_view(['GET'])
def FilterALLAppliencesDESC(request,query,price1,price2,brand,merchant):

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




       products = Applinces.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Applinces_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLSportsDESC(request,query,price1,price2,brand,merchant):

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




       products = SportingGoods.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Sports_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLHomeGardenDESC(request,query,price1,price2,brand,merchant):

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




       products = HomeandGarden.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = HomeandGarden_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLJewelryDESC(request,query,price1,price2,brand,merchant):

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




       products = Jewelry.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Jewelry_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLArtsDESC(request,query,price1,price2,brand,merchant):

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




       products = Arts.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Arts_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLClothesDESC(request,query,price1,price2,brand,merchant):

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




       products = Clothing.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Clothes_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLFlowerDESC(request,query,price1,price2,brand,merchant):

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




       products = FlowerandPlants.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Flowers_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLFurnitureDESC(request,query,price1,price2,brand,merchant):

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




       products = Furniture.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Furniture_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLBooksDESC(request,query,price1,price2,brand,merchant):

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




       products = Books.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Books_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLMoviesDESC(request,query,price1,price2,brand,merchant):

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




       products = Movies.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Movies_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLSoftwareDESC(request,query,price1,price2,brand,merchant):

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




       products = ComputerSoftware.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Software_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

@api_view(['GET'])
def FilterALLAudioDESC(request,query,price1,price2,brand,merchant):

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




       products = Audio.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Audio_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLSmartHomeDESC(request,query,price1,price2,brand,merchant):

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




       products = SmartHomes.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Smarthomes_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLToysDESC(request,query,price1,price2,brand,merchant):

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




       products = Toys.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Toys_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass





@api_view(['GET'])
def FilterALLVideoDESC(request,query,price1,price2,brand,merchant):

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




       products = VideoGames.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = VideoGames_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLVideoASC(request,query,price1,price2,brand,merchant):

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




       products = VideoGames.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = VideoGames_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLVideo(request,query,price1,price2,brand,merchant):

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




       products = VideoGames.objects.filter(que)
       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = VideoGames_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLCarsElecDESC(request,query,price1,price2,brand,merchant):

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




       products = CarsElectronics.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = CarsElec_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterCamsDESC(request,query,price1,price2,brand,merchant):

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




       products = Cams.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Cams_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLGadgetsDESC(request,query,price1,price2,brand,merchant):

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




       products = ElectronicGadgets.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLTVDESC(request,query,price1,price2,brand,merchant):

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




       products = TV.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = TV_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass




@api_view(['GET'])
def FilterALLOfficeDESC(request,query,price1,price2,brand,merchant):

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




       products = OfficeSupply.objects.filter(que).order_by('-SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Office_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass





@api_view(['GET'])
def FilterALLHealthASC(request,query,price1,price2,brand,merchant):

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




       products = HealthandFitness.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Health_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass


@api_view(['GET'])
def FilterALLHealth(request,query,price1,price2,brand,merchant):

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




       products = HealthandFitness.objects.filter(que)

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Health_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def FilterALLHealthDESC(request,query,price1,price2,brand,merchant):

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




       products = HealthandFitness.objects.filter(que).order_by('SNR_Price')

       paginator = Paginator(products, 18)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       product_serilizer = Health_Serializer(data, many=True, context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': product_serilizer.data
        }
       return Response(res)


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass





####################################

@api_view(['GET'])
def getAll_HotDeals(request):
    try:

        data_all = DailyDeals.objects.filter(SNR_Date__date=datetime.date.today())
        todayDeals = DailyDeals.objects.filter(SNR_Date__gt=today)

        dealsWithPrices = todayDeals.filter(SNR_PriceAfter__gt=-2, SNR_PriceBefore__gt=-1)

        hotDeals = sorted(dealsWithPrices, key=lambda deal: (deal.SNR_PriceAfter / deal.SNR_PriceBefore))


        paginator = Paginator(hotDeals, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = DailyDeals_Serializer(data, many=True, context=serializer_context)
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
        return Response(status=status.HTTP_404_NOT_FOUND)


from django.db.models import Count


@api_view(['GET'])
def getAll_CatsDeals(request):
    try:
        data_all = DailyDeals.objects.filter(SNR_Date__date=datetime.date.today()).values('SNR_Category').distinct()
        paginator = Paginator(data_all, 25)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = DailyDealsCategories_Serializer(data, many=True, context=serializer_context)
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
        return Response(status=status.HTTP_404_NOT_FOUND)

# Create your tests here.
@api_view(['GET'])
def FilterProductsRevs(request,query):
    entry_per_page = 10
    join_statement = 'from products_allproducts INNER JOIN products_product_reviews ON products_allproducts.id = products_product_reviews."Product_id"'
    count_q = 'select count(*) %s Where {0}' % (join_statement)

    temp = []
    temp.append('tsv_title @@ plainto_tsquery(%s)')
    temp = " AND ".join(temp)

    res = {}
    count_q = count_q.format(temp)




    offset = ' ORDER BY products_allproducts."SNR_Date" DESC LIMIT {0}'.format(entry_per_page)

    fields = ["SNR_Title",
        "SNR_ProductURL", "SNR_Available",
              'SNR_Review_Title', 'SNR_Review_Author', "SNR_Review_Body", "SNR_Review_Stars", "SNR_Review_UP",
              "SNR_Review_Down"
    ]

    q = 'Select %s %s Where {0}' % (  'products_allproducts."id",' +",".join(
        ['"{0}"'.format(i) for i in fields]
    ),join_statement)

    left_fields = fields[:3]
    right_fields = fields[3:]
    left_count = len(left_fields)
    right_count = len(right_fields)

    with connection.cursor() as cursor:
        cursor.execute(count_q,[query])
        query_count = cursor.fetchone()[0]
        if query_count ==0:
            return Response(status=status.HTTP_404_NOT_FOUND)

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

        cursor.execute(q, [query])
        temp = {}
        for i in cursor.fetchall():
            current_id = i[0]
            i = i[1:]
            right_data = i[3:]

            review = {}

            for j in range(right_count):
                review[right_fields[j]] = right_data[j]

            try:
                temp[current_id]["Reviews"].append(review)
            except KeyError:
                left_data = i[:3]
                current_item = {}
                for j in range(left_count):
                    current_item[left_fields[j]] = left_data[j]

                current_item["Reviews"] = [review]

                temp[current_id] = current_item



        res["results"] = temp.itervalues()

        return Response(res)

@api_view(['GET'])
def CategoryAll(request,category):


   try:
       products = AllProducts.objects.filter(SNR_Category__iexact=category).order_by("-SNR_Date")

       paginator = Paginator(products, 18)


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

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass
# Create your tests here.
@api_view(['GET'])
def StoreAll(request,store):
    
   try:
       print(store)
       products = AllProducts.objects.filter(SNR_Available__iexact=store)
       paginator = Paginator(products, 18)
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

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

# Create your tests here.
@api_view(['GET'])
def CategoryAll_DESC(request,category):


   try:
       products = AllProducts.objects.filter(SNR_Category__iexact=category).order_by("-SNR_Price")

       paginator = Paginator(products, 18)


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

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

@api_view(['GET'])
def CategoryAll_ASC(request,category):


   try:
       products = AllProducts.objects.filter(SNR_Category__iexact=category).order_by("SNR_Price")

       paginator = Paginator(products, 18)


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

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
def getAll_BrandsDeals(request):
    try:
        data_all = DailyDeals.objects.filter(SNR_Date__date=datetime.date.today()).values('SNR_Available').distinct()
        paginator = Paginator(data_all, 25)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = DailyDealsBrands_Serializer(data, many=True, context=serializer_context)
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
        return Response(status=status.HTTP_404_NOT_FOUND)



from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from django.template.loader import get_template

from django.contrib.auth.models import User
import itertools
import datetime
today = datetime.date.today()

@api_view(['POST'])
def SendDeals(request):
    if request.method == 'POST':
        deals=DailyDeals.objects.filter(SNR_Date__date=datetime.date.today())[:4]
        values =(deals)
        todayDeals = DailyDeals.objects.filter(SNR_Date__gt=today)

        dealsWithPrices = todayDeals.filter(SNR_PriceAfter__gt=-2, SNR_PriceBefore__gt=-1)

        hotDeals = sorted(dealsWithPrices, key=lambda deal: (deal.SNR_PriceAfter / deal.SNR_PriceBefore))[:10]

        emails=User.objects.all()
        # to_list = ['amad.uddin@brainplow.com','amad.aud@gmail.com','tariq.farooq@brainplow.com','amad.aud@gmail.com','amad.uddin@brainplow.com','amad.aud@gmail.com','amad.uddin@brainplow.com','amad.aud@gmail.com','amad.uddin@brainplow.com','amad.aud@gmail.com',]
        to_list = ['amad.uddin@brainplow.com']
        # for email in emails:
        #     to_list.append(email.email)
        #
        # to_list = list(itertools.imap(lambda x: x.encode("utf-8"), to_list))

        # serializer = DailyDeals_Serializer(data=request.data)
        print to_list
        message = get_template('deals.html').render({'value':deals,'hotdeals':hotDeals})


        from_email = settings.EMAIL_HOST_USER
        email_obj = EmailMessage('Don\'t miss this opportunity ', message, from_email, to=to_list)
        email_obj.content_subtype = 'html'
        email_obj.send()

        # if serializer.is_valid():
        #
        #
        # subject = "Password recovery"
        # code = random.randint(1000,99999)*5;
        # serializer.validated_data['Code'] = code
        # secretkey = ''.join(
        #     random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
        #     range(75))
        #
        # serializer.validated_data['link']= 'http://www.shopnroar.com/reset/'+secretkey
        #
        # values={
        #     'link':serializer.validated_data['link'],
        #     'code': str(serializer.validated_data['Code'])
        # }

        # message = get_template('forgotpassword.html').render(values)


        # serializer.save()

        # to_list = [serializer.validated_data['email']]
        # from_email = settings.EMAIL_HOST_USER
        # email_obj= EmailMessage('Reset Password ',message,from_email, to=to_list)
        # email_obj.content_subtype='html'
        # email_obj.send()

        # except :
        #     #print "false"

        return Response("", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAll_Deals(request):
    try:

        data_all = DailyDeals.objects.all()
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = DailyDeals_Serializer(data, many=True, context=serializer_context)
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
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ApplincesDESC(request):
    try:

        data_all = Applinces.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_OfficeItemsDESC(request):
    try:

        data_all = OfficeSupply.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_MoviesDESC(request):
    try:

        data_all = Movies.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_softwareDESC(request):
    try:

        data_all = ComputerSoftware.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ToysDESC(request):
    try:

        data_all = Toys.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_AudioDESC(request):
    try:

        data_all = Audio.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_SmartHomesDESC(request):
    try:

        data_all = SmartHomes.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_GadgetsDESC(request):
    try:

        data_all = ElectronicGadgets.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_CarsElectronicsDESC(request):
    try:

        data_all = CarsElectronics.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_CamsDESC(request):
    try:

        data_all = Cams.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_videoGamesDESC(request):
    try:

        data_all = VideoGames.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_TVDESC(request):
    try:

        laptopdata_all = TV.objects.all().order_by('-SNR_Price')
        paginator = Paginator(laptopdata_all, 21)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(data, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator.num_pages
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_TV(request):
    if request.method == 'POST':

        serializer = TV_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            walmart.TV_Walmart(mydata)

            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartTV1(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonTV(mydata)
            bestBuy = best.bestbuy()
            bestBuy.getTVS(mydata)
            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartTV2(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayTVAll(mydata)
            ebayapi.ebayTV(mydata)
            #
            #
            news = newsegg.newEggAPI()
            news.newEggTV(mydata)

            group = groupon.GroupOnAPI()
            group.groupTV(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Clothes(request):
    if request.method == 'POST':

        serializer = Clothes_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            walmart.Clothes_Walmart(mydata)
            #
            # amz=amazon.AmazonAPI()
            # amz.amazonTV(mydata)
            # bestBuy= best.bestbuy()
            # bestBuy.getTVS(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayHomeClothingAll(mydata)
            #
            #
            news = newsegg.newEggAPI()
            news.newEggTV(mydata)

            group = groupon.GroupOnAPI()
            group.groupTV(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Flowers(request):
    if request.method == 'POST':

        serializer = Flowers_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            walmart.Flowers_Walmart(mydata)

            # amz=amazon.AmazonAPI()
            # amz.amazonTV(mydata)
            # bestBuy= best.bestbuy()
            # bestBuy.getTVS(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayFlowersAll(mydata)

            #
            #
            news = newsegg.newEggAPI()
            news.newEggTV(mydata)

            group = groupon.GroupOnAPI()
            group.groupTV(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Jewelry(request):
    if request.method == 'POST':

        serializer = Jewelry_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            walmart.TV_Walmart(mydata)

            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartTV1(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonTV(mydata)
            bestBuy = best.bestbuy()
            bestBuy.getTVS(mydata)
            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartTV2(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayTVAll(mydata)
            ebayapi.ebayTV(mydata)
            #
            #
            news = newsegg.newEggAPI()
            news.newEggTV(mydata)

            group = groupon.GroupOnAPI()
            group.groupTV(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_HomeGraden(request):
    if request.method == 'POST':

        serializer = HomeandGarden_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            walmart.HomeandGradden_Walmart(mydata)

            # amz=amazon.AmazonAPI()
            # amz.amazonTV(mydata)
            # bestBuy= best.bestbuy()
            # bestBuy.getTVS(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayHomeGradenAll(mydata)
            #
            #
            news = newsegg.newEggAPI()
            news.newEggTV(mydata)

            group = groupon.GroupOnAPI()
            group.groupTV(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.


@api_view(['POST'])
def add_Furniture(request):
    if request.method == 'POST':

        serializer = Furniture_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            walmart.TV_Walmart(mydata)

            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartTV1(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonTV(mydata)
            bestBuy = best.bestbuy()
            bestBuy.getTVS(mydata)
            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartTV2(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayTVAll(mydata)
            ebayapi.ebayTV(mydata)
            #
            #
            news = newsegg.newEggAPI()
            news.newEggTV(mydata)

            group = groupon.GroupOnAPI()
            group.groupTV(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Books(request):
    if request.method == 'POST':

        serializer = TV_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            # walmart.Books_Walmart(mydata)

            # walmartapi = walmart.WalmartAPI()
            # walmartapi.walmartTV1(mydata)
            #
            #
            # amz=amazon.AmazonAPI()
            # amz.amazonTV(mydata)
            # bestBuy= best.bestbuy()
            # bestBuy.getTVS(mydata)
            # walmartapi = walmart.WalmartAPI()
            # walmartapi.walmartTV2(mydata)
            #
            ebayapi = ebay.EbayAPI()
            ebayapi.ebayBooksAll(mydata)
            # ebayapi.ebayTV(mydata)
            # #
            # #
            # news=newsegg.newEggAPI()
            # news.newEggTV(mydata)
            #
            #
            # group=groupon.GroupOnAPI()
            # group.groupTV(mydata)
            #
            #



            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Sports(request):
    if request.method == 'POST':

        serializer = TV_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # serializer.save();


            mydata = serializer.validated_data

            # walmart.Books_Walmart(mydata)

            # walmartapi = walmart.WalmartAPI()
            # walmartapi.walmartTV1(mydata)
            #
            #
            # amz=amazon.AmazonAPI()
            # amz.amazonTV(mydata)
            # bestBuy= best.bestbuy()
            # bestBuy.getTVS(mydata)
            # walmartapi = walmart.WalmartAPI()
            # walmartapi.walmartTV2(mydata)
            #
            ebayapi = ebay.EbayAPI()
            ebayapi.ebaySportsAll(mydata)
            # ebayapi.ebayTV(mydata)
            # #
            # #
            # news=newsegg.newEggAPI()
            # news.newEggTV(mydata)
            #
            #
            # group=groupon.GroupOnAPI()
            # group.groupTV(mydata)
            #
            #



            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Cams(request):
    if request.method == 'POST':

        serializer = Cams_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.Cams_Walmart(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayCamsAll(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getCams(mydata)

            newsegg.newEggAPI().newEggCams(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayCams(mydata)
            grouponapi = groupon.GroupOnAPI()
            grouponapi.groupCams(mydata)
            amz = amazon.AmazonAPI()
            amz.amazonCams(mydata)

            # walmart.Cams_Walmart()
            #
            # walmartapi= walmart.WalmartAPI()
            # walmartapi.walmartCamera(mydata)

            # atnt= ATnT.ATNT()
            # atnt.getLaptops(mydata)




            # walmart.search(mydata)
            #
            # ebay.search(mydata)
            #
            # best.search(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Gadgets(request):
    if request.method == 'POST':

        serializer = ElectronicsGadgets_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            # walmart.Cams_Walmart(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayGadgetsAll(mydata)
            #
            # bestBuy= best.bestbuy()
            # bestBuy.getCams(mydata)
            #
            #
            # newsegg.newEggAPI().newEggCams(mydata)
            #
            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayCams(mydata)
            # grouponapi = groupon.GroupOnAPI()
            # grouponapi.groupCams(mydata)
            # amz=amazon.AmazonAPI()
            # amz.amazonCams(mydata)
            #
            #

            # walmart.Cams_Walmart()
            #
            # walmartapi= walmart.WalmartAPI()
            # walmartapi.walmartCamera(mydata)

            # atnt= ATnT.ATNT()
            # atnt.getLaptops(mydata)




            # walmart.search(mydata)
            #
            # ebay.search(mydata)
            #
            # best.search(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.



@api_view(['POST'])
def add_CarsElectronics(request):
    if request.method == 'POST':

        serializer = CarsElec_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data
            walmart.cars_Walmart(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonCarsElectronics(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getCarsElect(mydata)

            walmartdata = walmart.WalmartAPI()
            walmartdata.walmartCarsElec(mydata)
            #
            grouponapi = groupon.GroupOnAPI()
            grouponapi.groupCarsElectronics(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayCarselecAll(mydata)
            ebayapi.ebayCars(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.


@api_view(['POST'])
def add_VideoGames(request):
    if request.method == 'POST':

        serializer = VideoGames_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.games_Walmart(mydata)

            walmartdata = walmart.WalmartAPI()
            walmartdata.walmartVideoGame(mydata)
            newsegg.newEggAPI().newEgggGames(mydata)

            group = groupon.GroupOnAPI()
            group.groupGames(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonVideoGames(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getVideoGames(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayVideo(mydata)
            ebayapi.ebayGamesAll(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
@api_view(['POST'])
def add_Toys(request):
    if request.method == 'POST':

        serializer = Toys_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.toys_Walmart(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getToys(mydata)

            walmartdata = walmart.WalmartAPI()
            walmartdata.walmartToys(mydata)

            group = groupon.GroupOnAPI()
            group.groupToys(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonToys(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayToys(mydata)

            ebayapi.ebayToysAll(mydata)

            # walmart.search(mydata)
            #
            # ebay.search(mydata)
            #
            # best.search(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.


@api_view(['POST'])
def add_SmartHomes(request):
    if request.method == 'POST':

        serializer = Smarthomes_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.smarthome_Walmart(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getSmartHomes(mydata)

            ebayapi = ebay.EbayAPI()

            ebayapi.ebaySmarthome(mydata)
            ebayapi.ebaySmartHomeAll(mydata)

            group = groupon.GroupOnAPI()
            group.groupHome(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.



@api_view(['POST'])
def add_Audio(request):
    if request.method == 'POST':

        serializer = Audio_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.audio_Walmart(mydata)

            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartAudio(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonAudio(mydata)

            walmart.audio_Walmart()
            bestBuy = best.bestbuy()
            bestBuy.getAudios(mydata)

            #
            group = groupon.GroupOnAPI()
            group.groupAudio(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayAudioAll(mydata)
            ebayapi.ebayAudio(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.



@api_view(['POST'])
def add_Applinces(request):
    if request.method == 'POST':

        serializer = Applinces_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();



            mydata = serializer.validated_data

            walmart.appliances_Walmart(mydata)

            newsegg.newEggAPI().newEggAppliances(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getApplinces(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayAppliancesAll(mydata)
            ebayapi.ebayApplinces(mydata)
            # #
            # #
            walmartapi = walmart.WalmartAPI()
            walmartapi.walmartApplinces(mydata)

            group = groupon.GroupOnAPI()
            group.groupAppliances(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonAppliances(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

@api_view(['POST'])
def add_Movies(request):
    if request.method == 'POST':

        serializer = Movies_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.Movies_Walmart(mydata)
            #
            walmart.WalmartAPI().walmartMovies(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getMovies(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayMoviesAll(mydata)
            ebayapi.ebayMovies(mydata)

            group = groupon.GroupOnAPI()
            group.groupMovies(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonMovies(mydata);

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.



@api_view(['POST'])
def add_software(request):
    if request.method == 'POST':

        serializer = Software_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            amz = amazon.AmazonAPI()
            amz.amazonSoftware(mydata)

            walmart.software_Walmart(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getsoftware(mydata)

            walmartdata = walmart.WalmartAPI()
            walmartdata.walmartSoftware(mydata)
            group = groupon.GroupOnAPI()
            group.groupSoftware(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebaySoftwareAll(mydata)
            ebayapi.ebaySoftware(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Office(request):
    if request.method == 'POST':

        serializer = Office_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.Office_Walmart(mydata)

            amz = amazon.AmazonAPI()
            amz.amazonOffice(mydata)

            group = groupon.GroupOnAPI()
            group.groupOffice(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayOffice(mydata)

            newsegg.newEggAPI().newEggOffice(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getOfficeSupply(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Health(request):
    if request.method == 'POST':

        serializer = Health_Serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save();

            mydata = serializer.validated_data

            walmart.Health_Walmart(mydata)

            bestBuy = best.bestbuy()
            bestBuy.getHealth(mydata)

            newsegg.newEggAPI().newEggHealth(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayHealthAll(mydata)
            ebayapi.ebayHealth(mydata)

            group = groupon.GroupOnAPI()
            group.groupOffice(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_4012_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAppliancesModelsebay(request):
    Laptop_all = Applinces.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Applinces_Serializer(data, many=True, context=serializer_context)
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
def getBooksModelsebay(request):
    Laptop_all = Books.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Books_Serializer(data, many=True, context=serializer_context)
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
def getSportsModelsebay(request):
    Laptop_all = SportingGoods.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Sports_Serializer(data, many=True, context=serializer_context)
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
def getOfficeModelsebay(request):
    Laptop_all = OfficeSupply.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Office_Serializer(data, many=True, context=serializer_context)
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
def getToysModelsebay(request):
    Laptop_all = Toys.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Toys_Serializer(data, many=True, context=serializer_context)
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
def getTVModelsebay(request):
    Laptop_all = TV.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = TV_Serializer(data, many=True, context=serializer_context)
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
def getAudioModelsebay(request):
    Laptop_all = Audio.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Audio_Serializer(data, many=True, context=serializer_context)
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
def getCarselecModelsebay(request):
    Laptop_all = CarsElectronics.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
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
def getMoviesModelsebay(request):
    Laptop_all = Movies.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Movies_Serializer(data, many=True, context=serializer_context)
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
def getSoftwareModelsebay(request):
    Laptop_all = ComputerSoftware.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Software_Serializer(data, many=True, context=serializer_context)
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
def getCamsModelsebay(request):
    Laptop_all = Cams.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Cams_Serializer(data, many=True, context=serializer_context)
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
def getSmarthomeModelsebay(request):
    Laptop_all = SmartHomes.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
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
def getGamesModelsebay(request):
    Laptop_all = VideoGames.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
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
def getGadgetsModelsebay(request):
    Laptop_all = ElectronicGadgets.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)
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
def getFlowerModelsebay(request):
    Laptop_all = FlowerandPlants.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Flowers_Serializer(data, many=True, context=serializer_context)
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
def getFurnitureModelsebay(request):
    Laptop_all = Furniture.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Furniture_Serializer(data, many=True, context=serializer_context)
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
def getClothesModelsebay(request):
    Laptop_all = Clothing.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Clothes_Serializer(data, many=True, context=serializer_context)
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
def getArtsModelsebay(request):
    Laptop_all = Arts.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Arts_Serializer(data, many=True, context=serializer_context)
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
def getJewelryModelsebay(request):
    Laptop_all = Jewelry.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Jewelry_Serializer(data, many=True, context=serializer_context)
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
def getHealthModelsebay(request):
    Laptop_all = HealthandFitness.objects.filter(SNR_Available__icontains='Ebay')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Health_Serializer(data, many=True, context=serializer_context)
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
def getAppliancesModelswalmart(request):
    Laptop_all = Applinces.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Applinces_Serializer(data, many=True, context=serializer_context)
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
def getBooksModelswalmart(request):
    Laptop_all = Books.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Books_Serializer(data, many=True, context=serializer_context)
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
def getSportsModelswalmart(request):
    Laptop_all = SportingGoods.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Sports_Serializer(data, many=True, context=serializer_context)
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
def getOfficeModelswalmart(request):
    Laptop_all = OfficeSupply.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Office_Serializer(data, many=True, context=serializer_context)
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
def getToysModelswalmart(request):
    Laptop_all = Toys.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Toys_Serializer(data, many=True, context=serializer_context)
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
def getTVModelswalmart(request):
    Laptop_all = TV.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = TV_Serializer(data, many=True, context=serializer_context)
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
def getAudioModelswalmart(request):
    Laptop_all = Audio.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Audio_Serializer(data, many=True, context=serializer_context)
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
def getCarselecModelswalmart(request):
    Laptop_all = CarsElectronics.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
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
def getMoviesModelswalmart(request):
    Laptop_all = Movies.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Movies_Serializer(data, many=True, context=serializer_context)
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
def getSoftwareModelswalmart(request):
    Laptop_all = ComputerSoftware.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Software_Serializer(data, many=True, context=serializer_context)
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
def getCamsModelswalmart(request):
    Laptop_all = Cams.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Cams_Serializer(data, many=True, context=serializer_context)
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
def getSmarthomeModelswalmart(request):
    Laptop_all = SmartHomes.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
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
def getGamesModelswalmart(request):
    Laptop_all = VideoGames.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
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
def getGadgetsModelswalmart(request):
    Laptop_all = ElectronicGadgets.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)
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
def getFlowerModelswalmart(request):
    Laptop_all = FlowerandPlants.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Flowers_Serializer(data, many=True, context=serializer_context)
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
def getFurnitureModelswalmart(request):
    Laptop_all = Furniture.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Furniture_Serializer(data, many=True, context=serializer_context)
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
def getClothesModelswalmart(request):
    Laptop_all = Clothing.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Clothes_Serializer(data, many=True, context=serializer_context)
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
def getArtsModelswalmart(request):
    Laptop_all = Arts.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Arts_Serializer(data, many=True, context=serializer_context)
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
def getJewelryModelswalmart(request):
    Laptop_all = Jewelry.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Jewelry_Serializer(data, many=True, context=serializer_context)
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
def getHealthModelswalmart(request):
    Laptop_all = HealthandFitness.objects.filter(SNR_Available__icontains='walmart')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Health_Serializer(data, many=True, context=serializer_context)
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
def getAppliancesModelebestbuy(request):
    Laptop_all = Applinces.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Applinces_Serializer(data, many=True, context=serializer_context)
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
def getBooksModelebestbuy(request):
    Laptop_all = Books.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Books_Serializer(data, many=True, context=serializer_context)
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
def getSportsModelebestbuy(request):
    Laptop_all = SportingGoods.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Sports_Serializer(data, many=True, context=serializer_context)
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
def getOfficeModelebestbuy(request):
    Laptop_all = OfficeSupply.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Office_Serializer(data, many=True, context=serializer_context)
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
def getToysModelebestbuy(request):
    Laptop_all = Toys.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Toys_Serializer(data, many=True, context=serializer_context)
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
def getTVModelebestbuy(request):
    Laptop_all = TV.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = TV_Serializer(data, many=True, context=serializer_context)
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
def getAudioModelebestbuy(request):
    Laptop_all = Audio.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Audio_Serializer(data, many=True, context=serializer_context)
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
def getCarselecModelebestbuy(request):
    Laptop_all = CarsElectronics.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
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
def getMoviesModelebestbuy(request):
    Laptop_all = Movies.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Movies_Serializer(data, many=True, context=serializer_context)
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
def getSoftwareModelebestbuy(request):
    Laptop_all = ComputerSoftware.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Software_Serializer(data, many=True, context=serializer_context)
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
def getCamsModelebestbuy(request):
    Laptop_all = Cams.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Cams_Serializer(data, many=True, context=serializer_context)
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
def getSmarthomeModelebestbuy(request):
    Laptop_all = SmartHomes.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
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
def getGamesModelebestbuy(request):
    Laptop_all = VideoGames.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
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
def getGadgetsModelebestbuy(request):
    Laptop_all = ElectronicGadgets.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = ElectronicsGadgets_Serializer(data, many=True, context=serializer_context)
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
def getFlowerModelebestbuy(request):
    Laptop_all = FlowerandPlants.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Flowers_Serializer(data, many=True, context=serializer_context)
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
def getFurnitureModelebestbuy(request):
    Laptop_all = Furniture.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Furniture_Serializer(data, many=True, context=serializer_context)
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
def getClothesModelebestbuy(request):
    Laptop_all = Clothing.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Clothes_Serializer(data, many=True, context=serializer_context)
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
def getArtsModelebestbuy(request):
    Laptop_all = Arts.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Arts_Serializer(data, many=True, context=serializer_context)
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
def getJewelryModelebestbuy(request):
    Laptop_all = Jewelry.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Jewelry_Serializer(data, many=True, context=serializer_context)
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
def getHealthModelebestbuy(request):
    Laptop_all = HealthandFitness.objects.filter(SNR_Available__icontains='Best Buy')
    paginator = Paginator(Laptop_all, 1000)
    page = request.GET.get('page')
    try:

        data = paginator.page(page)
    except PageNotAnInteger:

        data = paginator.page(1)
    except EmptyPage:

        data = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = Health_Serializer(data, many=True, context=serializer_context)
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