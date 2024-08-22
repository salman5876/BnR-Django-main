from rest_framework import serializers

from .models import userReviews,VendorReviews,VendorReviewsScore



class Review_Serializer(serializers.ModelSerializer):

    class Meta:

        model = userReviews
        fields = ('SNR_Username', 'SNR_ProductID', 'SNR_UPC', 'SNR_Brand','SNR_TitleReview','SNR_StarRating', 'SNR_Review','SNR_Date')

class Vendor_Review_Serializer(serializers.ModelSerializer):

    class Meta:

        model = VendorReviews
        fields = ('SNR_Category', 'SNR_ProductID', 'SNR_UPC', 'SNR_VendorName','SNR_StarRating','SNR_ProductTitle', 'SNR_Review','SNR_Date')



class Vendor_Review_Score_Serializer(serializers.ModelSerializer):
    reviews=Vendor_Review_Serializer()

    class Meta:
        model = VendorReviewsScore
        # fields = ('SNR_ProductID', 'SNR_VendorScoreAll', 'SNR_Date')
        fields = '__all__'
