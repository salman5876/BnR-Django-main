from django.db import models

# Create your models here.


class AllProductsPartition(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Category = models.CharField(max_length=100, default=None, null=True)
    SNR_CatID = models.IntegerField(default=0, null=True)
    SNR_SubCatID = models.IntegerField(default=0, null=True)
    SNR_MainCatID = models.IntegerField(default=0, null=True)
    SNR_SubCategory = models.CharField(max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_Description_Mobile = models.TextField(default=None, null=True, blank=True)
    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=10000, default=None, null=True)
    SNR_Description = models.TextField(default=None, null=True)
    SNR_isShow = models.BooleanField(default=True)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)
    SNR_Review = models.TextField(default='', null=True, blank=True)
    SNR_Review_score = models.CharField(max_length=1000, default='', null=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''
    def indexing(self):
        print ('indexing...')
        from products.search import SNRIndex
        print (self.SNR_SKU)
        obj = SNRIndex(
            SNR_SKU=self.SNR_SKU,
            SNR_Title=self.SNR_Title,
            SNR_ModelNo=self.SNR_ModelNo,
            SNR_Brand=self.SNR_Brand,
            SNR_UPC=self.SNR_UPC,
            SNR_Category=self.SNR_Category,
            SNR_Price=self.SNR_Price,
            SNR_CustomerReviews=self.SNR_CustomerReviews,
            SNR_Available=self.SNR_Available,
            SNR_ProductURL=self.SNR_ProductURL,
            SNR_ImageURL=self.SNR_ImageURL,
            SNR_Description=self.SNR_Description,
            SNR_isShow=self.SNR_isShow,

            SNR_Date=self.SNR_Date

        )
        obj.save(index='snr-index')
        print ('indexed...')
        return obj.to_dict(include_meta=True)
    class Meta:
        unique_together = (('SNR_Title', 'SNR_Available','id','SNR_ProductURL'),)


class merchants(models.Model):
    name = models.CharField(max_length=255, null=True)
    image20px=models.CharField(max_length=255, null=True)
    image40px = models.CharField(max_length=255, null=True)
    image60px = models.CharField(max_length=255, null=True)
    image80px = models.CharField(max_length=255, null=True)
    image100px = models.CharField(max_length=255, null=True)
    prefer=models.IntegerField(default=100,blank=True,null=True)
    active=models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return self.name


class merchantscoupons(models.Model):
    name = models.CharField(max_length=255, null=True)
    image20px=models.CharField(max_length=255, null=True)
    image40px = models.CharField(max_length=255, null=True)
    image60px = models.CharField(max_length=255, null=True)
    image80px = models.CharField(max_length=255, null=True)
    image100px = models.CharField(max_length=255, null=True)
    prefer=models.IntegerField(default=100,blank=True,null=True)
    count=models.CharField(max_length=255, null=True)
    active=models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return self.name


class DailyDeals(models.Model):
    SNR_SKU = models.CharField(db_index=True, max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=None, null=True)
    SNR_Category = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_PriceAfter = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Active = models.BooleanField(default=True)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + str(
            self.SNR_PriceAfter) if str(
            self.SNR_PriceAfter) else '' + ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + str(
            self.SNR_PriceBefore) if str(
            self.SNR_PriceBefore) else ''

    # class Meta:
    #     unique_together = (('SNR_Title', 'SNR_Available','SNR_PriceAfter'),)


class Active_DailyDeals(models.Model):
    SNR_SKU = models.CharField(db_index=True, max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=None, null=True)
    SNR_Category = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_PriceAfter = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    # SNR_Active = models.NullBooleanField(default=True)
    SNR_Active = models.BooleanField(default=True)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + str(
            self.SNR_PriceAfter) if str(
            self.SNR_PriceAfter) else '' + ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + str(
            self.SNR_PriceBefore) if str(
            self.SNR_PriceBefore) else ''


class AllProductsCoupons(models.Model):

    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_Description = models.TextField(default=None, null=True)
    SNR_Available = models.CharField(max_length=200, default=None, null=True)
    SNR_URl_Code=models.BooleanField(default=False)#false URL #true COde
    SNR_CouponCode_url = models.CharField(max_length=500, default=None, null=True)
    SNR_Discount = models.CharField(max_length=100, default=None, null=True)
    SNR_Expire=models.DateField(default='',blank=True,null=True)
    SNR_Expire_Status=models.BooleanField(default=False)
    # SNR_Active = models.NullBooleanField(default=False)
    SNR_Active = models.BooleanField(default=False)
    site=models.CharField(max_length=200, default=None, null=True,blank=True)
    Manual=models.BooleanField(default=False)
    # Manual=models.NullBooleanField(default=False)
    # SNR_Search = tsvector_field.SearchVectorField([
    #     tsvector_field.WeightedColumn('SNR_Title', 'A'),
    #     tsvector_field.WeightedColumn('SNR_Description', 'B'),
    # ], 'english')
    class Meta:
        unique_together = (('SNR_CouponCode_url'),)

class AllProductsCoupons_backup(models.Model):
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_Description = models.TextField(default=None, null=True)
    SNR_Available = models.CharField(max_length=200, default=None, null=True)
    SNR_URl_Code=models.BooleanField(default=False)#false URL #true COde
    SNR_CouponCode_url = models.CharField(max_length=500, default=None, null=True)
    SNR_Discount = models.CharField(max_length=100, default=None, null=True)
    SNR_Expire=models.DateField(default='',blank=True,null=True)
    SNR_Expire_Status=models.BooleanField(default=False)
    # SNR_Active = models.NullBooleanField(default=False)
    SNR_Active = models.BooleanField(default=False)
    site = models.CharField(max_length=200, default=None, null=True,blank=True)
    Manual = models.BooleanField(default=False)
    # Manual = models.NullBooleanField(default=False)
    class Meta:
        unique_together = (('SNR_CouponCode_url'),)

class AllProducts(models.Model):
    SNR_SKU = models.CharField(db_index=True, max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=None, null=True)
    SNR_Category = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_CatID = models.IntegerField(default=0, null=True)
    SNR_SubCatID = models.IntegerField(default=0, null=True)
    SNR_MainCatID = models.IntegerField(default=0, null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00,db_index=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True,db_index=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=10000, default=None, null=True)
    SNR_Description = models.TextField(default=None, null=True)
    SNR_Description_Mobile = models.TextField(max_length=50000, default=None, null=True,blank=True)
    SNR_isShow = models.BooleanField(db_index=True, default=True)
    SNR_Review = models.TextField(default='', null=True,blank=True)
    SNR_Review_score = models.CharField(max_length=1000, default='', null=True, blank=True)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True,db_index=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    def indexing(self):
        print ('indexing...')
        from products.search import SNRIndex
        print (self.SNR_SKU)
        obj = SNRIndex(
            SNR_SKU=self.SNR_SKU,
            SNR_Title=self.SNR_Title,
            SNR_ModelNo=self.SNR_ModelNo,
            SNR_Brand=self.SNR_Brand,
            SNR_UPC=self.SNR_UPC,
            SNR_Category=self.SNR_Category,
            SNR_Price=self.SNR_Price,
            SNR_CustomerReviews=self.SNR_CustomerReviews,
            SNR_Available=self.SNR_Available,
            SNR_ProductURL=self.SNR_ProductURL,
            SNR_ImageURL=self.SNR_ImageURL,
            SNR_Description=self.SNR_Description,
            SNR_isShow=self.SNR_isShow,

            SNR_Date=self.SNR_Date

        )
        obj.save(index='snr-index')
        print ('indexed...')
        return obj.to_dict(include_meta=True)

    class Meta:
        unique_together = (('SNR_Title','SNR_Available','SNR_ProductURL'),)


class EbayIndividualURLs(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="",unique=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    Cat = models.CharField(max_length=200, default='')
    SubCat = models.CharField(max_length=200, default='')
    SubSubCat = models.CharField(max_length=200, default='')
    SubSubSubCat = models.CharField(max_length=200, default='')
    soup = models.TextField(null=True, blank=True)
    status_scrape = models.BooleanField(default=False)
    status_error = models.BooleanField(default=False)
    class Meta:
        unique_together = (('SNR_Title', 'SNR_SKU'),)