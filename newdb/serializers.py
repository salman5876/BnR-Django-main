from rest_framework import serializers
from newdb.models import *

class Coupon_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AllProductsCoupons
        fields = ('SNR_Title', 'SNR_Description', 'SNR_Available','SNR_URl_Code','SNR_CouponCode_url','SNR_Discount','SNR_Expire','SNR_Expire_Status','SNR_Active')
