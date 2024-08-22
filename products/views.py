import string
import timeit
import random
import time
import re
from random import shuffle

from bs4 import BeautifulSoup
from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from rest_framework.decorators import permission_classes
from rest_framework import status, permissions
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response  # to send specific response
from rest_framework import status
# from newdb.models import *
from products.models import *
# from .models import *
from SNR.settings import *
from .serializers import *
from userReviews.models import *
# import walmart
# import ebay
# import best
# import groupon
import math
from django.db import connection
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
# import amazon
# import newsegg
from scrapetools import *
from datetime import datetime, timedelta
from .serializers import *
from django.core.cache import cache
from rest_framework.views import APIView
from django.db.models import Count
from django.http import HttpResponse
from .sharding import create_shards
# from elasticsearch.exceptions import RequestError
from math import ceil
from products.models import AllProducts


def sharding_view(request):
    create_shards()
    # insert_records()
    return HttpResponse("Table sharding complete!")


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
def Filter_Books(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Bookswithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_BooksBYbrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Sports(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Sportswithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Sportsbybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Furniture(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Furniturewithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Furniturebybrad(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Arts(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Artswithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Artsbybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Flowerbybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Flower(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Flowerwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Clothewithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Clothe(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGarden(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenbybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Jewelry(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Jewelrywithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_Jewelrybybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_BooksDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_BooksDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_BooksbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_SportsDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_SportsDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_SportsbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FurnitureDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FurnitureDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FurniturebybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ArtsDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ArtsDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ArtsbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FlowerDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FlowerDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FlowerbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ClotheDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ClotheDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ClothebybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_JewelryDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_JewelryDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_JewelrybybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_BooksASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_BooksASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_BooksbybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_SportsASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_SportsASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_SportsbybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FurnitureASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FurnitureASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FurniturebybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ArtsASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ArtsASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ArtsbybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FlowerASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FlowerASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_FlowerbybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ClotheASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ClotheASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_ClothebybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HomeandGardenbybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_JewelryASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_JewelryASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_JewelrybybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
def Filter_AppliencesDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_AppliencesbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HealthDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HealthDESCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_HealthbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogames(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogameswithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogamesbybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogamesASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogamesASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogamesbybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogamesDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_videogamesbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_GadgetsDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_GadgetsbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audio(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audiowithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audiobybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audioASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audioASCwithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audiobybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audiobybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_audioDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_cams(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_camswithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_camsbybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_camsASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_camsbybrandASC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_camsDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_camsbybrandDESC(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_smarthome(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_smarthomewithprice(request, query, price1, price2):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_smarthomebybrand(request, query):
    #print(query)
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
@permission_classes((permissions.AllowAny,))
def Filter_smarthomeASC(request, query):
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
    #print(query)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(laptopdata_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(laptopdata_all, 36)
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
@permission_classes((permissions.AllowAny,))
def getAll_Products(request):
    try:

        laptopdata_all = AllProducts.objects.all().order_by("-SNR_Date")
        paginator = Paginator(laptopdata_all, 36)
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
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def send_data(request):
    # try:
        data=request.data
        # print data

        data['SNR_Title'] = parseHtml(data['SNR_Title'])
        data["SNR_Description"] = parseHtml(data["SNR_Description"])
        data['SNR_CustomerReviews'] = float("%0.2f" % data['SNR_CustomerReviews'])
        data['SNR_Price'] = float("%0.2f" % data['SNR_Price'])
        data["SNR_PriceBefore"] = float("%0.2f" % data["SNR_PriceBefore"])
        try:
            data["SNR_Category"] = map_data(cap_dict, data["SNR_Category"])
        except:
            pass

        serializer = AllProducts_Serializer(data=data)

        if serializer.is_valid():
            print("---")
            serializer.save()
        else:
             print ("bad json")
            # print serializer.errors

        return Response({})
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getAll_TodayDeals(request):
    page = request.GET.get('page')
    cache_key = 'todaydeals'+str(page)
    cache_time = 90500  # time to live in seconds
    result = cache.get(cache_key)

    if not result:

        try:
            data_all = AllProducts.objects.filter(SNR_Date__gt=datetime.date.today()-timedelta(days=30),SNR_Category__exact="Deals")

            try:
                pagecount = int(request.GET.get('count'))
            except:
                pagecount = 36
            paginator = Paginator(data_all, pagecount)

            # print pagecount

            page = request.GET.get('page')
            try:

                data = paginator.page(page)
            except PageNotAnInteger:

                data = paginator.page(1)
            except EmptyPage:



                data = paginator.page(paginator.num_pages)

            data = product_to_deal(data)
            items = 0
            pages = 0
            items = paginator.count
            pages = paginator.num_pages
            res = {
                'totalItems': items,
                'totalPages': pages,
                'results': data

            }
            return Response(res)

            result=res;
            cache.set(cache_key, result, cache_time)
            # print "setting cache"
            return Response(res)

        except AllProducts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        # print "returning from cache"
        return Response(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_VendorCategories(request,query):
    print('in')
    if query =='All':
        main_data_query = 'Select DISTINCT("SNR_Category") from products_active_dailydeals Where "SNR_Active"=TRUE AND "SNR_Category" is not null'
    else:
        query=query.replace("'","''")
        main_data_query = 'Select DISTINCT("SNR_Category") from products_active_dailydeals Where "SNR_Active"=TRUE AND "SNR_Available" =\''+str(query)+'\'  AND "SNR_Category" is not null'
    current_item = []
    with connection.cursor() as cursor:
        cursor.execute(main_data_query)
        for i in cursor.fetchall():
            current_item.append(i[0])

    return Response(current_item, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_VocationCategories(request,query):
    print('in')
    if query=='All':
        main_data_query = 'Select DISTINCT("SNR_Category") from products_active_vocation Where "SNR_Active"=TRUE AND "SNR_Category" is not null'
    else:
        query=query.replace("'","''")
        main_data_query = 'Select DISTINCT("SNR_Category") from products_active_vocation Where "SNR_Active"=TRUE AND "SNR_Available" =\''+str(query)+'\'  AND "SNR_Category" is not null'
    current_item = []
    with connection.cursor() as cursor:
        cursor.execute(main_data_query)
        for i in cursor.fetchall():
            current_item.append(i[0])

    return Response(current_item, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter_VendorDeals_test(request,query,totalResult):

    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1
    except:
        page = 1

    # try:
    #     cat = request.GET.get('cat')
    #     print(cat)
    #     if (cat != 'undefined' or cat != None):
    #        print('incoming cat is OK', cat)
    #     else:
    #         cat = 'undefined'
    # except:
    #     pass

    dic=request.data
    temp=[]
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)

    my_map = client.get_map("Deal").blocking()
    cache_key = 'Hot_Deals=='+str(query)+'=='+str(dic['cat'])+'=='+str(dic['sort'])+'=='+str(dic['search'])+'=='+str(dic['minprice'])+'=='+str(dic['maxprice'])+'=='+str(totalResult)+'=='+str(page)
    # cache_key = 'Hot_Deals=='+str(query)+'bpl2023'
    print(cache_key)
    # cache_time = 36000

    # result =Nonepagepage
    try:
        result = my_map.get(cache_key)
    except Exception as e:
        print(e)
        Deal_map = client.get_map("Deal").blocking()
        Deal_map.clear()
        # my_map.remove(cache_key)
        result = None
    print("result is: ",result)
    # print(cache_key)
    # result=None
    # if result == None or result['results'] == []:
    # print("dic['cat']: ", dic['cat'])
    # print("dic['minprice']: ", dic['minprice'])
    # print("dic['cat']: ", dic['cat'])
    minprice = dic['minprice']
    maxprice = dic['maxprice']
    if result == None or result['results'] == []:
        print('inout')
        if query=='All':
            ls = ' where "SNR_Active"=TRUE AND "SNR_Available" IS NOT NULL'
        else:
            ls=' where "SNR_Active"=TRUE AND "SNR_Available" =\''+str(query.replace("'","''"))+'\''
        if dic['cat'] != "undefine":
            ls=ls+' AND "SNR_Category" =\''+request.data['cat'].replace("'","''")+'\''
        if int(minprice) != -1 and int(maxprice) != -1:
            ls=ls+' AND "SNR_PriceAfter" BETWEEN '+str(request.data['minprice'])+' AND '+str(request.data['maxprice'])
        if dic['search'] !='undefine':
            a=str(dic['search']).replace("\'","")
            a = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in a.split("\n")]
            ls=ls+' AND "tsv_title" @@ plainto_tsquery(\''+str(a[0])+'\')'
        if dic['sort'] != "undefine":
            if request.data['sort']=='ASC':
                lss=' order by "SNR_PriceAfter" ASC'
            elif request.data['sort']=='DESC':
                lss=' order by "SNR_PriceAfter" DESC'
            elif request.data['sort']=='LATEST':
                lss=' order by "id" DESC'
            elif request.data['sort']=='OLDEST':
                lss=' order by "id" ASC'
            main_data_query = 'Select {0} from public.products_active_dailydeals {1} '+str(lss)+' OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
            co = 'Select Count(\'*\') from public.products_active_dailydeals '+str(ls)
        else:
            main_data_query = 'Select {0} from public.products_active_dailydeals {1} OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
            co = 'Select Count(\'*\') from public.products_active_dailydeals '+str(ls)

        with connection.cursor() as cursor:
            cursor.execute(co)
            it=cursor.fetchall()
            it=[i[0] for i in it]
        connection.close()
        totalpages = int(int(it[0])/int(totalResult))
        per = int(it[0]) % int(totalResult)
        if per != 0:
            totalpages += 1

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available","id",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category","SNR_Description",
            "SNR_PriceBefore", "SNR_PriceAfter","SNR_Customer_Rating"
        ]
        out = ['"{0}"'.format(i) for i in fields]

        data_query = main_data_query.format(",".join(out), ls)
        f_count = len(fields)
        print(data_query)
        count=0
        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    current_item['index']=count
                count=count+1

                temp.append(current_item)
        connection.close()
        a = {'results': temp,
             'items': str(it[0]), 'pages': str(totalpages)
             }
        # my_map.remove(cache_key)
        my_map.put(cache_key, a)
        return Response({'items':it[0],'pages':totalpages, 'results':temp},status.HTTP_200_OK)
    else:
        print('in cache')
        # return Response({'data': 'NO'},status.HTTP_200_OK)
        return Response(result,status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter_VendorDeals_test_test(request,query,totalResult):

    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1
    except:
        page = 1

    # try:
    #     cat = request.GET.get('cat')
    #     print(cat)
    #     if (cat != 'undefined' or cat != None):
    #        print('incoming cat is OK', cat)
    #     else:
    #         cat = 'undefined'
    # exc
    # ept:
    #     pass

    dic=request.data
    temp=[]
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)

    my_map = client.get_map("Deal").blocking()
    cache_key = 'Hot_Deals=='+str(query)+'=='+str(dic['cat'])+'=='+str(dic['sort'])+'=='+str(dic['search'])+'=='+str(dic['minprice'])+'=='+str(dic['maxprice'])+'=='+str(totalResult)+'=='+str(page)
    # cache_key = 'Hot_Deals=='+str(query)+'bpl2023'
    print(cache_key)
    # cache_time = 36000

    # result =Nonepagepage
    try:
        result = my_map.get(cache_key)
    except Exception as e:
        print(e)
        Deal_map = client.get_map("Deal").blocking()
        Deal_map.clear()
        # my_map.remove(cache_key)
        result = None
    print("result is: ",result)
    #   print(cache_key)
    # result=None
    # if result == None or result['results'] == []:
    print("dic['cat']: ", dic['cat'])
    print("dic['minprice']: ", dic['minprice'])
    print("dic['cat']: ", dic['cat'])
    minprice = dic['minprice']
    maxprice = dic['maxprice']

    result = None
    if result == None or result['results'] == []:
        print('inout')
        if query=='All':
            ls = ' where "SNR_Active"=TRUE AND "SNR_Available" IS NOT NULL'
        else:
            ls=' where "SNR_Active"=TRUE AND "SNR_Available" =\''+str(query.replace("'","''"))+'\''
        if dic['cat'] != "undefine":
            ls=ls+' AND "SNR_Category" =\''+request.data['cat'].replace("'","''")+'\''
        # if dic['minprice'] != -1 and dic['maxprice'] != -1:
        if int(minprice) != -1 and int(maxprice) != -1:
            ls=ls+' AND "SNR_PriceAfter" BETWEEN '+str(request.data['minprice'])+' AND '+str(request.data['maxprice'])
        if dic['search'] !='undefine':
            a=str(dic['search']).replace("\'","")
            a = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in a.split("\n")]
            ls=ls+' AND "tsv_title" @@ plainto_tsquery(\''+str(a[0])+'\')'
        if dic['sort'] != "undefine":
            if request.data['sort']=='ASC':
                lss=' order by "SNR_PriceAfter" ASC'
            elif request.data['sort']=='DESC':
                lss=' order by "SNR_PriceAfter" DESC'
            elif request.data['sort']=='LATEST':
                lss=' order by "id" DESC'
            elif request.data['sort']=='OLDEST':
                lss=' order by "id" ASC'
            main_data_query = 'Select {0} from public.products_active_dailydeals {1} '+str(lss)+' OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
            co = 'Select Count(\'*\') from public.products_active_dailydeals '+str(ls)
        else:
            main_data_query = 'Select {0} from public.products_active_dailydeals {1} OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
            co = 'Select Count(\'*\') from public.products_active_dailydeals '+str(ls)

        with connection.cursor() as cursor:
            cursor.execute(co)
            it=cursor.fetchall()
            it=[i[0] for i in it]
        connection.close()
        totalpages = int(int(it[0])/int(totalResult))
        per = int(it[0]) % int(totalResult)
        if per != 0:
            totalpages += 1

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available","id",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category","SNR_Description",
            "SNR_PriceBefore", "SNR_PriceAfter","SNR_Customer_Rating"
        ]
        out = ['"{0}"'.format(i) for i in fields]

        data_query = main_data_query.format(",".join(out), ls)
        f_count = len(fields)
        print(data_query)
        count=0
        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    current_item['index']=count
                count=count+1

                temp.append(current_item)
        connection.close()
        a = {'results': temp,
             'items': str(it[0]), 'pages': str(totalpages)
             }
        # my_map.remove(cache_key)
        # my_map.put(cache_key, a)
        return Response({'items':it[0],'pages':totalpages,'results':temp},status.HTTP_200_OK)
    else:
        print('in cache')
        return Response({'data: ':'NO' },status.HTTP_200_OK)
        # return Response(result,status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter_Vocation(request,query,totalResult):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1
    except:
        page = 1
    que=Q()
    dic=request.data
    temp=[]
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    my_map = client.get_map("Vocation").blocking()
    cache_key = 'Vocation=='+str(query)+'=='+str(dic['cat'])+'=='+str(dic['sort'])+'=='+str(dic['search'])+'=='+str(dic['minprice'])+'=='+str(dic['maxprice'])+'=='+str(totalResult)+'=='+str(page)
    print(cache_key)
    cache_time = 36000
    result = my_map.get(cache_key)
    # print(cache_key)
    # result=None
    if result == None:
        print('inout')
        if query=='All':
            ls = ' where "SNR_Active"=TRUE '
        else:
            ls=' where "SNR_Active"=TRUE AND "SNR_Available" =\''+str(query.replace("'","''"))+'\''
        if dic['cat'] != "undefine":
            ls=ls+' AND "SNR_Category" =\''+request.data['cat'].replace("'","''")+'\''
        if dic['minprice'] != -1 and dic['maxprice'] != -1:
            ls=ls+' AND "SNR_PriceAfter" BETWEEN '+str(request.data['minprice'])+' AND '+str(request.data['maxprice'])
        if dic['search'] !='undefine':
            a=str(dic['search']).replace("\'","")
            print(a)
            ls=ls+' AND "tsv_title" @@ plainto_tsquery(\''+str(a)+'\')'
        if dic['sort'] != "undefine":
            if request.data['sort']=='ASC':
                lss=' order by "SNR_PriceAfter" ASC'
            elif request.data['sort']=='DESC':
                lss=' order by "SNR_PriceAfter" DESC'
            elif request.data['sort']=='LATEST':
                lss=' order by "id" DESC'
            elif request.data['sort']=='OLDEST':
                lss=' order by "id" ASC'
            main_data_query = 'Select {0} from public.products_active_vocation {1}  '+str(lss)+' OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
            co = 'Select Count(\'*\') from public.products_active_vocation '+str(ls)
        else:
            main_data_query = 'Select {0} from public.products_active_vocation {1}  OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
            co = 'Select Count(\'*\') from public.products_active_vocation '+str(ls)

        with connection.cursor() as cursor:
            cursor.execute(co)
            it=cursor.fetchall()
            it=[i[0] for i in it]
        connection.close()
        totalpages = int(int(it[0])/int(totalResult))
        per = int(it[0]) % int(totalResult)
        if per != 0:
            totalpages += 1

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available","id",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category","SNR_Description",
            "SNR_PriceBefore", "SNR_PriceAfter","SNR_Customer_Rating"
        ]
        out = ['"{0}"'.format(i) for i in fields]

        data_query = main_data_query.format(",".join(out), ls)
        f_count = len(fields)
        print(data_query)
        count=0
        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    current_item['index']=count
                count=count+1

                temp.append(current_item)
        connection.close()
        a = {'results': temp,
             'items': str(it[0]), 'pages': str(totalpages)
             }
        my_map.put(cache_key, a)
        return Response({'results':temp,'items':it[0],'pages':totalpages},status.HTTP_200_OK)
    else:
        print('in cache')
        return Response(result,status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter_VendorDeals_test_backup(request,query,totalResult):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    que=Q()
    dic=request.data
    temp=[]
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    key_backup = 'Hot_Deals_backup' + str(query) + str(dic['cat']) + str(dic['sort']) + str(dic['search']) + str(
        dic['minprice']) + str(dic['maxprice']) + str(totalResult) + str(page)
    key_backup_time = 43200
    result = cache.get(key_backup)
    # print(cache_key)
    # result=None
    if not result:
        print('inout')
        ls=' where "SNR_Active"=TRUE AND "SNR_Available" =\''+str(query.replace("'","''"))+'\''
        if dic['cat'] != "undefine":
            ls=ls+' AND "SNR_Category" =\''+request.data['cat'].replace("'","''")+'\''
        if dic['minprice'] != -1 and dic['maxprice'] != -1:
            ls=ls+' AND "SNR_PriceAfter" BETWEEN '+str(request.data['minprice'])+' AND '+str(request.data['maxprice'])
        if dic['search'] !='undefine':
            a=str(dic['search']).replace("\'","")
            print(a)
            ls=ls+' AND "tsv_title" @@ plainto_tsquery(\''+str(a)+'\')'
        if dic['sort'] != "undefine":
            if request.data['sort']=='ASC':
                ls=ls+' ORDER by "SNR_PriceAfter" ASC'
            elif request.data['sort']=='DESC':
                ls=ls+' ORDER by "SNR_PriceAfter" DESC'
            elif request.data['sort']=='LATEST':
                ls=ls+' ORDER by "id" DESC'
            elif request.data['sort']=='OLDEST':
                ls=ls+' ORDER by "id" ASC'
            main_data_query = 'Select {0} from public.products_active_dailydeals {1}  OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
        else:
            main_data_query = 'Select {0} from public.products_active_dailydeals {1} order by Random() OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
        co = 'Select Count(\'*\') from public.products_active_dailydeals '+str(ls)

        with connection.cursor() as cursor:
            cursor.execute(co)
            it=cursor.fetchall()
            it=[i[0] for i in it]
        connection.close()
        totalpages = int(int(it[0])/int(totalResult))
        per = int(it[0]) % int(totalResult)
        if per != 0:
            totalpages += 1

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available","id",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category",
            "SNR_PriceBefore", "SNR_PriceAfter"
        ]
        out = ['"{0}"'.format(i) for i in fields]

        data_query = main_data_query.format(",".join(out), ls)
        f_count = len(fields)

        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)
        connection.close()
        cache.set(key_backup,{'results':temp,'items':it[0],'pages':totalpages}, key_backup_time)
        return Response({'results':temp,'items':it[0],'pages':totalpages},status.HTTP_200_OK)
    else:
        print('in cache')
        return Response(result,status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter_VendorDeals_test_sm1(request):
    query=str(request.data['que'])
    with connection.cursor() as cursor:
        cursor.execute(query)
    return Response({'msg':'done'},status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter_VendorDeals_test_sm(request,query,totalResult):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    que=Q()
    dic=request.data
    temp=[]
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    cache_key = 'Hot_Deals' + str(query) + str(dic['cat']) + str(dic['sort']) + str(dic['search']) + str(
        dic['minprice']) + str(dic['maxprice']) + str(totalResult) + str(page)
    cache_time = 36000
    result = cache.get(cache_key)
    # print(cache_key)
    # result=None
    if not result:
        print('inout')
        ls=' where "SNR_Active"=TRUE AND "SNR_Available" =\''+str(query.replace("'","''"))+'\''
        if dic['cat'] != "undefine":
            ls=ls+' AND "SNR_Category" =\''+request.data['cat'].replace("'","''")+'\''
        if dic['minprice'] != -1 and dic['maxprice'] != -1:
            ls=ls+' AND "SNR_PriceAfter" BETWEEN '+str(request.data['minprice'])+' AND '+str(request.data['maxprice'])
        if dic['search'] !='undefine':
            a=str(dic['search']).replace("\'","")
            print(a)
            ls=ls+' AND "tsv_title" @@ plainto_tsquery(\''+str(a)+'\')'
        if dic['sort'] != "undefine":
            if request.data['sort']=='ASC':
                ls=ls+' ORDER by "SNR_PriceAfter" ASC'
            elif request.data['sort']=='DESC':
                ls=ls+' ORDER by "SNR_PriceAfter" DESC'
            elif request.data['sort']=='LATEST':
                ls=ls+' ORDER by "id" DESC'
            elif request.data['sort']=='OLDEST':
                ls=ls+' ORDER by "id" ASC'
            main_data_query = 'Select {0} from public.products_active_dailydeals {1}  OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
        else:
            main_data_query = 'Select {0} from public.products_active_dailydeals {1} order by Random() OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
        co = 'Select Count(\'*\') from public.products_active_dailydeals '+str(ls)

        with connection.cursor() as cursor:
            cursor.execute(co)
            it=cursor.fetchall()
            it=[i[0] for i in it]
        connection.close()
        totalpages = int(int(it[0])/int(totalResult))
        per = int(it[0]) % int(totalResult)
        if per != 0:
            totalpages += 1

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available","id",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category",
            "SNR_PriceBefore", "SNR_PriceAfter"
        ]
        out = ['"{0}"'.format(i) for i in fields]

        data_query = main_data_query.format(",".join(out), ls)
        f_count = len(fields)

        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)
        connection.close()
        cache.set(cache_key,{'results':temp,'items':it[0],'pages':totalpages}, cache_time)
        return Response({'results':temp,'items':it[0],'pages':totalpages},status.HTTP_200_OK)
    else:
        print('in cache')
        return Response(result,status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def filter_VendorDeals_mainsearch(request,merchant,query,totalResult):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    results=DailyDeals.objects.annotate(search=SearchVector('SNR_Title','SNR_Category')).filter(search=str(query)).filter(SNR_Available=str(merchant)).filter(SNR_PriceAfter__range=['0','100']).values()[offset:limit]
    return Response({'results':results},status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def filter_VendorDeals(request,query):
    try:
        page = int(request.GET.get('page'))
        pagecount = 36
    except:
        page = 1
        pagecount = 36
    try:
        pagecount = int(request.GET.get('count'))
    except:
        pagecount = 36
    try:
        category = request.GET.get('category').replace("'","''")
    except:
        category = '\'-1\''
    try:
        price1 = int(request.GET.get('price1'))
    except:
        price1 = -1
    try:
        price2 = int(request.GET.get('price2'))
    except:
        price2 = -1
    try:
        sort = str(request.GET.get('sort'))
    except:
        sort = -1
    print(category)
    cat_without_spaces=query.replace(" ","" )
    # cache_key = 'Vendor_Filter'+cat_without_spaces+str(page)+str(pagecount)+str(price1)+str(price2)+str(category)+str(sort)
    cache_time = 90500  # time to live in seconds
    cache_key='asfa'
    result = cache.get(cache_key)
    query=query.replace("'","''")
    query="'"+query+"'"
    if not result:

        res = {}
        main_query = 'Select count(*) from products_dailydeals Where "SNR_Available" = %s' % (query)
        main_data_query = 'Select {0} from products_dailydeals Where "SNR_Available" = %s' % (query)

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category",
            "SNR_PriceBefore", "SNR_PriceAfter"
        ]
        out = ['"{0}"'.format(i) for i in fields]
        data_query = main_data_query.format(",".join(out))

        if category != '\'-1\'':
            filter_category = ' AND "SNR_Category" ='+str(category)
            data_query = data_query + filter_category
            print(data_query)
        if price1 != -1 and price2 != -1:
            filter_price1 = ' AND "SNR_PriceAfter" BETWEEN {0} AND {1}'.format(price1,price2)
            data_query = data_query + filter_price1
        if sort != -1:
            if sort == 'Latest':
                filter_sort = ' ORDER BY "SNR_Date" DESC'
                data_query = data_query + filter_sort
            elif sort == 'Oldest':
                filter_sort = ' ORDER BY "SNR_Date" ASC'
                data_query = data_query + filter_sort
            elif sort == 'High':
                filter_sort = ' ORDER BY "SNR_PriceAfter" DESC'
                data_query = data_query + filter_sort
            elif sort == 'Low':
                filter_sort = ' ORDER BY "SNR_PriceAfter" ASC'
                data_query = data_query + filter_sort
        
        limit = page * pagecount
        offset = (page * pagecount) - pagecount
        filter_page = ' OFFSET {0} LIMIT {1}'.format(offset, limit)
        data_query = data_query + filter_page

        f_count = len(fields)
        with connection.cursor() as cursor:
            cursor.execute(data_query)
            temp = []
            for i in cursor.fetchall():

                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    if fields[j]!="SNR_Price":

                        current_item[fields[j]] = i[j]
                    else:
                        current_item["SNR_PriceAfter"] = i[j]

                temp.append(current_item)

            res["results"] = temp
            result = res
            # cache.set(cache_key, result, cache_time)
            # print "setting cache for "+cache_key

            return Response(res,status=status.HTTP_200_OK)
    else:
        # print "returning from cache " + cache_key

        return Response(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def filter_TodayDeals(request,query):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    try:
        pagecount = int(request.GET.get('count'))
    except:
        pagecount = 36

    cat_without_spaces=query.replace(" ","" )
    cache_key = 'Deals_cache_'+cat_without_spaces+str(page)+str(pagecount)
    cache_time = 90500  # time to live in seconds
    result = cache.get(cache_key)
    query=query.replace("'","''")
    query="'"+query+"'"
    if not result:

        res = {}
        main_query = 'Select count(*) from products_dailydeals Where "SNR_Available" = %s ' % (query)
        main_data_query = 'Select {0} from products_dailydeals Where "SNR_Available" = %s ' % (query)
        # and "SNR_Date" > current_timestamp - interval % s
        count_query = main_query.format("*")

        # print main_data_query
        offset = ' LIMIT {0}'.format(pagecount)


        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category",
            "SNR_PriceBefore", "SNR_PriceAfter"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        data_query = main_data_query.format(",".join(out))

        f_count = len(fields)
        # print "cout_q" + count_query
        with connection.cursor() as cursor:
            cursor.execute(count_query)
            # print "executed"
            # print count_query
            query_count = cursor.fetchone()[0]
            # print "aafter execution"
            print(query_count)
            # print(query_cat)
            # query_count = patSearch('rows=(\d+)', query_count).group(1)
            query_count = int(query_count)
            print(query_count)

            # print query_count
            if query_count == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)

            pageCount = int(math.ceil(query_count / float(pagecount)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                sort = (request.GET.get('sort'))
                if (sort != 'undefined' and sort != None):
                    que = (' ORDER BY "SNR_PriceAfter" %s ' % (sort))
                    data_query = data_query + que


            except:
                sort = -1

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, pagecount * (page - 1))

            data_query = data_query+ offset
            # print data_query
            cursor.execute(data_query)
            temp = []
            for i in cursor.fetchall():

                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):
                    if fields[j]!="SNR_Price":

                        current_item[fields[j]] = i[j]
                    else:
                        current_item["SNR_PriceAfter"] = i[j]

                temp.append(current_item)

            res["results"] = temp
            result = res
            cache.set(cache_key, result, cache_time)
            # print "setting cache for "+cache_key

            return Response(res,status=status.HTTP_200_OK)
    else:
        # print "returning from cache " + cache_key

        return Response(result)

#
# @api_view(['GET'])
# def filter_TodayDeals(request,query):
#     cat_without_spaces = query.replace(" ", "")
#     cache_key = 'todaydealsof'+cat_without_spaces+str(request.GET.get('page'))
#     cache_time = 90500  # time to live in seconds
#     result = cache.get(cache_key)
#
#     if not result:
#
#         try:
#             que = Q()
#
#             que &= Q(SNR_Date__gt=datetime.date.today()-timedelta(days=30)) & Q(SNR_Available__iexact=query) & Q(SNR_Category="Deals")
#
#             data_all = AllProducts.objects.filter(que)
#             try:
#                 pagecount = int(request.GET.get('count'))
#             except:
#                 pagecount = 36
#             paginator = Paginator(data_all, pagecount)
#
#             page = request.GET.get('page')
#             try:
#
#                 data = paginator.page(page)
#             except PageNotAnInteger:
#
#                 data = paginator.page(1)
#             except EmptyPage:
#
#                 data = paginator.page(paginator.num_pages)
#
#             data = product_to_deal(data)
#             # res = serializer.data
#             # res.update('pages_count:', paginator.num_pages())
#             # return Response(res)
#             items = 0
#             pages = 0
#             items = paginator.count
#             pages = paginator.num_pages
#             res = {
#                 'totalItems': items,
#                 'totalPages': pages,
#                 'results': data
#
#             }
#
#             result = res;
#             cache.set(cache_key, result, cache_time)
#             # print "setting cache"+cache_key
#             return Response(res)
#
#         except AllProducts.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         # print "returning from cache"+cache_key
#         return Response(result)
#



@api_view(['GET'])
def FilterALLAppliencesASC(request,query,price1,price2,brand,merchant):   # Sample Code

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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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
       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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

       paginator = Paginator(products, 36)


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
@permission_classes((permissions.AllowAny,))
def getAll_HotDeals(request):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    que=Q()
    dic=request.data
    temp=[]
    limit = page * int(40)
    offset = (page - 1) * int(40)
    my_map = client.get_map("Deal_all").blocking()
    cache_key = 'hot_deals_all' + str(request.GET.get('page'))
      # time to live in seconds
    result = my_map.get(cache_key)

    if result == None:
        with connection.cursor() as cursor:
            main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Active"=True order by random() offset '+str(offset)+' limit '+str(limit)
            fields = [
                "SNR_SKU", "SNR_Title",
                "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                "SNR_ProductURL", "SNR_ImageURL",
                "SNR_Date", "SNR_Category","SNR_Description","SNR_Customer_Rating"
            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_query.format(",".join(out))
            cursor.execute(data_query)
            temp = []
            for i in cursor.fetchall():
                current_item = {}
                for j in range(len(fields)):
                    current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                temp.append(current_item)
            connection.close()
            co = 'Select Count(\'*\') from public.products_active_dailydeals where "SNR_Active"=True'

            with connection.cursor() as cursor:
                cursor.execute(co)
                it = cursor.fetchall()
                it = [i[0] for i in it]
            connection.close()
            totalpages = int(int(it[0]) / int(40))
            per = int(it[0]) % int(40)
            if per != 0:
                totalpages += 1
            res = {
                'results': temp,
                'items': str(it[0]), 'pages': str(totalpages)
            }
            my_map.put(cache_key, res)
            return Response(res, status.HTTP_200_OK)
    else:
        print('in chache')
        return Response(result, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getop_3_HotDeals(request):
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    que=Q()
    dic=request.data
    temp=[]
    limit = page * int(20)
    offset = (page - 1) * int(20)
    with connection.cursor() as cursor:
        main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" IN (\'amazon\',\'ebay\',\'Walmart\') AND "SNR_Active"=True  order by random() offset '+str(offset)+' limit '+str(limit)
        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available","SNR_PriceAfter","SNR_PriceBefore",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category","SNR_Description","SNR_Customer_Rating"
        ]
        out = ['"{0}"'.format(i) for i in fields]
        data_query = main_query.format(",".join(out))
        cursor.execute(data_query)
        temp = []
        for i in cursor.fetchall():
            current_item = {}
            for j in range(len(fields)):
                current_item[fields[j]] = i[j]

            temp.append(current_item)
        connection.close()
        co = 'Select Count(\'*\') FROM products_active_dailydeals Where "SNR_Available" IN (\'amazon\',\'ebay\',\'Walmart\') AND "SNR_Active"=True'

        with connection.cursor() as cursor:
            cursor.execute(co)
            it = cursor.fetchall()
            it = [i[0] for i in it]
        connection.close()
        totalpages = int(int(it[0]) / int(20))
        per = int(it[0]) % int(20)
        if per != 0:
            totalpages += 1
        res = {
            'results': temp,'items': str(it[0]), 'pages': str(totalpages)
        }
        return Response(res,status.HTTP_200_OK)




@api_view(['GET'])
def getAll_CatsDeals(request):
    try:
        data_all = DailyDeals.objects.filter(SNR_Date__date=datetime.date.today()).values('SNR_Category').distinct()
        paginator = Paginator(data_all, 36)
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


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def AddSnrRev(request):
    temp = request.data
    #print temp
    try:
        temp["Product"] = AllProducts.objects.filter(id=temp["Product"])[0]
        new_rev = Product_Reviews(**temp)
        new_rev.SNR_IS_SNR = True
        new_rev.save()
        #print new_rev.id
        return Response({"status": "success"})

    except Exception as e:
        #print e.message
        return Response({"status": "failed"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterProductsRevs(request,query):
    query = query.lower()

    query= "".join(i for i in query if ord(i) < 128)

    query=re.sub('[^A-Za-z0-9]+', ' ', query)

    entry_per_page = 10
    join_statement = 'from products_allproducts INNER JOIN products_product_reviews ON products_allproducts.id = products_product_reviews."Product_id"'
    count_q = 'explain select count(*) %s Where {0}' % (join_statement)

    temp = []
    # temp.append('"SNR_Title" ~* %s')
    temp.append('tsv_title @@ plainto_tsquery(%s)')

    # temp.append('"SNR_CustomerReviews">=0')
    temp = " AND ".join(temp)

    res = {}
    count_q = count_q.format(temp)

    # offset = ' ORDER BY products_allproducts."SNR_Date" DESC LIMIT {0}'.format(entry_per_page)
    offset = ' LIMIT {0}'.format(entry_per_page)

    fields = ["SNR_Title",
        "SNR_ProductURL", "SNR_Available"
    ]

    q = 'Select %s %s Where {0}' % ( "products_allproducts.id," + ",".join(
        ['"{0}"'.format(i) for i in fields]
    ),join_statement)

    f_count = len(fields)

    with connection.cursor() as cursor:
        t1 = time.time()


        cursor.execute(count_q,[query])
        # print count_q
        query_count = cursor.fetchone()[0]
        query_count = patSearch('rows=(\d+)', query_count).group(1)
        query_count = int(query_count)
        # print(query_count)

        if query_count ==0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        pageCount = int(math.ceil( query_count/float(entry_per_page)))
        res['totalItems'] = query_count
        res['totalPages'] = pageCount

        try:
            page = int(request.GET.get('page'))
        except:
            page = 1

        if page > pageCount:
            page = pageCount

        if page > 0:
            offset = ' Order By products_product_reviews."SNR_Date" desc {0} OFFSET {1}'.format(offset, entry_per_page * (page - 1))

        q = q.format(temp) + offset



        # print q
        cursor.execute(q, [query])
        # print "after execute..."


        temp = []
        all_data = {}
        for i in cursor.fetchall():
            current_id = i[0]
            i = i[1:]
            #rev = Product_Reviews.objects.filter(Product__id=current_id)
            #reviews_array = [ProductReview_Serializer(current_rev).data  for current_rev in rev ]

            #current_item = {"Reviews":reviews_array}
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = i[j]

            all_data[current_id] = current_item

            # print current_id

        revs = Product_Reviews.objects.filter(Product__id__in=all_data.iterkeys())
        rev_obj = {}
        for current_rev in revs:
            temp = current_rev.Product.id
            try:
                rev_obj[temp].append(current_rev)
                # print current_rev
            except KeyError:
                rev_obj[temp] = [current_rev]


        temp = []
        for item_id,item_data in rev_obj.iteritems():
            current_item = all_data[item_id]
            reviews_array = [ProductReview_Serializer(current_rev).data  for current_rev in item_data]
            current_item["Reviews"] = reviews_array
            temp.append(current_item)

        res["results"] = temp

        #print time.time() - t1
        return Response(res)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def FilterProducts_RevAI(request,query):

    query = query.lower()

    query= "".join(i for i in query if ord(i) < 128)

    query=re.sub('[^A-Za-z0-9]+', ' ', query)

    # print 'Query isss', query


    entry_per_page = 1
    join_statement = 'from products_allproducts INNER JOIN products_product_review_ai ON products_allproducts.id = products_product_review_ai."Product_id"'
    count_q = 'explain select count(*) %s Where {0}' % (join_statement)

    temp = []
    temp.append('tsv_title @@ plainto_tsquery(%s)')
    # temp.append('"SNR_Title" ~* %s')
    temp = " AND ".join(temp)

    res = {}
    count_q = count_q.format(temp)




    offset = ' ORDER BY products_allproducts."SNR_Date" DESC LIMIT {0}'.format(entry_per_page)

    fields = ["SNR_Title",
        "SNR_ProductURL", "SNR_Available"
    ]

    q = 'Select %s %s Where {0}' % ( "products_allproducts.id," + ",".join(
        ['"{0}"'.format(i) for i in fields]
    ),join_statement)

    f_count = len(fields)

    with connection.cursor() as cursor:
        t1 = time.time()
        cursor.execute(count_q,[query])
        query_count = cursor.fetchone()[0]
        query_count=patSearch('rows=(\d+)',query_count).group(1)
        query_count=int(query_count)
        print(query_count)

        # query_count = cursor.fetchone()[0]
        # print count_q
        if query_count ==0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        pageCount = int(math.ceil( query_count/float(entry_per_page)))
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
        # print "full query"
        # print q
        cursor.execute(q, [query])

        temp = []
        all_data = {}
        for i in cursor.fetchall():
            current_id = i[0]
            i = i[1:]
            # print i[0]
            #rev = Product_Reviews.objects.filter(Product__id=current_id)
            #reviews_array = [ProductReview_Serializer(current_rev).data  for current_rev in rev ]

            #current_item = {"Reviews":reviews_array}
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = i[j]

            all_data[current_id] = current_item

        revs = Product_Review_AI.objects.filter(Product__id__in=all_data.iterkeys())
        rev_obj = {}
        for current_rev in revs:
            temp = current_rev.Product.id
            rev_obj[temp] = current_rev

        temp = []
        for item_id,item_data in rev_obj.iteritems():
            current_item = all_data[item_id]
            current_item["Reviews_AI"] = item_data.SNR_Review_Info
            temp.append(current_item)

        res["results"] = temp

        #print time.time() - t1
        return Response(res)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Products_Rec(request,query):
    total_rec = 20
    our_item = AllProducts.objects.filter(SNR_SKU=query)[0]
    margin = 0.36
    price = float(our_item.SNR_Price)
    print(price)
    lower_price = price*(1-margin)
    upper_price = price * (1 + margin)
    print(lower_price)


    filter_q = Q(SNR_SubCategory=our_item.SNR_SubCategory)
    for i in re.split("\W+",our_item.SNR_Category):
        i = re.sub("\d+","",i)
        i = i.strip()
        if len(i)>2:
            filter_q = filter_q | Q(SNR_SubCategory__icontains=i)

    products = AllProducts.objects.filter(filter_q).filter(
                                    SNR_Price__lte=upper_price,
                                    SNR_Price__gte=lower_price,
                                    SNR_Category=our_item.SNR_Category,
                                      ).exclude(SNR_SKU=query)


    paginator = Paginator(products, total_rec)

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

    serializer_context = {'request': request}
    product_serilizer = AllProducts_Serializer(data, many=True, context=serializer_context)


@api_view(['GET'])
def CategoryAll(request,category):
    res = {}
    main_query = 'Select {0} from products_allproducts Where "SNR_Category" ILIKE %s'
    count_query = main_query.format("count(*)")
    entry_per_page = 36
    offset = ' ORDER BY "SNR_Date" DESC LIMIT {0}'.format(entry_per_page)

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

    data_query = main_query.format(",".join(out))

    f_count = len(fields)

    with connection.cursor() as cursor:
        cursor.execute(count_query, [category])
        query_count = cursor.fetchone()[0]
        # print query_count
        if query_count == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)

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

        data_query = data_query+ offset
        cursor.execute(data_query, [category])
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
@permission_classes((permissions.AllowAny,))
def get_singleproduct(request,id):
    if request.method == 'GET':
        data = AllProductsPartition.objects.get(id = id)
        serializer = AllProducts_Serializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_singleproductdeal(request,id):
    if request.method == 'GET':
        data = Active_DailyDeals.objects.get(id = id)
        serializer = Active_DailyDeals_Serializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_singleproduct1(request,id):

    # cache_key = 'singleproductcache_for_xx'+str(id)
    # cache_time = 90500  # time to live in seconds
    # result = cache.get(cache_key)
    #
    # if not result:
        temp=[]
        main_data_query = 'Select {0} from public.products_allproductspartition  where  id='+str(id)+''
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
        data_query = main_data_query.format(",".join(out),)
        print("main query", data_query)
        f_count = len(fields)
        with connection.cursor() as cursor:
            cursor.execute(data_query)
            for i in cursor.fetchall():
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                # temp.append(current_item)
        # data = AllProductsPartition.objects.get(id = id)
        # serializer = AllProducts_Serializer(data)

        # cache.set(cache_key, temp, cache_time)

        return Response(current_item, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def subCategoryall_explainByID(request,category,subcategory):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    # cat_without_spaces=category.replace(" ","" )
    res = {}
    main_query = 'explain Select {0} from products_allproductspartition Where "SNR_CatID" = %s AND "SNR_SubCatID" = %s'
    main_data_query = 'Select {0} from products_allproductspartition Where "SNR_CatID" = %s AND "SNR_SubCatID" = %s'
    count_query = main_query.format("*")

    try:
        price1 = int(request.GET.get('low'))
    except:
        price1=-1
    try:
        price2 = int(request.GET.get('high'))
    except:
        price2=-1

    if (price1 != -1 and price2 != -1):
        # print 'added price'
        que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
        main_data_query=main_data_query+que

    try:
        merchant = (request.GET.get('merchant'))
        if(merchant!='undefined' and merchant!=None) :
            que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
            main_data_query = main_data_query + que


    except:
        merchant = -1

    try:
        brand = (request.GET.get('brand'))
        if( brand!='undefined' and brand!=None):
            que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
            main_data_query=main_data_query+que


    except:
        brand=-1


    try:
        sub = (request.GET.get('sub'))
        if ( sub!='undefined' and sub!=None):
            sub = sub.replace('(', '\(')
            sub = sub.replace(')', '\)')
            sub = sub.replace("'", "''")

            que = (' AND "SNR_SubCategory" ilike \'%s\'' % (sub))
            main_data_query = main_data_query + que


    except:
        sub=-1
        # print main_data_query

    # print main_data_query

    try:
        pagecount = int(request.GET.get('count'))
    except:
        pagecount = 36
    offset = ' LIMIT {0}'.format(pagecount)


    fields = [
        "SNR_SKU", "SNR_Title",
        "SNR_ModelNo", "SNR_Brand",
        "SNR_UPC", "SNR_Available",
        "SNR_ProductURL", "SNR_ImageURL","id",
        "SNR_Description", "SNR_isShow",
        "SNR_Date", "SNR_Category",
        "SNR_Condition","SNR_PriceBefore",
        "SNR_CustomerReviews", "SNR_Price",
        "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]

    extra_fields = []
    fields.extend(extra_fields)

    out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

    data_query = main_data_query.format(",".join(out))
    data_query = data_query + ' ORDER BY "id" DESC'

    f_count = len(fields)

    with connection.cursor() as cursor:
        cursor.execute(count_query, [category,subcategory])
        # print count_query
        query_count = cursor.fetchone()[0]
        print(query_count)
        # print(query_cat)
        query_count = patSearch('rows=(\d+)', query_count).group(1)
        query_count = int(query_count)
        print(query_count)

        # print query_count
        if query_count == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)

        pageCount = int(math.ceil(query_count / float(pagecount)))
        res['totalItems'] = query_count
        res['totalPages'] = pageCount

        try:
            page = int(request.GET.get('page'))
        except:
            page = 1

        if page > pageCount:
            page = pageCount

        if page > 0:
            offset = "{0} OFFSET {1}".format(offset, pagecount * (page - 1))

        data_query = data_query+ offset
        # print data_query
        cursor.execute(data_query, [category,subcategory])
        temp = []
        # print cursor.fetchall()
        for i in cursor.fetchall():

            # if i[5] > 0:
            current_item = {}
            for j in range(f_count):

                current_item[fields[j]] = i[j]

            temp.append(current_item)

        res["results"] = temp
        result = res
        # print "setting cache for "+cache_key

        return Response(res,status=status.HTTP_200_OK)



@api_view(['GET'])
def categoryall_explainByID(request,category):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    # cat_without_spaces=category.replace(" ","" )
    cache_key = 'categorycache_for_'+category+str(page)+str((request.GET.get('low')))+str((request.GET.get('high')))+str(request.GET.get('merchant')).replace(" ","")+str(request.GET.get('brand')).replace(" ","")+str(request.GET.get('sub')).replace(" ","")+str(request.GET.get('count'))+str(request.GET.get('sort'))
    cache_time = 3600  # time to live in seconds
    result = cache.get(cache_key)
    # print 'cache crossed'

    if not result:
        # lst =[]
        # Cat_Map = {
        #     'Baby & Toddler':['Activities & Gear',"Baby & child care","Baby Essentials", "Baby Registry"],
        #     'Health & Beauty':["All beauty","All health & household","Beauty",],
        #     'Sporting Goods':["All sports & fitness",],
        #     'Electronics':["Appliances","Batteries & Accessories","Bluetooth & wireless speakers"],
        #     'Arts & Entertainment':["Arts crafts & sewing","Arts, Crafts & Sewing","Books"],
        #     'Media':["Audio"],
        #     'Furniture':[],
        #     'Mature': [],
        #     'Religious & Ceremonial': ["Birthday Shop",],
        #     'Vehicles & Parts':["Auto & Tires","Auto Electronics","Auto Body Repair","Auto Detailing & Car Care","Auto Exterior","Auto Interior","Automotive parts & accessories","Automotive tools & equipment",
        #                         "Auto Replacement Parts","Bikes",],
        #     'Food, Beverages & Tobacco': [],
        #     'Home & Garden': ["Bath & Body","Better Homes & Gardens",],
        #     'Luggage & Bags': [],Me data migration bna ke push krun g us ke
        #     'Business & Industrial': [],
        #     'Hardware': [],
        #     'Office Supplies': [],
        #     'Cameras & Optics': [],
        #     'Animals & Pet Supplies': ["Birds",],
        #     'Software': [],
        #     'Apparel & Accessories': ["Baby","Baby Clothing","Boys",],
        #     'Toys & Games': []
        #
        # }
        #
        # with connection.cursor() as cursor:
        #     cursor.execute('select distinct("SNR_Category") from products_allproducts')
        #     for i in cursor.fetchall():
        #         lst.append(i)
        #     lst.append(len(lst))
        #
        # # data = AllProducts.objects.filter(SNR_Category= category).order_by('SNR_Date')[0:36]
        # # serializer = AllProducts_Serializer(data, many=True)
        # return Response(lst, status=status.HTTP_200_OK)

        res = {}
        main_query = 'explain Select {0} from products_allproducts Where "SNR_CatID" = %s'
        main_data_query = 'Select {0} from products_allproducts Where "SNR_CatID" = %s'
        count_query = main_query.format("*")

        try:
            sub = int(request.GET.get('sub'))
            if ( sub!='undefined' and sub!=None):
            #     sub = sub.replace('(', '\(')
            #     sub = sub.replace(')', '\)')
            #     sub = sub.replace("'", "''")

                que = (' AND "SNR_SubCatID" = %s' % (sub))
                main_data_query = main_data_query + que


        except:
            sub=-1
            # print main_data_query

        try:
            price1 = int(request.GET.get('low'))
        except:
            price1=-1
        try:
            price2 = int(request.GET.get('high'))
        except:
            price2=-1

        if (price1 != -1 and price2 != -1):
            # print 'added price'
            que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
            main_data_query=main_data_query+que

        try:
            merchant = (request.GET.get('merchant'))
            if(merchant!='undefined' and merchant!=None) :
                que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
                main_data_query = main_data_query + que


        except:
            merchant = -1


        try:
            brand = (request.GET.get('brand'))
            if( brand!='undefined' and brand!=None):
                que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
                main_data_query=main_data_query+que


        except:
            brand=-1


        # print main_data_query

        try:
            pagecount = int(request.GET.get('count'))
        except:
            pagecount = 36
        offset = ' LIMIT {0}'.format(pagecount)


        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL","id",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition","SNR_PriceBefore",
            "SNR_CustomerReviews", "SNR_Price",
            "SNR_SubCategory"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        data_query = main_data_query.format(",".join(out))

        f_count = len(fields)

        with connection.cursor() as cursor:
            cursor.execute(count_query, [category])
            # print count_query
            query_count = cursor.fetchone()[0]
            print(query_count)
            # print(query_cat)
            query_count = patSearch('rows=(\d+)', query_count).group(1)
            query_count = int(query_count)
            print(query_count)

            # print query_count
            if query_count == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)

            pageCount = int(math.ceil(query_count / float(pagecount)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, pagecount * (page - 1))

            try:
                sort = (request.GET.get('sort'))
                if (sort != 'undefined' and sort != None):
                    que = (' ORDER BY "SNR_Price" %s , id desc' % (sort))
                    data_query = data_query + que
            except:
                sort = -1

            data_query = data_query+ offset
            print(data_query)
            cursor.execute(data_query, [category])
            temp = []
            # print cursor.fetchall()
            for i in cursor.fetchall():

                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):

                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp
            result = res
            cache.set(cache_key, result, cache_time)
            # print "setting cache for "+cache_key

            return Response(res,status=status.HTTP_200_OK)
    else:
        # print "returning from cache " + cache_key

        return Response(result)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def categoryall_explain(request,category):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    cat_without_spaces=category.replace(" ","" )
    cache_key = 'categorycache_for_'+cat_without_spaces+str(page)+str((request.GET.get('low')))+str((request.GET.get('high')))+str(request.GET.get('merchant')).replace(" ","")+str(request.GET.get('brand')).replace(" ","")+str(request.GET.get('sub')).replace(" ","")+str(request.GET.get('count'))
    cache_time = 3600  # time to live in seconds
    result = cache.get(cache_key)
    # print 'cache crossed'

    if not result:

        res = {}
        main_query = 'explain Select {0} from products_allproducts_testing Where "SNR_Category_Main" = %s'
        main_data_query = 'Select {0} from products_allproducts_testing Where "SNR_Category_Main" = %s'
        count_query = main_query.format("*")

        try:
            price1 = int(request.GET.get('low'))
            # print 'low issss', price1
        except:
            price1=-1
        try:
            price2 = int(request.GET.get('high'))
        except:
            price2=-1

        if (price1 != -1 and price2 != -1):
            # print 'added price'
            que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
            main_data_query=main_data_query+que

        try:
            merchant = (request.GET.get('merchant'))
            if(merchant!='undefined' and merchant!=None) :
                que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
                main_data_query = main_data_query + que


        except:
            merchant = -1

        try:
            brand = (request.GET.get('brand'))
            if( brand!='undefined' and brand!=None):
                que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
                main_data_query=main_data_query+que


        except:
            brand=-1


        try:
            sub = (request.GET.get('sub'))
            if ( sub!='undefined' and sub!=None):
                sub = sub.replace('(', '\(')
                sub = sub.replace(')', '\)')
                sub = sub.replace("'", "''")

                que = (' AND "SNR_SubCategory" ilike \'%s\'' % (sub))
                main_data_query = main_data_query + que


        except:
            sub=-1
            # print main_data_query

        # print main_data_query

        try:
            pagecount = int(request.GET.get('count'))
        except:
            pagecount = 36
        offset = ' LIMIT {0}'.format(pagecount)


        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL","id",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition","SNR_PriceBefore",
            "SNR_CustomerReviews", "SNR_Price",
            "SNR_SubCategory"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        data_query = main_data_query.format(",".join(out))

        f_count = len(fields)

        with connection.cursor() as cursor:
            cursor.execute(count_query, [category])
            # print count_query
            query_count = cursor.fetchone()[0]
            print(query_count)
            # print(query_cat)
            query_count = patSearch('rows=(\d+)', query_count).group(1)
            query_count = int(query_count)
            print(query_count)

            # print query_count
            if query_count == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)

            pageCount = int(math.ceil(query_count / float(pagecount)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount

            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, pagecount * (page - 1))

            data_query = data_query+ offset
            # print data_query
            cursor.execute(data_query, [category])
            temp = []
            # print cursor.fetchall()
            for i in cursor.fetchall():

                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):

                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp
            result = res
            cache.set(cache_key, result, cache_time)
            # print "setting cache for "+cache_key

            return Response(res,status=status.HTTP_200_OK)
    else:
        # print "returning from cache " + cache_key

        return Response(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def testingRawData(request):
        with connection.cursor() as cursor:
            # cursor.execute('SELECT DISTINCT "SNR_Available" FROM products_allproducts Where "SNR_Category" = %s',[category])
            res = {}
            result = []
            fields = [
                "SNR_CatName"
            ]
            cursor.execute('SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
            temp = []
            temp2 = []
            # print cursor.fetchall()
            for i in cursor.fetchall():

                cursor.execute('SELECT "Cat_ID","SNR_SubCatName" FROM products_main_categories WHERE "SNR_CatName" = %s AND "SNR_TriCatName" IS NULL AND "SNR_SubCatName" IS NOT NULL order by "SNR_SubCatName"', [i[1]])

                for j in cursor.fetchall():
                    temp2.append({'id': j[0], 'SubCat': j[1]})

                temp.append({'id':i[0],'Category':i[1],'path':i[2], 'SubCategories':temp2})
                temp2 = []
            connection.close()
            # for i in temp:

            res["Categories"] = temp
            result = res
            return Response(res)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CountProduct(request,vendor):
    res = {}
    main_query = 'Select count(*) from products_allproducts Where "SNR_Available" ILIKE \'%s\'' % (vendor)
    # print main_query

    with connection.cursor() as cursor:
        cursor.execute(main_query, [vendor])
        # print main_query
        query_count = cursor.fetchone()[0]
        print(query_count)
        res={"count":query_count}
        return Response(res,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CountProductReviews(request):
    res = {}
    main_query = 'Select count(*) from products_product_reviews'
    # print main_query

    with connection.cursor() as cursor:
        cursor.execute(main_query)
        # print main_query
        query_count = cursor.fetchone()[0]
        print(query_count)
        res={"count":query_count}
        return Response(res,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CategoryAll_explainCount(request,category):
    cat_without_spaces = category.replace(" ", "")
    cache_key = 'category_count_cache_for_' + cat_without_spaces
    cache_time = 22500  # time to live in seconds
    result = cache.get(cache_key)

    if not result:

        res = {}
        main_query = 'Select count(*) from products_allproducts Where "SNR_Category" = %s'
        main_data_query = 'Select {0} from products_allproducts Where "SNR_Category" = %s'
        # count_query = main_query.format("*")

        try:
            price1 = int(request.GET.get('low'))
        except:
            price1=-1
        try:
            price2 = int(request.GET.get('high'))
        except:
            price2=-1

        if (price1 != -1 and price2 != -1):
            # print 'added price'
            que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
            main_query=main_query+que
            # print main_query
        try:
            merchant = (request.GET.get('merchant'))
            if(merchant!='undefined'):
                que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
                main_data_query = main_data_query + que


        except:
            merchant = -1

        try:
            brand = (request.GET.get('brand'))
            if( brand!='undefined'):
                que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
                main_data_query=main_data_query+que


        except:
            brand=-1


        try:
            sub = (request.GET.get('sub'))
            if ( sub!='undefined'):
                que = (' AND "SNR_SubCategory" ilike \'%s\'' % (sub))
                main_data_query = main_data_query + que


        except:
            sub=-1
            # print main_data_query

        # print main_query

        try:
            pagecount = int(request.GET.get('count'))
        except:
            pagecount = 36
        offset = ' LIMIT {0}'.format(pagecount)


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


        with connection.cursor() as cursor:
            cursor.execute(main_query, [category])
            # print main_query
            query_count = cursor.fetchone()[0]
            print(query_count)
            # print(query_cat)
            # query_count = patSearch('rows=(\d+)', query_count).group(1)
            # query_count = int(query_count)
            # print(query_count)

            # print query_count
            if query_count == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)

            pageCount = int(math.ceil(query_count / float(pagecount)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount
            result = res
            cache.set(cache_key, result, cache_time)
            # print "setting cache for " + cache_key
            return Response(res,status=status.HTTP_200_OK)
    else:
        # print "returning from cache " + cache_key

        return Response(result)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CategoryAll_explain_DESC(request,category):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    # cat_without_spaces = category.replace(" ", "")
    cache_key = 'category_cache_descfor_'+category+str(page)+str((request.GET.get('low')))+str((request.GET.get('high')))+str(request.GET.get('merchant')).replace(" ","")+str(request.GET.get('brand')).replace(" ","")+str(request.GET.get('sub')).replace(" ","")+str(request.GET.get('count'))

    cache_time = 90500  # time to live in seconds
    result = cache.get(cache_key)
    if not result:

        res = {}
        # print
        main_query = 'explain Select {0} from products_allproductspartition Where "SNR_CatID" = %s'
        main_data_query = 'Select {0} from products_allproductspartition Where "SNR_CatID" = %s'
        count_query = main_query.format("*")
        try:
            entry_per_page = int(request.GET.get('count'))
        except:
            entry_per_page = 36

        try:
            price1 = int(request.GET.get('low'))
        except:
            price1=-1
        try:
            price2 = int(request.GET.get('high'))
        except:
            price2=-1

        if (price1 != -1 and price2 != -1):
            # print 'added price'
            que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
            main_data_query=main_data_query+que

        try:
            merchant = (request.GET.get('merchant'))
            if(merchant!='undefined' and merchant!=None) :
                que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
                main_data_query = main_data_query + que


        except:
            merchant = -1

        try:
            brand = (request.GET.get('brand'))
            if( brand!='undefined' and brand!=None):
                que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
                main_data_query=main_data_query+que


        except:
            brand=-1


        try:
            sub = (request.GET.get('sub'))
            if ( sub!='undefined' and sub!=None):
                que = (' AND "SNR_SubCategory" ilike \'%s\'' % (sub))
                main_data_query = main_data_query + que


        except:
            sub=-1
            # print main_data_query


        try:
            sub = (request.GET.get('date'))
            if ( sub!='undefined' and sub!=None):
                if(sub.lower()=='desc'):
                    # print "date...."
                    offset = ' ORDER BY "SNR_Date" DESC LIMIT {0}'.format(entry_per_page)
                else:
                    # print "else"
                    offset = ' ORDER BY "SNR_Price" DESC LIMIT {0}'.format(entry_per_page)
            else:
                # print "undefinede else"
                offset = ' ORDER BY "SNR_Price" DESC LIMIT {0}'.format(entry_per_page)




        except:
            # print "except"
            offset = ' ORDER BY "SNR_Price" DESC LIMIT {0}'.format(entry_per_page)



        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Description", "SNR_isShow","id",
            "SNR_Date", "SNR_Category","SNR_Price",
            "SNR_Condition", "SNR_SubCategory","SNR_PriceBefore", "SNR_CustomerReviews"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        data_query = main_data_query.format(",".join(out))

        f_count = len(fields)

        with connection.cursor() as cursor:
            cursor.execute(count_query, [category])
            query_count = cursor.fetchone()[0]
            print(query_count)
            # print(query_cat)
            query_count = patSearch('rows=(\d+)', query_count).group(1)
            query_count = int(query_count)
            print(query_count)

            # print query_count
            if query_count == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)

            pageCount = int(math.ceil(query_count / float(entry_per_page)))
            res['totalItems'] = query_count
            res['totalPages'] = pageCount



            if page > pageCount:
                page = pageCount

            if page > 0:
                offset = "{0} OFFSET {1}".format(offset, entry_per_page * (page - 1))

            data_query = data_query+ offset

            # print data_query
            # print data_query
            cursor.execute(data_query, [category])
            temp = []
            for i in cursor.fetchall():

                # if i[5] > 0:
                current_item = {}
                for j in range(f_count):

                    current_item[fields[j]] = i[j]

                temp.append(current_item)

            res["results"] = temp



            result = res
            cache.set(cache_key, result, cache_time)
            # print "setting cache for " + cache_key

            return Response(res, status=status.HTTP_200_OK)
    else:
        # print "returning from cache " + cache_key

        return Response(result)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def CategoryAll_explain_ASC(request,category):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    # cat_without_spaces = category.replace(" ", "")
    cache_key = 'category_cache_ascfor_'+category+str(page)+str((request.GET.get('low')))+str((request.GET.get('high')))+str(request.GET.get('merchant')).replace(" ","")+str(request.GET.get('brand')).replace(" ","")+str(request.GET.get('sub')).replace(" ","")+str(request.GET.get('count'))


    cache_time = 90500  # time to live in seconds
    result = cache.get(cache_key)

    if not result:

        res = {}
        main_query = 'explain Select {0} from products_allproductspartition Where "SNR_CatID" = %s'
        main_data_query = 'Select {0} from products_allproductspartition Where "SNR_CatID" = %s'
        count_query = main_query.format("*")
        try:
            entry_per_page = int(request.GET.get('count'))
        except:
            entry_per_page = 36
        try:
            price1 = int(request.GET.get('low'))
        except:
            price1=-1;
        try:
            price2 = int(request.GET.get('high'))
        except:
            price2=-1;

        if (price1 != -1 and price2 != -1):
            # print 'added price'
            que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
            main_data_query=main_data_query+que;

        try:
            merchant = (request.GET.get('merchant'))
            if(merchant!='undefined' and merchant!=None) :
                que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
                main_data_query = main_data_query + que;


        except:
            merchant = -1

        try:
            brand = (request.GET.get('brand'))
            if( brand!='undefined' and brand!=None):
                que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
                main_data_query=main_data_query+que;


        except:
            brand=-1;


        try:
            sub = (request.GET.get('sub'))
            if ( sub!='undefined' and sub!=None):
                que = (' AND "SNR_SubCategory" ilike \'%s\'' % (sub))
                main_data_query = main_data_query + que;


        except:
            sub=-1;
            # print main_data_query


        try:
            sub = (request.GET.get('date'))
            if ( sub!='undefined' and sub!=None):
                if(sub.lower()=='asc'):
                    offset = ' ORDER BY "SNR_Date" ASC LIMIT {0}'.format(entry_per_page)
                else:
                    offset = ' ORDER BY "SNR_Price" ASC LIMIT {0}'.format(entry_per_page)
            else:
                offset = ' ORDER BY "SNR_Price" ASC LIMIT {0}'.format(entry_per_page)




        except:
            offset = ' ORDER BY "SNR_Price" ASC LIMIT {0}'.format(entry_per_page)


        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL","id",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category","SNR_Price",
            "SNR_Condition", "SNR_SubCategory"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = ["SNR_PriceBefore", "SNR_CustomerReviews" ]
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])

        data_query = main_data_query.format(",".join(out))

        f_count = len(fields)

        with connection.cursor() as cursor:
            cursor.execute(count_query, [category])
            query_count = cursor.fetchone()[0]
            print(query_count)
            # print(query_cat)
            query_count = patSearch('rows=(\d+)', query_count).group(1)
            query_count = int(query_count)
            print(query_count)

            # print query_count
            if query_count == 0:
                return Response(status=status.HTTP_204_NO_CONTENT)

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

            data_query = data_query+ offset

            # print data_query
            # print data_query
            cursor.execute(data_query, [category])
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
            # print "setting cache for " + cache_key

            return Response(res, status=status.HTTP_200_OK)
    else:
        # print "returning from cache " + cache_key

        return Response(result)


# Create your tests here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def StoreAll(request,store):

   try:
       #print store
       products = AllProducts.objects.filter(SNR_Available__iexact=store)


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

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

# Create your tests here.
@api_view(['GET'])
def CategoryAll_DESC(request,category):


   try:
       products = AllProducts.objects.filter(SNR_Category__iexact=category).order_by("-SNR_Price")

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

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass

@api_view(['GET'])
def CategoryAll_ASC(request,category):


   try:
       products = AllProducts.objects.filter(SNR_Category__iexact=category).order_by("SNR_Price")

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

       return Response(status=status.HTTP_404_NOT_FOUND)


   pass



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getAll_BrandsDeals(request):
    cache_key = 'todaydealsbrands'
    cache_time = 90500  # time to live in seconds
    result = cache.get(cache_key)

    if not result:


        try:
            cats=[]
            query_data = 'SELECT DISTINCT "SNR_Available" FROM products_dailydeals where "SNR_Available" IS NOT NULL ORDER BY "SNR_Available" ASC'

            with connection.cursor() as cursor:
                cursor.execute(query_data)
                # temp = cursor.fetchall()
                # if not temp:
                #     return Response(empty_brands)
                # # out[ mappings[i] ] = [{i:j[0]} for j in cursor.fetchall()]

                # print temp
                for i in cursor.fetchall():
                    cats.append(i[0])


                # cats = list(set(i[0]) for i in temp)
                # cats = list(temp)
                # cats.sort()

                res={"results":cats}
                result = res
            # data_all = AllProducts.objects.filter(SNR_Category__exact="Deals").values('SNR_Available').distinct()
            # # SNR_Date__gt = datetime.date.today() - timedelta(days=30),
            # paginator = Paginator(data_all, 36)
            # page = request.GET.get('page')
            # vendors=[]
            # for vendor in data_all:
            #     if vendor['SNR_Available'] != 'Samsclub':
            #         vendors.append(vendor)
            # print vendors
            # try:
            #
            #     data = paginator.page(page)
            # except PageNotAnInteger:
            #
            #     data = paginator.page(1)
            # except EmptyPage:
            #
            #     data = paginator.page(paginator.num_pages)
            #
            # items = paginator.count
            # pages = paginator.num_pages
            # res = {
            #     'totalItems': items,
            #     'totalPages': pages,
            #     'results': vendors
            #
            # }
            # cache.set(cache_key, result, cache_time)
            # # print "setting cache" + cache_key
            return Response(res)

        except AllProducts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        # # print "returning from cache" + cache_key
        return Response(result)


from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from django.template.loader import get_template

from django.contrib.auth.models import User
import itertools
import datetime
today = datetime.date.today()

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
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
        message = get_template('permotion.html').render({'value':deals,'hotdeals':hotDeals})


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
        #     ### print "false"

        return Response("", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def product_to_deal(arr):

    deals_arr = []

    attr = list({
    "SNR_Title": "King Service Holdings Inc Upper Bounce UBSF01-15 15 Ft Trampoline & Enclosure Set equipped with Upper Bounce Easy Assemble Feature",
    "SNR_Category": "Trampolines",
    "SNR_ImageURL": "http://c.shld.net/rpx/i/s/i/spin/10143968/prod_16351736912",
    "SNR_SKU": "KM05248420000P",
    "SNR_ProductURL": "http://www.sears.com/upper-bounce-15-ft-trampoline-enclosure-set-equipped/p-05248420000P",

    "SNR_Available": "Kmart",
    "SNR_Date": "2018-03-16T02:47:18.770469Z"
    }.iterkeys())

    for current_deal in arr:
        deal = {}
        for at in attr:
            deal[at] = getattr(current_deal, at)
        deal["SNR_PriceAfter"] = str(current_deal.SNR_Price)
        deal["SNR_PriceBefore"] = str(current_deal.SNR_PriceBefore)
        deals_arr.append(deal)

    return deals_arr

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getAll_Deals(request):
    try:
        data_all = AllProducts.objects.filter(SNR_Category="Deals")
        paginator = Paginator(data_all, 36)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        data = product_to_deal(data)
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
            'results': data

        }
        return Response(res)

    except AllProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getproductsforScrapping(request,category):
    # category=category.replace("'","''")
    try:

        data_all = AllProducts.objects.filter(SNR_Available__iexact=category)
        # print data_all
        paginator = Paginator(data_all, 100)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)


        serializer_context = {'request': request}
        serializer = AllProductsComplete_Serializer(data, many=True, context=serializer_context)

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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(data_all, 36)
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
        paginator = Paginator(laptopdata_all, 36)
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
        # #print serializer

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
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def InsertData(request):
    if request.method == 'PUT':

        serializer = AllProducts_Serializer(data=request.data)
        # print serializer

        # # print "inserting"
        if serializer.is_valid():
            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])

            serializer.save()
            # print serializer
            print ('--------inserted----------')

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            # print serializer.errors
            return Response(serializer.errors)

    else:

        # # print "bad request"
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def InsertProductReviews(request):
    if request.method == 'PUT':

        serializer = Product_Reviews_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])

            serializer.save()
            # print serializer
            print ('--------')

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:

            # print serializer.error_messages
            return Response(serializer.errors)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_Clothes(request):
    if request.method == 'POST':

        serializer = Clothes_Serializer(data=request.data)
        # #print serializer

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
        # #print serializer

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
        # #print serializer

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
        # #print serializer

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
        # #print serializer

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
        # #print serializer

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
        # #print serializer

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

empty_brands = {"brands":[]}
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def GetMerchantsCategories(request,category):
    q = 'Select Distinct "SNR_Available" from products_allproducts_'+str(category)+' WHERE "SNR_Available" is not NULL'
    temp = []
    try:

        with connection.cursor() as cursor:
            cursor.execute(q)
            temp = cursor.fetchall()
            res={"Merchants": temp}
            connection.close()
            result = res;
            # # print "setting cache for " + cache_key
            return Response(res)
    except:
        return Response('something went wrong')



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def GetBrandsCategories(request,category):
    q = 'Select Distinct "SNR_Brand" from products_allproducts_'+str(category)+' Where "SNR_Brand" IS NOT NULL limit 20'
    try:
        with connection.cursor() as cursor:
            cursor.execute(q)
            temp = cursor.fetchall()
            cats = list(temp)
            connection.close()
            res={"Brands": cats}
            result = res;
            return Response(res)
    except:

        return Response(empty_brands)





@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def GetSubCatsCategories(request,category):
    q = 'Select Distinct "SNR_SubCatName", "Cat_ID" from products_main_categories Where "SNR_SubCatName" IS NOT NULL AND "SNR_TriCatName" IS NULL AND "SNR_CatName" = (select "SNR_CatName" from products_main_categories where "Cat_ID" = \'%s\')' % category

    # print q
    cats =[]
    try:

        with connection.cursor() as cursor:
            cursor.execute(q)
            for i in cursor.fetchall():
                cats.append({'SubCat': i[0], 'id':i[1]})
            connection.close()

            res={"SubCategories":cats}
            result = res
            return Response(res)
    except:

        return Response(empty_brands)


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


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def filter(request,id,item):          # Sample Code
    if request.method == 'POST':

        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        dic = request.data
        que = Q()
        if 'minprice' in dic and 'maxprice' in dic:
            minprice=request.data['minprice']
            maxprice=request.data['maxprice']
            que &= Q(SNR_Price__lte=minprice, SNR_Price__gte=maxprice)
        else:
            minprice='undefined'
            maxprice='undefined'
        if 'merchant' in dic:
            merchant=request.data['merchant']
            que &= Q(SNR_Available=merchant)
        else:
            merchant='undefined'
        if 'brand' in dic:
            brand=request.data['brand']
            que &= Q(SNR_Brand=brand)
        else:
            brand='undefined'
        if 'sub' in dic:
            sub=request.data['sub']
            que &= Q(SNR_Brand=sub)
        else:
            sub='undefined'
        cache_key = 'categorycache_for_' + id + str(page) + str(minprice) + str(maxprice) + str(merchant).replace(" ", "") + str(brand).replace(" ", "") + str(sub).replace(" ", "") + str(
            item)
        cache_time = 3600  # time to live in seconds
        result = cache.get(cache_key)
        if not result:
            print(page)
            items = page * int(item)
            offset = (page - 1) * int(item)
            if 'sort' in dic:
                if request.data['sort']=='ASC':

                    re=AllProducts.objects.filter(SNR_CatID=int(id)).filter(que).values('SNR_Title','SNR_Brand','SNR_Available','SNR_SKU','SNR_ModelNo','SNR_UPC','SNR_ProductURL','SNR_ImageURL','SNR_SubCategory',
                                                                                'SNR_Price','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition',
                                                                                'SNR_Category','SNR_Date','SNR_Description','SNR_isShow','id').order_by('SNR_Price','-id')[offset:items]
                if request.data['sort'] == 'DSC':
                    re = AllProducts.objects.filter(SNR_CatID=int(id)).filter(que).values('SNR_Title', 'SNR_Brand',
                                                                                          'SNR_Available', 'SNR_SKU',
                                                                                          'SNR_ModelNo', 'SNR_UPC',
                                                                                          'SNR_ProductURL',
                                                                                          'SNR_ImageURL',
                                                                                          'SNR_SubCategory',
                                                                                          'SNR_Price',
                                                                                          'SNR_CustomerReviews',
                                                                                          'SNR_PriceBefore',
                                                                                          'SNR_Condition',
                                                                                          'SNR_Category', 'SNR_Date',
                                                                                          'SNR_Description',
                                                                                          'SNR_isShow', 'id').order_by('-SNR_Price', '-id')[offset:items]
            else:

                re = AllProducts.objects.filter(SNR_CatID=int(id)).filter(que).values('SNR_Title', 'SNR_Brand',
                                                                                          'SNR_Available', 'SNR_SKU',
                                                                                          'SNR_ModelNo', 'SNR_UPC',
                                                                                          'SNR_ProductURL',
                                                                                          'SNR_ImageURL',
                                                                                          'SNR_SubCategory',
                                                                                          'SNR_Price',
                                                                                          'SNR_CustomerReviews',
                                                                                          'SNR_PriceBefore',
                                                                                          'SNR_Condition',
                                                                                          'SNR_Category', 'SNR_Date',
                                                                                          'SNR_Description',
                                                                                          'SNR_isShow', 'id').order_by('-id')[offset:items]
            # totalitems = int(AllProducts.objects.filter(SNR_CatID=int(id)).filter(que).count())
            # totalpages = int(totalitems / int(item))
            # per = totalitems % int(item)
            # if per != 0:
            #     totalpages += 1
            res={
                'result':re,
                'totalitems':0,
                'totalpages':0
            }
            cache.set(cache_key, res, cache_time)
            return Response(res,status.HTTP_200_OK)
        else:
            return Response(result, status.HTTP_200_OK)

@api_view(['POST','GET'])
@permission_classes((permissions.AllowAny,))
def category_Home(request,category):
    if request.method == 'GET':
        temp = []
        ls = ' where "SNR_isShow" = TRUE'
        
        print('in')
        main_data_query = 'Select {0} from public.products_allproducts_' + str(
        category) + ' {1} order by random()  LIMIT 20'
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
        data_query = main_data_query.format(",".join(out), ls)
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
    else:
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['POST','GET'])
@permission_classes((permissions.AllowAny,))
def categoryall_explainByID_test(request,category,totalResult):
    if request.method == 'GET':
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        print(totalResult)
        print(category)
        temp = []
        limit = page * int(totalResult)
        offset = (page - 1) * int(totalResult)
        cursor = connection.cursor()
        cursor.execute("SELECT reltuples FROM pg_class WHERE relname =\'products_allproducts_" + str(category)+"\'")
        count1 = int(cursor.fetchone()[0])
        # count1=0
        ls = ' where "SNR_isShow" = TRUE'
        cache_key = 'categorycache_for_newfilter' + str(category) + str(page) +str(totalResult)
        # ls=ls+' ORDER BY "SNR_Price" ASC'
        cache_time = 3600  # time to live in seconds
        results = cache.get(cache_key)
        if not results:
            print('in')
            main_data_query = 'Select {0} from public.products_allproducts_' + str(
                category) + ' {1} order by Random() OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
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

            data_query = main_data_query.format(",".join(out), ls)
            print("main query", data_query)

            f_count = len(fields)

            with connection.cursor() as cursor:
                cursor.execute(data_query)

                for i in cursor.fetchall():

                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)
            res = {
                'results': temp,
                'count':count1
            }
            # cache.set(cache_key, res, cache_time)
            return Response(res, status.HTTP_200_OK)
        else:
            print('in chache')
            return Response(results, status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        print(totalResult)
        print(category)
        temp = []
        limit = page * int(totalResult)
        offset = (page - 1) * int(totalResult)
        # ls=' '
        # ls=' where "SNR_CatID" = '+str(category)
        ls = ' where "SNR_isShow" = TRUE'
        dic = request.data
        cache_key = 'categorycache_for_newfilter'+str(category)+str(page)
        if dic['sub'] != 'undefine':
            ls = ls + ' AND  "SNR_SubCatID" = '+str(request.data['sub'])+' '
            cache_key=cache_key+str(request.data['sub'])
        if dic['minprice'] != -1 and dic['maxprice'] !=-1:
            ls=ls +' AND "SNR_Price" BETWEEN '+str(request.data['minprice'])+' AND '+str(request.data['maxprice'])
            cache_key = cache_key + str(request.data['minprice'])+str(request.data['maxprice'])
        if dic['merchant'] != 'undefine':
            ls=ls +' AND  "SNR_Available" ilike \'%'+str(request.data['merchant'])+'%\' '
            cache_key = cache_key + str(request.data['merchant'])
        if dic['brand'] != 'undefine':
            ls = ls + ' AND  "SNR_Brand" ilike \'%' + str(request.data['brand']) +'%\' '
            cache_key = cache_key + str(request.data['brand'])
        # ls=ls+' ORDER BY "SNR_Price" ASC'
        cache_time = 3600  # time to live in seconds
        results = cache.get(cache_key)
        if not results:
            print('in')
            main_data_query = 'Select {0} from public.products_allproducts_'+str(category)+' {1} order by Random() OFFSET '+str(offset)+' LIMIT '+str(limit)
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


            data_query = main_data_query.format(",".join(out), ls)
            print("main query", data_query)

            f_count = len(fields)

            with connection.cursor() as cursor:
                cursor.execute(data_query)

                for i in cursor.fetchall():

                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]

                    temp.append(current_item)
            if dic['sort'] != 'undefine':
                if request.data['sort']=='ASC':
                    temp = sorted(temp, key=lambda k: k['SNR_Price'])
                elif request.data['sort']=='DSC':
                    temp = sorted(temp, key=lambda k: k['SNR_Price'],reverse=True)
            res = {
                'results': temp
            }
            # cache.set(cache_key, res, cache_time)
            return Response(res,status.HTTP_200_OK)
        else:
            print('in chache')
            if dic['sort'] != 'undefine':
                if request.data['sort']=='ASC':
                    results = sorted(results, key=lambda k: k['SNR_Price'])
                elif request.data['sort']=='DSC':
                    results = sorted(results, key=lambda k: k['SNR_Price'],reverse=True)
            return Response(results, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def categoryall_explainByID2(request,category):

    ls = Q()
    ls &= Q(SNR_isShow=True)
    try:
        sub = int(request.GET.get('sub'))
        if ( sub!='undefined' and sub!=None):
            ls &=Q(SNR_SubCatID=sub)
    except:
        sub=-1
    try:
        price1 = int(request.GET.get('low'))
    except:
        price1=-1
    try:
        price2 = int(request.GET.get('high'))
    except:
        price2=-1
    if (price1 != -1 and price2 != -1):
        # print 'added price'
        ls &=Q(SNR_Price__range=[price1,price2])

    try:
        merchant = (request.GET.get('merchant'))
        if(merchant!='undefined' and merchant!=None) :
            ls &=Q(SNR_Available__icontains=merchant)
    except:
        merchant = -1

    try:
        brand = (request.GET.get('brand'))
        if( brand!='undefined' and brand!=None):
            ls &=Q(SNR_Brand__icontains=brand)
    except:
        brand=-1
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    try:
        count = int(request.GET.get('count'))
        if count < 1:
            count = 1

    except:
        count = 1
    # cache_key = 'categorycache_for_' + str(category) + str(page) + str(price1) + str(price2) + str(merchant).replace(" ","") + str(brand).replace(" ", "") + str(sub).replace(" ", "") + str(merchant).replace(" ","")
    cache_key='abc'
    cache_time = 3600  # time to live in seconds
    result = cache.get(cache_key)
    # result=None
    if not result:
        temp = []
        limit = page * int(count)
        offset = (page - 1) * int(count)

        main_data_query = AllProductsPartition.objects.filter(ls).order_by('?')[offset:limit]
        serializer=AllProducts_Serializer(main_data_query,many=True)
        # cache.set(cache_key, serializer.data, cache_time)
        return Response({'results':serializer.data},status=status.HTTP_200_OK)
    else:
        print('in chache')
        return Response({'results':result},status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def categoryall_explainByID1(request,category):
    ls = ' where "SNR_isShow" = TRUE'
    try:
        sub = int(request.GET.get('sub'))
        if ( sub!='undefined' and sub!=None):
            ls = ls + ' AND  "SNR_SubCatID" = '+str(sub)+' '
    except:
        sub=-1
    try:
        price1 = int(request.GET.get('low'))
    except:
        price1 = -1
    try:
        price2 = int(request.GET.get('high'))
    except:
        price2=-1
    if (price1 != -1 and price2 != -1):
        # print 'added price'
        ls=ls +' AND "SNR_Price" BETWEEN '+str(price1)+' AND '+str(price2)

    try:
        merchant = (request.GET.get('merchant'))
        if(merchant != 'undefined' and merchant != None) :
            ls=ls +' AND  "SNR_Available" ilike \'%'+str(merchant)+'%\' '
    except:
        merchant = -1

    try:
        brand = (request.GET.get('brand'))
        if( brand!='undefined' and brand!=None):
            ls = ls + ' AND  "SNR_Brand" ilike \'%' + str(brand) +'%\' '
    except:
        brand=-1
    try:
        sort = (request.GET.get('sort'))
    except:
        sort=-1
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1

    except:
        page = 1
    try:
        count = int(request.GET.get('count'))
        if count < 1:
            count = 1

    except:
        count = 1
    my_map = client.get_map("MainCat").blocking()
    cache_key = 'categorycache_for_' + str(category) + str(page) + str(price1) + str(price2) + str(merchant).replace(" ","") + str(brand).replace(" ", "") + str(sub).replace(" ", "") + str(merchant).replace(" ","") +str(sort).replace(" ","")+str(count)
    # cache_time = 36000  # time to live in seconds
    result = my_map.get(cache_key)
    # result=None
    if result == None:
        temp = []
        limit = page * int(count)
        offset = (page - 1) * int(count)
        if (sort != 'undefined' and sort != None):
            if sort == 'ASC':
                so=' order by "SNR_Price" ASC'
            else:
                so=' order by "SNR_Price" DESC'
            main_data_query = 'Select {0} from public.products_allproducts_' + str(
                category) + ' {1} '+str(so)+' OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
        else:
            # main_data_query = 'Select {0} from public.products_allproducts_' + str(
            #     category) + ' {1} TABLESAMPLE SYSTEM(1) OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
            main_data_query = 'Select {0} from public.products_allproducts_' + str(
                category) + ' {1} OFFSET ' + str(offset) + ' LIMIT ' + str(limit)
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

        data_query = main_data_query.format(",".join(out), ls)
        print("main query", data_query)

        f_count = len(fields)
        count=0
        with connection.cursor() as cursor:
            cursor.execute(data_query)
            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    current_item['index']=count
                count=count+1

                temp.append(current_item)
        connection.close()
        # co = 'Select Count(\'*\')  from public.products_allproducts_'+str(category)+ str(ls)+' limit '+str(count*20)
        # with connection.cursor() as cursor:
        #     cursor.execute(co)
        #     it = cursor.fetchall()
        #     it = [i[0] for i in it]
        # if it[0] >= (count*20):
        #     item='5000+'
        #     totalpages='20'
        # else:
        #     item=it[0]
        #     totalpages=int(it[0])/int(count)
        # connection.close()
        a = {'results': temp,
             'items': str('5000+'), 'Pages': str('20')
             }
        my_map.put(cache_key, a)
        return Response({'results':temp,'items':'5000+','Pages':'20'},status=status.HTTP_200_OK)
    else:
        print('inchache')
        return Response(result,status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def categoryall_explainByID(request,category):
        res = {}
        main_query = 'explain Select {0} from products_allproducts Where "SNR_CatID" = %s'
        main_data_query = 'Select {0} from products_allproducts Where "SNR_CatID" = %s'
        count_query = main_query.format("*")

        try:
            sub = int(request.GET.get('sub'))
            if ( sub!='undefined' and sub!=None):
            #     sub = sub.replace('(', '\(')
            #     sub = sub.replace(')', '\)')
            #     sub = sub.replace("'", "''")

                que = (' AND "SNR_SubCatID" = %s' % (sub))
                main_data_query = main_data_query + que


        except:
            sub=-1
            # print main_data_query

        try:
            price1 = int(request.GET.get('low'))
        except:
            price1=-1
        try:
            price2 = int(request.GET.get('high'))
        except:
            price2=-1

        if (price1 != -1 and price2 != -1):
            # print 'added price'
            que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
            main_data_query=main_data_query+que

        try:
            merchant = (request.GET.get('merchant'))
            if(merchant!='undefined' and merchant!=None) :
                que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
                main_data_query = main_data_query + que


        except:
            merchant = -1


        try:
            brand = (request.GET.get('brand'))
            if( brand!='undefined' and brand!=None):
                que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
                main_data_query=main_data_query+que


        except:
            brand=-1


        # print main_data_query

        try:
            pagecount = int(request.GET.get('count'))
        except:
            pagecount = 36
        offset = ' LIMIT {0}'.format(pagecount)


        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL","id",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition","SNR_PriceBefore",
            "SNR_CustomerReviews", "SNR_Price",
            "SNR_SubCategory"

        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])
        data_query = main_data_query.format(",".join(out))
        print(data_query)
        f_count = len(fields)
        try:
            with connection.cursor() as cursor:
                cursor.execute(count_query, [category])
                # print count_query
                query_count = cursor.fetchone()[0]
                print(query_count)
                # print(query_cat)
                query_count = patSearch('rows=(\d+)', query_count).group(1)
                query_count = int(query_count)
                print(query_count)

                # print query_count
                if query_count == 0:
                    return Response(status=status.HTTP_204_NO_CONTENT)

                pageCount = int(math.ceil(query_count / float(pagecount)))
                res['totalItems'] = query_count
                res['totalPages'] = pageCount
                print(res['totalItems'])

                try:
                    page = int(request.GET.get('page'))
                except:
                    page = 1

                if page > pageCount:
                    page = pageCount

                if page > 0:
                    offset = "{0} OFFSET {1}".format(offset, pagecount * (page - 1))

                try:
                    sort = (request.GET.get('sort'))
                    if (sort != 'undefined' and sort != None):
                        que = (' ORDER BY "SNR_Price" %s' % (sort))
                        data_query = data_query + que
                    else:
                        print('in')
                        que = (' ORDER BY id')
                        data_query = data_query + que
                except:
                    sort = -1

                data_query = data_query+ offset
                print(data_query)
                cursor.execute(data_query, [category])
                temp = []
                # print cursor.fetchall()
                for i in cursor.fetchall():

                    # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):

                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

                res["results"] = temp
                result = res
                return Response(res,status=status.HTTP_200_OK)
        except:
            res={
                'totalItems':0,
                'totalPages':0,
                'results':[]

            }
            return Response(res, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def categoryall_explainByID_test(request,category):
        res = {}
        main_query = 'explain Select {0} from products_allproducts Where "SNR_CatID" = %s'
        main_data_query = 'Select {0} from products_allproducts Where "SNR_CatID" = %s'
        count_query = main_query.format("*")

        try:
            sub = int(request.GET.get('sub'))
            if ( sub!='undefined' and sub!=None):
            #     sub = sub.replace('(', '\(')
            #     sub = sub.replace(')', '\)')
            #     sub = sub.replace("'", "''")

                que = (' AND "SNR_SubCatID" = %s' % (sub))
                main_data_query = main_data_query + que
        except:
            sub=-1
            # print main_data_query

        try:
            price1 = int(request.GET.get('low'))
        except:
            price1=-1
        try:
            price2 = int(request.GET.get('high'))
        except:
            price2=-1

        if (price1 != -1 and price2 != -1):
            # print 'added price'
            que=(' AND "SNR_Price" BETWEEN %s AND %s' % (price1, price2))
            main_data_query=main_data_query+que

        try:
            merchant = (request.GET.get('merchant'))
            if(merchant!='undefined' and merchant!=None) :
                que = (' AND "SNR_Available" ilike \'%s\'' % (merchant))
                main_data_query = main_data_query + que
        except:
            merchant = -1

        try:
            brand = (request.GET.get('brand'))
            if( brand!='undefined' and brand!=None):
                que = (' AND "SNR_Brand" ilike \'%s\'' % (brand))
                main_data_query=main_data_query+que
        except:
            brand=-1


        # print main_data_query

        try:
            pagecount = int(request.GET.get('count'))
        except:
            pagecount = 36
        offset = ' LIMIT {0}'.format(pagecount)

        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL","id",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition","SNR_PriceBefore",
            "SNR_CustomerReviews", "SNR_Price",
            "SNR_SubCategory"
        ]
        out = ['"{0}"'.format(i) for i in fields]

        extra_fields = []
        fields.extend(extra_fields)

        out.extend(['cast("{0}" as varchar)'.format(i) for i in extra_fields])
        data_query = main_data_query.format(",".join(out))
        f_count = len(fields)
        try:
            with connection.cursor() as cursor:
                cursor.execute(count_query, [category])
                # print count_query
                query_count = cursor.fetchone()[0]
                print(query_count)
                # print(query_cat)
                query_count = patSearch('rows=(\d+)', query_count).group(1)
                query_count = int(query_count)
                print(query_count)

                # print query_count
                if query_count == 0:
                    return Response(status=status.HTTP_204_NO_CONTENT)

                pageCount = int(math.ceil(query_count / float(pagecount)))
                res['totalItems'] = query_count
                res['totalPages'] = pageCount
                print(res['totalItems'])

                try:
                    page = int(request.GET.get('page'))
                except:
                    page = 1

                if page > pageCount:
                    page = pageCount

                if page > 0:
                    offset = "{0} OFFSET {1}".format(offset, pagecount * (page - 1))

                try:
                    sort = (request.GET.get('sort'))
                    if (sort != 'undefined' and sort != None):
                        que = (' ORDER BY "SNR_Price" %s' % (sort))
                        data_query = data_query + que
                    else:
                        print('in')
                        que = (' ORDER BY id')
                        data_query = data_query + que
                except:
                    sort = -1

                data_query = data_query+ offset
                print(data_query)
                cursor.execute(data_query, [category])
                temp = []
                # print cursor.fetchall()
                for i in cursor.fetchall():

                    # if i[5] > 0:
                    current_item = {}
                    for j in range(f_count):

                        current_item[fields[j]] = i[j]

                    temp.append(current_item)

                res["results"] = temp
                result = res
                return Response(res,status=status.HTTP_200_OK)
        except:
            res={
                'totalItems':0,
                'totalPages':0,
                'results':[]

            }
            return Response(res, status=status.HTTP_200_OK)

class GetVendorsCategories(APIView):
    # authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, *args, **kwargs):
        try:
            my_map = client.get_map("Categories_Names_Vendors1").blocking()
            cache_key = 'Categories_Logos_On_Home1'
            # my_map.remove(cache_key)
            result = my_map.get(cache_key)

            res = {}
            # result=None
            if result == None:
                categories = Vendors_Categories.objects.using('newdb').order_by('id')
                serializer = Vendors_Categories_Serializer(categories, many=True)
                serializer_data = serializer.data
                for item in serializer_data:
                    item['SNR_Cat_Image'] = ("https://"
                                             ""
                                             ""
                                             "storage.buynroar.com/MerchantLogos/ApparelAccessories.png")
                serialized_data = json.dumps(serializer_data)
                # my_map.remove(cache_key)
                my_map.put(cache_key, serialized_data)
                res["Categories"] = serializer_data
                return Response(res, status.HTTP_200_OK)
            else:
                deserialized_data = json.loads(result.replace('\\', ''))
                for item in deserialized_data:
                    item['SNR_Cat_Image'] = "https://storage.buynroar.com/MerchantLogos/ApparelAccessories.png"
                res["Categories"] = deserialized_data
                return Response(res,status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)


class GetCategoriesDataByName(APIView):
     # FilterALLAppliencesASC
    # authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny,]

    def get(self, request, category_name, products_per_page):
        query_filters = Q()
        query_filters &= Q(SNR_isShow=True)
        query_filters &= Q(SNR_Category=category_name)
        # print('category_nameL ', category_name)

        # data = request.data
        # min_price = data['minprice']
        # max_price = data['maxprice']
        # sort = data['sort']
        # search = data['search']
        # cat = data['cat']

        products_per_page = products_per_page

        # Set the current page number or default to 1
        page_number = int(request.GET.get('page', 1))

        # limit = page_number * int(products_per_page)
        # offset = (page_number - 1) * int(products_per_page)


        # if min_price != -1 and max_price != -1:
        #     query_filters &= Q(SNR_Price__gte=min_price, SNR_Price__lte=max_price)
        #
        # if sort != "undefine":
        #     if sort == "ASC" :
        #         queryset = AllProducts.objects.using('newdb').filter(query_filters).exclude(SNR_Title='00', SNR_Category='00').order_by('SNR_Price')[0:5000]
        #     elif sort == "DESC":
        #         queryset = AllProducts.objects.using('newdb').filter(query_filters).exclude(SNR_Title='00',SNR_Category='00').order_by('-SNR_Price')[0:500]
        #     elif sort == "LATEST":
        #         queryset = AllProducts.objects.using('newdb').filter(query_filters).exclude(SNR_Title='00',SNR_Category='00').order_by('-id')[0:5000]
        #     elif sort == "OLDEST":
        #         queryset = AllProducts.objects.using('newdb').filter(query_filters).exclude(SNR_Title='00',SNR_Category='00').order_by('id')[0:5000]
        # else:
        #     # Apply all filter
        #     queryset = AllProducts.objects.using('newdb').filter(query_filters).exclude(SNR_Title='00',
        #                                                                                 SNR_Category='00')[0:10000]



        try:
            queryset = AllProducts.objects.using('newdb').filter(query_filters).exclude(SNR_Title='00',
                                                                                        SNR_Category='00')[0:7000]
            # queryset = AllProducts.objects.using('newdb').filter(SNR_Category=category_name, SNR_isShow=True).exclude(SNR_Title='00',SNR_Category='00')[0:10000]
            # queryset = AllProducts.objects.using('newdb').filter(SNR_Category=category_name, SNR_isShow=True).exclude(SNR_Title='00',SNR_Category='00').values()[offset:limit]
            # print(queryset.count())

            paginator = Paginator(queryset, per_page=products_per_page)
            # p1 = paginator.count
            # p2 = paginator.num_pages
            # p3 = paginator.page_range
            # p4 = paginator.ELLIPSIS
            try:
                record = paginator.page(page_number)
            except PageNotAnInteger:
                record = paginator.page(1)
            except EmptyPage:
                record = paginator.page(paginator.num_pages)

            serializer_context = {'request': request}
            serializer = AllProducts_Serializer(record, many=True, context=serializer_context)
            items = paginator.count
            total_pages = paginator.num_pages
            res = {
                'totalItems': items,
                'totalPages': total_pages,
                'results': serializer.data

            }
            return Response(res)
        except Exception as e:
            print(e)
            return Response({'results': ['Data not found']}, status=status.HTTP_404_NOT_FOUND)

    # def Filter_smarthomeDESC(request, query):
    #     # print(query)
    #     try:
    #         que = Q()
    #         for word in query.split():
    #             que &= Q(SNR_Title__icontains=word)
    #
    #         que |= Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)
    #         data = SmartHomes.objects.filter(que).order_by('-SNR_Price')
    #         paginator = Paginator(data, 12)
    #         page = request.GET.get('page')
    #         try:
    #             record = paginator.page(page)
    #         except PageNotAnInteger:
    #
    #             record = paginator.page(1)
    #         except EmptyPage:
    #
    #             record = paginator.page(paginator.num_pages)
    #
    #         serializer_context = {'request': request}
    #         serializer = Smarthomes_Serializer(record, many=True, context=serializer_context)
    #         # res = serializer.data
    #         # res.update('pages_count:', paginator.num_pages())
    #         # return Response(res)
    #         items = 0
    #         pages = 0
    #         items = paginator._count
    #         pages = paginator._get_num_pages()
    #         res = {
    #             'totalItems': items,
    #             'totalPages': pages,
    #             'results': serializer.data
    #
    #         }
    #         return Response(res)
    #
    #
    #     except SmartHomes.DoesNotExist:
    #
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    x = 5
    # def testbed1(self, request, category, *args, **kwargs):
    #     ls = Q()
    #     ls &= Q(SNR_isShow=True)
    #     try:
    #         sub = int(request.GET.get('sub'))
    #         if (sub != 'undefined' and sub != None):
    #             ls &= Q(SNR_SubCatID=sub)
    #     except:
    #         sub = -1
    #     try:
    #         price1 = int(request.GET.get('low'))
    #     except:
    #         price1 = -1
    #     try:
    #         price2 = int(request.GET.get('high'))
    #     except:
    #         price2 = -1
    #     if (price1 != -1 and price2 != -1):
    #         # print 'added price'
    #         ls &= Q(SNR_Price__range=[price1, price2])
    #
    #     try:
    #         merchant = (request.GET.get('merchant'))
    #         if (merchant != 'undefined' and merchant != None):
    #             ls &= Q(SNR_Available__icontains=merchant)
    #     except:
    #         merchant = -1
    #
    #     try:
    #         brand = (request.GET.get('brand'))
    #         if (brand != 'undefined' and brand != None):
    #             ls &= Q(SNR_Brand__icontains=brand)
    #     except:
    #         brand = -1
    #
    #     try:
    #         page = int(request.GET.get('page'))
    #         if page < 1:
    #             page = 1
    #     except:
    #         page = 1
    #     try:
    #         count = int(request.GET.get('count'))
    #         if count < 1:
    #             count = 1
    #     except:
    #         count = 1
    #     # cache_key = 'categorycache_for_' + str(category) + str(page) + str(price1) + str(price2) + str(merchant).replace(" ","") + str(brand).replace(" ", "") + str(sub).replace(" ", "") + str(merchant).replace(" ","")
    #     cache_key = 'abc'
    #     cache_time = 3600  # time to live in seconds
    #     result = cache.get(cache_key)
    #     # result=None
    #     if not result:
    #         temp = []
    #         limit = page * int(count)
    #         offset = (page - 1) * int(count)
    #
    #         main_data_query = AllProductsPartition.objects.filter(ls).order_by('?')[offset:limit]
    #         serializer = AllProducts_Serializer(main_data_query, many=True)
    #         # cache.set(cache_key, serializer.data, cache_time)
    #         return Response({'results': serializer.data}, status=status.HTTP_200_OK)
    #     else:
    #         print('in chache')
    #         return Response({'results': result}, status=status.HTTP_200_OK)

    # def testbed2(self, request, category, *args, **kwargs):
    #     try:
    #         page = int(request.GET.get('page'))
    #         if page < 1:
    #             page = 1
    #
    #     except:
    #         page = 1
    #     dic = request.data
    #     temp = []
    #     main_data_querylimit = page * int(totalResult)
    #     offset = (page - 1) * int(totalResult)
    #     my_map = client.get_map("Deal").blocking()
    #     cache_key = 'Hot_Deals==' + str(query) + '==' + str(dic['cat']) + '==' + str(dic['sort']) + '==' + str(
    #         dic['search']) + '==' + str(dic['minprice']) + '==' + str(dic['maxprice']) + '==' + str(
    #         totalResult) + '==' + str(page)
    #     print(cache_key)
    #     # cache_time = 36000
    #     result = None
    #     try:
    #         result = my_map.get(cache_key)
    #     except Exception as e:
    #         print(e)
    #         Deal_map = client.get_map("Deal").blocking()
    #         Deal_map.clear()
    #         # my_map.remove(cache_key)
    #         result = None
    #     print("this is ", result)
    #     # print(cache_key)
    #     # result=None
    #     if result == None:
    #         print('inout')
    #         if query == 'All':
    #             ls = ' where "SNR_Active"=TRUE AND "SNR_Available" IS NOT NULL'
    #         else:
    #             ls = ' where "SNR_Active"=TRUE AND "SNR_Available" =\'' + str(query.replace("'", "''")) + '\''
    #         if dic['cat'] != "undefine":
    #             ls = ls + ' AND "SNR_Category" =\'' + request.data['cat'].replace("'", "''") + '\''
    #         if dic['minprice'] != -1 and dic['maxprice'] != -1:
    #             ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
    #                 request.data['maxprice'])
    #         if dic['search'] != 'undefine':
    #             a = str(dic['search']).replace("\'", "")
    #             a = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in a.split("\n")]
    #             ls = ls + ' AND "tsv_title" @@ plainto_tsquery(\'' + str(a[0]) + '\')'
    #         if dic['sort'] != "undefine":
    #             if request.data['sort'] == 'ASC':
    #                 lss = ' order by "SNR_PriceAfter" ASC'
    #             elif request.data['sort'] == 'DESC':
    #                 lss = ' order by "SNR_PriceAfter" DESC'
    #             elif request.data['sort'] == 'LATEST':
    #                 lss = ' order by "id" DESC'
    #             elif request.data['sort'] == 'OLDEST':
    #                 lss = ' order by "id" ASC'
    #             main_data_query = 'Select {0} from public.products_active_dailydeals {1} ' + str(
    #                 lss) + ' OFFSET ' + str(
    #                 offset) + ' LIMIT ' + str(limit)
    #             co = 'Select Count(\'*\') from public.products_active_dailydeals ' + str(ls)
    #         else:
    #             main_data_query = 'Select {0} from public.products_active_dailydeals {1} OFFSET ' + str(
    #                 offset) + ' LIMIT ' + str(limit)
    #             co = 'Select Count(\'*\') from public.products_active_dailydeals ' + str(ls)
    #
    #         with connection.cursor() as cursor:
    #             cursor.execute(co)
    #             it = cursor.fetchall()
    #             it = [i[0] for i in it]
    #         connection.close()
    #         totalpages = int(int(it[0]) / int(totalResult))
    #         per = int(it[0]) % int(totalResult)
    #         if per != 0:
    #             totalpages += 1
    #
    #         fields = [
    #             "SNR_SKU", "SNR_Title",
    #             "SNR_Available", "id",
    #             "SNR_ProductURL", "SNR_ImageURL",
    #             "SNR_Date", "SNR_Category", "SNR_Description",
    #             "SNR_PriceBefore", "SNR_PriceAfter", "SNR_Customer_Rating"
    #         ]
    #         out = ['"{0}"'.format(i) for i in fields]
    #
    #         data_query = main_data_query.format(",".join(out), ls)
    #         f_count = len(fields)
    #         print(data_query)
    #         count = 0
    #         with connection.cursor() as cursor:
    #             cursor.execute(data_query)
    #
    #             for i in cursor.fetchall():
    #
    #                 current_item = {}
    #                 for j in range(f_count):
    #                     current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
    #                     current_item['index'] = count
    #                 count = count + 1
    #
    #                 temp.append(current_item)
    #         connection.close()
    #         a = {'results': temp,
    #              'items': str(it[0]), 'pages': str(totalpages)
    #              }
    #         # my_map.remove(cache_key)
    #         my_map.put(cache_key, a)
    #         return Response({'results': temp, 'items': it[0], 'pages': totalpages}, status.HTTP_200_OK)
    #     else:
    #         print('in cache')
    #         return Response(result, status.HTTP_200_OK)

class HomePageCategoriesData(APIView):
    # FilterALLAppliencesASC
    # authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        # my_map = client.get_map('CategoriesData').blocking()
        # cache_key = 'Category_Data_On_HomePage'
        # result = my_map.get(cache_key)
        result = None
        if result == None:
            exclude_filter = Q()
            exclude_filter &= Q(SNR_Title='00', SNR_Category='00', SNR_ImageURL='00')

            # Retrieve the desired limit and offset from the request query parameters
            limit = int(request.GET.get('limit', 150))
            offset = int(request.GET.get('offset', 0))

            # Convert the limit and offset parameters to integers
            limit = int(limit)
            offset = int(offset)

            page_number = int(request.GET.get('page', 1))

            # Define a static list of merchant names
            merchant_names = ['Amazon', 'ebay']
            try:
                # Select a limited number of random products from each merchant
                products = []
                for merchant_name in merchant_names:
                    merchant_logos = merchants.objects.using('default').filter(name__iexact=merchant_name, active=True).order_by('prefer').values()[0]

                    # Select a limited number of random products from the specified merchant
                    merchant_products = AllProducts.objects.using('newdb').filter(SNR_Available=merchant_name, SNR_isShow=True,SNR_Title__isnull=False).exclude(exclude_filter).values()[offset:offset + limit]
                    for product in merchant_products:
                        product['image60px'] = merchant_logos['image60px']
                        products.append(product)

                paginator = Paginator(products, per_page=30)
                # p1 = paginator.count
                # p2 = paginator.num_pages
                # p3 = paginator.page_range
                # p4 = paginator.ELLIPSIS
                try:
                    record = paginator.page(page_number)
                except PageNotAnInteger:
                    record = paginator.page(1)
                except EmptyPage:
                    record = paginator.page(paginator.num_pages)
                serializer = AllProducts_Logos_Serializer(record, many=True)
                items = paginator.count
                total_pages = paginator.num_pages
                res = {
                    'totalItems': items,
                    'totalPages': total_pages,
                    'results': serializer.data
                }
                # my_map.put(cache_key, res)
                return Response(res)
            except Exception as e:
                print(e)
                return Response({'results': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            print('inchache')
            # return Response(result, status=status.HTTP_200_OK)
            return Response({'resutl': 'In Cache'}, status=status.HTTP_200_OK)


class GetCategoriesDataByName_PostTest(APIView):
    # FilterALLAppliencesASC
    # authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, category_name, products_per_page):
        query_filters = Q()
        query_filters &= Q(SNR_isShow=True)
        query_filters &= Q(SNR_Category=category_name)
        # print('category_nameL ', category_name)

        data = request.data
        min_price = data['minprice']
        max_price = data['maxprice']
        sort = data['sort']
        search = data['search']
        cat = data['cat']

        products_per_page = products_per_page
        # Set the current page number or default to 1
        page_number = int(request.GET.get('page', 1))

        # limit = page_number * int(products_per_page)
        # offset = (page_number - 1) * int(products_per_page)

        if int(min_price) != -1 and int(max_price) != -1:
            query_filters &= Q(SNR_Price__gte=min_price, SNR_Price__lte=max_price)

        fields = ['id', 'SNR_Title', 'SNR_Brand', 'SNR_Description', 'SNR_Category',
                  'SNR_ImageURL', 'SNR_ModelNo', 'SNR_UPC', 'SNR_SKU', 'SNR_ProductURL',
                  'SNR_Price', 'SNR_Available', 'SNR_Date', 'SNR_CustomerReviews',
                  'SNR_PriceBefore', 'SNR_Condition', 'SNR_SubCategory', 'SNR_isShow',
                  'SNR_SubCategory']
        defer_fields = ['SNR_CatID', 'SNR_MainCatID', 'SNR_SubCatID', 'SNR_Description_Mobile']
        exclude_filter = Q()
        exclude_filter &= Q(SNR_Title='00',SNR_Category='00', SNR_ImageURL='00')

        # main_query = AllProducts.objects.using('newdb').filter(query_filters).exclude(exclude_filter)
        main_query = AllProducts.objects.using('newdb').filter(query_filters)

        if sort != "undefine":
            if sort == "ASC" :
                queryset = main_query.only(*fields).order_by('SNR_Price')[0:5000]
            elif sort == "DESC":
                queryset = main_query.order_by('-SNR_Price')[0:5000]
            elif sort == "LATEST":
                queryset = main_query.order_by('-id').defer(*defer_fields).values(*fields)[:5000]
            elif sort == "OLDEST":
                queryset = main_query.only(*fields).order_by('id')[0:5000]
        else:
            # Apply all filter
            queryset = main_query.values(*fields)[0:50000]

        try:
            # queryset = AllProducts.objects.using('newdb').filter(query_filters).exclude(SNR_Title='00',
            #                                                                             SNR_Category='00')[0:10000]
            # print(queryset.count())

            paginator = Paginator(queryset, per_page=products_per_page)
            # p1 = paginator.count
            # p2 = paginator.num_pages
            # p3 = paginator.page_range
            # p4 = paginator.ELLIPSIS
            try:
                record = paginator.page(page_number)
            except PageNotAnInteger:
                record = paginator.page(1)
            except EmptyPage:
                record = paginator.page(paginator.num_pages)

            serializer_context = {'request': request}
            serializer = AllProducts_Serializer(record, many=True, context=serializer_context)
            items = paginator.count
            total_pages = paginator.num_pages
            res = {
                'totalItems': items,
                'totalPages': total_pages,
                'results': serializer.data

            }
            return Response(res)
        except Exception as e:
            print(e)
            return Response({'results': ['Data not found']}, status=status.HTTP_404_NOT_FOUND)


class CategoryNamesFromCache(APIView):
    # authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        my_map = client.get_map('category_name_map').blocking()
        cache_key = 'Category_Name_Map_Key'
        result = my_map.get(cache_key)
        if result == None:
            categories = AllProducts.objects.using('newdb').filter(SNR_isShow=True).exclude(SNR_Title='00', SNR_Category='00', SNR_ImageURL='00').values('SNR_Category').annotate(total_products=Count('id')).order_by('-total_products')
            print(categories)
            # if request.content_type in ['application/json', 'application/xml']:
            serializer = AllProductsCateogriesCache_Serializer(data=categories, many=True)
            if serializer.is_valid():
                print(serializer.data)
            else:
                print(serializer.errors)

            # my_map.put(cache_key, serializer.data)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            print('inchache')
            # return Response(result, status=status.HTTP_200_OK)
            return Response({'resutl': 'No'}, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def recentlyitem(request):
    if request.method == 'GET':
        res = Recently_Items.objects.filter(user=request.user).order_by('-id')
        serializer=RecentlyProducts(res,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    if request.method == 'POST':
        pro= AllProductsPartition.objects.get(pk=int(request.data['id']))
        if Recently_Items.objects.filter(product=pro, user=request.user).exists():
            Recently_Items.objects.filter(product=pro, user=request.user).delete()
            Recently_Items.objects.create(product=pro,user=request.user)
            check = Recently_Items.objects.filter(user=request.user)[15:]
            for dele in check:
                dele.delete()
        else:
            Recently_Items.objects.create(product=pro,user=request.user)
            check=Recently_Items.objects.filter(user=request.user)[15:]
            for dele in check:
                dele.delete()
        return Response({'msg':'successfully added'},status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def merchantlogos(request):
    if request.method == 'GET':
        my_map = client.get_map("Logo").blocking()
        cache_key = 'Merchant_Logos_Home'

        result = my_map.get(cache_key)
        # result=None
        if result == None:
            res = merchants.objects.using('default').filter(active=True).order_by('prefer')
            serializer=merchantslizer(res,many=True)
            my_map.put(cache_key,serializer.data)
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            return Response(result,status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

from feedback.models import *

@api_view(['GET','DELETE'])
@permission_classes((IsAuthenticated,))
def ADDwishlist_pro(request,pk):
    if request.method == 'GET':
        print('in')
        print(pk)
        res=AllProducts.objects.get(id=pk)
        if Wishlist.objects.filter(SNR_Title=str(res.SNR_Title),user=request.user).exists():
            return Response({'msg':'Already In WishList'},status.HTTP_200_OK)
        else:
            obj=Wishlist(
                SNR_SKU=res.SNR_SKU,
                user=request.user,
                SNR_Title=res.SNR_Title,
                SNR_ModelNo=res.SNR_ModelNo,
                SNR_Brand=res.SNR_Brand,
                SNR_UPC=res.SNR_UPC,
                SNR_Price=res.SNR_Price,
                SNR_CustomerReviews=res.SNR_CustomerReviews,
                SNR_Available=res.SNR_Available,
                SNR_ProductURL=res.SNR_ProductURL,
                SNR_ImageURL=res.SNR_ImageURL,
                SNR_Description=res.SNR_Description,
                SNR_isShow=res.SNR_isShow,
            )
            obj.save()
            return Response({'msg':'Successfully Added In WhishList'},status.HTTP_200_OK)
    if request.method =='DELETE':
        res=AllProducts.objects.get(id=pk)
        de=Wishlist.objects.get(SNR_Title=str(res.SNR_Title),user=request.user)
        de.delete()
        return Response({'msg':'Delete Successful'},status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def detail_of_product(request):
    if request.data['type']=='Deals':
        try:
            data=Active_DailyDeals.objects.get(id=request.data['id'])
            serilzer_obj=DailyDealsSearizlerofSingleProduct(data)
            return Response(serilzer_obj.data,status=status.HTTP_200_OK)
        except:
            return Response({"result":"item expired"},status=status.HTTP_400_BAD_REQUEST)
    elif request.data['type']=='Vocation':
        try:
            data = Active_Vocation.objects.get(id=request.data['id'])
            serilzer_obj = ActiveVocationSingleProduct(data)
            return Response(serilzer_obj.data, status=status.HTTP_200_OK)
        except:
            return Response({"result": "item expired"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.data['type']=="All":
        try:
            data = AllProducts.objects.using("newdb").get(id=request.data['id'])
            serilzer_obj = AllProducts_Serializer(data)
            return Response(serilzer_obj.data, status=status.HTTP_200_OK)
        except:
            return Response({"result": "item expired"}, status=status.HTTP_400_BAD_REQUEST)
    return Response("eror",status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Home_test(request):
    if request.method == 'GET':
        print("before cache")
        my_map = client.get_map("Home_old").blocking()
        cache_key = 'HomePageOldAPI'
        # cache_time = 36000  # time to live in seconds
        result_cache = my_map.get(cache_key)
        print("after cache")
        print(result_cache)
        if result_cache == None:
            print('3rd')
            mer = merchants.objects.filter(active=True).order_by('prefer')
            serializer = merchantslizer1(mer, many=True)
            print(serializer.data)
            with connection.cursor() as cursor:
                # cursor.execute('SELECT DISTINCT "SNR_Available" FROM products_allproducts Where "SNR_Category" = %s',[category])
                res = {}
                result = []
                fields = [
                    "SNR_CatName"
                ]
                cursor.execute(
                    'SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
                temp = []
                temp2 = []
                # print cursor.fetchall()
                for i in cursor.fetchall():
                    temp.append({'id': i[0], 'Category': i[1], 'path': i[2]})
                    temp2 = []
                res["Categories"] = temp
            connection.close()
            temp11=[]
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" IN (\'amazon\',\'ebay\',\'Walmart\') AND "SNR_Active"=True order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category","id","SNR_Description",
                    "SNR_Customer_Rating",
                ]
                out = ['"{0}"'.format(i) for i in fields]
                data_query = main_query.format(",".join(out))
                cursor.execute(data_query)
                temp1 = []
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(len(fields)):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                    temp11.append(current_item)
            connection.close()
            temp22=[]
            temp3=[]
            temp4=[]
            temp5=[]
            ls = ' where "SNR_isShow" = TRUE'
            li=[222,536,166,469]
            main_data_query = 'Select {0} from public.products_allproducts_' + str(
                222) + ' {1} order by random()  LIMIT 20'
            fields = [
                "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out),ls)
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    temp22.append(current_item)
            connection.close()
            main_data_query = 'Select {0} from public.products_allproducts_' + str(
                536) + ' {1} order by random()  LIMIT 20'
            fields = [
                "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out), ls)
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    temp3.append(current_item)
            connection.close()
            main_data_query = 'Select {0} from public.products_allproducts_' + str(
                111) + ' {1} order by random()  LIMIT 20'
            fields = [
                "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out), ls)
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] =str(i[j]).encode('utf-8').strip()
                    temp4.append(current_item)
            connection.close()
            main_data_query = 'Select {0} from public.products_allproducts_' + str(
                469) + ' {1} order by random()  LIMIT 20'
            fields = [
                "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out), ls)
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    temp5.append(current_item)
            connection.close()
            final={
                'Categories':res,
                'merchants':serializer.data,
                'home_Electronics':temp22,
                'home_Garden':temp3,
                'home_Apperel':temp4,
                'home_Health':temp5,
                'Hot_Deals':temp11,
                'Coupon': merchantscoupons.objects.filter(active=True).values(),
            }
            try:
                my_map.clear()
            except:
                pass
            my_map.put(cache_key,final)
            return Response(final,status.HTTP_200_OK)
        else:
            print('inchache')
            return Response(result_cache,status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Home_Cats(request):
    if request.method == 'GET':
        print("before cache")
        my_map = client.get_map("Home_old").blocking()
        cache_key = 'HomeCats'
        # cache_time = 36000  # time to live in seconds
        result_cache = my_map.get(cache_key)
        print("after cache")
        print(result_cache)
        if result_cache == None:
            print('3rd')
            mer = merchants.objects.filter(active=True).order_by('prefer')
            serializer = merchantslizer1(mer, many=True)
            print(serializer.data)
            with connection.cursor() as cursor:
                # cursor.execute('SELECT DISTINCT "SNR_Available" FROM products_allproducts Where "SNR_Category" = %s',[category])
                res = {}
                result = []
                fields = [
                    "SNR_CatName"
                ]
                cursor.execute(
                    'SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
                temp = []
                temp2 = []
                # print cursor.fetchall()
                for i in cursor.fetchall():
                    temp.append({'id': i[0], 'Category': i[1], 'path': i[2]})
                    temp2 = []
                res["Categories"] = temp
            connection.close()





            # final={
            #     'Categories':res,
            #
            # }
            try:
                my_map.clear()
            except:
                pass
            my_map.put(cache_key,res)
            return Response(res,status.HTTP_200_OK)
        else:
            print('inchache')
            return Response(result_cache,status.HTTP_200_OK)
    

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Home_test_mobile(request):
    if request.method == 'GET':
        print("before cache")
        my_map = client.get_map("Home_old").blocking()
        cache_key = 'HomePageOldAPIMobile'
        # cache_time = 36000  # time to live in seconds
        result_cache = my_map.get(cache_key)
        print("after cache")
        print(result_cache)
        if result_cache == None:
            print('3rd')
            mer = merchants.objects.filter(active=True).order_by('prefer')
            serializer = merchantslizer1(mer, many=True)
            print(serializer.data)
            final={
                'merchants':serializer.data,
                'Coupon': merchantscoupons.objects.filter(active=True).values(),
            }
            try:
                my_map.clear()
            except:
                pass
            my_map.put(cache_key,final)
            return Response(final,status.HTTP_200_OK)
        else:
            print('inchache')
            return Response(result_cache,status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Home_test_New(request):
    if request.method == 'GET':
        my_map = client.get_map("Home").blocking()
        cache_key = 'Home_Page_New_cust'
        # cache_time = 36000  # time to live in seconds
        result = my_map.get(cache_key)
        print('1st')
        # result = None
        # result=None
        if result == None:
            print('3rd')
            mer = merchants.objects.filter(active=True).order_by('prefer')
            serializer = merchantslizer1(mer, many=True)
            print(serializer.data)
            with connection.cursor() as cursor:
                res= {}

                fields = [
                    "SNR_CatName"
                ]
                cursor.execute(
                    'SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
                temp = []
                for i in cursor.fetchall():
                    temp.append({'id': i[0], 'Category': i[1], 'path': i[2]})
                    temp2 = []
                res["Categories"] = temp
            connection.close()
            amazondata=[]
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'amazon\' AND "SNR_Active"=True order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category","id","SNR_Description","SNR_Customer_Rating"
                ]
                out = ['"{0}"'.format(i) for i in fields]
                data_query = main_query.format(",".join(out))
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(len(fields)):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                    amazondata.append(current_item)
            connection.close()
            ebaydata=[]
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'ebay\' AND "SNR_Active"=True order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category","id","SNR_Description","SNR_Customer_Rating"
                ]
                out = ['"{0}"'.format(i) for i in fields]
                data_query = main_query.format(",".join(out))
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(len(fields)):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                    ebaydata.append(current_item)
            connection.close()

            walmartdata = []
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'Walmart\' AND "SNR_Active"=True order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category", "id", "SNR_Description","SNR_Customer_Rating"
                ]
                out = ['"{0}"'.format(i) for i in fields]
                data_query = main_query.format(",".join(out))
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(len(fields)):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                    walmartdata.append(current_item)
            connection.close()
            bestbuydata = []
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'BEST BUY\' AND "SNR_Active"=True order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category", "id", "SNR_Description","SNR_Customer_Rating"
                ]
                out = ['"{0}"'.format(i) for i in fields]
                data_query = main_query.format(",".join(out))
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(len(fields)):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                    bestbuydata.append(current_item)
            connection.close()
            targetdata = []
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'target\' AND "SNR_Active"=True order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category", "id", "SNR_Description","SNR_Customer_Rating"
                ]
                out = ['"{0}"'.format(i) for i in fields]
                data_query = main_query.format(",".join(out))
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(len(fields)):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                    targetdata.append(current_item)
            connection.close()



            final={
                'merchants':serializer.data,
                'amazon':amazondata,
                'ebay':ebaydata,
                'walmart' : walmartdata,
                'bestbuy' : bestbuydata,
                'target':targetdata,
                # 'Coupon': merchantscoupons.objects.filter(active=True).values(),
            }

            try:
                my_map.remove(cache_key)
            except:
                pass
            my_map.put(cache_key,final)
            return Response(final,status.HTTP_200_OK)
        else:
            print('inchache')
            return Response(result,status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Home_test1(request):
    if request.method == 'GET':
        my_map = client.get_map("Home").blocking()
        cache_key = 'Home_Page1'
        # cache_time = 36000  # time to live in seconds
        result = my_map.get(cache_key)
        print('1st')
        # result=None
        if result == None:
            print('3rd')
            mer = merchants.objects.filter(active=True).order_by('prefer')
            serializer = merchantslizer1(mer, many=True)
            print(serializer.data)
            with connection.cursor() as cursor:
                # cursor.execute('SELECT DISTINCT "SNR_Available" FROM products_allproducts Where "SNR_Category" = %s',[category])
                res = {}
                result = []
                fields = [
                    "SNR_CatName"
                ]
                cursor.execute(
                    'SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
                temp = []
                temp2 = []
                # print cursor.fetchall()
                for i in cursor.fetchall():
                    temp.append({'id': i[0], 'Category': i[1], 'path': i[2]})
                    temp2 = []
                res["Categories"] = temp
            connection.close()
            temp11=[]
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" IN (\'amazon\',\'ebay\',\'Walmart\')  order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category",
                ]
                out = ['"{0}"'.format(i) for i in fields]
                data_query = main_query.format(",".join(out))
                cursor.execute(data_query)
                temp1 = []
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(len(fields)):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                    temp11.append(current_item)
            connection.close()
            li222=[]
            li536=[]
            li166=[]
            li469=[]
            a222=AllProductsPartition.objects.filter(SNR_CatID=222)[:20]
            for i in a222:
                se222={
                    'id':str(i.id).encode('utf-8').strip(),
                    'SNR_Title':str(i.SNR_Title).encode('utf-8').strip(),
                    # 'SNR_Description':str(i.SNR_Description).encode('utf-8').strip(),
                    'SNR_ImageURL':str(i.SNR_ImageURL).encode('utf-8').strip(),
                    'SNR_ProductURL':str(i.SNR_ProductURL).encode('utf-8').strip(),
                    'SNR_Price':str(i.SNR_Price).encode('utf-8').strip(),
                    'SNR_Available':str(i.SNR_Available).encode('utf-8').strip(),
                    'SNR_CustomerReviews':str(i.SNR_CustomerReviews).encode('utf-8').strip(),
                    'SNR_PriceBefore':str(i.SNR_PriceBefore).encode('utf-8').strip(),
                }
                li222.append(se222)
            a536=AllProductsPartition.objects.filter(SNR_CatID=536)[:20]
            for i in a536:
                se536 = {
                    'id':str(i.id).encode('utf-8').strip(),
                    'SNR_Title':str(i.SNR_Title).encode('utf-8').strip(),
                    # 'SNR_Description':str(i.SNR_Description).encode('utf-8').strip(),
                    'SNR_ImageURL':str(i.SNR_ImageURL).encode('utf-8').strip(),
                    'SNR_ProductURL':str(i.SNR_ProductURL).encode('utf-8').strip(),
                    'SNR_Price':str(i.SNR_Price).encode('utf-8').strip(),
                    'SNR_Available':str(i.SNR_Available).encode('utf-8').strip(),
                    'SNR_CustomerReviews':str(i.SNR_CustomerReviews).encode('utf-8').strip(),
                    'SNR_PriceBefore':str(i.SNR_PriceBefore).encode('utf-8').strip(),
                }
                li536.append(se536)
            a166=AllProductsPartition.objects.filter(SNR_CatID=166)[:20]
            for i in a166:
                se166 = {
                    'id':str(i.id).encode('utf-8').strip(),
                    'SNR_Title':str(i.SNR_Title).encode('utf-8').strip(),
                    # 'SNR_Description':str(i.SNR_Description).encode('utf-8').strip(),
                    'SNR_ImageURL':str(i.SNR_ImageURL).encode('utf-8').strip(),
                    'SNR_ProductURL':str(i.SNR_ProductURL).encode('utf-8').strip(),
                    'SNR_Price':str(i.SNR_Price).encode('utf-8').strip(),
                    'SNR_Available':str(i.SNR_Available).encode('utf-8').strip(),
                    'SNR_CustomerReviews':str(i.SNR_CustomerReviews).encode('utf-8').strip(),
                    'SNR_PriceBefore':str(i.SNR_PriceBefore).encode('utf-8').strip(),
                }
                li166.append(se166)
            a469=AllProductsPartition.objects.filter(SNR_CatID=469)[:20]
            for i in a469:
                se469 = {
                    'id':str(i.id).encode('utf-8').strip(),
                    'SNR_Title':str(i.SNR_Title).encode('utf-8').strip(),
                    # 'SNR_Description':str(i.SNR_Description).encode('utf-8').strip(),
                    'SNR_ImageURL':str(i.SNR_ImageURL).encode('utf-8').strip(),
                    'SNR_ProductURL':str(i.SNR_ProductURL).encode('utf-8').strip(),
                    'SNR_Price':str(i.SNR_Price).encode('utf-8').strip(),
                    'SNR_Available':str(i.SNR_Available).encode('utf-8').strip(),
                    'SNR_CustomerReviews':str(i.SNR_CustomerReviews).encode('utf-8').strip(),
                    'SNR_PriceBefore':str(i.SNR_PriceBefore).encode('utf-8').strip(),
                }
                li469.append(se469)
            final={
                'Categories':res,
                'merchants':serializer.data,
                'home_Electronics':li222,
                'home_Garden':li536,
                'home_Apperel':li166,
                'home_Health':li469,
                'Hot_Deals':temp11
            }
            my_map.put(cache_key,final)
            return Response(final,status.HTTP_200_OK)
        else:
            print('inchache')
            return Response(result,status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def AllMerchantCoupns1(request):
    if request.method == 'GET':
        my_map = client.get_map("map-name").blocking()
        cache_key = 'Merchant_CouponsLogos_Home'

        result = my_map.get(cache_key)
        # result=None
        if result == None:
            res=merchantscoupons.objects.filter(active=True).values()
            my_map.put(cache_key, res)
            return Response(res,status.HTTP_200_OK)
        else:
            return Response(result,status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def AllMerchantCoupns(request):
    if request.method == 'GET':
        res=AllProductsCoupons.objects.filter(SNR_Active=True).distinct('SNR_Available').values('SNR_Available')
        return Response(res,status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def AllCoupns(request,que,item):
    # from newdb.models import AllProductsCoupons
    if request.method == 'GET':
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1

        except:
            page = 1
        print(page)
        limit = page * int(item)
        offset = (page - 1) * int(item)
        res=AllProductsCoupons.objects.filter(SNR_Available=str(que),SNR_Active=True).values()[offset:limit]
        totalitems=int(AllProductsCoupons.objects.filter(SNR_Available=str(que),SNR_Active=True).count())
        totalpages = int(totalitems / int(item))
        per = totalitems % int(item)
        if per != 0:
            totalpages += 1
        re={
            'result':res,
            'items':totalitems,
            'pages':totalpages
        }
        return Response(re,status.HTTP_200_OK)


@api_view(['POST','GET'])
@permission_classes((IsAuthenticated,))
def CouponsInsertion(request):
    if request.method == 'GET':
        res = AllProductsCoupons.objects.filter(Manual=True).values()
        return Response(res,status.HTTP_200_OK)
    if request.method == 'POST':
        if AllProductsCoupons.objects.filter(SNR_CouponCode_url=str(request.data['SNR_CouponCode_url'])).exists():
            return Response({"msg":"Already Exist"},status.HTTP_200_OK)
        else:
            obj=AllProductsCoupons(SNR_Title=request.data['SNR_Title'],SNR_Available=request.data['SNR_Available'],SNR_URl_Code=request.data['SNR_URl_Code'],SNR_CouponCode_url=request.data['SNR_CouponCode_url']
                                   ,SNR_Discount=request.data['SNR_Discount'],SNR_Active=request.data['SNR_Active'],Manual=True,SNR_Expire=None)
            obj.save()
            return Response({"msg":"Successfully Post"},status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def AllCouponsMerchants(request):
    if request.method =='GET':
        res =merchantscoupons.objects.all().values('name')
        return Response(res,status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def Coupons_edit_del(request,id):
    if request.method == 'PUT':
        res= AllProductsCoupons.objects.get(id=id)
        res.SNR_Title=request.data['SNR_Title']
        res.SNR_Available=request.data['SNR_Available']
        res.SNR_URl_Code=request.data['SNR_URl_Code']
        res.SNR_CouponCode_url=request.data['SNR_CouponCode_url']
        res.SNR_Discount=request.data['SNR_Discount']
        res.SNR_Active=request.data['SNR_Active']
        res.save()
        return Response({"msg":"Successfully Updated"},status.HTTP_200_OK)
    if request.method == 'DELETE':
        res = AllProductsCoupons.objects.get(id=id)
        res.delete()
        return Response({"msg":"Successfully Deleted"},status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def newsuggest(request,query):
    if request.method =='GET':
        li=[]
        query=query.strip()
        query=query.replace(" ","%20")
        url="https://completion.amazon.com/api/2017/suggestions?session-id=139-7818303-6479523&customer-id=&request-id=HDBER4G3248ZX88WJEE6&page-type=Gateway&lop=en_US&site-variant=desktop&client-info=amazon-search-ui&mid=ATVPDKIKX0DER&alias=aps&b2b=0&fresh=0&ks=83&prefix="+str(query)+"&event=onKeyPress&limit=11&fb=1&suggestion-type=KEYWORD&suggestion-type=WIDGET&_=1572004155098"
        re = requests.get(url)
        main = re.json()
        main = main['suggestions']
        for i in main:
            li.append(i['value'])
        li=set(li)
        return Response(li,status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def upc(request,query):
    if request.method =='GET':
        url='https://api.upcitemdb.com/prod/trial/lookup?upc='+str(query)
        re=requests.get(url)
        main=re.json()
        return Response(main, status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def test1(request,query):
    if request.method =='GET':
        que = query
        url = 'https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ZeeShan-Dhaar-PRD-f38876c40-7ef67ffa&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=' + str(
            que) + '&paginationInput.entriesPerPage=40  '
        re = requests.get(url)
        main = re.json()
        # print(main)
        li = []
        count = 0
        for i in main['findItemsByKeywordsResponse']:
            # print(i['searchResult'])
            for j in i['searchResult']:

                for k in j['item']:
                    print(k['sellingStatus'])
                    for m in k['sellingStatus']:
                        for n in m['convertedCurrentPrice']:
                            price=n['__value__']
                    dic = {
                        'index': count,
                        'SNR_Title': k['title'][0],
                        'SNR_Available': 'ebay',
                        'SNR_ProductURL': k['viewItemURL'][0],
                        'SNR_ImageURL': k['galleryURL'][0],
                        'SNR_Description': 'None',
                        'SNR_Price':price,
                        'SNR_PriceBefore': '0.00',
                        'SNR_CustomerReviews': '3.50'
                    }
                    count = count + 1
                    li.append(dic)
            return Response({'tes':li},status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def AllSearch__(request,totalResult):
    li=[]

    type=request.data['type']
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1
    except:
        page = 1
    print(">>>>>>>>>>>>",page)
    # limit = page *
    # offset = (page - 1) * int(10)
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    totalResult = int(totalResult)
    if type == 'Coupon':
        keyword = request.data['keyword']
        keyword = keyword.replace("'","")
        keyword = keyword.replace('"','')
       # ls = ' "SNR_Active"=\'' + str(True) + '\''
        count=0
        data = 'select count(*) from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'# + 'And' + str(
            #ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","Manual","SNR_CouponCode_url","SNR_Discount","SNR_Expire","SNR_Expire_Status","SNR_URl_Code","site","SNR_Active" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'Manual':i[4],
                    'SNR_CouponCode_url':i[5],
                    'SNR_Discount':i[6],
                    'SNR_Expire':i[7],
                    'SNR_Expire_Status':i[8],
                    'SNR_URl_Code':i[9],
                    'site':i[10],
                    'SNR_Active':i[11]


                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")
            results = AllProductsCoupons.objects.annotate(
                similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                           keyword) + TrigramSimilarity(
                    'SNR_Description', keyword)).filter(similarity__gte=0.3,).order_by("-similarity")[:800]
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = Products_Coupons_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)
    elif type == 'Vocation':
        q1 = Q()
        q1 &= Q(SNR_Active=True)
        keyword = request.data['keyword']
        keyword = keyword.replace("'", "")
        keyword = keyword.replace('"', '')
        ls = ' "SNR_Active"=\'' + str(True) + '\''
        if 'minprice' and 'maxprice' in request.data:
            if request.data['minprice'] != -1 and request.data['maxprice'] != -1:
                print("in price")
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                    request.data['maxprice'])
                q1 &= Q(SNR_PriceAfter__gte=request.data['minprice'], SNR_PriceAfter__lte=request.data['maxprice'])
        count=0
        data = 'select count(*) from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            if 'sort' in request.data and request.data['sort'] != "undefine":
                print("in sort")
                if request.data['sort'] == 'ASC':
                    ls = ls + ' order by "SNR_PriceAfter" ASC'
                elif request.data['sort'] == 'DESC':
                    ls = ls + ' order by "SNR_PriceAfter" DESC'
                elif request.data['sort'] == 'LATEST':
                    ls = ls + ' order by "id" DESC'
                elif request.data['sort'] == 'OLDEST':
                    ls = ls + ' order by "id" ASC'

            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' +'AND' + str(ls)+ ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceAfter':i[7],
                    'SNR_PriceBefore':i[8],
                    'SNR_Customer_Rating':i[9]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")

            if request.data['minprice'] != "-1" and request.data['maxprice'] != "-1":
                results = Active_Vocation.objects.annotate(
                    similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                               keyword) + TrigramSimilarity(
                        'SNR_Description', keyword)).filter(similarity__gte=0.3).filter(q1).order_by("-similarity")[:800]



            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = Active_Vocation_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)
    elif type == 'Deals':
        ls = ' "SNR_Active"=\'' + str(True) + '\''
        q1 = Q()
        q1 &= Q(SNR_Active=True)
        if ('minprice' and 'maxprice' in request.data) :
            if request.data['minprice']!=-1 and request.data['maxprice']!=-1:
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                    request.data['maxprice'])
                q1 &= Q(SNR_PriceAfter__gte=request.data['minprice'], SNR_PriceAfter__lte=request.data['maxprice'])

        if 'merchant' in request.data:
            ls = ls + 'And "SNR_Category"=\'' + str(request.data['merchant']) + '\''
            q1 &= Q(SNR_Category=request.data['merchant'])
        count=0
        if 'keyword' in request.data:
            keyword = request.data['keyword']
            keyword = keyword.replace("'", "")
            keyword = keyword.replace('"', '')
            data = 'select count(*) from public."products_active_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
            print("sssssss",data)
        else:
            data = 'select count(*) from public."products_active_dailydeals" where' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            if 'sort' in request.data and request.data['sort'] != "undefine":
                print("in sort")
                if request.data['sort'] == 'ASC':
                    ls = ls + ' order by "SNR_PriceAfter" ASC'
                elif request.data['sort'] == 'DESC':
                    ls = ls + ' order by "SNR_PriceAfter" DESC'
                elif request.data['sort'] == 'LATEST':
                    ls = ls + ' order by "id" DESC'
                elif request.data['sort'] == 'OLDEST':
                    ls = ls + ' order by "id" ASC'

            if 'keyword' in request.data:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'+ 'And' + str(
            ls) + ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            else:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_dailydeals" where ' + str(
            ls) + ' LIMIT ' + str(
                    totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceAfter':i[7],
                    'SNR_PriceBefore':i[8],
                    'SNR_Customer_Rating':i[9]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)

        else:
            keyword = request.data['keyword']
            print("Similarity")
            results = Active_DailyDeals.objects.annotate(
                similarity=TrigramSimilarity('SNR_Title',keyword)).filter(similarity__gte=0.3, ).order_by("-similarity")

            # results = Active_DailyDeals.objects.annotate(
            #     similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
            #                                                                                keyword) + TrigramSimilarity(
            #         'SNR_Description', keyword)).filter(similarity__gte=0.3,).filter(q1).order_by("-similarity")
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = DailyDeals_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)
    else:
        return Response({ "results": "Type Not Matched", "status": False,},status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def AllSearch(request,totalResult):
    li=[]

    type=request.data['type']
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1
    except:
        page = 1
    print(">>>>>>>>>>>>",page)
    # limit = page *
    # offset = (page - 1) * int(10)
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    totalResult = int(totalResult)
    if type == 'Coupon':
        keyword = request.data['keyword']
        keyword = keyword.replace("'","")
        keyword = keyword.replace('"','')
       # ls = ' "SNR_Active"=\'' + str(True) + '\''
        count=0
        data = 'select count(*) from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'# + 'And' + str(
            #ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","Manual","SNR_CouponCode_url","SNR_Discount","SNR_Expire","SNR_Expire_Status","SNR_URl_Code","site","SNR_Active" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'Manual':i[4],
                    'SNR_CouponCode_url':i[5],
                    'SNR_Discount':i[6],
                    'SNR_Expire':i[7],
                    'SNR_Expire_Status':i[8],
                    'SNR_URl_Code':i[9],
                    'site':i[10],
                    'SNR_Active':i[11]


                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")
            results = AllProductsCoupons.objects.annotate(
                similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                           keyword) + TrigramSimilarity(
                    'SNR_Description', keyword)).filter(similarity__gte=0.3,).order_by("-similarity")[:800]
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = Products_Coupons_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)
    elif type == 'Vocation':
        q1 = Q()
        q1 &= Q(SNR_Active=True)
        keyword = request.data['keyword']
        keyword = keyword.replace("'", "")
        keyword = keyword.replace('"', '')
        ls = ' "SNR_Active"=\'' + str(True) + '\''
        if 'minprice' and 'maxprice' in request.data:
            if request.data['minprice'] != -1 and request.data['maxprice'] != -1:
                print("in price")
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                    request.data['maxprice'])
                q1 &= Q(SNR_PriceAfter__gte=request.data['minprice'], SNR_PriceAfter__lte=request.data['maxprice'])
        count=0
        data = 'select count(*) from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data),
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            if 'sort' in request.data and request.data['sort'] != "undefine":
                print("in sort")
                if request.data['sort'] == 'ASC':
                    ls = ls + ' order by "SNR_PriceAfter" ASC'
                elif request.data['sort'] == 'DESC':
                    ls = ls + ' order by "SNR_PriceAfter" DESC'
                elif request.data['sort'] == 'LATEST':
                    ls = ls + ' order by "id" DESC'
                elif request.data['sort'] == 'OLDEST':
                    ls = ls + ' order by "id" ASC'

            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' +'AND' + str(ls)+ ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceAfter':i[7],
                    'SNR_PriceBefore':i[8],
                    'SNR_Customer_Rating':i[9]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")

            if request.data['minprice'] != "-1" and request.data['maxprice'] != "-1":
                results = Active_Vocation.objects.annotate(
                    similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                               keyword) + TrigramSimilarity(
                        'SNR_Description', keyword)).filter(similarity__gte=0.3).filter(q1).order_by("-similarity")[:800]



            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = Active_Vocation_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)
    elif type == 'Deals':
        ls = ' "SNR_Active"=\'' + str(True) + '\''
        q1 = Q()
        q1 &= Q(SNR_Active=True)
        if ('minprice' and 'maxprice' in request.data) :
            if request.data['minprice']!=-1 and request.data['maxprice']!=-1:
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                    request.data['maxprice'])
                q1 &= Q(SNR_PriceAfter__gte=request.data['minprice'], SNR_PriceAfter__lte=request.data['maxprice'])

        if 'merchant' in request.data:
            ls = ls + 'And "SNR_Category"=\'' + str(request.data['merchant']) + '\''
            q1 &= Q(SNR_Category=request.data['merchant'])
        count=0
        if 'keyword' in request.data:
            keyword = request.data['keyword']
            keyword = keyword.replace("'", "")
            keyword = keyword.replace('"', '')
            data = 'select count(*) from public."products_active_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
            print("sssssss",data)
        else:
            data = 'select count(*) from public."products_active_dailydeals" where' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            if 'sort' in request.data and request.data['sort'] != "undefine":
                print("in sort")
                if request.data['sort'] == 'ASC':
                    ls = ls + ' order by "SNR_PriceAfter" ASC'
                elif request.data['sort'] == 'DESC':
                    ls = ls + ' order by "SNR_PriceAfter" DESC'
                elif request.data['sort'] == 'LATEST':
                    ls = ls + ' order by "id" DESC'
                elif request.data['sort'] == 'OLDEST':
                    ls = ls + ' order by "id" ASC'

            if 'keyword' in request.data:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'+ 'And' + str(
            ls) + ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            else:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_dailydeals" where ' + str(
            ls) + ' LIMIT ' + str(
                    totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceAfter':i[7],
                    'SNR_PriceBefore':i[8],
                    'SNR_Customer_Rating':i[9]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)

        else:
            keyword = request.data['keyword']
            print("Similarity")
            results = Active_DailyDeals.objects.annotate(
                similarity=TrigramSimilarity('SNR_Title',keyword)).filter(similarity__gte=0.3, ).order_by("-similarity")

            # results = Active_DailyDeals.objects.annotate(
            #     similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
            #                                                                                keyword) + TrigramSimilarity(
            #         'SNR_Description', keyword)).filter(similarity__gte=0.3,).filter(q1).order_by("-similarity")
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = DailyDeals_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)
    elif type == 'All':
        try: search_param = request.data['keyword']
        except: search_param = None

        page_number = int(request.GET.get('page', 1))

        try: type = request.data['type']
        except: type = None
        try: min_price = request.data['minprice']
        except: min_price = None

        try:
            max_price = request.data['maxprice']
        except: max_price = None

        try: sort_by = request.data['sort']
        except: sort_by = 'undefined'

        try: category = request.data['cat']
        except: category = None

        limit = page_number * int(totalResult)
        offset = (page_number - 1) * int(totalResult)
        totalResult = int(totalResult)

        index_name = 'all_products_index'

        # Create an Elasticsearch connection
        es = connections.get_connection()

        search_query = {
            'query': {
                'bool': {
                    'should': [],
                    'minimum_should_match': '60%',
                    'filter': []
                }
            },
            'from': offset,
            'size': limit
        }

        if category is not None:
            # category_filter = {
            #     'term': {
            #         'SNR_Category.keyword': category,
            #     }
            # }
            category_filter = {
                'term': {
                    'SNR_Category.keyword': {
                        'value': category,
                        'case_insensitive': True
                    }
                }
            }
            search_query['query']['bool']['filter'].append(category_filter)


        elif search_param:
            search_query['query']['bool']['should'].extend([
                {
                    'match_phrase': {
                    # 'match': {
                        'SNR_Title': {
                            'query': search_param,
                            'boost': 3.0,
                        }
                    }
                },
                {
                    'match': {
                        'SNR_Category': {
                            'query': search_param,
                            'boost': 1.0
                        }
                    }
                },
                {
                    'match': {
                        'SNR_Description': {
                            'query': search_param,
                            'boost': 0.8
                        }
                    }
                },

            ])

        # Add price range filter to the search query
        if min_price is not None and min_price != '' and int(min_price) != -1:
            price_range_filter = {
                'range': {
                    'SNR_Price': {
                        'gte': min_price
                    }
                }
            }
            search_query['query']['bool']['filter'].append(price_range_filter)


        if max_price is not None and max_price != '' and int(max_price) != -1:
            price_range_filter = {
                'range': {
                    'SNR_Price': {
                        'lte': max_price
                    }
                }
            }
            search_query['query']['bool']['filter'].append(price_range_filter)

        # Add sorting to the search query
        if sort_by == 'ASC':
            sort_option = {'SNR_Price': {'order': 'asc'}}
        elif sort_by == 'DESC':
            sort_option = {'SNR_Price': {'order': 'desc'}}
        elif sort_by == 'LATEST':
            # sort_option = {'_id': {'order': 'desc'}}
            # sort_option = {'_doc': {'order': 'desc'}}
            sort_option = {'SNR_Date': {'order': 'desc'}}
        elif sort_by == 'OLDEST':
            # sort_option = {'id': {'order': 'asc'}}
            sort_option = {'SNR_Date': {'order': 'asc'}}
        else:
            # Default sorting if not specified or invalid value
            sort_option = {'_score': {'order': 'desc'}}
        search_query['sort'] = [sort_option]


        # Execute the search query and process the results
        try:
            response = es.search(index=index_name, body=search_query)
        except RequestError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        total_items = response['hits']['total']['value']
        total_pages = ceil(total_items / limit)

        if total_items == 0:
            return Response({'Status: ': ' No Data Available'})

        # Process the search results with filters and sorting
        results = []
        for hit in response['hits']['hits']:
            source = hit['_source']
            result = {
                'id': hit['_id'],
                'score': hit['_score'],
                'SNR_Title': source.get('SNR_Title', ''),
                'SNR_Category': source.get('SNR_Category', ''),
                'SNR_SKU': source.get('SNR_SKU', ''),
                'SNR_ModelNo': source.get('SNR_ModelNo', ''),
                'SNR_Brand': source.get('SNR_Brand', ''),
                'SNR_UPC': source.get('SNR_UPC', ''),
                'SNR_SubCategory': source.get('SNR_SubCategory', ''),
                'SNR_Condition': source.get('SNR_Condition', ''),
                'SNR_PriceBefore': source.get('SNR_PriceBefore', ''),
                'SNR_Price': source.get('SNR_Price', ''),
                'SNR_CustomerReviews': source.get('SNR_CustomerReviews', ''),
                'SNR_Available': source.get('SNR_Available', ''),
                'SNR_ProductURL': source.get('SNR_ProductURL', ''),
                'SNR_ImageURL': source.get('SNR_ImageURL', ''),
                'SNR_Description': source.get('SNR_Description', ''),
                'SNR_Description_Mobile': source.get('SNR_Description_Mobile', ''),
                'SNR_isShow': source.get('SNR_isShow', ''),
                'SNR_Date': source.get('SNR_Date', '')
            }
            results.append(result)

        return Response({'total_pages': total_pages, 'total_items': total_items, "status": True, "type":"All", "results": results})

    else:
        return Response({ "results": "Type Not Matched", "status": False,},status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def AllSearch_(request,totalResult):
    li=[]

    type=request.data['type']
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1
    except:
        page = 1
    print(">>>>>>>>>>>>",page)
    # limit = page *
    # offset = (page - 1) * int(10)
    limit = page * int(totalResult)
    offset = (page - 1) * int(totalResult)
    totalResult = int(totalResult)
    if type == 'Coupon':
        keyword = request.data['keyword']
        keyword = keyword.replace("'","")
        keyword = keyword.replace('"','')
       # ls = ' "SNR_Active"=\'' + str(True) + '\''
        count=0
        data = 'select count(*) from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'# + 'And' + str(
            #ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","Manual","SNR_CouponCode_url","SNR_Discount","SNR_Expire","SNR_Expire_Status","SNR_URl_Code","site","SNR_Active" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'Manual':i[4],
                    'SNR_CouponCode_url':i[5],
                    'SNR_Discount':i[6],
                    'SNR_Expire':i[7],
                    'SNR_Expire_Status':i[8],
                    'SNR_URl_Code':i[9],
                    'site':i[10],
                    'SNR_Active':i[11]


                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")
            results = AllProductsCoupons.objects.annotate(
                similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                           keyword) + TrigramSimilarity(
                    'SNR_Description', keyword)).filter(similarity__gte=0.3,).order_by("-similarity")[:800]
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = Products_Coupons_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)
    elif type == 'Vocation':
        q1 = Q()
        q1 &= Q(SNR_Active=True)
        keyword = request.data['keyword']
        keyword = keyword.replace("'", "")
        keyword = keyword.replace('"', '')
        ls = ' "SNR_Active"=\'' + str(True) + '\''
        if 'minprice' and 'maxprice' in request.data:
            if request.data['minprice'] != -1 and request.data['maxprice'] != -1:
                print("in price")
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                    request.data['maxprice'])
                q1 &= Q(SNR_PriceAfter__gte=request.data['minprice'], SNR_PriceAfter__lte=request.data['maxprice'])
        count=0
        data = 'select count(*) from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data),
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            if 'sort' in request.data and request.data['sort'] != "undefine":
                print("in sort")
                if request.data['sort'] == 'ASC':
                    ls = ls + ' order by "SNR_PriceAfter" ASC'
                elif request.data['sort'] == 'DESC':
                    ls = ls + ' order by "SNR_PriceAfter" DESC'
                elif request.data['sort'] == 'LATEST':
                    ls = ls + ' order by "id" DESC'
                elif request.data['sort'] == 'OLDEST':
                    ls = ls + ' order by "id" ASC'

            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' +'AND' + str(ls)+ ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceAfter':i[7],
                    'SNR_PriceBefore':i[8],
                    'SNR_Customer_Rating':i[9]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")

            if request.data['minprice'] != "-1" and request.data['maxprice'] != "-1":
                results = Active_Vocation.objects.annotate(
                    similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                               keyword) + TrigramSimilarity(
                        'SNR_Description', keyword)).filter(similarity__gte=0.3).filter(q1).order_by("-similarity")[:800]



            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = Active_Vocation_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)
    elif type == 'Deals':
        ls = ' "SNR_Active"=\'' + str(True) + '\''
        q1 = Q()
        q1 &= Q(SNR_Active=True)
        if ('minprice' and 'maxprice' in request.data) :
            if request.data['minprice']!=-1 and request.data['maxprice']!=-1:
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                    request.data['maxprice'])
                q1 &= Q(SNR_PriceAfter__gte=request.data['minprice'], SNR_PriceAfter__lte=request.data['maxprice'])

        if 'merchant' in request.data:
            ls = ls + 'And "SNR_Category"=\'' + str(request.data['merchant']) + '\''
            q1 &= Q(SNR_Category=request.data['merchant'])
        count=0
        if 'keyword' in request.data:
            keyword = request.data['keyword']
            keyword = keyword.replace("'", "")
            keyword = keyword.replace('"', '')
            data = 'select count(*) from public."products_active_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
            print("sssssss",data)
        else:
            data = 'select count(*) from public."products_active_dailydeals" where' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / totalResult)
            if (count % totalResult != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            if 'sort' in request.data and request.data['sort'] != "undefine":
                print("in sort")
                if request.data['sort'] == 'ASC':
                    ls = ls + ' order by "SNR_PriceAfter" ASC'
                elif request.data['sort'] == 'DESC':
                    ls = ls + ' order by "SNR_PriceAfter" DESC'
                elif request.data['sort'] == 'LATEST':
                    ls = ls + ' order by "id" DESC'
                elif request.data['sort'] == 'OLDEST':
                    ls = ls + ' order by "id" ASC'

            if 'keyword' in request.data:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'+ 'And' + str(
            ls) + ' LIMIT ' + str(totalResult) + ' OFFSET ' + str(offset);
            else:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore","SNR_Customer_Rating" from public."products_active_dailydeals" where ' + str(
            ls) + ' LIMIT ' + str(
                    totalResult) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceAfter':i[7],
                    'SNR_PriceBefore':i[8],
                    'SNR_Customer_Rating':i[9]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)

        else:
            keyword = request.data['keyword']
            print("Similarity")
            results = Active_DailyDeals.objects.annotate(
                similarity=TrigramSimilarity('SNR_Title',keyword)).filter(similarity__gte=0.3, ).order_by("-similarity")

            # results = Active_DailyDeals.objects.annotate(
            #     similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
            #                                                                                keyword) + TrigramSimilarity(
            #         'SNR_Description', keyword)).filter(similarity__gte=0.3,).filter(q1).order_by("-similarity")
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / totalResult)
            if (items % totalResult) != 0:
                totalpages += 1
            serializer = DailyDeals_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)
    elif type == 'All':
        try: search_param = request.data['keyword']
        except: search_param = None

        page_number = int(request.GET.get('page', 1))

        try: type = request.data['type']
        except: type = None
        try: min_price = request.data['minprice']
        except: min_price = None

        try:
            max_price = request.data['maxprice']
        except: max_price = None

        try: sort_by = request.data['sort']
        except: sort_by = 'undefined'

        try: category = request.data['cat']
        except: category = None

        try: brand = request.data['brand']
        except: brand = None

        limit = page_number * int(totalResult)
        offset = (page_number - 1) * int(totalResult)
        totalResult = int(totalResult)

        index_name = 'all_products_index'

        # Create an Elasticsearch connection
        es = connections.get_connection()

        search_query = {
            'query': {
                'bool': {
                    'should': [],
                    'minimum_should_match': '60%',
                    'filter': []
                }
            },
            'from': offset,
            'size': limit
        }

        if category is not None:
            # category_filter = {
            #     'term': {
            #         'SNR_Category.keyword': category,
            #     }
            # }
            category_filter = {
                'term': {
                    'SNR_Category.keyword': {
                        'value': category,
                        'case_insensitive': True
                    }
                }
            }
            search_query['query']['bool']['filter'].append(category_filter)

        # elif brand is not None:
        #
        #     brand_filter = {
        #         'term': {
        #             'SNR_Brand.keyword': {
        #                 'value': category,
        #                 'case_insensitive': True
        #             }
        #         }
        #     }
        #     search_query['query']['bool']['filter'].append(brand_filter)

        elif search_param:
            search_query['query']['bool']['should'].extend([
                {
                    'match_phrase': {
                    # 'match': {
                        'SNR_Title': {
                            'query': search_param,
                            'boost': 3.0,
                        }
                    }
                },
                {
                    'match': {
                        'SNR_Category': {
                            'query': search_param,
                            'boost': 1.0
                        }
                    }
                },
                {
                    'match': {
                        'SNR_Description': {
                            'query': search_param,
                            'boost': 0.8
                        }
                    }
                },

            ])

        # Add price range filter to the search query
        if min_price is not None and min_price != '' and int(min_price) != -1:
            price_range_filter = {
                'range': {
                    'SNR_Price': {
                        'gte': min_price
                    }
                }
            }
            search_query['query']['bool']['filter'].append(price_range_filter)


        if max_price is not None and max_price != '' and int(max_price) != -1:
            price_range_filter = {
                'range': {
                    'SNR_Price': {
                        'lte': max_price
                    }
                }
            }
            search_query['query']['bool']['filter'].append(price_range_filter)

        # Add sorting to the search query
        if sort_by == 'ASC':
            sort_option = {'SNR_Price': {'order': 'asc'}}
        elif sort_by == 'DESC':
            sort_option = {'SNR_Price': {'order': 'desc'}}
        elif sort_by == 'LATEST':
            # sort_option = {'_id': {'order': 'desc'}}
            # sort_option = {'_doc': {'order': 'desc'}}
            sort_option = {'SNR_Date': {'order': 'desc'}}
        elif sort_by == 'OLDEST':
            # sort_option = {'id': {'order': 'asc'}}
            sort_option = {'SNR_Date': {'order': 'asc'}}
        else:
            # Default sorting if not specified or invalid value
            sort_option = {'_score': {'order': 'desc'}}
        search_query['sort'] = [sort_option]


        # Execute the search query and process the results
        try:
            response = es.search(index=index_name, body=search_query)
        except RequestError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        total_items = response['hits']['total']['value']
        total_pages = ceil(total_items / limit)

        if total_items == 0:
            return Response({'Status: ': ' No Data Available'})

        # Process the search results with filters and sorting
        results = []
        for hit in response['hits']['hits']:
            source = hit['_source']
            result = {
                'id': hit['_id'],
                'score': hit['_score'],
                'SNR_Title': source.get('SNR_Title', ''),
                'SNR_Category': source.get('SNR_Category', ''),
                'SNR_SKU': source.get('SNR_SKU', ''),
                'SNR_ModelNo': source.get('SNR_ModelNo', ''),
                'SNR_Brand': source.get('SNR_Brand', ''),
                'SNR_UPC': source.get('SNR_UPC', ''),
                'SNR_SubCategory': source.get('SNR_SubCategory', ''),
                'SNR_Condition': source.get('SNR_Condition', ''),
                'SNR_PriceBefore': source.get('SNR_PriceBefore', ''),
                'SNR_Price': source.get('SNR_Price', ''),
                'SNR_CustomerReviews': source.get('SNR_CustomerReviews', ''),
                'SNR_Available': source.get('SNR_Available', ''),
                'SNR_ProductURL': source.get('SNR_ProductURL', ''),
                'SNR_ImageURL': source.get('SNR_ImageURL', ''),
                'SNR_Description': source.get('SNR_Description', ''),
                'SNR_Description_Mobile': source.get('SNR_Description_Mobile', ''),
                'SNR_isShow': source.get('SNR_isShow', ''),
                'SNR_Date': source.get('SNR_Date', '')
            }
            results.append(result)

        return Response({'total_pages': total_pages, 'total_items': total_items, "status": True, "type":"All", "results": results})


    else:
        return Response({ "results": "Type Not Matched", "status": False,},status.HTTP_400_BAD_REQUEST)



@permission_classes((permissions.AllowAny,))
def AllSearchcopy(request):
    li=[]

    type=request.data['type']
    try:
        page = int(request.GET.get('page'))
        if page < 1:
            page = 1
    except:
        page = 1
    print(page)
    limit = page * int(10)
    offset = (page - 1) * int(10)
    if type == 'Coupon':
        keyword = request.data['keyword']
       # ls = ' "SNR_Active"=\'' + str(True) + '\''
        count=0
        data = 'select count(*) from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'# + 'And' + str(
            #ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / 10)
            if (count % 10 != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")
            results = AllProductsCoupons.objects.annotate(
                similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                           keyword) + TrigramSimilarity(
                    'SNR_Description', keyword)).filter(similarity__gte=0.3,).order_by("-similarity")[:800]
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / 10)
            if (items % 10) != 0:
                totalpages += 1
            serializer = Products_Coupons_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Coupon"},
                            status.HTTP_200_OK)
    elif type == 'Vocation':
        keyword = request.data['keyword']
        ls = ' "SNR_Active"=\'' + str(True) + '\''

        count=0
        data = 'select count(*) from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / 10)
            if (count % 10 != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore" from public."products_active_vocation" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceBefore':i[8]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)

        else:

            print("Similarity")
            results = Active_Vocation.objects.annotate(
                similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                           keyword) + TrigramSimilarity(
                    'SNR_Description', keyword)).filter(similarity__gte=0.3,).order_by("-similarity")[:800]
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / 10)
            if (items % 10) != 0:
                totalpages += 1
            serializer = Active_Vocation_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Vocation"},
                            status.HTTP_200_OK)
    elif type == 'Deals':
        ls = ' "SNR_Active"=\'' + str(True) + '\''
        q1 = Q()
        q1 &= Q(SNR_Active=True)
        if ('minprice' and 'maxprice' in request.data) :
            if request.data['minprice']!="-1" and request.data['maxprice']!="-1":
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(request.data['minprice']) + ' AND ' + str(
                    request.data['maxprice'])
                q1 &= Q(SNR_PriceAfter__gte=request.data['minprice'], SNR_PriceAfter__lte=request.data['maxprice'])
        if 'merchant' in request.data:
            ls = ls + 'And "SNR_Category"=\'' + str(request.data['merchant']) + '\''
            q1 &= Q(SNR_Category=request.data['merchant'])
        count=0
        if 'keyword' in request.data:
            keyword = request.data['keyword']
            data = 'select count(*) from public."products_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            ls)
        else:
            data = 'select count(*) from public."products_dailydeals" where' + str(
            ls)
        with connection.cursor() as cursor:
            cursor.execute(data)
            res = cursor.fetchall()
        for i in res:
                count = i[0]

        print("Total Coupans",count)
        if count>0:
            totalpages = int(count / 10)
            if (count % 10 != 0):
                totalpages += 1
            # data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available" from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')' + 'And' + str(
            #     ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            if 'keyword' in request.data:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore" from public."products_dailydeals" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'+ 'And' + str(
            ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
            else:
                data1 = 'select "id","SNR_Title","SNR_Description","SNR_Available","SNR_ProductURL","SNR_SKU","SNR_ImageURL","SNR_PriceAfter","SNR_PriceBefore" from public."products_dailydeals" where ' + str(
            ls) + ' LIMIT ' + str(
                    10) + ' OFFSET ' + str(offset);
            with connection.cursor() as cursor:
                cursor.execute(data1)
                res = cursor.fetchall()
            for i in res:
                a = {
                    'id': i[0],
                    'SNR_Title': i[1],
                    'SNR_Description': i[2],
                    'SNR_Available': i[3],
                    'SNR_ProductURL':i[4],
                    'SNR_SKU':i[5],
                    'SNR_ImageURL':i[6],
                    'SNR_Price':i[7],
                    'SNR_PriceBefore':i[8]

                }
                li.append(a)
            return Response({"totalitems": count, "totalpages": totalpages, "results": li, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)

        else:
            keyword = request.data['keyword']
            print("Similarity")
            results = DailyDeals.objects.annotate(
                similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                           keyword) + TrigramSimilarity(
                    'SNR_Description', keyword)).filter(similarity__gte=0.3,).filter(q1).order_by("-similarity")[:800]
            items = int(len(results))
            results = results[offset:limit]
            li = []

            totalpages = int(items / 10)
            if (items % 10) != 0:
                totalpages += 1
            serializer = DailyDeals_Serializer(results, many=True)
            return Response({"totalitems": items, "totalpages": totalpages, "results": serializer.data, "status": True,"type":"Deals"},
                            status.HTTP_200_OK)
    else:
        return Response({ "results": "Type Not Matched", "status": False,},status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def GetVendroNames(request):
    data = VendorNamesandImages.objects.filter(vendor_type='Deals')
    deals = []
    for value in data:
        data = {
            "name": value.vendor_name,
            "image": value.vendor_image
        }
        deals.append(data)

    data = VendorNamesandImages.objects.filter(vendor_type='Coupons')
    Coupons = []
    for value in data:
        data = {
            "name": value.vendor_name,
            "image": value.vendor_image
        }
        Coupons.append(data)

    data = VendorNamesandImages.objects.filter(vendor_type='Vacations')
    Vactions = []
    for value in data:
        data = {
            "name": value.vendor_name,
            "image": value.vendor_image
        }
        Vactions.append(data)
    dic = {
        "deals":deals,
        "vacations":Vactions,
        "coupons":Coupons
    }
    return Response(dic,status=status.HTTP_200_OK)
