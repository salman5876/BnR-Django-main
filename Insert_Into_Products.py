import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import *
from django.db import connection
from django.db import connections


def insert_into_products1():
    a = {
        'SNR_ModelNo': '0001',
        'SNR_Title': 'hamza1',
        'SNR_SKU': 'abc',
        'SNR_PriceBefore': '26',
        'SNR_Price': '16',
        'SNR_CustomerReviews': '4.0',
        'SNR_ProductURL': 'hamza1',
        'SNR_isShow': True,
        'SNR_Brand': 'jhu',
        'SNR_UPC': 'upc',
        'SNR_Category': 'test',
        'SNR_Condition': 'New',
        'SNR_Description_Mobile': 'see site',
        'SNR_Available': 'hamza1',
        'SNR_ImageURL': 'img.png',
        'SNR_Description': 'test'

    }
    try:
        obj = AllProducts(SNR_Title=a['SNR_Title'], SNR_ModelNo=a['SNR_ModelNo'], SNR_SKU=a['SNR_SKU'],
                          SNR_PriceBefore=a['SNR_PriceBefore'],
                          SNR_Price=a['SNR_Price'], SNR_CustomerReviews=a['SNR_CustomerReviews'],
                          SNR_ProductURL=a['SNR_ProductURL'],
                          SNR_isShow=a['SNR_isShow'], SNR_Brand=a['SNR_Brand'], SNR_UPC=a['SNR_UPC'],
                          SNR_Category=a['SNR_Category'],
                          SNR_Condition=a['SNR_Condition'], SNR_Description_Mobile=a['SNR_Description_Mobile'],
                          SNR_Available=a['SNR_Available'],
                          SNR_ImageURL=a['SNR_ImageURL'], SNR_Description=a['SNR_Description'])
        obj.save(using='newdb')
        print('Save')
    except:
        pass
        print('some thing went wrong')


insert_into_products1()