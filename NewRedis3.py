import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
import requests
from django.core.cache import cache
from django.db import connection


def new1():
    # Brand Category
    count=0
    catID = [1, 111, 1239, 141, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    # catID=[166]
    # Categories
    try:
        for i in catID:
            try:
                cache.delete('category_brands_cache_for_' + str(i))
                brandpath = 'https://backend.shopnroar.com/products/GetBrandsofCategory/' + str(i)
                date = requests.get(brandpath)
                print(date.status_code)
                print('Done')
                count = count + 1
            except:
                print('something went wrong')
    except:
        pass
    # Sub Category
    try:
        for i in catID:
            try:
                cache.delete('category_subcats_merchants_cache_for_' + str(i))
                Subpath = 'https://backend.shopnroar.com/products/GetSubCategoryofCategory/' + str(i)
                date = requests.get(Subpath)
                print(date.status_code)
                print('Done')
                count = count + 1
            except:
                print('something went wrong')
    except:
        pass
    # Merchant Category
    try:
        for i in catID:
            try:
                cache.delete('category_merchants_cache_for_' + str(i))
                Merchantpath = 'https://backend.shopnroar.com/products/GetMerchantsofCategory/' + str(i)
                date = requests.get(Merchantpath)
                print(date.status_code)
                print('Done')
                count = count + 1
            except:
                print('something went wrong')
    except:
        pass

new1()