from django.shortcuts import render

# Create your views here.



# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Feedback,Wishlist,Blog
from .serializer import Feedback_serializer,Wishlist_serializer, Blog_serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from products.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def Allunreadfeedback(request):
    if request.method == 'GET':
        customers = Feedback.objects.all()
        serializer = Feedback_serializer(customers, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def feedback(request):
    if request.method == 'POST':
        serializer = Feedback_serializer(data=request.data)
        if serializer.is_valid():
            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def blogAddition(request):


    if request.method == 'POST':

        file = request.FILES['image']
        user = request.data['user']

        print (file, user)


        # api_url = 'https://ns3101486.ip-54-36-177.eu/index.php'
        # base_url = 'https://ns3101486.ip-54-36-177.eu/'+user + '/' + str(user) + '/'+file.name
        # print base_url
        #
        # Blog_ImagePath =base_url

        # userdata = {'path': username + '/' + str(user) + '/', 'filename': file.name}
        # files = {'file': file.read()}
        # r = requests.post(api_url, files=files, params=userdata, verify=False)
        #
        # print r
        #
        # print r.status
        #
        #
        #
        # print serializer
        # blog = Blog(user_id=user,Blog_Title= request.data['Title'],Blog_Meta=request.data['Meta'],Blog_Detail=request.data['Content'],Blog_ImagePath=base_url)
        # print blog

            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg': 'ok'}, status=status.HTTP_201_CREATED)


@api_view(['GET','DELETE'])
@permission_classes((IsAuthenticated,))
def ADDwishlist_pro(request,pk):
    if request.method == 'GET':
        print('in')
        print(pk)
        res=Active_DailyDeals.objects.get(id=pk)
        if Wishlist.objects.filter(SNR_ProductURL=str(res.SNR_ProductURL),user=request.user).exists():
            print(">>>",res.SNR_ProductURL)
            return Response({'msg':'Already In WishList'},status.HTTP_403_FORBIDDEN)
        else:
            obj=Wishlist(
                SNR_SKU=res.SNR_SKU,
                user=request.user,
                SNR_Title=res.SNR_Title,
                # SNR_ModelNo=res.SNR_ModelNo,
                SNR_Brand=res.SNR_Available,
                # SNR_UPC=res.SNR_UPC,
                SNR_Price=res.SNR_PriceAfter,
                SNR_CustomerReviews=res.SNR_Customer_Rating,
                SNR_Available=res.SNR_Available,
                SNR_ProductURL=res.SNR_ProductURL,
                SNR_ImageURL=res.SNR_ImageURL,
                SNR_Description=res.SNR_Description,
                SNR_isShow=True,
                SNR_item_id=pk
            )
            obj.save()
            return Response({'msg':'Successfully Added In WhishList'},status.HTTP_200_OK)




@api_view(['POST'])
def deletefromwihslist(request):
    if Wishlist.objects.filter(SNR_ProductURL=request.data['url'], user=request.user).exists():
        res = Wishlist.objects.get(SNR_ProductURL=request.data['url'], user=request.user)

        res.delete()
        return Response({'msg': 'Delete Successful'}, status.HTTP_200_OK)
    return Response({"msg":"not found in wish list"},status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def ADDwishlist(request):

    if request.method == 'POST':
        #print request.data
        serializer = Wishlist_serializer(data=request.data)

        if serializer.is_valid():
            que = Q()
            que = Q(SNR_isShow=True)
            que &= Q(SNR_ProductURL=serializer.validated_data['SNR_ProductURL'])

            Data = Wishlist.objects.filter(que)
            print(len(Data))

            if(len(Data) > 0):
                return Response({"status":"Item already in wishlist"})

            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])
            else:
                que = Q()
                que = Q(SNR_isShow=False)
                que &= Q(SNR_ProductURL=serializer.validated_data['SNR_ProductURL'])

                Data = Wishlist.objects.filter(que)

                if (len(Data) > 0):
                    for prod in Data:
                        prod.SNR_isShow=True
                        prod.save()
                    return Response({"status": "Item added in wishlist"})
                else:

                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def checkwishlist(request):

    if request.method == 'POST':
            data = request.data
            user = request.user.id
            Data = Wishlist.objects.filter(SNR_ProductURL=request.data['SNR_ProductURL'],user__id=request.user.id).count()

            if(Data) > 0:
                return Response({"is_exist":True,
                                 "Description":"Item already in wishlist"})
            else:

                return Response({"is_exist":False,
                                 "Description":"Item not in wishlist"})

    else:
        return Response( status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def AllUsersWishlist(request):
    if request.method == 'GET':
        customers = Wishlist.objects.all()
        serializer = Wishlist_serializer(customers, many=True)
        return Response(serializer.data)



@api_view(['DELETE'])
def delete(self):

    snippet = Wishlist.objects.all()
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def deletefromWishlist(request,query,product):
    # print query
    # print product
    if request.method == 'DELETE':
        # print 'amad...'

        que = Q()
        que = Q(user=query)
        que &=Q(SNR_SKU__icontains=product)
        Data = Wishlist.objects.filter(que)
        # print "Data/..............",Data.count()

        for prod in Data:
            prod.SNR_isShow=False
            prod.save()
            # print prod.SNR_isShow


        # if(Data.count() > 0):
        #     Data.delete()
        #     return Response({
        #         "Found": "found"
        #     })
        #
        # else:
        #     return Response({
        #         "Found": "No Data found"
        #     })
        #

    else:

        return Response({
            "Error": "Erooooor"
        })

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def deletefromWishlistbyURL(request):
    if request.method == 'POST':
        #print request.data
        serializer = Wishlist_serializer(data=request.data)


        if serializer.is_valid():
            que = Q()
            que = Q(user=request.data['user'])
            que &= Q(SNR_ProductURL=request.data['SNR_ProductURL'])
            Data = Wishlist.objects.filter(que)
            # print len(Data)

            for prod in Data:
                prod.SNR_isShow = False
                prod.save()
                # print prod.SNR_isShow



            return Response({"status":True,
                             "Description":"Item Deleted"})


            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def Wishlistby_user(request):
    if request.method=='GET':
        res = Wishlist.objects.filter(user=request.user)
        paginator = Paginator(res, 30)
        page = request.GET.get('page')
        try:

            data = paginator.page(page)
        except PageNotAnInteger:

            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)
        items = paginator.count
        pages = paginator.num_pages
        serializer = Wishlist_serializer(data, many=True)
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res,status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Wishlistbyuser(request,query):
    #print(query)
   try:

       que = Q()
       que = Q(user=query)
       que &= Q(SNR_isShow=True)

       Data = Wishlist.objects.filter(que)
       paginator = Paginator(Data, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Wishlist_serializer(data,many=True,context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Wishlist.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass


@csrf_exempt
@api_view(['GET'])
def blogs(request):

   # #print(query)
   try:
       Data = Wishlist.objects.all()
       paginator = Paginator(Data, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Wishlist_serializer(data,many=True,context=serializer_context)

       items=paginator.count
       pages=paginator.num_pages
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Wishlist.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def WishlistALL(request):

   # #print(query)
   try:
       Data = Wishlist.objects.filter(SNR_isShow=True).order_by('SNR_Date')
       paginator = Paginator(Data, 30)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Wishlist_serializer(data,many=True,context=serializer_context)
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


   except Wishlist.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   pass


