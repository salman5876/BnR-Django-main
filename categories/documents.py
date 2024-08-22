

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from products.models import AllProducts


@registry.register_document
class AllProductsDocument(Document):
    """
        Document for AllProducts model.
    """
    SNR_SKU = fields.TextField(attr='SNR_SKU')
    SNR_Title = fields.TextField(attr='SNR_Title')
    SNR_ModelNo = fields.TextField(attr='SNR_ModelNo')
    SNR_Brand = fields.TextField(attr='SNR_Brand')
    SNR_UPC = fields.TextField(attr='SNR_UPC')
    SNR_Category = fields.TextField(attr='SNR_Category')
    SNR_SubCategory = fields.TextField(attr='SNR_SubCategory')
    SNR_Condition = fields.TextField(attr='SNR_Condition')
    SNR_PriceBefore = fields.FloatField(attr='SNR_PriceBefore')
    SNR_Price = fields.FloatField(attr='SNR_Price')
    SNR_CustomerReviews = fields.FloatField(attr='SNR_CustomerReviews')
    SNR_Available = fields.TextField(attr='SNR_Available')
    SNR_ProductURL = fields.TextField(attr='SNR_ProductURL')
    SNR_ImageURL = fields.TextField(attr='SNR_ImageURL')
    SNR_Description = fields.TextField(attr='SNR_Description')
    SNR_Description_Mobile = fields.TextField(attr='SNR_Description_Mobile')
    SNR_isShow = fields.BooleanField(attr='SNR_isShow')
    SNR_Review = fields.TextField(attr='SNR_Review')
    SNR_Review_score = fields.FloatField(attr='SNR_Review_score')
    SNR_Date = fields.DateField(attr='SNR_Date')

    class Index:
        name = 'all_products_index'
        # name = 'all_products_demo2'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
            'similarity': {
                'default': {
                    'type': 'BM25'
                }
            }

        }

    # def index./elf.to_dict(include_meta=True)

    class Django:
        model = AllProducts



@registry.register_document
class AllProductsAutoDocument(Document):
    """
        Document for AllProducts model.
    """
    SNR_SKU = fields.TextField(attr='SNR_SKU')
    SNR_Title = fields.TextField(attr='SNR_Title')
    SNR_ModelNo = fields.TextField(attr='SNR_ModelNo')
    SNR_Brand = fields.TextField(attr='SNR_Brand')
    SNR_UPC = fields.TextField(attr='SNR_UPC')
    SNR_Category = fields.TextField(attr='SNR_Category')
    SNR_SubCategory = fields.TextField(attr='SNR_SubCategory')
    SNR_Condition = fields.TextField(attr='SNR_Condition')
    SNR_PriceBefore = fields.FloatField(attr='SNR_PriceBefore')
    SNR_Price = fields.FloatField(attr='SNR_Price')
    SNR_CustomerReviews = fields.FloatField(attr='SNR_CustomerReviews')
    SNR_Available = fields.TextField(attr='SNR_Available')
    SNR_ProductURL = fields.TextField(attr='SNR_ProductURL')
    SNR_ImageURL = fields.TextField(attr='SNR_ImageURL')
    SNR_Description = fields.TextField(attr='SNR_Description')
    SNR_Description_Mobile = fields.TextField(attr='SNR_Description_Mobile')
    SNR_isShow = fields.BooleanField(attr='SNR_isShow')
    SNR_Review = fields.TextField(attr='SNR_Review')
    SNR_Review_score = fields.FloatField(attr='SNR_Review_score')
    SNR_Date = fields.DateField(attr='SNR_Date')

    class Index:
        name = 'all_products_auto_index'

        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
            'similarity': {
                'default': {
                    'type': 'BM25'
                }
            }

        }

    # def index./elf.to_dict(include_meta=True)

    class Django:
        model = AllProducts



# python manage.py search_index --rebuild



