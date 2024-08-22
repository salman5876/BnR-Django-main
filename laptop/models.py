from __future__ import unicode_literals
from time import time


from django.db import models

def get_name(instance,filename):
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)

#(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
# Create your models here.
#
# import django.db.models.options as options
# options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
#     'es_index_name', 'es_type_name', 'es_mapping'
# )

class Laptop_DB(models.Model):

    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True,max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(db_index=True,max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)

    SNR_UPC = models.CharField(db_index=True,max_length=500, default=None, null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2,blank=True)
    SNR_CustomerReviews= models.DecimalField(max_digits=10, decimal_places=2, blank=True , default=00)
    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)


    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else '' + ' , ' + self.SNR_Condition if self.SNR_Condition else '' + ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else '' + ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU','SNR_ProductURL','SNR_ImageURL'),)
