

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *


# from drf_extra_fields.fields import Base64ImageField



class Product_Reviews_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Product_Reviews
        fields=('Product','SNR_Review_Title','SNR_Review_Author','SNR_Review_Body','SNR_Review_Stars','SNR_Review_UP','SNR_Review_Down','SNR_Date','SNR_IS_SNR')

class Product_Reviews_NoDate_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Product_Reviews
        fields=('Product','SNR_Review_Title','SNR_Review_Author','SNR_Review_Body','SNR_Review_Stars','SNR_Review_UP','SNR_Review_Down','SNR_IS_SNR')


class AllProducts_Serializer(serializers.ModelSerializer):
    class Meta:

        model = AllProducts
        fields=('id','SNR_Title','SNR_Brand','SNR_Description','SNR_Category','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory','SNR_isShow','SNR_PriceBefore','SNR_Condition','SNR_SubCategory','SNR_CatID','SNR_MainCatID', 'SNR_SubCatID','SNR_Description_Mobile')
        encoding = 'utf-8'

class AllProducts_Logos_Serializer(serializers.ModelSerializer):
    image60px = serializers.CharField()
    class Meta:

        model = AllProducts
        fields=('id','SNR_Title', 'image60px','SNR_Brand','SNR_Description','SNR_Category','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory','SNR_isShow','SNR_PriceBefore','SNR_Condition','SNR_SubCategory','SNR_CatID','SNR_MainCatID', 'SNR_SubCatID','SNR_Description_Mobile')
        encoding = 'utf-8'


class Vendors_Categories_Serializer(serializers.ModelSerializer):
    class Meta:

        model = Vendors_Categories
        # fields=('id', 'SNR_CatName', 'SNR_Cat_Image')
        fields=('id', 'SNR_CatName')
        # encoding = 'utf-8'


class AllProductsCateogriesCache_Serializer(serializers.ModelSerializer):

    class Meta:

        model = AllProducts
        fields=('id', 'SNR_Category','SNR_ProductURL')


class AllProductsComplete_Serializer(serializers.ModelSerializer):

    class Meta:

        model = AllProducts
        fields=('id','SNR_Title','SNR_Brand','SNR_Description','SNR_Category','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory','SNR_isShow','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')

class AllProductspartition_Serializer(serializers.ModelSerializer):

    class Meta:

        model = AllProducts
        fields=('id','SNR_Title','SNR_Brand','SNR_Description','SNR_Category','SNR_ImageURL','SNR_ProductURL','SNR_Price','SNR_Available','SNR_CustomerReviews','SNR_PriceBefore','SNR_SubCategory','SNR_isShow','SNR_PriceBefore','SNR_SubCategory')



class CentralTable_Serializer(serializers.ModelSerializer):

    class Meta:

        model = CentralTableProducts
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_Category','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory','SNR_isShow','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')

class AmazonURLs_Serializer(serializers.ModelSerializer):

    class Meta:
        model = AmazonURLs
        fields='__all__'

class AmazonProxies_Serializer(serializers.ModelSerializer):

    class Meta:
        model = AmazonProxies
        fields='__all__'

class ProductReview_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Product_Reviews
        fields=('SNR_Review_Title','SNR_Review_Author', "SNR_Review_Body","SNR_Review_Stars", "SNR_Review_UP","SNR_Review_Down","SNR_IS_SNR")

class DailyDealsSearizlerofSingleProduct(serializers.ModelSerializer):
    class Meta:
        model = Active_DailyDeals
        fields = '__all__'


class ActiveVocationSingleProduct(serializers.ModelSerializer):
    class Meta:
        model = Active_Vocation
        fields = '__all__'

class DailyDeals_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Active_DailyDeals
        fields=('id','SNR_Title','SNR_Category','SNR_ImageURL','SNR_SKU','SNR_ProductURL','SNR_PriceAfter','SNR_PriceBefore','SNR_Available','SNR_Date','SNR_Customer_Rating')


class DailyDealsCategories_Serializer(serializers.ModelSerializer):

    class Meta:

        model = DailyDeals
        fields=('SNR_Category',)



class DailyDealsBrands_Serializer(serializers.ModelSerializer):

    class Meta:

        model = DailyDeals
        fields=('SNR_Available',)



class AllProductsFilterStores_Serializer(serializers.ModelSerializer):

    class Meta:

        model = AllProducts
        fields=('SNR_Available',)


class AllProductsFilterBrands_Serializer(serializers.ModelSerializer):

    class Meta:

        model = AllProducts
        fields=('SNR_Brand',)


class HomeandGarden_Serializer(serializers.ModelSerializer):

    class Meta:

        model = HomeandGarden
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')





class Furniture_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Furniture
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')



class Flowers_Serializer(serializers.ModelSerializer):

    class Meta:

        model = FlowerandPlants
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')



class Clothes_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Clothing
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Jewelry_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Jewelry
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')



class Arts_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Arts
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')






class Software_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = ComputerSoftware
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Health_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = HealthandFitness
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Office_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = OfficeSupply
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Movies_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Movies
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Applinces_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Applinces
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class TV_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = TV
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Cams_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Cams
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class CarsElec_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = CarsElectronics
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class VideoGames_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = VideoGames
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Toys_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Toys
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Smarthomes_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = SmartHomes
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Audio_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Audio
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Coupon_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AllProductsCoupons
        fields = ('SNR_Title', 'SNR_Description', 'SNR_Available','SNR_URl_Code','SNR_CouponCode_url','SNR_Discount','SNR_Expire','SNR_Expire_Status','SNR_Active')


class RecentlyProducts(serializers.ModelSerializer):
    product=AllProductsComplete_Serializer()
    class Meta:
        model = Recently_Items
        fields = ('id','product',)

class merchantslizer(serializers.ModelSerializer):
    class Meta:
        model = merchants
        fields = ('id','name','image20px','image40px','image60px','image80px','image100px',)

class merchantslizer1(serializers.ModelSerializer):
    class Meta:
        model = merchants
        fields = ('id','name','image100px','image60px',)


class Software_Serializer(serializers.ModelSerializer):

    class Meta:

        model = ComputerSoftware
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')



class ElectronicsGadgets_Serializer(serializers.ModelSerializer):

    class Meta:

        model = ElectronicGadgets
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')





class Health_Serializer(serializers.ModelSerializer):

    class Meta:

        model = HealthandFitness
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Office_Serializer(serializers.ModelSerializer):

    class Meta:

        model = OfficeSupply
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')





class Movies_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Movies
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')



class Applinces_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Applinces
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class TV_Serializer(serializers.ModelSerializer):

    class Meta:

        model = TV
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Cams_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Cams
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class CarsElec_Serializer(serializers.ModelSerializer):

    class Meta:

        model = CarsElectronics
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class VideoGames_Serializer(serializers.ModelSerializer):

    class Meta:

        model = VideoGames
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Toys_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Toys
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Smarthomes_Serializer(serializers.ModelSerializer):

    class Meta:

        model = SmartHomes
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Audio_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Audio
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')



class Sports_Serializer(serializers.ModelSerializer):

    class Meta:
        model = SportingGoods
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Books_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Books
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_SubCategory','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available','SNR_Date','SNR_CustomerReviews','SNR_PriceBefore','SNR_Condition','SNR_SubCategory')


class Active_DailyDeals_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Active_DailyDeals
        fields=('SNR_Title','SNR_Category','SNR_ImageURL','SNR_SKU','SNR_ProductURL','SNR_PriceAfter','SNR_PriceBefore','SNR_Available','SNR_Date','SNR_Active','SNR_Customer_Rating','SNR_Description')
class Products_Coupons_Serializer(serializers.ModelSerializer):
    class Meta:
        model=AllProductsCoupons
        fields='__all__'
class Active_Vocation_Serializer(serializers.ModelSerializer):
    SNR_Price = serializers.IntegerField(source='SNR_PriceAfter')
    class Meta:
        model=Active_Vocation
        fields='__all__'

class DailyDeals_check_Serializer(serializers.ModelSerializer):
        SNR_Price = serializers.IntegerField(source='SNR_PriceAfter')
        class Meta:
            model = DailyDeals
            fields = '__all__'
