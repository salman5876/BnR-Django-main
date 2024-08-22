pi__author__ = 'Amad'
from rest_framework import serializers

from .models import Wearable_DB

class Wearable_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Wearable_DB
        fields = ('SNR_SKU', 'SNR_Title', 'SNR_ModelNo', 'SNR_Brand', 'SNR_UPC', 'SNR_Price', 'SNR_Available', 'SNR_ProductURL', 'SNR_ImageURL', 'SNR_Description','SNR_Date','SNR_CustomerReviews')







class Wearable_SerializerTitle(serializers.ModelSerializer):

    class Meta:
        model = Wearable_DB
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')
