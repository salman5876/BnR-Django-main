import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
import requests
from django.core.cache import cache
from django.db import connection



def newredis():
    count = 0
    catID = [1, 111, 1239, 141, 2092, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988,222,166]
    # catID=[166]
    # Categories
    for f in catID:
        cache.delete('categorycache_for_backup' + str(f) + '1-1-1undefinedundefined-1undefinedundefined')
        key_backup = 'categorycache_for_backup' + str(f) + '1-1-1undefinedundefined-1undefinedundefined'
        key_backup_time = 43200  # time to live in seconds
        temp = []
        ls = ' where "SNR_isShow" = TRUE'
        main_data_query = 'Select {0} from public.products_allproducts_' + str(
            f) + '{1} order by Random() OFFSET ' + str(0) + ' LIMIT ' + str(40)
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

        with connection.cursor() as cursor:
            cursor.execute(data_query)

            for i in cursor.fetchall():

                current_item = {}
                for j in range(f_count):
                    current_item[fields[j]] = i[j]

                temp.append(current_item)
        print('ok')
        co = 'Select Count(\'*\')  from public.products_allproducts_' + str(f) + str(ls) + ' limit ' + str(40 * 20)
        print(co)
        with connection.cursor() as cursor:
            cursor.execute(co)
            it = cursor.fetchall()
            it = [i[0] for i in it]
            print(it)
        print(it[0])
        if it[0] >= (count * 20):
            item = '5000+'
            totalpages = '20'
        else:
            item = it[0]
            totalpages = int(it[0]) / int(count)
        cache.set(key_backup, {'results': temp, 'items': item, 'Pages': totalpages}, key_backup_time)
    print('done')

newredis()

