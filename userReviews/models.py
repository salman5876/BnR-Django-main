from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userReviews(models.Model):

    SNR_ProductID = models.CharField(max_length=500, default="")

    SNR_Username = models.CharField(max_length=200, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Review = models.CharField(max_length=8000, default=None, null=True)
    SNR_TitleReview = models.CharField(max_length=500, default=None, null=True)
    SNR_StarRating = models.DecimalField(max_digits=10, decimal_places=2, blank=True , default=00)


    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
          return self.SNR_Username if self.SNR_Username else ''+' , '+self.SNR_StarRating if self.SNR_StarRating else ''+' , '+self.SNR_ProductID if self.SNR_ProductID else ''+' , '+' , '+' , '+self.SNR_Brand if self.SNR_Brand else ''+' , '+self.SNR_UPC if self.SNR_UPC else ''+' , '+self.SNR_TitleReview if self.SNR_TitleReview else ''+' , '+self.SNR_Review if self.SNR_Review else ''+' , '+str(self.SNR_Date)


    class Meta:
        unique_together = (('SNR_Username','SNR_TitleReview','SNR_Review','SNR_StarRating','SNR_ProductID'),)

class VendorReviews(models.Model):

    SNR_ProductID = models.CharField(max_length=500, default="")
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Review = models.TextField(default=None, null=True)
    SNR_Category = models.CharField(max_length=200, default=None, null=True)
    SNR_ProductTitle = models.CharField(max_length=1500, default="")
    SNR_VendorName = models.CharField(max_length=200, default=None, null=True)
    SNR_StarRating = models.DecimalField(max_digits=10, decimal_places=2, blank=True , default=00)


    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
          return self.SNR_Category if self.SNR_Category  else ''+' , '+self.SNR_StarRating if self.SNR_StarRating else ''+' , '+self.SNR_ProductID if self.SNR_ProductID else ''+' , '+' , '+' , '+self.SNR_VendorName if self.SNR_VendorName else ''+' , '+self.SNR_UPC if self.SNR_UPC else ''+' , '+self.SNR_Review if self.SNR_Review else ''+' , '+str(self.SNR_Date)


    class Meta:
        unique_together = (('SNR_ProductID','SNR_Review'),)



from jsonfield import JSONField


# from django_upgrade.fixers import jsonfield
class VendorReviewsScore(models.Model):
    reviews = models.ForeignKey(VendorReviews,related_name='reviews', on_delete=models.CASCADE, default="")

    SNR_VendorScoreAll = JSONField(null=True)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    def __VendorReviews__(self):
        return self.reviews
          # return self.SNR_ProductID if self.SNR_ProductID else ''+' , '+self.SNR_VendorScoreAll if self.SNR_VendorScoreAll else ''+' , '+str(self.SNR_Date)






class EmailAlert(models.Model):
    user_id = models.ForeignKey(User,related_name='email_alter_user0',on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    alerty_type = models.CharField(max_length=100)


class VendorNamesandImages(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_image = models.CharField(max_length=100)
    vendor_type = models.CharField(max_length=100)
