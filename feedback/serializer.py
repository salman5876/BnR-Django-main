from rest_framework import serializers

from .models import Feedback,Wishlist,Blog

from products.models import *

class Feedback_serializer(serializers.ModelSerializer):
    # SNR_Thumbnail = Base64ImageField(required=False,use_url=True)

    class Meta:
        model=Feedback
        fields = ('SNR_FullName', 'SNR_Email', 'SNR_Subject', 'SNR_Feedback','SNR_isRead','SNR_Date')






class Wishlist_serializer(serializers.ModelSerializer):
    class Meta:
        model=Wishlist
        fields = ('id','user', 'SNR_SKU','SNR_Title','SNR_ModelNo', 'SNR_Brand','SNR_UPC', 'SNR_Price','SNR_ProductURL','SNR_Available','SNR_Description','SNR_ImageURL','SNR_CustomerReviews','SNR_item_id')

class Blog_serializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = ('user', 'Blog_Title','Blog_Meta','Blog_Detail', 'Blog_ImagePath','SNR_Date')
