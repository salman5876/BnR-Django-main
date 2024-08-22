from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Laptop_DB
# from drf_extra_fields.fields import Base64ImageField
from drf_extra_fields.fields import Base64ImageField

class Laptop_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Laptop_DB
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews')


class Laptop_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Laptop_DB
        fields = ('SNR_Title','SNR_UPC','SNR_ModelNo')


