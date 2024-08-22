from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .models import userReviews,VendorReviews, VendorReviewsScore,VendorNamesandImages,EmailAlert
from .serilizers import Review_Serializer,Vendor_Review_Serializer, Vendor_Review_Score_Serializer
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import bestbuyReviews



@api_view(['POST'])
def add_Reviews(request):

    if request.method == 'POST':

        serializer = Review_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            serializer.save();


            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_ReviewsBestBuy(request):

    if request.method == 'POST':

        serializer = Review_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            requestdata = serializer.validated_data
            # serializer.save();
            # print "Calling"

            bestapi = bestbuyReviews.bestbuy()
            bestapi.scrapeBestBuyProduct_Reviews(requestdata)


            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Filter_reviews(request,query):

   print(query)
   try:
       que =   Q(SNR_ProductID__icontains=query) |Q(SNR_UPC__icontains=query)
       Mobile_all = userReviews.objects.filter(que).order_by("-SNR_Date")
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Review_Serializer(record,many=True,context=serializer_context)
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


   except userReviews.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)







@api_view(['GET'])
def Filter_VendorReviews(request,query):

   print(query)
   try:
       que =   Q(SNR_ProductID__icontains=query) |Q(SNR_UPC__icontains=query)
       Mobile_all = VendorReviews.objects.filter(que)
       paginator = Paginator(Mobile_all, 15)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Vendor_Review_Serializer(record,many=True,context=serializer_context)
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


   except userReviews.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




from rest_framework import serializers


@api_view(['GET'])
def Filter_ReviewsScores(request,query):

   print(query)
   try:
       que =   Q(reviews__SNR_UPC=query) |Q(reviews__SNR_ProductID=query) |Q(reviews__SNR_ProductTitle=query)
       Mobile_all = VendorReviewsScore.objects.filter(que).select_related()
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Vendor_Review_Score_Serializer(record,many=True,context=serializer_context)
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


   except userReviews.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





def allreviews():
    reviewData=VendorReviews.objects.all()

    return reviewData


@api_view(['DELETE'])
def deleteallreviews():
    reviewData=VendorReviews.objects.all()

    reviewData.delete()
    return "amad"








import requests
import json

@api_view(['POST'])
def Calculate_VendorReviewsScore(request):

   # print(query)
   try:
        reviewData=allreviews();
        # print reviewData.count()
        for data in reviewData:
            # print data.SNR_Review
            # print str(reviewData[0].SNR_Review)

            headers ={'Content-Type': 'application/json'}
            userdata = {'category': "laptop2" , 'review':str(data.SNR_Review)}
            try:
                r = requests.post('http://ns519750.ip-158-69-23.net:8100/func/demo/',  json=userdata, headers=headers)
                print('rrrr    ', r.content)
                print('rrrr    ', r)

                review = VendorReviewsScore(SNR_ProductID=data, SNR_VendorScoreAll=r.json())
                review.save()

            except:
                # print "Error while calling...."
                pass

        return Response(r.json())


   except userReviews.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['DELETE'])
def delete(self):

    snippet = userReviews.objects.all()
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def GetVendorReviews(request):

   try:
       Mobile_all = VendorReviews.objects.all()
       paginator = Paginator(Mobile_all, 25)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Vendor_Review_Serializer(record,many=True,context=serializer_context)
       items=paginator.count
       pages=paginator.num_pages
       res={
            'totalItems':items,
            'totalPages':pages,
                'results': serializer.data

        }
       return Response(res)


   except userReviews.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def getAll_Revies(request):
    try:

        data_all = userReviews.objects.all().order_by("-SNR_Date")
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Review_Serializer(data,many=True,context=serializer_context)
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

    except userReviews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ReviewsScore(request):
    try:

        data_all = VendorReviewsScore.objects.all().order_by("-SNR_Date")
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Vendor_Review_Score_Serializer(data,many=True,context=serializer_context)
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

    except userReviews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




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


@api_view(['POST'])
def EmailforUser(request):
    data=request.data
    if 'deals' in data:
        EmailAlert.objects.filter(user_id__id=request.user.id, alerty_type='Deals').delete()
        for valu in data['deals']:
            # EmailAlert.objects.filter(user_id__id=request.user.id,alerty_type='Deals').delete()
            if  not EmailAlert.objects.filter(user_id__id=request.user.id,vendor_name=valu,alerty_type='Deals').exists():
                EmailAlert.objects.create(
                    user_id=request.user,
                    vendor_name=valu,
                    alerty_type='Deals'
                )
                print(valu)
    if 'coupons' in data:
        EmailAlert.objects.filter(user_id__id=request.user.id, alerty_type='Coupons').delete()
        for valu2 in data['coupons']:
            if not EmailAlert.objects.filter(user_id__id=request.user.id, vendor_name=valu2,
                                             alerty_type='Coupons').exists():
                EmailAlert.objects.create(
                    user_id=request.user,
                    vendor_name=valu2,
                    alerty_type='Coupons'
                )
    if 'vacations' in data:
        EmailAlert.objects.filter(user_id__id=request.user.id, alerty_type='Vacations').delete()
        for valu3 in data['vacations']:
            if not EmailAlert.objects.filter(user_id__id=request.user.id, vendor_name=valu3,
                                             alerty_type='Vacations').exists():

                EmailAlert.objects.create(
                    user_id=request.user,
                    vendor_name=valu3,
                    alerty_type='Vacations'
                )
    return Response(data,status=status.HTTP_200_OK)




@api_view(['GET'])
def GetActiveEmilVendors(request):
    userdata = EmailAlert.objects.filter(user_id__id=request.user.id)
    deals = []
    vacations = []
    coupons = []
    for data in userdata:
        if data.alerty_type=='Deals':
            deals.append(data.vendor_name)
        elif data.alerty_type == 'Vacations':
            vacations.append(data.vendor_name)
        elif data.alerty_type =='Coupons':
            coupons.append(data.vendor_name)
    dic = {
        "deals": deals,
        "vacations": vacations,
        "coupons" : coupons
    }
    return Response(dic,status=status.HTTP_200_OK)


