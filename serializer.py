from products.models import *
from rest_framework import serializers

class Active_DailyDeals_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Active_DailyDeals
        fields=('SNR_Title','SNR_Category','SNR_ImageURL','SNR_SKU','SNR_ProductURL','SNR_PriceAfter','SNR_PriceBefore','SNR_Available','SNR_Date','SNR_Active')