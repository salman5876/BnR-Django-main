import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
import requests
from django.core.cache import cache
from django.db import connection


def newfilter():
    catID = [1, 111, 1239, 141, 2092, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988,222,166]
    # catID=[166]
    # Categories
    for i in catID:
        cache.delete('categorycache_for_newfilter_backup' + str(i))
        cache_key = 'categorycache_for_newfilter_backup' + str(i)
        cache_time = 36000
        temp=[]
        ls = ' where "SNR_isShow" = TRUE'
        main_data_query = 'Select {0} from public.products_allproducts_' + str(
            i) + ' {1} order by random()  LIMIT 20'
        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_ModelNo", "SNR_Brand",
            "SNR_UPC", "SNR_Available",
            "SNR_ProductURL", "SNR_ImageURL", "id",
            "SNR_Description", "SNR_isShow",
            "SNR_Date", "SNR_Category",
            "SNR_Condition", "SNR_PriceBefore",
            "SNR_CustomerReviews", "SNR_Price",
            "SNR_SubCategory"

        ]
        out = ['"{0}"'.format(i) for i in fields]
        data_query = main_data_query.format(",".join(out), ls)
        print("main query", data_query)
        f_count = len(fields)
        with connection.cursor() as cursor:
            cursor.execute(data_query)
            for i in cursor.fetchall():
                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]
                temp.append(current_item)
        res = {
            'results': temp,
        }
        cache.set(cache_key, res, cache_time)
        print('done')

newfilter()