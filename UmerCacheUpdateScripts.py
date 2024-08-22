from SNR.settings import client
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from django.db import connection
from products.models import *
from products.serializers import *
from django.db.models import Q
import re
def Home_Page_Updataion():
    Home_map = client.get_map("Home").blocking()
    try:
        data = Home_map.key_set()
        print(data)
        for keys in data:
            if keys=='Home_Page_New_cust':


                mer = merchants.objects.filter(active=True).order_by('prefer')
                serializer = merchantslizer1(mer, many=True)
                print(serializer.data)
                with connection.cursor() as cursor:
                    res = {}

                    fields = [
                        "SNR_CatName"
                    ]
                    cursor.execute(
                        'SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
                    temp = []
                    for i in cursor.fetchall():
                        temp.append({'id': i[0], 'Category': i[1], 'path': i[2]})
                        temp2 = []
                    res["Categories"] = temp
                connection.close()
                amazondata = []
                with connection.cursor() as cursor:
                    main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'amazon\' AND "SNR_Active"=True order by random() limit 20'
                    fields = [
                        "SNR_SKU", "SNR_Title",
                        "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                        "SNR_ProductURL", "SNR_ImageURL",
                        "SNR_Date", "SNR_Category", "id", "SNR_Description", "SNR_Customer_Rating"
                    ]
                    out = ['"{0}"'.format(i) for i in fields]
                    data_query = main_query.format(",".join(out))
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(len(fields)):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                        amazondata.append(current_item)
                connection.close()
                ebaydata = []
                with connection.cursor() as cursor:
                    main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'ebay\' AND "SNR_Active"=True order by random() limit 20'
                    fields = [
                        "SNR_SKU", "SNR_Title",
                        "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                        "SNR_ProductURL", "SNR_ImageURL",
                        "SNR_Date", "SNR_Category", "id", "SNR_Description", "SNR_Customer_Rating"
                    ]
                    out = ['"{0}"'.format(i) for i in fields]
                    data_query = main_query.format(",".join(out))
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(len(fields)):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                        ebaydata.append(current_item)
                connection.close()

                walmartdata = []
                with connection.cursor() as cursor:
                    main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'Walmart\' AND "SNR_Active"=True order by random() limit 20'
                    fields = [
                        "SNR_SKU", "SNR_Title",
                        "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                        "SNR_ProductURL", "SNR_ImageURL",
                        "SNR_Date", "SNR_Category", "id", "SNR_Description", "SNR_Customer_Rating"
                    ]
                    out = ['"{0}"'.format(i) for i in fields]
                    data_query = main_query.format(",".join(out))
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(len(fields)):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                        walmartdata.append(current_item)
                connection.close()
                bestbuydata = []
                with connection.cursor() as cursor:
                    main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'BEST BUY\' AND "SNR_Active"=True order by random() limit 20'
                    fields = [
                        "SNR_SKU", "SNR_Title",
                        "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                        "SNR_ProductURL", "SNR_ImageURL",
                        "SNR_Date", "SNR_Category", "id", "SNR_Description", "SNR_Customer_Rating"
                    ]
                    out = ['"{0}"'.format(i) for i in fields]
                    data_query = main_query.format(",".join(out))
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(len(fields)):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                        bestbuydata.append(current_item)
                connection.close()
                targetdata = []
                with connection.cursor() as cursor:
                    main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" = \'target\' AND "SNR_Active"=True order by random() limit 20'
                    fields = [
                        "SNR_SKU", "SNR_Title",
                        "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                        "SNR_ProductURL", "SNR_ImageURL",
                        "SNR_Date", "SNR_Category", "id", "SNR_Description", "SNR_Customer_Rating"
                    ]
                    out = ['"{0}"'.format(i) for i in fields]
                    data_query = main_query.format(",".join(out))
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(len(fields)):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                        targetdata.append(current_item)
                connection.close()

                final = {
                    'merchants': serializer.data,
                    'amazon': amazondata,
                    'ebay': ebaydata,
                    'walmart': walmartdata,
                    'bestbuy': bestbuydata,
                    'target': targetdata,
                    # 'Coupon': merchantscoupons.objects.filter(active=True).values(),
                }
                Home_map.remove(keys)
                Home_map.put(keys, final)
            elif keys=='HomePageOldAPI':
                mer = merchants.objects.filter(active=True).order_by('prefer')
                serializer = merchantslizer1(mer, many=True)
                print(serializer.data)
                with connection.cursor() as cursor:
                    # cursor.execute('SELECT DISTINCT "SNR_Available" FROM products_allproducts Where "SNR_Category" = %s',[category])
                    res = {}
                    result = []
                    fields = [
                        "SNR_CatName"
                    ]
                    cursor.execute(
                        'SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
                    temp = []
                    temp2 = []
                    # print cursor.fetchall()
                    for i in cursor.fetchall():
                        temp.append({'id': i[0], 'Category': i[1], 'path': i[2]})
                        temp2 = []
                    res["Categories"] = temp
                connection.close()
                temp11 = []
                with connection.cursor() as cursor:
                    main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" IN (\'amazon\',\'ebay\',\'Walmart\') AND "SNR_Active"=True order by random() limit 20'
                    fields = [
                        "SNR_SKU", "SNR_Title",
                        "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                        "SNR_ProductURL", "SNR_ImageURL",
                        "SNR_Date", "SNR_Category", "id", "SNR_Description",
                        "SNR_Customer_Rating",
                    ]
                    out = ['"{0}"'.format(i) for i in fields]
                    data_query = main_query.format(",".join(out))
                    cursor.execute(data_query)
                    temp1 = []
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(len(fields)):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()

                        temp11.append(current_item)
                connection.close()
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
                with connection.cursor() as cursor:
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(f_count):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                        temp22.append(current_item)
                connection.close()
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
                with connection.cursor() as cursor:
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(f_count):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                        temp3.append(current_item)
                connection.close()
                main_data_query = 'Select {0} from public.products_allproducts_' + str(
                    111) + ' {1} order by random()  LIMIT 20'
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
                with connection.cursor() as cursor:
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(f_count):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                        temp4.append(current_item)
                connection.close()
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
                with connection.cursor() as cursor:
                    cursor.execute(data_query)
                    for i in cursor.fetchall():
                        current_item = {}
                        for j in range(f_count):
                            current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                        temp5.append(current_item)
                connection.close()
                final = {
                    'Categories': res,
                    'merchants': serializer.data,
                    'home_Electronics': temp22,
                    'home_Garden': temp3,
                    'home_Apperel': temp4,
                    'home_Health': temp5,
                    'Hot_Deals': temp11,
                    'Coupon': merchantscoupons.objects.filter(active=True).values(),
                }
                Home_map.remove(keys)
                Home_map.put(keys, final)
    except:
        Home_map.clear()
    print("Cache Updated")

Home_Page_Updataion()
# Vocation_map = client.get_map('Vocation').blocking()
# data = Vocation_map.key_set()
# print(data)
# Vocation_map = client.get_map('Vocation').blocking()
# new=Vocation_map.get('Vocation==All==undefine==undefine==undefine==-1==-1==40==1')
# print(new)
def Vocation_Filter_Cache():



    Vocation_map = client.get_map('Vocation').blocking()
    try:
        data = Vocation_map.key_set()
        print(data)
        for keys in data:
            splited_data=keys.split('==')
            query = splited_data[1]
            cat = splited_data[2]
            sort = splited_data[3]
            search = splited_data[4]
            minprice= int(splited_data[5])
            maxprice = int(splited_data[6])
            totalResult = splited_data[7]
            page = splited_data[8]
            print("min",minprice)
            print("mac",maxprice)
            try:
                page = int(page)
                if page < 1:
                    page = 1

            except:
                page = 1

            temp = []
            limit = page * int(totalResult)
            offset = (page - 1) * int(totalResult)
            if query == 'All':
                ls = ' where "SNR_Active"=TRUE '
            else:
                ls = ' where "SNR_Active"=TRUE AND "SNR_Available" =\'' + str(query.replace("'", "''")) + '\''
            if cat != "undefine":
                print("in cat")
                ls = ls + ' AND "SNR_Category" =\'' + cat.replace("'", "''") + '\''
            if minprice != -1 and maxprice != -1:
                print(minprice,maxprice)
                print("in price")
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + str(minprice) + ' AND ' + str(
                    maxprice)
            if search != 'undefine':
                print("in search")
                a = str(search).replace("\'", "")
                print(a)
                ls = ls + ' AND "tsv_title" @@ plainto_tsquery(\'' + str(a) + '\')'
            if sort != "undefine":
                print("in sort")
                if sort == 'ASC':
                    lss = ' order by "SNR_PriceAfter" ASC'
                elif sort == 'DESC':
                    lss = ' order by "SNR_PriceAfter" DESC'
                elif sort == 'LATEST':
                    lss = ' order by "id" DESC'
                elif sort == 'OLDEST':
                    lss = ' order by "id" ASC'
                main_data_query = 'Select {0} from public.products_active_vocation {1}  ' + str(lss) + ' OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
                co = 'Select Count(\'*\') from public.products_active_vocation ' + str(ls)
            else:
                print("no filter")
                main_data_query = 'Select {0} from public.products_active_vocation {1}  OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
                co = 'Select Count(\'*\') from public.products_active_vocation ' + str(ls)

            with connection.cursor() as cursor:
                cursor.execute(co)
                it = cursor.fetchall()
                it = [i[0] for i in it]
            connection.close()
            # print("????",it)
            totalpages = int(int(it[0]) / int(totalResult))
            per = int(it[0]) % int(totalResult)
            if per != 0:
                totalpages += 1

            fields = [
                "SNR_SKU", "SNR_Title",
                "SNR_Available", "id",
                "SNR_ProductURL", "SNR_ImageURL",
                "SNR_Date", "SNR_Category", "SNR_Description",
                "SNR_PriceBefore", "SNR_PriceAfter", "SNR_Customer_Rating"
            ]
            out = ['"{0}"'.format(i) for i in fields]

            data_query = main_data_query.format(",".join(out), ls)
            f_count = len(fields)
            # print(data_query)
            count = 0
            with connection.cursor() as cursor:
                cursor.execute(data_query)

                for i in cursor.fetchall():

                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                        current_item['index'] = count
                    count = count + 1

                    temp.append(current_item)
            connection.close()
            a = {'results': temp,
                 'items': str(it[0]), 'pages': str(totalpages)
                 }
            print(keys)
            print("sss",a)
            print("ss",temp)
            Vocation_map.clear(keys)

            Vocation_map.put(keys, a)
            # new = Vocation_map.get('Vocation==All==undefine==undefine==undefine==-1==-1==40==1')
            # print(new)
            print("Vocation Updated")
            # break
    except Exception as e:
        # print(e)
        Vocation_map.clear()
Vocation_Filter_Cache()



def DealsCacheUpdation():

    Deal_map = client.get_map("Deal").blocking()
    try:
        data = Deal_map.key_set()
        print(data)
        for keys in data:
            splited_data = keys.split('==')
            query = splited_data[1]
            cat = splited_data[2]
            sort = splited_data[3]
            search = splited_data[4]
            minprice = int(splited_data[5])
            maxprice = int(splited_data[6])
            totalResult = splited_data[7]
            page = splited_data[8]
            try:
                page = int(page)
                if page < 1:
                    page = 1

            except:
                page = 1
            temp = []
            limit = page * int(totalResult)
            offset = (page - 1) * int(totalResult)

            if query == 'All':
                ls = ' where "SNR_Active"=TRUE AND "SNR_Available" IS NOT NULL'
            else:
                ls = ' where "SNR_Active"=TRUE AND "SNR_Available" =\'' + str(query.replace("'", "''")) + '\''
            if cat != "undefine":
                ls = ls + ' AND "SNR_Category" =\'' + cat.replace("'", "''") + '\''
            if minprice != -1 and maxprice != -1:
                ls = ls + ' AND "SNR_PriceAfter" BETWEEN ' + minprice + ' AND ' + str(
                    maxprice)
            if search != 'undefine':
                a = str(search).replace("\'", "")
                a = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in a.split("\n")]
                ls = ls + ' AND "tsv_title" @@ plainto_tsquery(\'' + str(a[0]) + '\')'
            if sort != "undefine":
                if sort == 'ASC':
                    lss = ' order by "SNR_PriceAfter" ASC'
                elif sort == 'DESC':
                    lss = ' order by "SNR_PriceAfter" DESC'
                elif sort == 'LATEST':
                    lss = ' order by "id" DESC'
                elif sort == 'OLDEST':
                    lss = ' order by "id" ASC'
                main_data_query = 'Select {0} from public.products_active_dailydeals {1} ' + str(
                    lss) + ' OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
                co = 'Select Count(\'*\') from public.products_active_dailydeals ' + str(ls)
            else:
                main_data_query = 'Select {0} from public.products_active_dailydeals {1} OFFSET ' + str(
                    offset) + ' LIMIT ' + str(limit)
                co = 'Select Count(\'*\') from public.products_active_dailydeals ' + str(ls)

            with connection.cursor() as cursor:
                cursor.execute(co)
                it = cursor.fetchall()
                it = [i[0] for i in it]
            connection.close()
            totalpages = int(int(it[0]) / int(totalResult))
            per = int(it[0]) % int(totalResult)
            if per != 0:
                totalpages += 1

            fields = [
                "SNR_SKU", "SNR_Title",
                "SNR_Available", "id",
                "SNR_ProductURL", "SNR_ImageURL",
                "SNR_Date", "SNR_Category", "SNR_Description",
                "SNR_PriceBefore", "SNR_PriceAfter", "SNR_Customer_Rating"
            ]
            out = ['"{0}"'.format(i) for i in fields]

            data_query = main_data_query.format(",".join(out), ls)
            f_count = len(fields)
            print(data_query)
            count = 0
            with connection.cursor() as cursor:
                cursor.execute(data_query)

                for i in cursor.fetchall():

                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = str(i[j]).encode('utf-8').strip()
                        current_item['index'] = count
                    count = count + 1

                    temp.append(current_item)
            connection.close()
            a = {'results': temp,
                 'items': str(it[0]), 'pages': str(totalpages)
                 }
            Deal_map.remove(keys)
            Deal_map.put(keys, a)
            print("Deals Updated")
    except:
        Deal_map.clear()
DealsCacheUpdation()


# Deal_map2 = client.get_map("Deal_all").blocking()
# Deal_map2.clear()
#
#
#
#
#
#
# Coupons_map = client.get_map("map-name").blocking()
# Coupons_map.clear()
#
# Category_map = client.get_map("MainCat").blocking()
# Category_map.clear()
#
# logo_map = client.get_map("Logo").blocking()
# logo_map.clear()


print("All Updated")
