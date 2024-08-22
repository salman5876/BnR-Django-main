__author__ = 'Amad'

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetails,sendFriends, Subscribers,Reset_password


class SubscriberSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Subscribers
        fields = ('email','isSend','SNR_Date')


class UserSerializerforPassword(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',  'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username',  'password','email')

class UserSerializerwithoutPassword(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','email')


class friendEmailSerilizer(serializers.ModelSerializer):

    class Meta:
        model = sendFriends
        fields =('email','sharedlink')

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email', 'password')


class UserLoginIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username')


class ResetPasswordSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Reset_password
        fields = ('email','link','isValid','Code','SNR_Date')

class UserDetailsSerializer(serializers.Serializer):
    class Meta:
        model = UserDetails
        fields = ('user', 'Mobile', 'newsLetter', 'email', 'isAuthenticated','SeceretKey')