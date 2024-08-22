from __future__ import unicode_literals

import django.db.models
from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.indexes import GinIndex
# Create your models here.
from products.sharding_old import ShardedByCategoryModel


class Sub_CategoriesStatus(models.Model):
    SNR_URL = models.CharField(db_index=True, max_length=500, default="", unique=True)
    SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
    SNR_ScrapeStatus = models.BooleanField(default=False)
    SNR_Category = models.CharField(db_index=True, max_length=200, default=None, null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=200, default=None, null=True)
    SNR_ErrorStatus = models.BooleanField(default=False)
    SNR_Error = models.CharField(db_index=True, max_length=1000, default=None, null=True)
    SNR_TotalRecords = models.IntegerField(default=0)
    SNR_CurrentRecords = models.IntegerField(default=0)
    SNR_PageNo = models.IntegerField(default=0)
    SNR_CompleteStatus = models.BooleanField(default=False)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True, db_index=True)




class CentralTableProducts(models.Model):
    SNR_SKU = models.CharField(db_index=True, max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=None, null=True)
    SNR_Category = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)
    SNR_isShow = models.BooleanField(db_index=True, default=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''


    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


# Create your models here.
class CategoryMapping(models.Model):
    Cat_ID = models.IntegerField(null=True)
    MainCat_ID = models.IntegerField(null=True)
    SubCat_ID = models.IntegerField(null=True)
    TriCat_ID = models.IntegerField(null=True)
    TetCat_ID = models.IntegerField(null=True)
    PentCat_ID = models.IntegerField(null=True)
    HexCat_ID = models.IntegerField(null=True)
    HeptCat_ID = models.IntegerField(null=True)
    SNR_SourceCatName = models.CharField(max_length=255, default=None, null=True)
    SNR_SourceSubCatName = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return str(self.Cat_ID)


class Main_Categories(models.Model):
    Cat_ID = models.IntegerField(unique=True)
    SNR_CatName = models.CharField(max_length=255, default=None, null=True)
    SNR_Cat_Image=models.CharField(max_length=255, default=None, null=True)
    SNR_SubCatName = models.CharField(max_length=255,default=None, null=True)
    SNR_TriCatName = models.CharField(max_length=255,default=None, null=True)
    SNR_TetCatName = models.CharField(max_length=255,default=None, null=True)
    SNR_PentCatName = models.CharField(max_length=255,default=None, null=True)
    SNR_HexCatName = models.CharField(max_length=255,default=None, null=True)
    SNR_HeptCatName = models.CharField(max_length=255,default=None, null=True)
    

    def __str__(self):
        return str(self.Cat_ID)


class Vendors_Categories(models.Model):
    SNR_CatName = models.CharField(max_length=255, default=None, null=True)
    SNR_Cat_Image = models.CharField(max_length=255, default=None, null=True)
    items_count = models.IntegerField(default=None)
    SNR_SubCatName = models.CharField(max_length=255, default=None, null=True)
    SNR_SubCat_Image = models.CharField(max_length=255, default=None, null=True)
    SNR_TriCatName = models.CharField(max_length=255, default=None, null=True)
    SNR_TetCatName = models.CharField(max_length=255, default=None, null=True)
    SNR_PentCatName = models.CharField(max_length=255, default=None, null=True)
    SNR_HexCatName = models.CharField(max_length=255, default=None, null=True)
    SNR_HeptCatName = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return str(self.id) if str(self.id) else '' + ' , ' + self.SNR_CatName if self.SNR_CatName else ''

    # class Meta:
    #     using = 'newdb'

class Categories_Data_Transfer(models.Model):
    SNR_CatName = models.CharField(max_length=255, default=None, null=True)
    SNR_CatdataStatus = models.BooleanField(default=False)
    items_count = models.IntegerField(default=None, blank=True)
    shard_items_count = models.IntegerField(default=None, blank=True)


    def __str__(self):
        return str(self.id) if str(self.id) else '' + ' , ' + self.SNR_CatName if self.SNR_CatName else '' + ' , ' + \
        self.SNR_CatdataStatus if self.SNR_CatdataStatus else ''  + ' , ' + \
        str(self.items_count) if str(self.items_count) else ''+ ' , ' + self.shard_items_count if self.shard_items_count else ''

    # class Meta:
    #     using = 'newdb'


# class Category_Mapping(models.Model):
#     Cat_ID = models.IntegerField(unique=True, default=0)
#     SNR_SourceCatName = models.CharField(max_length=255, default=None, null=True)
#
#     def __str__(self):
#         return str(self.Cat_ID)



class CategoryTable(models.Model):
    SNR_Category = models.CharField(db_index=True, max_length=100, default=None, null=True,unique=True)

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
        return str(self.id) if str(self.id) else '' + ' , ' +self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
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

class AllProductsDuplicateData(models.Model):
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
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00, db_index=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, db_index=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="", unique=True)
    SNR_ImageURL = models.CharField(max_length=10000, default=None, null=True)
    SNR_Description = models.TextField(default=None, null=True)
    SNR_Description_Mobile = models.TextField(max_length=50000, default=None, null=True, blank=True)
    SNR_isShow = models.BooleanField(db_index=True, default=True)
    SNR_Review = models.TextField(default='', null=True, blank=True)
    SNR_Review_score = models.CharField(max_length=1000, default='', null=True, blank=True)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True, db_index=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else '' + ' , ' + self.SNR_Condition if self.SNR_Condition else '' + ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else '' + ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    def indexing(self):
        print('indexing...')
        from products.search import SNRIndex
        print(self.SNR_SKU)
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
        print('indexed...')
        return obj.to_dict(include_meta=True)

    class Meta:
        unique_together = (('SNR_Title', 'SNR_Available', 'SNR_ProductURL'),)

# class AllProducts(ShardedByCategoryModel):
#     SNR_SKU = models.CharField(db_index=True, max_length=500, default="")
#     SNR_Title = models.CharField(db_index=True, max_length=1000, default=None, null=True)
#     SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
#     SNR_Brand = models.CharField(max_length=200, default=None, null=True)
#     SNR_UPC = models.CharField(db_index=True, max_length=500, default=None, null=True)
#     SNR_Category = models.CharField(db_index=True, max_length=100, default=None, null=True)
#     SNR_CatID = models.IntegerField(default=0, null=True)
#     SNR_SubCatID = models.IntegerField(default=0, null=True)
#     SNR_MainCatID = models.IntegerField(default=0, null=True)
#     SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
#     SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
#     SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00,db_index=True)
#     SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True,db_index=True)
#     SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
#
#     SNR_Available = models.CharField(db_index=True, max_length=50, default=None, null=True)
#     SNR_ProductURL = models.CharField(max_length=2000, default="")
#     SNR_ImageURL = models.CharField(max_length=10000, default=None, null=True)
#     SNR_Description = models.TextField(default=None, null=True)
#     SNR_Description_Mobile = models.TextField(max_length=50000, default=None, null=True,blank=True)
#     SNR_isShow = models.BooleanField(db_index=True, default=True)
#     SNR_Review = models.TextField(default='', null=True,blank=True)
#     SNR_Review_score = models.CharField(max_length=1000, default='', null=True, blank=True)
#     SNR_Date = models.DateTimeField(auto_now_add=True, blank=True,db_index=True)
#
#     def __str__(self):
#         return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
#             self.SNR_Price) if str(
#             self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
#             self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''
#
#     def indexing(self):
#         print ('indexing...')
#         from products.search import SNRIndex
#         print (self.SNR_SKU)
#         obj = SNRIndex(
#             SNR_SKU=self.SNR_SKU,
#             SNR_Title=self.SNR_Title,
#             SNR_ModelNo=self.SNR_ModelNo,
#             SNR_Brand=self.SNR_Brand,
#             SNR_UPC=self.SNR_UPC,
#             SNR_Category=self.SNR_Category,
#             SNR_Price=self.SNR_Price,
#             SNR_CustomerReviews=self.SNR_CustomerReviews,
#             SNR_Available=self.SNR_Available,
#             SNR_ProductURL=self.SNR_ProductURL,
#             SNR_ImageURL=self.SNR_ImageURL,
#             SNR_Description=self.SNR_Description,
#             SNR_isShow=self.SNR_isShow,
#
#             SNR_Date=self.SNR_Date
#
#         )
#         obj.save(index='snr-index')
#         print ('indexed...')
#         return obj.to_dict(include_meta=True)
#
#     class Meta:
#         unique_together = (('SNR_Title','SNR_Available','SNR_ProductURL'),)

class AmazonURLs(models.Model):
    Cat = models.CharField(max_length=200)
    SubCat = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)
    status_scrape = models.BooleanField(default=False)
    status_range = models.BooleanField(default=False)

class EbayURLs(models.Model):
    Cat = models.CharField(max_length=200)
    SubCat = models.CharField(max_length=200)
    SubSubCat = models.CharField(max_length=200)
    SubSubSubCat = models.CharField(max_length=200,default='')
    url = models.CharField(max_length=2000)
    count = models.IntegerField(default=0)
    count_str = models.CharField(max_length=500,default='')
    status_scrape = models.BooleanField(default=False)
    status_range = models.BooleanField(default=False)


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

class AmazonProxies(models.Model):
    proxy = models.CharField(max_length=200, unique= True)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class AllProductsData(models.Model):
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
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)
    SNR_isShow = models.BooleanField(db_index=True, default=True)

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
        unique_together = (('SNR_Title', 'SNR_Available'),)

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
    # Manual=models.NullBooleanField(default=False)
    Manual=models.BooleanField(default=False)
    # SNR_Search1 = tsvector_field.SearchVectorField([
    #     tsvector_field.WeightedColumn('SNR_Title', 'A'),
    #     tsvector_field.WeightedColumn('SNR_Description', 'B'),
    # ], 'english')


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
    # Manual = models.NullBooleanField(default=False)
    Manual = models.BooleanField(default=False)


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


class Product_Review_AI(models.Model):

    Product = models.OneToOneField(AllProducts, on_delete=models.CASCADE)
    # SNR_Review_Info = JSONField()
    SNR_Review_Info = models.JSONField()

    class Meta:
        indexes = [
            GinIndex(
                fields=['SNR_Review_Info'],
                name='SNR_Review_Info_gin',
            ),
        ]

    def __str__(self):
          return str(self.Product) + "Review_AI Data"


class Product_Reviews(models.Model):

    Product = models.ForeignKey(AllProducts, on_delete=models.CASCADE, default='0')


    SNR_Review_Title = models.CharField(max_length=500, default="")
    SNR_Review_Author = models.CharField(max_length=500, default="")
    SNR_Review_Body = models.TextField(default="")
    SNR_Review_Stars = models.FloatField(blank=True , default=0)
    SNR_Review_UP = models.IntegerField(blank=True , default=0)
    SNR_Review_Down = models.IntegerField(blank=True , default=0)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)
    SNR_IS_SNR = models.BooleanField(default=False)


    def __str__(self):
          return str(self.Product) +self.SNR_Review_Title if self.SNR_Review_Title else ''+' , '+self.SNR_Review_Author if self.SNR_Review_Author else ''+' , '+self.SNR_Review_Body if self.SNR_Review_Body else ''+' , '+self.SNR_Review_UP if self.SNR_Review_UP else ''+' , '+self.SNR_Review_Down if self.SNR_Review_Down else ''+' , '+str(self.SNR_Date)+str(self.SNR_isRead)

    class Meta:
        unique_together = (('Product','SNR_Review_Title','SNR_Review_Author','SNR_Review_Body'),)


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
    SNR_Description = models.TextField(default=None, null=True, blank=True)
    SNR_Customer_Rating=models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_CategoryURL = models.CharField(max_length=2000, default="")
    SNR_PageURL = models.CharField(max_length=2000, default="")

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
    SNR_Active = models.BooleanField(default=True)
    # SNR_Active = models.BooleanField(default=True)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)
    SNR_Description = models.TextField(default=None, null=True, blank=True)
    SNR_Customer_Rating = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_CategoryURL = models.CharField(max_length=2000, default="")
    SNR_PageURL = models.CharField(max_length=2000, default="")
    SNR_CategoryScrapeStatus = models.BooleanField(default=False)
    SNR_PageScrapeStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + str(
            self.SNR_PriceAfter) if str(
            self.SNR_PriceAfter) else '' + ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + str(
            self.SNR_PriceBefore) if str(
            self.SNR_PriceBefore) else ''


    # class Meta:
    #     unique_together = (('SNR_Title', 'SNR_Available','SNR_PriceAfter'),)

# Create your models here.
class TV(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_ImageURL'),)


class ElectronicGadgets(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_ImageURL'),)


class Cams(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_ImageURL', 'SNR_ModelNo', 'SNR_Title', 'SNR_Price'),)


class CarsElectronics(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class VideoGames(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class Toys(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ModelNo', 'SNR_ImageURL', 'SNR_ProductURL'),)


class SmartHomes(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL'),)


class Audio(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL'),)


class ComputerSoftware(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(max_length=1000, default=None, null=True)
    SNR_ModelNo = models.CharField(max_length=500, default=None, null=True)
    SNR_Brand = models.CharField(max_length=200, default=None, null=True)
    SNR_UPC = models.CharField(max_length=500, default=None, null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=None, null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default="")
    SNR_ImageURL = models.CharField(max_length=2000, default=None, null=True)
    SNR_Description = models.CharField(max_length=8000, default=None, null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL'),)


class Applinces(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class Movies(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class Books(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class Furniture(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class FlowerandPlants(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class Clothing(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class Arts(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class Jewelry(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class HomeandGarden(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class SportingGoods(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_SubCategory = models.CharField(max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


class OfficeSupply(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)


import django.db.models.options as options

options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping'
)


class HealthandFitness(models.Model):
    SNR_SKU = models.CharField(max_length=500, default="")
    SNR_Title = models.CharField(db_index=True, max_length=1000, default=" ", null=True)
    SNR_ModelNo = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Brand = models.CharField(max_length=200, default=" ", null=True)
    SNR_UPC = models.CharField(db_index=True, max_length=500, default=" ", null=True)
    SNR_Price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_CustomerReviews = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    SNR_Available = models.CharField(max_length=50, default=" ", null=True)
    SNR_ProductURL = models.CharField(max_length=2000, default=" ")
    SNR_ImageURL = models.CharField(max_length=2000, default=" ", null=True)
    SNR_Description = models.CharField(max_length=8000, default=" ", null=True)
    SNR_SubCategory = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_Condition = models.CharField(db_index=True, max_length=100, default=None, null=True)
    SNR_PriceBefore = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=00)
    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_ModelNo if self.SNR_ModelNo else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + self.SNR_Brand if self.SNR_Brand else '' + ' , ' + self.SNR_UPC if self.SNR_UPC else '' + ' , ' + str(
            self.SNR_Price) if str(
            self.SNR_Price) else ''+ ' , ' + self.SNR_Condition if self.SNR_Condition else ''+ ' , ' + self.SNR_SubCategory if self.SNR_SubCategory else '' + ' , ' + self.SNR_PriceBefore if self.SNR_PriceBefore else ''+ ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + self.SNR_Description if self.SNR_Description else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + self.SNR_CustomerReviews if self.SNR_CustomerReviews else '' + ' , ' + self.SNR_isShow if self.SNR_isShow else ''

    class Meta:
        unique_together = (('SNR_SKU', 'SNR_ProductURL', 'SNR_Price'),)



class Recently_Items(models.Model):
    product = models.ForeignKey(AllProducts,on_delete=models.CASCADE, null=True, blank=True, default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE, default='', null=True, blank=True)
    Cat_Name = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.product.SNR_Title


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

class EbayUrlsBasedOnOnlyPrice(models.Model):
    parent = models.CharField(max_length=2000)
    total = models.IntegerField(default=0)
    until_sum = models.IntegerField(default=0)
    url = models.CharField(max_length=2000, unique=True)
    price_start = models.FloatField(blank=True, default=0)
    price_end = models.FloatField(blank=True, default=0)
    count = models.IntegerField(default=0)
    count_str = models.CharField(max_length=500,default='')
    status_scrape = models.BooleanField(default=False)
    script_run = models.BooleanField(default=False)
    totalpage = models.CharField(max_length=500, default='')
    error = models.CharField(max_length=500, default='')
    soup = models.TextField(null=True, blank=True)
    status_latest = models.BooleanField(default=False)


class Vocation_backup(models.Model):
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
    SNR_Description = models.TextField(default=None, null=True, blank=True)
    SNR_Customer_Rating=models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + str(
            self.SNR_PriceAfter) if str(
            self.SNR_PriceAfter) else '' + ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + str(
            self.SNR_PriceBefore) if str(
            self.SNR_PriceBefore) else ''

    # class Meta:
    #     unique_together = (('SNR_Title', 'SNR_Available','SNR_PriceAfter'),)


class Active_Vocation(models.Model):
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
    SNR_Description = models.TextField(default=None, null=True, blank=True)
    SNR_Customer_Rating = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=00)

    def __str__(self):
        return self.SNR_SKU if self.SNR_SKU else '' + ' , ' + self.SNR_Title if self.SNR_Title else '' + ' , ' + self.SNR_Category if self.SNR_Category else '' + ' , ' + str(
            self.SNR_PriceAfter) if str(
            self.SNR_PriceAfter) else '' + ' , ' + self.SNR_Available if self.SNR_Available else '' + ' , ' + self.SNR_ProductURL if self.SNR_ProductURL else '' + ' , ' + self.SNR_ImageURL if self.SNR_ImageURL else '' + ' , ' + str(
            self.SNR_Date) + ' , ' + str(
            self.SNR_PriceBefore) if str(
            self.SNR_PriceBefore) else ''
