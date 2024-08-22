from django.contrib import admin
from categories.models import CategoriesBrandNames


class CategoriesBrandNamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name','products_count', )

admin.site.register(CategoriesBrandNames, CategoriesBrandNamesAdmin)







# from categories.models import (
#     AllProductsShard0,
#
# )
#
# # Register your models here.
# admin.site.register(AllProductsShard1)
#
# class AllProductsShard0Admin(admin.ModelAdmin):
#     list_display = ('id', 'SNR_Title','SNR_isShow', 'SNR_Category', 'SNR_SubCategory',
#                     'SNR_Condition','SNR_PriceBefore', 'SNR_Price', 'SNR_CustomerReviews', 'SNR_Available',
#                     'SNR_ProductURL', 'SNR_ImageURL', 'SNR_Date',
#                     )
# admin.site.register(AllProductsShard0, AllProductsShard0Admin)