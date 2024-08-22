from .models import UserDetails, sendFriends
from credential.serializer import UserLoginSerializer, UserSerializer, UserSerializerforPassword, UserDetailsSerializer, \
    UserLoginIDSerializer, friendEmailSerilizer, UserSerializerwithoutPassword
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from social_django.models import UserSocialAuth
# from rest_framework_jwt.settings import api_settings
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# from open_facebook import OpenFacebook
from django.contrib.auth import logout
from .serializer import SubscriberSerilizer, ResetPasswordSerilizer
from .models import Subscribers, Reset_password
import random

########################################################


from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import JsonResponse


##########################


import json
import random
import re
import string

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.mail import EmailMessage
# from simple_email_confermation.models import EmailMessage
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import render
from django.http import HttpResponse
import base64
import uuid
from django.template.loader import get_template
from django.core.mail import EmailMessage
import requests
from django.contrib.auth import authenticate
# from rest_framework_jwt.settings import api_settings
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
# from rest_framework_jwt.serializers import JSONWebTokenSerializer


#############################
def logout_view(request):
    if not request.user.is_authenticated:
        logout(request)
        return redirect('http://www.buynroar.com/login')
    else:
        logout(request)
        return redirect('http://www.buynroar.com')

    # Redirect to a success page.


def social_oauth_error(request):
    print ("errrrrrrrrrrorrrrrrrrrrr")





@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def customer_social_register_login_backup(request):
    # serializer_class =
    # try:
    user_name=""
    print(request.data)

    temp = request.data["user"]

    socialAuthToken = temp[u"authToken"]
    headers = {
        'Authorization': 'Bearer {0}'.format(socialAuthToken),
        "Content-Type": "application/json"}

    def Facebook():
        social_verification = requests.post("https://graph.facebook.com/v2.8/me", headers=headers)
        return social_verification.status_code == 200

    def Google(token):
        print(token)
        social_verification = requests.get("https://www.googleapis.com/oauth2/v2/tokeninfo?access_token={0}".format(token))
        print("social Varification",social_verification)
        return social_verification.status_code == 200


    is_valid = Facebook() if temp[u"provider"] == "FACEBOOK" else Google(socialAuthToken)

    if is_valid:

        """if (email_verifying(request.data['email'])):
            return generate_email_error()

        if (username_verifying(request.data['username'])):
            return generate_username_error()
        """
        password = "{0}{1}{2}".format(temp["provider"], temp["id"], "coursefrenzy")
        print("password")
        try:
            # return token if user exists
            print ("tryyyyyy....")
            object_user = UserDetails.objects.get(social_id=temp["id"],social_provider=temp["provider"]).user
            # payload = jwt_payload_handler(object_user)
            # token = jwt_encode_handler(payload)
            username = "{0}_{1}_{2}".format(temp["provider"], temp["id"], temp["name"]).lower()
            username = re.sub("[^\+\d\w_@\.-]+","",username)
            print(user_name)
            # print(token)
        except Exception as e:
            # print "except"
            # create user and return token
            # print temp["email"]
            user_already = User.objects.filter(email=temp["email"])
            # print user_already
            # print user_already['username']
            # print "length"
            # print len(user_already)
            if(len(user_already)>0):
                # payload = jwt_payload_handler(user_already)
                # token = jwt_encode_handler(payload)

                return HttpResponse(json.dumps({"error": True,
                                                # "token":token,
                                                "message":"this email is registered manually",
                                                }))

            username = "{0}_{1}_{2}".format(temp["provider"], temp["id"], temp["name"]).lower()
            username = re.sub("[^\+\d\w_@\.-]+","",username)
            user_name=username
            object_user = User(username=username,email=temp["email"],first_name=temp['firstName'],last_name=temp['lastName'])
            object_user.set_password(password)
            # print "saving user before"
            object_user.save()
            # print object_user
            # print "saved user"
            profile = UserDetails(
                isAuthenticated=True,
                is_social=True,
                email=temp["email"],
                user=object_user,
                social_id = temp["id"],
                social_provider = temp["provider"],
                profilePhoto = temp["photoUrl"]
                # # user=object_user
            )

            profile.save()

            # payload = jwt_payload_handler(object_user)
            # token = jwt_encode_handler(payload)

        # return HttpResponse(json.dumps({"token": token,
        #                                 "username":username}))

    else:
        return Response({'status': False, 'message': 'Invalid Information. Please try again.'}, status=status.HTTP_200_OK)

def social_oauth_error(request):
    print ("errrrrrrrrrrorrrrrrrrrrr")



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def customer_social_register_login(request):
    # serializer_class =
    # try:
    user_name=""
    print(request.data)

    temp = request.data["user"]

    socialAuthToken = temp[u"authToken"]
    headers = {
        'Authorization': 'Bearer {0}'.format(socialAuthToken),
        "Content-Type": "application/json"}

    def Facebook():
        social_verification = requests.post("https://graph.facebook.com/v2.8/me", headers=headers)
        return social_verification.status_code == 200

    def Google(token):
        print(token)
        social_verification = requests.get("https://www.googleapis.com/oauth2/v2/tokeninfo?access_token={0}".format(token))
        print ("social Varification",social_verification)
        return social_verification.status_code == 200


    is_valid = Facebook() if temp[u"provider"] == "FACEBOOK" else Google(socialAuthToken)

    if is_valid:

        """if (email_verifying(request.data['email'])):
            return generate_email_error()

        if (username_verifying(request.data['username'])):
            return generate_username_error()
        """
        password = "{0}{1}{2}".format(temp["provider"], temp["id"], "coursefrenzy")
        print("password")
        try:
            # return token if user exists
            print ("tryyyyyy....")
            object_user = UserDetails.objects.get(social_id=temp["id"],social_provider=temp["provider"]).user
            # payload = jwt_payload_handler(object_user)
            # token = jwt_encode_handler(payload)
            username = "{0}_{1}_{2}".format(temp["provider"], temp["id"], temp["name"]).lower()
            username = re.sub("[^\+\d\w_@\.-]+","",username)
            print(user_name)
            # print(token)
        except Exception as e:
            # print "except"
            # create user and return token
            # print temp["email"]
            user_already = User.objects.filter(email=temp["email"])
            # print user_already
            # print user_already['username']
            # print "length"
            # print len(user_already)
            if(len(user_already)>0):
                # payload = jwt_payload_handler(user_already)
                # token = jwt_encode_handler(payload)

                return HttpResponse(json.dumps({"error": True,
                                                # "token":token,
                                                "message":"this email is registered manually",
                                                }))

            username = "{0}_{1}_{2}".format(temp["provider"], temp["id"], temp["name"]).lower()
            username = re.sub("[^\+\d\w_@\.-]+","",username)
            user_name=username
            object_user = User(username=username,email=temp["email"],first_name=temp['firstName'],last_name=temp['lastName'])
            object_user.set_password(password)
            # print "saving user before"
            object_user.save()
            # print object_user
            # print "saved user"
            profile = UserDetails(
                isAuthenticated=True,
                is_social=True,
                email=temp["email"],
                user=object_user,
                social_id = temp["id"],
                social_provider = temp["provider"],
                profile_image = temp["photoUrl"]
                # profilePhoto = temp["photoUrl"]
                # # user=object_user
            )

            profile.save()

            # payload = jwt_payload_handler(object_user)
            # token = jwt_encode_handler(payload)
        # return HttpResponse(json.dumps({"token": token,
        #                                 "username":username})) # "image":temp["photoUrl"]

    else:
        return Response({'status': False, 'message': 'Invalid Information. Please try again.'}, status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
def customer_social_register_login_testing(request):
    # serializer_class =
    # try:
    user_name=""
    print(request.data)

    temp = request.data["user"]

    socialAuthToken = temp[u"authToken"]
    headers = {
        'Authorization': 'Bearer {0}'.format(socialAuthToken),
        "Content-Type": "application/json"}

    def Facebook():
        social_verification = requests.post("https://graph.facebook.com/v2.8/me", headers=headers)
        return social_verification.status_code == 200

    def Google(token):
        print(token)
        social_verification = requests.get("https://www.googleapis.com/oauth2/v2/tokeninfo?access_token={0}".format(token))
        print("social Varification",social_verification)
        return social_verification.status_code == 200


    is_valid = Facebook() if temp[u"provider"] == "FACEBOOK" else Google(socialAuthToken)

    if is_valid:

        """if (email_verifying(request.data['email'])):
            return generate_email_error()

        if (username_verifying(request.data['username'])):
            return generate_username_error()
        """
        password = "{0}{1}{2}".format(temp["provider"], temp["id"], "coursefrenzy")
        print("password")
        try:
            # return token if user exists
            print ("tryyyyyy....")
            object_user = UserDetails.objects.get(social_id=temp["id"],social_provider=temp["provider"]).user
            # payload = jwt_payload_handler(object_user)
            # token = jwt_encode_handler(payload)
            username = "{0}_{1}_{2}".format(temp["provider"], temp["id"], temp["name"]).lower()
            username = re.sub("[^\+\d\w_@\.-]+","",username)
            print(user_name)
            # print(token)
        except Exception as e:
            # print "except"
            # create user and return token
            # print temp["email"]
            user_already = User.objects.filter(email=temp["email"])
            # print user_already
            # print user_already['username']
            # print "length"
            # print len(user_already)
            if(len(user_already)>0):
                # payload = jwt_payload_handler(user_already)
                # token = jwt_encode_handler(payload)

                return HttpResponse(json.dumps({"error": True,
                                                # "token":token,
                                                "message":"this email is registered manually",
                                                }))

            username = "{0}_{1}_{2}".format(temp["provider"], temp["id"], temp["name"]).lower()
            username = re.sub("[^\+\d\w_@\.-]+","",username)
            user_name=username
            object_user = User(username=username,email=temp["email"],first_name=temp['firstName'],last_name=temp['lastName'])
            object_user.set_password(password)
            # print "saving user before"
            object_user.save()
            # print object_user
            # print "saved user"
            profile = UserDetails(
                isAuthenticated=True,
                is_social=True,
                email=temp["email"],
                user=object_user,
                social_id = temp["id"],
                social_provider = temp["provider"],
                # profilePhoto = temp["photoUrl"]
                # # user=object_user
            )

            profile.save()

            # payload = jwt_payload_handler(object_user)
            # token = jwt_encode_handler(payload)

        # return HttpResponse(json.dumps({"token": token,
        #                                 "username":username}))

    else:
        return Response({'status': False, 'message': 'Invalid Information. Please try again.'}, status=status.HTTP_200_OK)



# @login_required
# def social_settings(request):
    # print "asmasd"
    # print request

    # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    # agent=request.META['HTTP_USER_AGENT']
    #
    # # print agent;
    #
    # # print request.user
    # user = request.user
    # request.session['username'] = user.username
    # # payload = jwt_payload_handler(user)
    # # token = jwt_encode_handler(payload)
    # # try:
    # #     github_login = user.social_auth.get(provider='github')
    # # except UserSocialAuth.DoesNotExist:
    # #     github_login = None
    #
    # try:
    #     # logout(request=request)
    #
    #     try:
    #         google_login = user.social_auth.get(provider='google-oauth2')
    #     except:
    #         google_login = user.social_auth.filter(provider='google-oauth2')[0]
    #
    #     accesstokengoogle = google_login.extra_data['access_token']
    #     # print accesstokengoogle
    #     # return redirect(
    #         # 'https://www.buynroar.com/?username=' + user.username + '&token=' + token + '&ft=' + accesstokengoogle)
    # # except UserSocialAuth.DoesNotExist:
    #     try:
    #         google_login = user.social_auth.filter(provider='google-oauth2')[0]
    #         accesstokengoogle = google_login.extra_data['access_token']
    #         # print accesstokengoogle
    #         # return redirect(
    #             # 'https://www.buynroar.com/?username=' + user.username + '&token=' + token + '&ft=' + accesstokengoogle)
    #     except:
    #         # print "Error"
    #         pass
    # try:
    #     twitter_login = user.social_auth.get(provider='twitter')
    #     accesstokenfb = twitter_login.extra_data['access_token']
    #     return redirect(
    #         'http://www.buynroar.com/login?username=' + user.username + '&token=' + token + '&ft=' + accesstokenfb)
    # # except UserSocialAuth.DoesNotExist:
    #     github_login = None
    # try:
    #
    #     facebook_login = user.social_auth.get(provider='facebook')
    #
    #     accesstokenfb = facebook_login.extra_data['access_token']
    #     facebook = OpenFacebook(accesstokenfb)
    #     # print(facebook.me())
    #     logout(request=request)
    #     return redirect(
    #         'https://www.buynroar.com/login?username=' + user.username + '&token=' + token + '&ft=' + accesstokenfb + '&img=' + facebook.my_image_url(
    #             size='large'))
    # except UserSocialAuth.DoesNotExist:
    #     facebook_login = None
    #
    # can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    # to_json = {'username': user.username,
    #                      'email':  user.email,
    #                      'token': token},

    # consumer_key = 'qG3i9jwAh1jday01dJxp1adgm'
    # consumer_secret = 'Xw4iyZYxL9ksQpV8X7cZKhUMYl3HVS5A90iazywEE663gUnq09'

    # instance = UserSocialAuth.objects.filter(user=user).get()
    # oauth_access_token = (instance.tokens).get('oauth_token')
    # oauth_access_secret = (instance.tokens).get('oauth_token_secret')

    #
    # return redirect('https://www.influexp.com/twlogin?username='+user.username+'&token='+token+'&img='+twuser.profile_image_url)

    # return JsonResponse({'username': user.username,
    #                      'email':  user.email,
    # #                      'token': token})
    # return render(request, 'core/settings.html', {
    #     'github_login': github_login,
    #     'twitter_login': twitter_login,
    #     'facebook_login': facebook_login,
    #     'can_disconnect': can_disconnect
    # })


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def verify_username(request, username):
    if User.objects.filter(username=username).exists():
        return Response({'Res': True,'status':"Already Exists"},status.HTTP_404_NOT_FOUND)
    else:

        return Response({'Res': False,"status":"Not Exist"},status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def verify_account(request):
    if request.method == 'POST':
        verification = request.data['verification']
        # print verification
        if UserDetails.objects.filter(SeceretKey=verification).exists():
            verify = UserDetails.objects.get(SeceretKey=verification)
            # print verify
            verify.isAuthenticated=True
            verify.save()
            key = {
                'fname': verify.user.first_name
            }
            message = get_template('Account_Verify.html').render(key)
            email = EmailMessage('BUYnROAR Account Verification Successful', message, to=[verify.email])
            email.content_subtype = 'html'
            email.send()
            return Response(
                {'result': 'verification succeeded',
                 'code': True},
            status=status.HTTP_200_OK)
        else:
            return Response({
                'result':'verification failed',
            'code':False},
                status=status.HTTP_200_OK
                )

        return Response(
             status=status.HTTP_400_BAD_REQUEST)
    return Response(
        status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def verify_user_authenticated(request):
    if request.method == 'POST':
        username = request.data['username']
        if UserDetails.objects.filter(user__username=username).exists():
            verify=UserDetails.objects.get(user__username=username)
            isAuthenticated=verify.isAuthenticated;
            if(isAuthenticated==True):
                return Response({'result': 'Verified', 'code': True}, status=status.HTTP_200_OK)
            else:
                return Response({'result': 'Not Verified', 'code': False}, status=status.HTTP_200_OK)
        else:
            return Response({'result': 'User name not exists', 'code': False}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def resend_authentication(request):
    if request.method == 'POST':
        username = request.data['username']
        if UserDetails.objects.filter(user__username=username).exists():

            verify=UserDetails.objects.get(user__username=username)


            isAuthenticated = verify.isAuthenticated;
            if (isAuthenticated == False):


                email=verify.email;
                # print email

                secretkey = ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
                    range(75))

                link = 'buynroar.com/register/?verification=' + secretkey
                values = {
                    'link': link,
                    'code': ''
                }
                # message="Thanks for signing-up with SHOPNROAR"


                message = get_template('shopnroar-activation-account.html').render(values)

                to_list = [email]
                # to_list = [email]
                from_email = settings.EMAIL_HOST_USER
                email_obj = EmailMessage('Account Verification ', message, from_email, to=to_list)
                email_obj.content_subtype = 'html'
                email_obj.send()
                verify.SeceretKey=secretkey;
                verify.save();
                # print verify

                return Response(
                    {'result': 'Mail Sent',
                     'code': True},
                status=status.HTTP_200_OK)
            else:
                return Response(
                    {'result': 'Account already verified',
                     'code': True},
                    status=status.HTTP_200_OK)

        else:

            return Response(
                {'result': 'Username DoesNot Exist',
                 'code': False},
                 status=status.HTTP_400_BAD_REQUEST)
    return Response(
        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def email_verify(response, email):
    arr = User.objects.filter(email=email)
    if (arr.count() > 0):
        return Response({'Res': True,'status':"Already Exists"},status.HTTP_404_NOT_FOUND)

    else:
        return Response({'Res': False,'status':"Not Exists"},status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def check_password(request):
    if request.method == 'POST':

        user = request.data['username']
        password = request.data['password']
        arr = User.objects.get(username=user)
        if (arr.check_password(password)):
            data = {'exists': 'Yes'}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'exists': 'No'}
            return Response(data, status=status.HTTP_200_OK)

        # serializer = UserSerializerforPassword(data=request.data)
        # print serializer
        #
        # if serializer.is_valid():
        #     print "here..................//////////////"
        #
        #     user=serializer.validated_data['username']
        #     arr = User.objects.get(username = user)
        #     print arr
        #     password=serializer.validated_data['password']
        #     if (arr.check_password(password)):
        #         data = {'exists': 'Yes'}
        #         return Response(data,status=status.HTTP_200_OK)
        #     else:
        #         data = {'exists': 'No'}
        #         return Response(data,status=status.HTTP_200_OK)
        # else:
        #     Response( {'exists': 'No'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'exists': 'No'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.authentication import SessionAuthentication

class DeleteUser(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, pk):
        user = User.objects.filter(pk=pk)
        if user.exists():
            user.delete()
            return Response({'detail': 'User has been deleted successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

class DeleteUserByEmail(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # return Response({"status" : False ,'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({"status" : False ,'detail': 'User not found.'}, status=404)
            # return HttpResponse('<h1>User not found.</h1>', status=404)

        user.delete()
        print(user, 'User deleted by email')
        # return Response({"status" : True, 'detail': 'User deleted successfully.'}, status=status.HTTP_200_OK)
        return JsonResponse({"status" : True, 'detail': 'User deleted successfully.'}, status=status.HTTP_200_OK)
        # return HttpResponse('<h1>User deleted successfully.</h1>', status=200)





@csrf_exempt
#; @permission_classes((IsAuthenticated,))
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def user_list(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.data['username']).exists():
            if User.objects.filter(email=request.data['email']).exists():
                sts = {'Message': 'Username And Email Aleady Exist', 'status': False}
            else:
                sts = {'Message': 'UserName ALready Exist', 'status': False}
            return Response(sts, status=status.HTTP_404_NOT_FOUND)
        else:
            if User.objects.filter(email=request.data['email']).exists():
                sts = {'Message': 'Email ALready Exist', 'status': False}
                return Response(sts, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    user = User(username=serializer.validated_data['username'], email=serializer.validated_data['email'],
                                first_name=serializer.validated_data['first_name'],
                                last_name=serializer.validated_data['last_name'])
                    user.set_password(raw_password=serializer.validated_data['password'])
                    user.save()

                    secretkey = ''.join(
                        random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
                        range(75))

                    # link = 'http://www.shopnroar.com/register/?verification=' + secretkey
                    link = 'http://www.buynroar.com/register/?verification=' + secretkey
                    values = {
                        'link': link,
                        'fname':request.data['first_name'],
                        'code': ''
                    }
                    message="Thanks for signing-up with BUYnROAR"
                    userdetail = UserDetails(user=user,
                                             Mobile=request.data.get('Mobile', ''),
                                             email=request.data['email'],
                                             newsLetter=request.data.get('newsLetter', False),
                                             SeceretKey=secretkey,
                                             snr_uid=request.data.get('snr_uid', ''),
                                             lat=request.data.get('lat', None),
                                             lng=request.data.get('lng', None),
                                             city=request.data.get('city', ''),
                                             state=request.data.get('state', ''),
                                             country=request.data.get('country', '')
                                             )

                    userdetail.save()
                    message = get_template('Activation_Email.html').render(values)
                    to_list = [serializer.validated_data['email']]
                    email_obj = EmailMessage('Activate your account on BUYnROAR', message, to=to_list)
                    email_obj.content_subtype = 'html'
                    email_obj.send()
                    serializer = UserSerializer(user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_user_credentials(request):
    if request.method == 'POST':
        # serializer = JSONWebTokenSerializer(data=request.data)
        serializer = None
        if serializer.is_valid():

            data = serializer.validated_data
            response = {'token': data.get('token', None)}
            user = data.get('user', None)
            if user:
                response['first_name'] = user.first_name
                response['last_name'] = user.last_name
                response['snr_uid'] = user.user_detail.snr_uid
                response['lat'] = user.user_detail.lat
                response['lng'] = user.user_detail.lng
                response['city'] = user.user_detail.city
                response['state'] = user.user_detail.state
                response['country'] = user.user_detail.country
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def user_login(request):
    # usercred= serializers();

    json = {}
    u = User()
    serializer = UserLoginSerializer(u, data=request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            if request.method == 'POST':
                if user.validate_password(serializer.validated_data['password']):

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    json['message'] = 'success'
                    return Response(json['message'], status=status.HTTP_406_NOT_ACCEPTABLE)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getID(request, query):
    try:
        data = User.objects.filter(username=query)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserLoginIDSerializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@csrf_exempt
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getProfile_backup(request, query):
    try:
        data = User.objects.get(username=query)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializerwithoutPassword(data)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

# @csrf_exempt
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def getProfile(request, query):
#     try:
#         data = User.objects.get(username=query)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSerializerwithoutPassword(data)  # many=True so it doesn't return only 1 JSON Object
#         data = dict(serializer.data)
#         data['image'] = str(UserDetails.objects.get(user__username=serializer.data['username']).profile_image)
#
#         return Response(data)
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)


from urllib.request import urlopen
@csrf_exempt
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getProfile(request, query):
    try:
        data = User.objects.get(username=query)
    except User.DoesNotExist:
        return Response({"Detail": "User does not exit"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializerwithoutPassword(data)  # many=True so it doesn't return only 1 JSON Object
        data = dict(serializer.data)
        image = UserDetails.objects.get(user__username=query).profile_image
        if image=='':
            data['image'] = ''
        else:
            try:
                urlopen(str(image))
                data['image'] = str(image)
            except:
                data['image'] = request.build_absolute_uri(image.url)
        return Response(data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updateProfile(request):
    if request.method == 'POST':
        try:
            data = User.objects.get(username=request.data['username'])
            user_details = UserDetails.objects.get(user__username=request.data['username'])
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # print ('saataaaaaaa  ', data)
        data.email = request.data['email']
        data.username = request.data['username']
        data.first_name = request.data['first_name']
        data.last_name = request.data['last_name']

        # data = data(username=request.data['username'],email=request.data['email'],first_name=request.data['first_name'],last_name=request.data['last_name'])
        data.save()
        user_details.profile_image = request.data['image']
        user_details.save()
        # if(data.save()):
        #     return Response({
        #         "update":"True"
        #     })
        # else:
        #     return Response({
        #         "update": "False"
        #     })
        return Response({"message":"Profile Updated Succesfully"},status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updateProfile_backup(request):
    if request.method == 'POST':
        try:
            data = User.objects.get(username=request.data['username'])
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # print ('saataaaaaaa  ', data)
        data.email = request.data['email']
        data.username = request.data['username']
        data.first_name = request.data['first_name']
        data.last_name = request.data['last_name']

        # data = data(username=request.data['username'],email=request.data['email'],first_name=request.data['first_name'],last_name=request.data['last_name'])
        data.save()
        # if(data.save()):
        #     return Response({
        #         "update":"True"
        #     })
        # else:
        #     return Response({
        #         "update": "False"
        #     })
        return Response({"message":"Profile Updated Succesfully"},status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updatePassword(request):
    try:
        email = request.data['email']
        password = request.data['password']

        if request.method == 'POST':

            Obj = User.objects.get(email__icontains=email)
            Obj2 = Reset_password.objects.filter(email__icontains=email).order_by('id').last()

            if Obj:
                Obj.set_password(password)
                Obj.save()
                Obj2.isValid = True
                Obj2.save()

                return Response({"result": "true"})

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pass


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updatePasswordManually(request):
    try:

        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']

            Obj = User.objects.get(username=username)
            if Obj:
                Obj.set_password(password)
                Obj.save()
                key={
                    'fname':Obj.first_name
                }
                message = get_template('Change_Password.html').render(key)
                email = EmailMessage('BUYnROAR Notification - Your password has been changed', message, to=[Obj.email])
                email.content_subtype = 'html'
                email.send()
                return Response({"result": "true"})

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pass


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def CheckResetPassword(request):
    serializer = ResetPasswordSerilizer(data=request.data)
    if request.method == 'POST':
        if serializer.is_valid():
            # print serializer.validated_data['link']
            data = Reset_password.objects.filter(link=serializer.validated_data['link'])
            serializer = ResetPasswordSerilizer(data, many=True)
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def CheckResetCodemail(request):
    serializer = ResetPasswordSerilizer(data=request.data)
    if request.method == 'POST':
        if serializer.is_valid():
            # print serializer.validated_data['Code']
            data = Reset_password.objects.filter(Code=serializer.validated_data['Code'])
            serializer = ResetPasswordSerilizer(data, many=True)
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def CheckResetCode(request):
    serializer = ResetPasswordSerilizer(data=request.data)
    if request.method == 'POST':
        if serializer.is_valid():

            data = Reset_password.objects.filter(Code=serializer.validated_data['Code'])
            if (data.count() > 0):
                data = {'exists': 'Yes'}
                return Response(data)
            else:
                data = {'exists': 'No'}
                return Response(data)


from django.template.loader import get_template
from random import randint
import string


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def ResetPassword(request):
    # if request.method == 'GET':
    #     data = Reset_password.objects.all()
    #     serializer = ResetPasswordSerilizer(data, many=True)
    #     return Response(serializer.data)
    #
    # elif request.method == 'POST':
    #
    #     serializer = ResetPasswordSerilizer(data=request.data)
    #
    #     if serializer.is_valid():
    #         #
    #         #
    #         # subject = "Password recovery"
    #         code = random.randint(1000, 99999) * 5;
    #         serializer.validated_data['Code'] = code
    #         secretkey = ''.join(
    #             random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
    #             range(75))
    #
    #         serializer.validated_data['link'] = 'http://www.shopnroar.com/reset/' + secretkey
    #
    #         values = {
    #             'link': serializer.validated_data['link'],
    #
    #             'code': str(serializer.validated_data['Code'])
    #         }
    #
    #         message = get_template('reset_email.html').render(values)
    #
    #         serializer.save()
    #
    #         to_list = [serializer.validated_data['email']]
    #         from_email = settings.EMAIL_HOST_USER
    #         email_obj = EmailMessage('Reset Password ', message, from_email, to=to_list)
    #         email_obj.content_subtype = 'html'
    #         email_obj.send()
    #
    #         # except :
    #         #     #print "false"
    #
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            username = request.data['user']
            if User.objects.filter(email=username).exists():
                user = User.objects.get(email=username)
                reg_obj = UserDetails.objects.get(user = user)
                if (reg_obj.isAuthenticated == True):
                    reset_email_token = ''.join(
                        random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(75))
                    while (UserDetails.objects.filter(SeceretKey=reset_email_token).exists()):
                        reset_email_token = ''.join(
                            random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                            for _ in range(75))
                    key = {
                        'link': 'http://www.buynroar.com/reset/' + reset_email_token,
                        'fname':user.first_name
                    }
                    message = get_template('reset_email.html').render(key)
                    email = EmailMessage('BUYnROAR Password Reset Request', message, to=[reg_obj.email])
                    email.content_subtype = 'html'
                    email.send()
                    reg_obj.Activation_Key = reset_email_token
                    reg_obj.save()
                    return Response({'message':'Reset Password mail send Successfully'},status.HTTP_200_OK)
                else:
                    return Response({'message':'User Not verify'},status.HTTP_200_OK)
            else:
                return Response({'message': 'Email Not Exist'}, status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdateLink(request, email):
    if request.method == 'POST':
        Obj = Reset_password.objects.get(email__icontains=email)
        if Obj:
            Obj.isValid = "False"
            Obj.save()
            return Response({"result": "true"})


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def userDetaillist(request):
    if request.method == 'GET':
        customers = UserDetails.objects.all()
        serializer = UserDetailsSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def AllSubscribers(request):
    if request.method == 'GET':
        customers = Subscribers.objects.all()
        serializer = SubscriberSerilizer(customers, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def Subscribe(request):
    if request.method == 'POST':

        serializer = SubscriberSerilizer(data=request.data)
        if serializer.is_valid():
            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def friendmailList(request):
    if request.method == 'GET':
        customers = sendFriends.objects.all()
        serializer = friendEmailSerilizer(customers, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def emailToFriend(request):
    if request.method == 'POST':

        serializer = friendEmailSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            subject = "Your friend share this page with you"
            link = request.data['sharedlink']
            mail = request.data['email']

            message = "here you can visit our page by clicking on this link " + link
            to_list = [mail]
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .models import *

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def intrst(request):
    if request.method == 'POST':
        if Interst.objects.filter(user=request.user,Product=request.data['title']).exists():
            re = Interst.objects.get(user=request.user,SNR_Available=request.data['merchant'])
            re.Count=re.Count + 1
            re.Product=request.data['title']
            re.save()
        else:
            obj=Interst(user=request.user,Product=request.data['title'],Count=1,SNR_Available=request.data['merchant'])
            obj.save()
        return Response({'msg':'Success'},status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_count_merchant(request,mer):
    if request.method == 'GET':
        re = Interst.objects.filter(SNR_Available=str(mer)).values()
        return Response(re,status.HTTP_200_OK)
# import after_response
# @after_response.enable
def emailsending(key,template,email,msg):
    print('ok')
    message = get_template(template).render(key)
    email = EmailMessage(msg, message, to=[email])
    email.content_subtype = 'html'
    email.send()
    # email = EmailMessage(msg, message, to=['muhammad.zeeshan@brainplow.com',])
    # email.content_subtype = 'html'
    # email.send()
    print('Email Send Successfully')
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def ForgetPssword(request):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            reg_obj = UserDetails.objects.get(user= user)
            if (reg_obj.isAuthenticated == True):
                reset_email_token = ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _
                    in range(200))
                while (UserDetails.objects.filter(SeceretKey=reset_email_token).exists()):
                    reset_email_token = ''.join(
                        random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                        for _
                        in
                        range(100))
                key = {
                    'link': 'https://www.buynroar.com/reset_Password/'+ reset_email_token,
                    'Fname':reg_obj.user.username
                }
                # emailsending.after_response(key,'Activation_Email.html',user.email,'ShopnRoar Password Reset Request')
                message = get_template('forgotpassword1.html').render(key)
                email = EmailMessage('BUYnROAR Password Reset Request', message, to=[user.email])
                email.content_subtype = 'html'
                email.send()
                # email = EmailMessage(msg, message, to=['muhammad.zeeshan@brainplow.com',])
                # email.content_subtype = 'html'
                # email.send()
                print('Email Send Successfully')
                reg_obj.SeceretKey = reset_email_token
                reg_obj.ISConfirmed=False
                reg_obj.save()
                print(reset_email_token)
                return Response({'message':'Reset Password mail send Successfully'},status.HTTP_200_OK)
            else:
                return Response({'message':'User Not verify'},status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Email Not Exist'}, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def reset_password_verification(request):
        activition_key = request.data['activation_key']
        if (UserDetails.objects.filter(SeceretKey=activition_key,ISConfirmed=False).exists()):
            return Response({"status": True}, status.HTTP_200_OK)
        else:
            return Response({"status": False}, status.HTTP_400_BAD_REQUEST)
        return Response({"staus": False}, status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def reset_password(request):
        activition_key = request.data['activation_key']
        password= request.data['password']
        if(UserDetails.objects.filter(SeceretKey=activition_key).exists()):
            customer = UserDetails.objects.get(SeceretKey=activition_key)
            if customer.ISConfirmed==False:
                user= User.objects.get(email=customer.user.email)
                user.set_password(password)
                user.save()
                customer.ISConfirmed=True
                customer.save()
                if user.first_name != None and user.first_name != '':
                    username = user.first_name
                else:
                    username = user.username
                key = {
                    'name': username,
                }
                # emailsending.after_response(key, 'Change_Password.html', user.email,
                #                             'OgreSpace Notification - Your password has been changed')
                message = get_template('Change_Password.html').render(key)
                email = EmailMessage('BUYnRoar Password Reset Notification', message, to=[user.email])
                email.content_subtype = 'html'
                email.send()
                return Response({'message':'Password Reset Successfully','status':True},status.HTTP_200_OK)
            else:
                return Response({'message': 'Link Expired', 'status': False}, status.HTTP_400_BAD_REQUEST)
        return Response(False)




