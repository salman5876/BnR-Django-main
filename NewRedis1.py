import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
import requests
from django.core.cache import cache
from django.db import connection

def Home():
    try:
        cache.delete('GetAllCategoryCache')
        cache.delete('getCategories')
        cache.delete('Merchant_Logos_Home')
        cache.delete('hot_deals_cache_top31')
        li = ['https://backend.shopnroar.com/products/todayTop3hotdeals?page=1',
              'https://backend.shopnroar.com/products/GetAllCategories',
              'https://backend.shopnroar.com/products/merchantlogos/']
        for i in li:
            date = requests.get(i)
            print(date.status_code)
            print('Done')
            count = count + 1
    except:
        print('something went wrong')

Home()