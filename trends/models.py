from django.db import models
from time import time


def get_name(instance,filename):
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)

# Create your models here.
class Trends(models.Model):

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


    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
          return self.SNR_SKU if self.SNR_SKU else ''+' , '+self.SNR_Title if self.SNR_Title else ''+' , '+self.SNR_ModelNo if self.SNR_ModelNo else ''+' , '+self.SNR_Brand if self.SNR_Brand else ''+' , '+self.SNR_UPC if self.SNR_UPC else ''+' , '+str(self.SNR_Price) if str(self.SNR_Price) else ''+' , '+self.SNR_Available if self.SNR_Available else ''+' , '+self.SNR_ProductURL if self.SNR_ProductURL else ''+' , '+self.SNR_ImageURL if self.SNR_ImageURL else ''+' , '+self.SNR_Description if self.SNR_Description else ''+' , '+str(self.SNR_Date)+' , '+self.SNR_CustomerReviews if self.SNR_CustomerReviews else ''


    class Meta:
        unique_together = (('SNR_SKU','SNR_ProductURL','SNR_Price'),)
