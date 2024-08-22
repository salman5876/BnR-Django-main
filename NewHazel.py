import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
# import requests
from django.db import connection
from SNR.settings import *

my_map = client.get_map("MainCat").blocking()
# my_map.clear()
def newredis():
    # count = 0
    # catID = [1, 111, 1239, 141, 2092, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988,222,166]
    catID=[166]
    # Categories
    for f in catID:

        my_map.remove('categorycache_for_' + str(f) + '1-1-1undefinedundefined-1undefinedundefined40')
        cache_key = 'categorycache_for_' + str(f) + '1-1-1undefinedundefined-1undefinedundefined40'
        temp = []
        ls = ' where "SNR_isShow" = TRUE'
        main_data_query = 'Select {0} from public.products_allproducts_' + str(
            f) + '{1} TABLESAMPLE SYSTEM(1) OFFSET ' + str(0) + ' LIMIT ' + str(40)
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

        data_query = main_data_query.format(",".join(out),ls)
        print("main query", data_query)

        f_count = len(fields)
        count=0
        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                    current_item['index'] = count
                count=count+1
                temp.append(current_item)
        connection.close()
        print('ok')
        a = {'results': temp,
             'items': str('5000+'), 'Pages': str('20')
             }
        my_map.put(cache_key, a)
    print('done')

newredis()
# my_map.remove("categorycache_for_8881-1-1undefinedundefined-1undefinedundefined40")