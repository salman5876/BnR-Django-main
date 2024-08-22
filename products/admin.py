from django.contrib import admin

from .models import TV, Cams, CarsElectronics, VideoGames, Toys, SmartHomes, Audio, ComputerSoftware, Applinces, Movies, \
    OfficeSupply, Books, CategoryTable, Main_Categories,merchants,AllProductsCoupons,EbayIndividualURLs,AllProducts ,\
    AllProductsDuplicateData, Vendors_Categories, Categories_Data_Transfer

# Register your models here.

admin.site.register(TV)
admin.site.register(OfficeSupply)
admin.site.register(Movies)
admin.site.register(ComputerSoftware)
admin.site.register(Applinces)
admin.site.register(Audio)
admin.site.register(Cams)
admin.site.register(Books)
admin.site.register(CarsElectronics)
admin.site.register(VideoGames)
admin.site.register(Toys)
admin.site.register(SmartHomes)
admin.site.register(merchants)
admin.site.register(AllProductsCoupons)
admin.site.register(EbayIndividualURLs)
admin.site.register(AllProducts)
admin.site.register(AllProductsDuplicateData)
# admin.site.register(Vendors_Categories)



class VendorsCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id','SNR_CatName', 'SNR_Cat_Image', 'SNR_SubCatName', 'SNR_SubCat_Image')
admin.site.register(Vendors_Categories, VendorsCategoriesAdmin)

class CategoriesDataTransferAdmin(admin.ModelAdmin):
    list_display = ('id','SNR_CatName', 'SNR_CatdataStatus', 'items_count', 'shard_items_count')
admin.site.register(Categories_Data_Transfer, CategoriesDataTransferAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'SNR_Category')
admin.site.register(CategoryTable, BookAdmin)

class Category(admin.ModelAdmin):
    list_display = ('id', 'SNR_CatName')
admin.site.register(Main_Categories, Category)