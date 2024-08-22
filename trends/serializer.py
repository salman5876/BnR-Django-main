__author__ = 'Amad'
from rest_framework import serializers

from .models import Trends

class TrendsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Trends
        fields = ('SNR_SKU', 'SNR_Title', 'SNR_ModelNo', 'SNR_Brand', 'SNR_UPC', 'SNR_Price', 'SNR_Available', 'SNR_ProductURL', 'SNR_ImageURL', 'SNR_Description','SNR_Date','SNR_CustomerReviews')


