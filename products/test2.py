@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def Home_test(request):
    if request.method == 'GET':
        print("before cache")
        my_map = client.get_map("Home").blocking()
        cache_key = 'HomePageOldAPI'
        # cache_time = 36000  # time to live in seconds
        result_cache = my_map.get(cache_key)
        print("after cache")
        print(result_cache)
        if result_cache == None:
            print('3rd')
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
            temp11=[]
            with connection.cursor() as cursor:
                main_query = 'SELECT {0} FROM products_active_dailydeals Where "SNR_Available" IN (\'amazon\',\'ebay\',\'Walmart\') AND "SNR_Active"=True order by random() limit 20'
                fields = [
                    "SNR_SKU", "SNR_Title",
                    "SNR_Available", "SNR_PriceAfter", "SNR_PriceBefore",
                    "SNR_ProductURL", "SNR_ImageURL",
                    "SNR_Date", "SNR_Category","id","SNR_Description",
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
            temp22=[]
            temp3=[]
            temp4=[]
            temp5=[]
            ls = ' where "SNR_isShow" = TRUE'
            li=[222,536,166,469]
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
            data_query = main_data_query.format(",".join(out),ls)
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
                        current_item[fields[j]] =str(i[j]).encode('utf-8').strip()
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
            final={
                'Categories':res,
                'merchants':serializer.data,
                'home_Electronics':temp22,
                'home_Garden':temp3,
                'home_Apperel':temp4,
                'home_Health':temp5,
                'Hot_Deals':temp11,
                'Coupon': merchantscoupons.objects.filter(active=True).values(),
            }
            try:
                my_map.remove(cache_key)
            except:
                pass
            my_map.put(cache_key,final)
            return Response(final,status.HTTP_200_OK)
        else:
            print('inchache')
            return Response(result_cache,status.HTTP_200_OK)
