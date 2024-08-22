import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
import requests
from django.core.cache import cache

def redisfunclive():
    count=0
    catID=[1, 111, 1239, 141, 166, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    #Categories
    try:
        for i in catID:
            try:
                cache.delete('categorycache_for_'+str(i)+'1-1-1undefinedundefined-1undefined')
                path='https://backend.shopnroar.com/products/categoryByID1/'+str(i)+'?count=40&low=undefined&high=undefined&brand=undefined&merchant=undefined&sub=undefined&page=1&sort=undefined'
                date = requests.get(path)
                print(date.status_code)
                print('Done')
                count=count+1
            except:
                print('something went wrong')
    except:
        pass
    #Category Home
    try:
        for i in catID:
            try:
                cache.delete('categorycache_for_newfilter' + str(i))
                Homepath='https://backend.shopnroar.com/products/category_Home/'+str(i)
                date = requests.get(Homepath)
                print(date.status_code)
                print('Done')
                count = count + 1
            except:
                print('something went wrong')
    except:
        pass
    #Brand Category
    try:
        for i in catID:
            try:
                cache.delete('category_brands_cache_for_' + str(i))
                brandpath='https://backend.shopnroar.com/products/GetBrandsofCategory/'+str(i)
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
                cache.delete('category_subcats_merchants_cache_for_'+str(i))
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
    #Other
    try:
        cache.delete('GetAllCategoryCache')
        cache.delete('getCategories')
        cache.delete('Merchant_Logos_Home')
        cache.delete('hot_deals_cache_top31')
        li=['https://backend.shopnroar.com/products/todayTop3hotdeals?page=1','https://backend.shopnroar.com/products/GetAllCategories','https://backend.shopnroar.com/products/merchantlogos/']
        for i in li:
            date = requests.get(i)
            print(date.status_code)
            print('Done')
            count = count + 1
    except:
        print('something went wrong')
    print('Total:-',count)
    count = 0
# redisfunclive()

print('-----------------------------------------')


def redisfunclocal():
    count=0
    catID=[1, 111, 1239, 141,166,2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    #Categories
    try:
        for i in catID:
            try:
                # cache.delete('categorycache_for_'+str(i)+'1-1-1undefinedundefined-1undefined')
                path='http://127.0.0.1:8000/products/categoryByID1/'+str(i)+'?count=40&low=undefined&high=undefined&brand=undefined&merchant=undefined&sub=undefined&page=1&sort=undefined'
                date = requests.get(path)
                print(date.status_code)
                print('Done')
                count=count+1
            except:
                print('something went wrong')
    except:
        pass
    #Category Home
    try:
        for i in catID:
            try:
                # cache.delete('categorycache_for_newfilter' + str(i))
                Homepath='http://127.0.0.1:8000/products/category_Home/'+str(i)
                date = requests.get(Homepath)
                print(date.status_code)
                print('Done')
                count = count + 1
            except:
                print('something went wrong')
    except:
        pass
    #Brand Category
    try:
        for i in catID:
            try:
                # cache.delete('category_brands_cache_for_' + str(i))
                brandpath='http://127.0.0.1:8000/products/GetBrandsofCategory/'+str(i)
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
                # cache.delete('category_subcats_merchants_cache_for_'+str(i))
                Subpath = 'http://127.0.0.1:8000/products/GetSubCategoryofCategory/' + str(i)
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
                # cache.delete('category_merchants_cache_for_' + str(i))
                Merchantpath = 'http://127.0.0.1:8000/products/GetMerchantsofCategory/' + str(i)
                date = requests.get(Merchantpath)
                print(date.status_code)
                print('Done')
                count = count + 1
            except:
                print('something went wrong')
    except:
        pass
    #Other
    try:
        # cache.delete('GetAllCategoryCache')
        # cache.delete('getCategories')
        # cache.delete('Merchant_Logos_Home')
        # cache.delete('hot_deals_cache_top31')
        li=['http://127.0.0.1:8000/products/todayTop3hotdeals?page=1','http://127.0.0.1:8000/products/GetAllCategories','http://127.0.0.1:8000/products/merchantlogos/']
        for i in li:
            date = requests.get(i)
            print(date.status_code)
            print('Done')
            count = count + 1
    except:
        print('something went wrong')
    print('Total:-',count)
    count = 0
# redisfunclocal()

print('-----------------------------------------')
