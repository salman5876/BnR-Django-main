import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import *
from django.db import connection
from django.db import connections
from products.serializers import *


def Walmart_image_update():
    a=AllProducts.objects.filter(SNR_Available='Walmart')[:10] #Limit apply for Testing
    for i in a:
        rpl = i.SNR_ImageURL.replace("Height=180&odnWidth=180", "Height=500&odnWidth=500")
        i.SNR_ImageURL=rpl
        # i.save()    #when U run It Uncomment
        print('Done')
# Walmart_image_update()


def addproduct_to_partitiontable():
    print('start')
    li=[1, 111, 1239, 141, 166, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    for i in li:
        res = AllProducts.objects.filter(SNR_CatID=i)
        for j in res:
            try:
                print(j)
                query_data = 'INSERT INTO public.products_allproducts_' + str(
                    i) + '("SNR_Title","SNR_ModelNo","SNR_SKU","SNR_PriceBefore","SNR_Price","SNR_CustomerReviews","SNR_ProductURL","SNR_isShow","SNR_Date","SNR_Brand","SNR_UPC","SNR_Category","SNR_CatID","SNR_SubCatID","SNR_MainCatID","SNR_SubCategory","SNR_Condition","SNR_Description_Mobile","SNR_Available","SNR_ImageURL","SNR_Description") VALUES(\'' + str(
                    j.SNR_Title) + '\',\'' + str(j.SNR_ModelNo) + '\',\'' + str(j.SNR_SKU) + '\',\'' + str(
                    j.SNR_PriceBefore) + '\',\'' + str(j.SNR_Price) + '\',\'' + str(
                    j.SNR_CustomerReviews) + '\',\'' + str(j.SNR_ProductURL) + '\',\'' + str(
                    j.SNR_isShow) + '\',CURRENT_TIMESTAMP,\'' + str(j.SNR_Brand) + '\',\'' + str(
                    j.SNR_UPC) + '\',\'' + str(j.SNR_Category) + '\',\'' + str(i) + '\',\'' + str(
                    j.SNR_SubCatID) + '\',\'' + str(j.SNR_MainCatID) + '\',\'' + str(j.SNR_SubCategory) + '\',\'' + str(
                    j.SNR_Condition) + '\',\'' + str(j.SNR_Description_Mobile) + '\',\'' + str(
                    j.SNR_Available) + '\',\'' + str(j.SNR_ImageURL) + '\',\'' + str(j.SNR_Description) + '\')'

                with connection.cursor() as cursor:
                    cursor.execute(query_data)
                with connections["newdb"].cursor() as cursor:
                    cursor.execute(query_data)
                connections.close()
                print('Save SuccessFully')
            except:
                print('Something Went Wrong')


# addproduct_to_partitiontable()


def insert_into_products():
    try:
        a={
            'SNR_ModelNo':'0001',
            'SNR_Title':'hamza',
            'SNR_SKU':'abc',
            'SNR_PriceBefore':'26',
            'SNR_Price':'16',
            'SNR_CustomerReviews':'4.0',
            'SNR_ProductURL':'hamza',
            'SNR_isShow':True,
            'SNR_Brand':'jhu',
            'SNR_UPC':'upc',
            'SNR_Category':'test',
            'SNR_CatID':1,
            'SNR_SubCatID':1,
            'SNR_MainCatID':1,
            'SNR_SubCategory':1,
            'SNR_Condition':'New',
            'SNR_Description_Mobile':'see site',
            'SNR_Available':'hamza',
            'SNR_ImageURL':'img.png',
            'SNR_Description':'test'

        }
        query_data = 'INSERT INTO public.products_allproducts("SNR_Title","SNR_ModelNo","SNR_SKU","SNR_PriceBefore","SNR_Price","SNR_CustomerReviews","SNR_ProductURL","SNR_isShow","SNR_Date","SNR_Brand","SNR_UPC","SNR_Category","SNR_CatID","SNR_SubCatID","SNR_MainCatID","SNR_SubCategory","SNR_Condition","SNR_Description_Mobile","SNR_Available","SNR_ImageURL","SNR_Description") VALUES(\'' + str(
            a['SNR_Title']) + '\',\'' + str(a['SNR_ModelNo']) + '\',\'' + str(a['SNR_SKU']) + '\',\'' + str(
            a['SNR_PriceBefore']) + '\',\'' + str(a['SNR_Price']) + '\',\'' + str(
            a['SNR_CustomerReviews']) + '\',\'' + str(a['SNR_ProductURL']) + '\',\'' + str(
            a['SNR_isShow']) + '\',CURRENT_TIMESTAMP,\'' + str(a['SNR_Brand']) + '\',\'' + str(
            a['SNR_UPC']) + '\',\'' + str(a['SNR_Category']) + '\',\'' + str(a['SNR_CatID']) + '\',\'' + str(
            a['SNR_SubCatID']) + '\',\'' + str(a['SNR_MainCatID']) + '\',\'' + str(a['SNR_SubCategory']) + '\',\'' + str(
            a['SNR_Condition']) + '\',\'' + str(a['SNR_Description_Mobile']) + '\',\'' + str(
            a['SNR_Available']) + '\',\'' + str(a['SNR_ImageURL']) + '\',\'' + str(a['SNR_Description']) + '\')'
        with connections["newdb"].cursor() as cursor:
            cursor.execute(query_data)
        connections['newdb'].close()
        print('Save SuccessFully')
    except:
        print('Something Went Wrong')

# insert_into_products()

def insert_into_products1():
        a={
            'SNR_ModelNo':'0001',
            'SNR_Title':'hamza1',
            'SNR_SKU':'abc',
            'SNR_PriceBefore':'26',
            'SNR_Price':'16',
            'SNR_CustomerReviews':'4.0',
            'SNR_ProductURL':'hamza1',
            'SNR_isShow':True,
            'SNR_Brand':'jhu',
            'SNR_UPC':'upc',
            'SNR_Category':'test',
            'SNR_Condition':'New',
            'SNR_Description_Mobile':'see site',
            'SNR_Available':'hamza1',
            'SNR_ImageURL':'img.png',
            'SNR_Description':'test'

        }
        try:
            obj= AllProducts(SNR_Title=a['SNR_Title'],SNR_ModelNo=a['SNR_ModelNo'],SNR_SKU=a['SNR_SKU'],SNR_PriceBefore=a['SNR_PriceBefore'],
                             SNR_Price=a['SNR_Price'],SNR_CustomerReviews=a['SNR_CustomerReviews'],SNR_ProductURL=a['SNR_ProductURL'],
                             SNR_isShow=a['SNR_isShow'],SNR_Brand=a['SNR_Brand'],SNR_UPC=a['SNR_UPC'],SNR_Category=a['SNR_Category'],
                             SNR_Condition=a['SNR_Condition'],SNR_Description_Mobile=a['SNR_Description_Mobile'],SNR_Available=a['SNR_Available'],
                             SNR_ImageURL=a['SNR_ImageURL'],SNR_Description=a['SNR_Description'])
            obj.save(using='newdb')
            django.db.connection.close()
            print('Save')
        except:
            pass
            print('some thing went wrong')


# insert_into_products1()


def insert_into_products2():
    a = {
        'SNR_ModelNo': '0001',
        'SNR_Title': 'hamza2',
        'SNR_SKU': 'abc',
        'SNR_PriceBefore': '26',
        'SNR_Price': '16',
        'SNR_CustomerReviews': '4.0',
        'SNR_ProductURL': 'hamza2',
        'SNR_isShow': True,
        'SNR_Brand': 'jhu',
        'SNR_UPC': 'upc',
        'SNR_Category': 'test',
        'SNR_Condition': 'New',
        'SNR_Description_Mobile': 'see site',
        'SNR_Available': 'hamza2',
        'SNR_ImageURL': 'img.png',
        'SNR_Description': 'test'

    }
    # try:
    serializer=AllProducts_Serializer(data=a)
    if serializer.is_valid():
        serializer.save('newdb')
        print('done')
        # obj = AllProducts(SNR_Title=a['SNR_Title'], SNR_ModelNo=a['SNR_ModelNo'], SNR_SKU=a['SNR_SKU'],
        #                   SNR_PriceBefore=a['SNR_PriceBefore'],
        #                   SNR_Price=a['SNR_Price'], SNR_CustomerReviews=a['SNR_CustomerReviews'],
        #                   SNR_ProductURL=a['SNR_ProductURL'],
        #                   SNR_isShow=a['SNR_isShow'], SNR_Brand=a['SNR_Brand'], SNR_UPC=a['SNR_UPC'],
        #                   SNR_Category=a['SNR_Category'],
        #                   SNR_Condition=a['SNR_Condition'], SNR_Description_Mobile=a['SNR_Description_Mobile'],
        #                   SNR_Available=a['SNR_Available'],
        #                   SNR_ImageURL=a['SNR_ImageURL'], SNR_Description=a['SNR_Description'])
        # obj.save(using='newdb')
        # print('Save')
    # except:
    #     pass
    #     print('some thing went wrong')


# insert_into_products2()

def wrongmapping_Cat_id():
    print('start')
    li = [1, 111, 1239, 141, 166, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    res =AllProducts.objects.distinct('SNR_CatID').exclude(SNR_CatID__in=li)
    cat_id=[]
    for i in res:
        cat_id.append(i.SNR_CatID)
    print(cat_id)

# wrongmapping_Cat_id()


#[0, 182, 188, 262, 342, 491, 551, 594, 784, 998, 1167, 2096, 5252, 7235, 9888] these Cat_id exist in All_products table that are not mapped


def updatewaltmart_iamges():
    try:
        li=[1, 8, 111, 141, 166, 222, 412, 436, 469, 536, 537, 632, 772, 783, 888, 922, 988, 1239, 2092, 5181, 5605]
        # li=[1]
        temp=[]
        for ii in li:
            main_data_query = 'Select {0} from public.products_allproducts_'+str(ii)+'  where  "SNR_Available"=\'Walmart\''
            fields = [
                 "SNR_ImageURL", "id",
            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out))
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]
                    temp.append(current_item)
            for k in temp:
                print('id',k['id'])
                print('image',k['SNR_ImageURL'])
                rpl = k['SNR_ImageURL'].replace("Height=180&odnWidth=180", "Height=500&odnWidth=500")
                print(rpl)
                data='Update public.products_allproducts_'+str(ii)+' set "SNR_ImageURL"=\''+str(rpl)+'\' where id=\''+str(k['id'])+'\''
                with connection.cursor() as cursor:
                    cursor.execute(data)
                print('done')
    except:
        print('something went wrong')

# updatewaltmart_iamges()
#=============================================================================================================================
def scri():
    a='test'
    return a


def review_insert_all_products_table():
    res = AllProducts.objects.filter(SNR_Available='') #Merchant pass in this
    for i in res:
        revi=scri(i.SNR_ProductURL)   #scrapping function call url hit on site and return review
        i.SNR_Review=revi
        i.save()
        print('Done')

def review_Insert_Partiton_table():
    try:
        merchant='' # merchants pass in this
        li = [1, 8, 111, 141, 166, 222, 412, 436, 469, 536, 537, 632, 772, 783, 888, 922, 988, 1239, 2092, 5181, 5605]
        temp = []
        for ii in li:
            main_data_query = 'Select {0} from public.products_allproducts_' + str(ii) + ' WHERE "SNR_Available"='+str(merchant)+''
            fields = [
                "SNR_ProductURL", "id",
            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out))
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]
                    temp.append(current_item)
            for k in temp:
                print('id', k['id'])
                print('URL', k['SNR_ProductURL'])
                Review = scri(k['SNR_ProductURL'])  #scrapping function call url hit on site and return review
                data = 'Update public.products_allproducts_' + str(ii) + ' set "SNR_Review"=\'' + str(
                    Review) + '\' where id=\'' + str(k['id']) + '\''
                with connection.cursor() as cursor:
                    cursor.execute(data)
                print('done')
    except:
        print('something went wrong')


def description_tag_remove_update_all_products_table():
    res = AllProducts.objects.all()
    for i in res:
        mobile_des = scri(i.SNR_Description) #Decription clean function call return clean description
        i.SNR_Description_Mobile=mobile_des
        i.save()
        print('Done')


def description_tag_remove_update_partition_table():
    try:
        li = [1, 8, 111, 141, 166, 222, 412, 436, 469, 536, 537, 632, 772, 783, 888, 922, 988, 1239, 2092, 5181, 5605]
        temp = []
        for ii in li:
            main_data_query = 'Select {0} from public.products_allproducts_' + str(ii) + ''
            fields = [
                "SNR_Description", "id",
            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out))
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]
                    temp.append(current_item)
            for k in temp:
                print('id', k['id'])
                print('Des', k['SNR_Description'])
                mobile_des = scri(k['SNR_Description']) #Decription clean function call return clean description
                data = 'Update public.products_allproducts_' + str(ii) + ' set "SNR_Description_Mobile"=\'' + str(
                    mobile_des) + '\' where id=\'' + str(k['id']) + '\''
                with connection.cursor() as cursor:
                    cursor.execute(data)
                print('done')
    except:
        print('something went wrong')


def cat_distinct():
    res = AllProductsPartition.objects.distinct('SNR_Category','SNR_SubCategory').values('SNR_Category','SNR_SubCategory','SNR_CatID','SNR_SubCatID','SNR_MainCatID')
    for i in res:
        f= open("demofile2.txt", "a")
        f.write("'"+i['SNR_Category']+","+str(i['SNR_SubCategory'])+"':["+str(i['SNR_CatID'])+","+str(i['SNR_SubCatID'])+","+str(i['SNR_MainCatID'])+"]\n")
        f.close()





def update_status_in_all_products_table_that_already_move_in_partion():
    try:
        res  = AllProductsPartition.objects.all()
        for i in res:
            if AllProducts.objects.filter(SNR_ProductURL=str(i.SNR_ProductURL)).exists():
                pro = AllProducts.objects.get(SNR_ProductURL=i.SNR_ProductURL)
                pro.SNR_isShow=False
                pro.save()
                print('DONE')
    except:
        print('something went wrong')



def addproduct_to_partitiontable_update():
    print('start')
    li=[1, 111, 1239, 141, 166, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    for i in li:
        res = AllProducts.objects.filter(SNR_CatID=i,SNR_isShow=True)
        print(i,' :Cat Product is',len(res))
        for index,j in enumerate(res):
            try:
                print(j)
                query_data = 'INSERT INTO public.products_allproducts_' + str(
                    i) + '("SNR_Title","SNR_ModelNo","SNR_SKU","SNR_PriceBefore","SNR_Price","SNR_CustomerReviews","SNR_ProductURL","SNR_isShow","SNR_Date","SNR_Brand","SNR_UPC","SNR_Category","SNR_CatID","SNR_SubCatID","SNR_MainCatID","SNR_SubCategory","SNR_Condition","SNR_Description_Mobile","SNR_Available","SNR_ImageURL","SNR_Description") VALUES(\'' + str(
                    j.SNR_Title) + '\',\'' + str(j.SNR_ModelNo) + '\',\'' + str(j.SNR_SKU) + '\',\'' + str(
                    j.SNR_PriceBefore) + '\',\'' + str(j.SNR_Price) + '\',\'' + str(
                    j.SNR_CustomerReviews) + '\',\'' + str(j.SNR_ProductURL) + '\',\'' + str(
                    j.SNR_isShow) + '\',CURRENT_TIMESTAMP,\'' + str(j.SNR_Brand) + '\',\'' + str(
                    j.SNR_UPC) + '\',\'' + str(j.SNR_Category) + '\',\'' + str(i) + '\',\'' + str(
                    j.SNR_SubCatID) + '\',\'' + str(j.SNR_MainCatID) + '\',\'' + str(j.SNR_SubCategory) + '\',\'' + str(
                    j.SNR_Condition) + '\',\'' + str(j.SNR_Description_Mobile) + '\',\'' + str(
                    j.SNR_Available) + '\',\'' + str(j.SNR_ImageURL) + '\',\'' + str(j.SNR_Description) + '\',\''+str(j.SNR_Review)+'\',\''+str(j.SNR_Review_score)+'\')'

                with connection.cursor() as cursor:
                    cursor.execute(query_data)
                print('INSERT:',index)
            except:
                print('Something Went Wrong')
        print('successfully insert all',i)






def coupon_move_func():
    try:
        AllProductsCoupons.objects.filter(SNR_Active=True).update(SNR_Active=None)
        AllProductsCoupons.objects.filter(SNR_Active=False).update(SNR_Active=True)
        old = AllProductsCoupons.objects.filter(SNR_Active=None)
        for i in old:
            transfer = AllProductsCoupons_backup(SNR_Available=i.SNR_Available,SNR_Title=i.SNR_Title,SNR_Description=i.SNR_Description,
                               SNR_URl_Code=i.SNR_URl_Code,SNR_CouponCode_url=i.SNR_CouponCode_url,SNR_Discount=i.SNR_Discount,
                               SNR_Expire=i.SNR_Expire,SNR_Expire_Status=i.SNR_Expire_Status,SNR_Active=False)
            transfer.save()
    except:
        pass


import datetime

def expirecoupon():
    a=datetime.datetime.now().date()
    re = AllProductsCoupons.objects.filter(SNR_Active=True)
    for i in re:
        try:
            if i.SNR_Expire < a:
                i.SNR_Expire_Status=True
                i.save()
                print(i.SNR_Expire)
        except:
            pass

# expirecoupon()



from bs4 import BeautifulSoup
import re
from multiprocessing.pool import ThreadPool

def anc(temp):
    for k in temp:
        print('id', k['id'])
        try:
            soup = BeautifulSoup(str(k['SNR_Description']), u'html.parser')
            mobile_des = soup.text.strip()  # Decription clean function call return clean description
            SNR_Description_Mobile = mobile_des
            SNR_Description_Mobile = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in SNR_Description_Mobile.split("\n")]
            print(SNR_Description_Mobile)
            data = 'Update public.products_allproducts_' + str(412) + ' set "SNR_Description_Mobile"=\'' + str(
                SNR_Description_Mobile[0]) + '\' where id=\'' + str(k['id']) + '\''
            with connection.cursor() as cursor:
                cursor.execute(data)
            print('done')
        except:
            print('>>>')

def updatewaltmart_iamges1():
    # try:
        li=[412, 436, 469, 536, 537, 632, 772, 783, 888, 922, 988, 1239, 2092, 5181, 5605]
        # li=[222]
        temp=[]
        for ii in li:
            main_data_query = 'Select {0} from public.products_allproducts_'+str(ii)+' where "SNR_Description"!=\'None\' limit 1000'
            fields = [
                  "id","SNR_Description"
            ]
            out = ['"{0}"'.format(i) for i in fields]
            data_query = main_data_query.format(",".join(out))
            f_count = len(fields)
            with connection.cursor() as cursor:
                cursor.execute(data_query)
                for i in cursor.fetchall():
                    current_item = {}
                    for j in range(f_count):
                        current_item[fields[j]] = i[j]
                    temp.append(current_item)
            chunksList=[]
            for i in range(0, len(temp), 50):
                chunk = temp[i:i + 50]
                print('1')
                chunksList.append(chunk)
            print(chunksList)
            print('Done Chunk')
            # print('chunk end:', datetime.now())
            pool = ThreadPool(10)
            pool.map(anc, chunksList)
            pool.join()
            pool.close()

            print('Done All Description')

    # except:
    #     print('something went wrong')

updatewaltmart_iamges1()

def move_Data(merchant):
    try:
        Active_Vocation.objects.filter(SNR_Active=True, SNR_Available=str(merchant)).update(SNR_Active=None)
        Active_Vocation.objects.filter(SNR_Active=False, SNR_Available=str(merchant)).update(SNR_Active=True)
        old = Active_Vocation.objects.filter(SNR_Active=None, SNR_Available=str(merchant))
        for i in old:
            transfer = Vocation_backup(SNR_SKU=i.SNR_SKU, SNR_Title=i.SNR_Title, SNR_Category=i.SNR_Category,
                                  SNR_PriceBefore=i.SNR_PriceBefore
                                  , SNR_PriceAfter=i.SNR_PriceAfter, SNR_Available=i.SNR_Available,
                                  SNR_ProductURL=i.SNR_ProductURL,SNR_Description=i.SNR_Description, SNR_Customer_Rating=i.SNR_Customer_Rating
                                  ,SNR_ImageURL=i.SNR_ImageURL, SNR_Active=False)
            transfer.save()
        Active_Vocation.objects.filter(SNR_Active=None, SNR_Available=str(merchant)).delete()
        print('Moving Data completed')

    except:
        print('In Move Data Exceptoin')


def filecre():
    with open("/home/hamza/Desktop/newmap_ebay", "w") as fpp:
        with open("/home/hamza/Downloads/TOYAL RE CHECK eBag DONE.txt") as fp:
            a=fp.readlines()
            for i in a:
                print("abccc>>",i)
                print('')
                if i.replace("\n","")[-1:]==',':
                    a=i.replace("\n","")[:-1]
                    fpp.write(str(a.replace("\n",""))+","+"\n")
                else:
                    fpp.write(str(i.replace("\n", "")) + "," + "\n")
# filecre()