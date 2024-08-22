from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.db import models

class Feedback(models.Model):

    SNR_FullName = models.CharField(max_length=100, default=" ", null=True)
    SNR_Email = models.CharField(max_length=100, default=" ", null=True)
    SNR_Subject = models.CharField(max_length=100, default= " ", null=True)

    SNR_Feedback = models.CharField(max_length=1000, default=" ", null=True)
    SNR_isRead = models.BooleanField( default=False )

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
          return self.SNR_FullName if self.SNR_FullName else ''+' , '+self.SNR_Email if self.SNR_Email else ''+' , '+self.SNR_Subject if self.SNR_Subject else ''+' , '+self.SNR_Feedback if self.SNR_Feedback else ''+' , '+str(self.SNR_Date)+str(self.SNR_isRead)

class Wishlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')

    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True,max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True,max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True,max_length=500, default= " ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True , default=00)
    SNR_CustomerReviews= models.DecimalField(max_digits=10, decimal_places=2, blank=True , default=00)

    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_isShow = models.BooleanField( default=True )
    SNR_item_id = models.CharField(null=True,blank=True,default=None,max_length=200)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
          return str(self.user) +self.SNR_Title if self.SNR_Title else ''+' , '+self.SNR_ProductURL if self.SNR_ProductURL else ''+' , '+self.SNR_Price if self.SNR_Price else ''+' , '+str(self.SNR_Date)+str(self.SNR_isRead)

    class Meta:
        unique_together = (('SNR_SKU','SNR_ProductURL','SNR_ImageURL','SNR_Date'),)

# class Wishlist_vendors(models.Model):
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')
#
#     SNR_SKU = models.CharField(db_index=True, max_length=500, default="")
#     SNR_Title = models.CharField(db_index=True, max_length=1000, default=None, null=True)
#     SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
#     SNR_Brand = models.CharField(max_length=200, default=None, null=True)
#     SNR_UPC = models.CharField(db_index=True, max_length=500, default=None, null=True)
#     SNR_Category = models.CharField(db_index=True, max_length=100, default=None, null=True)
#     SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
#     SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00, db_index=True)
#     SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, db_index=True)
#     SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
#
#     SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
#     SNR_ProductURL = models.CharField(max_length=2000, default="")
#     SNR_ImageURL = models.CharField(max_length=10000, default=None, null=True)
#     SNR_Description = models.TextField(default=None, null=True)
#     SNR_Description_Mobile = models.TextField(max_length=50000, default=None, null=True, blank=True)
#
#     SNR_isShow = models.BooleanField(db_index=True, default=True)
#     SNR_item_id = models.CharField(null=True, blank=True, default=None, max_length=200)
#     SNR_Date = models.DateTimeField(auto_now_add=True, blank=True, db_index=True)
#
#
#     def __str__(self):
#           return str(self.user) +self.SNR_Title if self.SNR_Title else ''+' , '+self.SNR_ProductURL if self.SNR_ProductURL else ''+' , '+self.SNR_Price if self.SNR_Price else ''+' , '+str(self.SNR_Date)+str(self.SNR_isRead)
#
#     class Meta:
#         unique_together = (('SNR_SKU','SNR_ProductURL','SNR_ImageURL','SNR_Date'),)

class Blog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')

    Blog_Title = models.CharField(db_index=True,max_length=200, default=" ", null=True)
    Blog_Meta = models.CharField(db_index=True,max_length=200, default=" ", null=True)
    Blog_Detail=  models.CharField(db_index=True,max_length=5000, default=" ", null=True)
    Blog_ImagePath=  models.CharField(db_index=True,max_length=200, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
          return str(self.user) +self.Blog_Title if self.Blog_Title else ''+' , '+self.Blog_Meta if self.Blog_Meta else ''+' , '+self.Blog_Detail if self.Blog_Detail else ''+' , '+self.Blog_ImagePath if self.Blog_ImagePath else ''+' , '+str(self.SNR_Date)+str(self.SNR_isRead)
