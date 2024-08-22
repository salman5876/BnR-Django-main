import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from django.db import connection
import requests
from products.models import *
from django.core.cache import cache
from products.serializers import *
from SNR.settings import *

my_map = client.get_map("Home").blocking()

def updatelogo():
    a=Active_DailyDeals.objects.filter(SNR_Active=True).distinct('SNR_Available')
    merchants.objects.filter(active=True).update(active=False)
    for i in a:
        print(i.SNR_Available)
        if merchants.objects.filter(name=str(i.SNR_Available)).exists():
            res=merchants.objects.get(name=str(i.SNR_Available))
            res.active=True
            res.save()
            print('Done')
        else:
            print('Not IN Merchant Table :',i.SNR_Available)

# updatelogo()

#
def cac():
    cache.delete('Merchant_Logos_Home')
    date = requests.get('https://backend.shopnroar.com/products/merchantlogos/')
    print(date.status_code)
    print('Done')

# cac()




def homepage():
    my_map.clear()
    # my_map.remove('Home_Page')
    cache_key = 'Home_Page'
    mer = merchants.objects.filter(active=True).order_by('prefer')
    serializer = merchantslizer1(mer, many=True)
    print(serializer.data)
    with connection.cursor() as cursor:
        res = {}
        cursor.execute(
            'SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
        temp = []
        for i in cursor.fetchall():


            temp.append({'id': i[0], 'Category': i[1], 'path': i[2]})
        res["Categories"] = temp
    temp11 = []
    count=0
    with connection.cursor() as cursor:
        main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" IN (\'Amazon\',\'Ebay\',\'Walmart\') AND "SNR_Active"=True order by random() limit 20'
        fields = [
            "SNR_SKU", "SNR_Title",
            "SNR_Available","SNR_PriceAfter","SNR_PriceBefore",
            "SNR_ProductURL", "SNR_ImageURL",
            "SNR_Date", "SNR_Category","id","SNR_Description","SNR_Customer_Rating"
        ]
        out = ['"{0}"'.format(i) for i in fields]
        data_query = main_query.format(",".join(out))
        cursor.execute(data_query)
        for i in cursor.fetchall():
            current_item = {}
            for j in range(len(fields)):
                current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                current_item['index'] = count
            count=count+1
            temp11.append(current_item)
    temp22 = []
    temp3 = []
    temp4 = []
    temp5 = []
    ls = ' where "SNR_isShow" = TRUE'
    li = [222, 536, 166, 469]
    main_data_query = 'Select {0} from public.products_allproducts_' + str(
        222) + ' {1} order by random()  LIMIT 20'
    fields = [
        "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]
    data_query = main_data_query.format(",".join(out), ls)
    f_count = len(fields)
    count=0
    with connection.cursor() as cursor:
        cursor.execute(data_query)
        for i in cursor.fetchall():
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                current_item['index'] = count
            temp22.append(current_item)
            count=count+1
    main_data_query = 'Select {0} from public.products_allproducts_' + str(
        536) + ' {1} order by random()  LIMIT 20'
    fields = [
        "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]
    data_query = main_data_query.format(",".join(out), ls)
    f_count = len(fields)
    count=0
    with connection.cursor() as cursor:
        cursor.execute(data_query)
        for i in cursor.fetchall():
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                current_item['index'] = count
            temp3.append(current_item)
            count=count+1
    main_data_query = 'Select {0} from public.products_allproducts_' + str(
        166) + ' {1} order by random()  LIMIT 20'
    fields = [
        "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]
    data_query = main_data_query.format(",".join(out), ls)
    f_count = len(fields)
    count=0
    with connection.cursor() as cursor:
        cursor.execute(data_query)
        for i in cursor.fetchall():
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                current_item['index'] = count
            temp4.append(current_item)
            count=count+1
    main_data_query = 'Select {0} from public.products_allproducts_' + str(
        469) + ' {1} order by random()  LIMIT 20'
    fields = [
        "SNR_Title",
                "SNR_Brand",
                "SNR_Available",
                "SNR_ProductURL", "SNR_ImageURL", "id",
                "SNR_Description",
                "SNR_Category",
                "SNR_Condition", "SNR_PriceBefore",
                "SNR_CustomerReviews", "SNR_Price",
                "SNR_SubCategory"

    ]
    out = ['"{0}"'.format(i) for i in fields]
    data_query = main_data_query.format(",".join(out), ls)
    f_count = len(fields)
    count=0
    with connection.cursor() as cursor:
        cursor.execute(data_query)
        for i in cursor.fetchall():
            current_item = {}
            for j in range(f_count):
                current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                current_item['index']=count
            temp5.append(current_item)
            count=count+1

    final = {
        'Categories': res,
        'merchants': serializer.data,
        'home_Electronics': temp22,
        'home_Garden': temp3,
        'home_Apperel': temp4,
        'home_Health': temp5,
        'Hot_Deals': temp11,
        'Coupon':merchantscoupons.objects.filter(active=True).values(),
    }
    my_map.put(cache_key,final)
    print('OK DONE')

# homepage()


# a=Active_DailyDeals.objects.distinct('SNR_Category')
# with open("/home/hamza/Desktop/catdeal","w") as fp:
#     for i in a:
#         print(i.SNR_Category)
#         fp.write(str(i.SNR_Category)+"\n")