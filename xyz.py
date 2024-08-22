import django
import os

from django.contrib.postgres.search import TrigramSimilarity

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import *
from userReviews.models import *

data=Active_DailyDeals.objects.filter(SNR_Available='verizon').count()
print(data)

# aa=EmailAlert.objects.all().delete()
# print(aa)
# for value in aa:


# for data in aa:
#     print(data)


input()
from SNR.settings import client

# my_map = client.get_map('Deal').blocking()

data=Active_Vocation.objects.all()[:50]
for val in data:
    print(val.SNR_Available)
    print(val.SNR_Active)
print(data)
# lis=client.get_list()
# # print(my_map)
# print(lis)

# y_map = client.get_map('a').blocking()
#
# print(y_map)

# data=client.loa
# print(data)
# print(data.
    # print(/li)
# for val in data:
#     print(val)
# data = client.



input()



# a=DailyDeals.objects.all()[:2]
# for i in a:
#     print(i.SNR_ImageURL)

# print(DailyDeals.objects.filter(SNR_Available='ebay').count())

# def updateebaydealname():
#     count = 0
#     DailyDeals.objects.filter(SNR_Available='Ebay').update(SNR_Available='ebay')
#     count=count+1
#     print(count)
#
# updateebaydealname()


# from django.db import connection
# cursor = connection.cursor()
# cursor.execute('''SELECT count(*) FROM products_allproducts''')
# query_count = cursor.fetchone()
# print(query_count)
from django.db import connection

def logoimages():
    cats = []
    query_data = 'SELECT DISTINCT "SNR_Available" FROM products_dailydeals where "SNR_Available" IS NOT NULL ORDER BY "SNR_Available" ASC'
    with connection.cursor() as cursor:
        cursor.execute(query_data)
        for i in cursor.fetchall():
            cats.append(i[0])
    for i in cats:
        print(i.lower().replace(" ",""))
        a=i.lower().replace(" ","")
        obj=merchants(name=i,image20px='https://storage.shopnroar.com/MerchantLogos/'+a+'@20.png',image40px='https://storage.shopnroar.com/MerchantLogos/'+a+'@40.png',image60px='https://storage.shopnroar.com/MerchantLogos/'+a+'@60.png',image80px='https://storage.shopnroar.com/MerchantLogos/'+a+'@80.png',image100px='https://storage.shopnroar.com/MerchantLogos/'+a+'@100.png')
        obj.save()


# logoimages()

def countcategorydata():
    print(AllProducts.objects.filter(SNR_CatID=536).count())

# countcategorydata()
# newlist=[]
# A=[{'price':54,'name':'hamza'},{'price':46,'name':'umar'}]
# newlist = sorted(A, key=lambda k: k['price'])
# print(newlist)
# newlist = sorted(A, key=lambda k: k['price'] ,reverse=True)
# print(newlist)

# a=AllProducts.objects.get(pk=32482925)
# print(a.SNR_CatID)

# a=DailyDeals.objects.filter(SNR_Category='Men''s accessories')
# print(a.count())

# a=merchants.objects.get(name='Sam\'s Club')
# print(a.name)
# a.prefer=23
# a.save()
# print('done')
from django.db.models import Count

# a=AllProducts.objects.annotate(Count('id'))
# print(a.count())
# a=AllProducts.objects.filter(SNR_CatID=166)
# print(len(a))

def new():
    # temp={}
    # obj = Active_DailyDeals(SNR_SKU=temp['snrsku'],SNR_Title=a,SNR_Category=a,SNR_PriceBefore=a,SNR_PriceAfter=a,
    #                       SNR_Available=a,SNR_ProductURL=a,SNR_ImageURL=a,SNR_Active=False)
    # obj.save()
    # serializer save()
    Active_DailyDeals.objects.filter(SNR_Active=True).update(SNR_Active=None)
    Active_DailyDeals.objects.filter(SNR_Active=False).update(SNR_Active=True)
    old = Active_DailyDeals.objects.filter(SNR_Active=None)
    for i in old:
        transfer = DailyDeals(SNR_SKU=i.SNR_SKU,SNR_Title=i.SNR_Title,SNR_Category=i.SNR_Category,SNR_PriceBefore=i.SNR_PriceBefore
                              ,SNR_PriceAfter=i.SNR_PriceAfter,SNR_Available=i.SNR_Available,SNR_ProductURL=i.SNR_ProductURL
                              ,SNR_ImageURL=i.SNR_ImageURL,SNR_Active=False)
        transfer.save()
    Active_DailyDeals.objects.filter(SNR_Active=None).delete()
    print('Done')

from django.db import connection
# print(AllProductsPartition.objects.count())
# cursor=connection()
# main_data_query='Select "SNR_ImageURL" from public.products_allproductspartition  where  id=204'
# with connection.cursor() as cursor:
#     cursor.execute(main_data_query)
#     a=[i[0] for i in cursor.fetchall()]
#     print(a)

import xml
from bs4 import BeautifulSoup
def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())
# a=AllProductsPartition.objects.filter(SNR_Available='Amazon')[:10]
# # print(a.SNR_Available)
# for i in a:
#     x=1
#     ab=None
#     soup=BeautifulSoup(i.SNR_Description,'html.parser')
#     for lis in soup.find_all('li'):
#         if x==1:
#             ab=lis.text.strip()
#         else:
#             ab=ab+' '+lis.text.strip()
#         x+=1
#     print(soup)
#     print(ab)
#     print('////////////////')
# a=AllProductsPartition.objects.get(id=4523703)
# a=AllProductsPartition.objects.filter(SNR_Available='Amazon')[:10]
# for i in a:
#     print(i.SNR_Description)
#     c=remove_tags(i.SNR_Description).strip()
#     print(c)
#     c=c.replace("\n","")
#     c=c.replace("\t","")
#     c=c.replace("  "," ")
#     g={'abc':c}
#     print(c)
#     print(g)
# # print(soup)
#
# Select {0} from public.products_allproducts_
from django.core.cache import cache
# from common.redis_client import get_redis_client
# cache = get_redis_client()
# x = cache.keys('prefix:*')
#
# x=cache.keys('*')
# print(len(x))
# # x=cache.clear()
# catID = [1, 111, 1239, 141, 166, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
# for i in catID:
#     cache.delete('categorycache_for_newfilter'+str(i))
# x=cache.keys('*')
# print(len(x))
# print(x)
# result = cache.get('categorycache_for_1661-1-1undefinedundefined-1undefined')
# print(result)
# category_brands_cache_for_166

def cat_images():
    res =Main_Categories.objects.filter(SNR_Cat_Image=None)
    for i in res:
        new=i.SNR_CatName.replace(" ","")
        new=new.replace("&","")
        new='https://storage.shopnroar.com/MerchantLogos/'+new+'.png'
        print(new)
        i.SNR_Cat_Image=new
        i.save()


# cat_images()

import requests

def redisfunc():
    # x = cache.clear()
    catID=[1, 111, 1239, 141, 166, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    for i in catID:
        path='https://backend.shopnroar.com/products/categoryByID1/'+str(i)+'?count=40&low=undefined&high=undefined&brand=undefined&merchant=undefined&sub=undefined&page=1&sort=undefined'
        date = requests.get(path)
        print(date.status_code)
        print('Done')
    for i in catID:
        Homepath='https://backend.shopnroar.com/products/category_Home/'+str(i)
        date = requests.get(Homepath)
        print(date.status_code)
        print('Done')
    li=['https://backend.shopnroar.com/products/todayTop3hotdeals?page=1','https://backend.shopnroar.com/products/GetAllCategories']
    for i in li:
        date = requests.get(i)
        print(date.status_code)
        print('Done')

# redisfunc()

# with connection.cursor() as cursor:
#     cursor.execute('SELECT "Cat_ID", "SNR_CatName","SNR_Cat_Image" FROM products_main_categories WHERE "SNR_SubCatName" IS NULL ORDER BY "SNR_CatName"')
#     temp = []
#     temp2 = []
#     # print cursor.fetchall()
#     for i in cursor.fetchall():
#
#         cursor.execute('SELECT "Cat_ID","SNR_SubCatName" FROM products_main_categories WHERE "SNR_CatName" = %s AND "SNR_TriCatName" IS NULL AND "SNR_SubCatName" IS NOT NULL order by "SNR_SubCatName"', [i[1]])
#
#         for j in cursor.fetchall():
#             temp2.append({'id': j[0]})
#
#         temp.append({'id':i[0],'Subid':temp2})
#         temp2=[]
#         print('j>',temp)
#     print('complete',temp)

def subcat():
    count=0
    a=[1, 111, 1239, 141, 166, 2092, 222, 412, 436, 469, 5181, 536, 537, 5605, 632, 772, 783, 8, 888, 922, 988]
    b=[{'id': 1, 'Subid': [{'id': 3237}, {'id': 2}]}, {'id': 166, 'Subid': [{'id': 1604}, {'id': 167}, {'id': 184}, {'id': 6551}, {'id': 6552}, {'id': 188}, {'id': 1933}, {'id': 187}]}, {'id': 8, 'Subid': [{'id': 499969}, {'id': 5710}, {'id': 5709}]}, {'id': 537, 'Subid': [{'id': 4678}, {'id': 5859}, {'id': 5252}, {'id': 540}, {'id': 2847}, {'id': 2764}, {'id': 4386}, {'id': 548}, {'id': 561}, {'id': 6952}, {'id': 6899}]}, {'id': 111, 'Subid': [{'id': 5863}, {'id': 112}, {'id': 7261}, {'id': 114}, {'id': 7497}, {'id': 2155}, {'id': 1813}, {'id': 135}, {'id': 1827}, {'id': 7240}, {'id': 1795}, {'id': 1475}, {'id': 5830}, {'id': 8025}, {'id': 500086}, {'id': 1556}, {'id': 1470}, {'id': 6987}, {'id': 2496}, {'id': 2187}, {'id': 4285}, {'id': 138}, {'id': 1624}, {'id': 976}, {'id': 2047}]}, {'id': 141, 'Subid': [{'id': 2096}, {'id': 142}, {'id': 156}, {'id': 39}]}, {'id': 222, 'Subid': [{'id': 3356}, {'id': 223}, {'id': 3702}, {'id': 262}, {'id': 1801}, {'id': 278}, {'id': 2082}, {'id': 3895}, {'id': 339}, {'id': 6544}, {'id': 340}, {'id': 342}, {'id': 345}, {'id': 912}, {'id': 500091}, {'id': 4488}, {'id': 386}, {'id': 1270}, {'id': 1294}]}, {'id': 412, 'Subid': [{'id': 413}, {'id': 422}, {'id': 435}]}, {'id': 436, 'Subid': [{'id': 554}, {'id': 6433}, {'id': 441}, {'id': 6356}, {'id': 442}, {'id': 7248}, {'id': 443}, {'id': 457}, {'id': 6345}, {'id': 6860}, {'id': 2786}, {'id': 450}, {'id': 6362}, {'id': 503765}, {'id': 458}, {'id': 4299}, {'id': 6963}, {'id': 6915}, {'id': 4163}, {'id': 464}, {'id': 8023}, {'id': 7212}, {'id': 460}, {'id': 6913}, {'id': 6392}]}, {'id': 632, 'Subid': [{'id': 503739}, {'id': 115}, {'id': 128}, {'id': 502975}, {'id': 2878}, {'id': 500096}, {'id': 499873}, {'id': 1974}, {'id': 133}, {'id': 127}, {'id': 499982}, {'id': 1910}, {'id': 3650}, {'id': 1167}]}, {'id': 469, 'Subid': [{'id': 491}, {'id': 5573}, {'id': 2915}]}, {'id': 536, 'Subid': [{'id': 574}, {'id': 359}, {'id': 696}, {'id': 5835}, {'id': 6792}, {'id': 2862}, {'id': 1679}, {'id': 3348}, {'id': 604}, {'id': 630}, {'id': 638}, {'id': 689}, {'id': 594}, {'id': 2956}, {'id': 4171}, {'id': 4358}, {'id': 985}, {'id': 729}, {'id': 600}, {'id': 6173}, {'id': 2639}]}, {'id': 5181, 'Subid': [{'id': 100}, {'id': 101}, {'id': 108}, {'id': 549}, {'id': 502974}, {'id': 103}, {'id': 104}, {'id': 105}, {'id': 110}, {'id': 106}, {'id': 5608}, {'id': 107}, {'id': 6553}]}, {'id': 772, 'Subid': [{'id': 773}, {'id': 780}]}, {'id': 783, 'Subid': [{'id': 784}, {'id': 499995}, {'id': 839}, {'id': 886}, {'id': 855}, {'id': 5037}, {'id': 887}]}, {'id': 922, 'Subid': [{'id': 6174}, {'id': 8078}, {'id': 923}, {'id': 932}, {'id': 5829}, {'id': 8499}, {'id': 2435}, {'id': 6373}, {'id': 6519}, {'id': 950}, {'id': 2986}, {'id': 2014}, {'id': 964}, {'id': 2636}]}, {'id': 5605, 'Subid': [{'id': 5606}, {'id': 97}, {'id': 5455}]}, {'id': 2092, 'Subid': [{'id': 313}, {'id': 5032}, {'id': 1279}]}, {'id': 988, 'Subid': [{'id': 499713}, {'id': 990}, {'id': 1001}, {'id': 1011}]}, {'id': 1239, 'Subid': [{'id': 3793}, {'id': 4648}, {'id': 1249}, {'id': 3867}, {'id': 1253}]}, {'id': 888, 'Subid': [{'id': 5613}, {'id': 5614}]}]
    for i in a:
        for d in b:
            print(d['id'])
            if i==d['id']:
                for k in d['Subid']:
                    print(k['id'])
                    count=count+1
                    print('>>>>',count)
                    # path = 'https://backend.shopnroar.com/products/categoryByID1/' + str(
                    #     d['id']) + '?count=40&low=undefined&high=undefined&brand=undefined&merchant=undefined&sub='+str(k['id'])+'&page=1&sort=undefined'
                    # date = requests.get(path)
                    # print(date.status_code)
                    # print('Done')


# a=DailyDeals.objects.filter(SNR_Active=False).distinct('SNR_Available')
# for i in a:
#     print(i.SNR_Available)

# x=cache.delete('getCategories')
# print(x)
# x=cache.keys('*')
# print(len(x))
# print(x)





# a=[["Missouri","ABOUT 6520-6530 Raytown Rd , Raytown, MO 64133  1,700 SF of Retail Space Available in Raytown, MO Raytown Missouri"],["Texas","ABOUT 9204 E Freeway Service Rd , Baytown, TX 77523  45 Acres of Commercial Land for Lease in Baytown, TX Baytown Texas"]]
# print(a)
# a.reverse()
# print(a)



# cats = []
# query_data = 'SELECT DISTINCT "SNR_Available" FROM products_active_dailydeals where "SNR_Active"=True AND "SNR_Available" IS NOT NULL ORDER BY "SNR_Available" ASC'
# with connection.cursor() as cursor:
#     cursor.execute(query_data)
#     for i in cursor.fetchall():
#         cats.append(i[0])
#
# print(cats)
#
#
# a=Active_DailyDeals.objects.filter(SNR_Available='T-Mobiles')
# print(a.count())


def updatelogo():
    a=Active_DailyDeals.objects.filter(SNR_Active=True).distinct('SNR_Available')
    for i in a:
        print(i.SNR_Available)
        if merchants.objects.filter(name=str(i.SNR_Available)).exists():
            print('in')
            res=merchants.objects.get(name=str(i.SNR_Available))
            res.active=True
            res.save()
            print('Done')

# updatelogo()


# obj =merchants(name='Straight Talk',image100px='https://storage.shopnroar.com/MerchantLogos/straight%20talk@100.png',image80px='https://storage.shopnroar.com/MerchantLogos/straight%20talk@80.png',image60px='https://storage.shopnroar.com/MerchantLogos/straight%20talk@60.png',image40px='https://storage.shopnroar.com/MerchantLogos/straight%20talk@40.png',image20px='https://storage.shopnroar.com/MerchantLogos/straight%20talk@20.png',prefer=59,active=True)
# obj.save()
# obj =merchants(name='Nike',image100px='https://storage.shopnroar.com/MerchantLogos/nike@100.png',image80px='https://storage.shopnroar.com/MerchantLogos/nike@80.png',image60px='https://storage.shopnroar.com/MerchantLogos/nike@60.png',image40px='https://storage.shopnroar.com/MerchantLogos/nike@40.png',image20px='https://storage.shopnroar.com/MerchantLogos/nike@20.png',prefer=58,active=True)
# obj.save()
# obj =merchants(name='Jet',image100px='https://storage.shopnroar.com/MerchantLogos/Jet@100.png',image80px='https://storage.shopnroar.com/MerchantLogos/Jet@80.png',image60px='https://storage.shopnroar.com/MerchantLogos/jet@60.png',image40px='https://storage.shopnroar.com/MerchantLogos/Jet@40.png',image20px='https://storage.shopnroar.com/MerchantLogos/Jet@20.png',prefer=57,active=True)
# obj.save()
# obj =merchants(name='hp',image100px='https://storage.shopnroar.com/MerchantLogos/hp@100.png',image80px='https://storage.shopnroar.com/MerchantLogos/hp@80.png',image60px='https://storage.shopnroar.com/MerchantLogos/hp@60.png',image40px='https://storage.shopnroar.com/MerchantLogos/hp@40.png',image20px='https://storage.shopnroar.com/MerchantLogos/hp.png',prefer=56,active=True)
# obj.save()
# obj =merchants(name='FINISH LINE',image100px='https://storage.shopnroar.com/MerchantLogos/finish%20line@100.png',image80px='https://storage.shopnroar.com/MerchantLogos/finish%20line@80.png',image60px='https://storage.shopnroar.com/MerchantLogos/finish%20line@60.png',image40px='https://storage.shopnroar.com/MerchantLogos/finish%20line@40.png',image20px='https://storage.shopnroar.com/MerchantLogos/finish%20line@20.png',prefer=55,active=True)
# obj.save()
# obj =merchants(name='chewy',image100px='https://storage.shopnroar.com/MerchantLogos/chewy@100.png',image80px='https://storage.shopnroar.com/MerchantLogos/chewy@80.png',image60px='https://storage.shopnroar.com/MerchantLogos/chewy@60.png',image40px='https://storage.shopnroar.com/MerchantLogos/chewy@40.png',image20px='https://storage.shopnroar.com/MerchantLogos/chewy@20.png',prefer=54,active=True)
# obj.save()
# obj=merchants(name='Straight Talk')
# obj.save()
# obj=merchants(name='Nike')
# obj.save()
# obj=merchants(name='Jet')
# obj.save()
# obj=merchants(name='hp')
# obj.save()
# obj=merchants(name='FINISH LINE')
# obj.save()
# obj=merchants(name='chewy')
# obj.save()


# a=merchants.objects.filter(name="SUMSUNG").update(name="SAMSUNG")
# a=merchants.objects.get(name='OReilly AUTOPARTS')
# print(a.image40px)
# a.image20px='https://storage.shopnroar.com/MerchantLogos/OReillyAUTOPARTS@20.png'
# a.image40px='https://storage.shopnroar.com/MerchantLogos/OReillyAUTOPARTS@40.png'
# a.image60px='https://storage.shopnroar.com/MerchantLogos/OReillyAUTOPARTS@60.png'
# a.image80px='https://storage.shopnroar.com/MerchantLogos/OReillyAUTOPARTS@80.png'
# a.image100px='https://storage.shopnroar.com/MerchantLogos/OReillyAUTOPARTS@100.png'
# a.save()
import requests

# url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/matches.php"
#
# querystring = {"completedlimit":"7","inprogresslimit":"7","upcomingLimit":"7"}
#
# headers = {
#     'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com",
#     'x-rapidapi-key': "51ce25beb5msh045d260b81d40afp1ce059jsnc01b9034e53f"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

# print(Active_DailyDeals.objects.filter(SNR_Available='Amazon',SNR_Active=True).count())

# a=merchants.objects.get(name='Amazon')
# print(a.active)

# a=AllProductsPartition.objects.get(id=423280)
# print(a)



# cache.delete('Hot_DealsAmazonundefineundefineundefine-1-140')
# Hot_DealsAmazonundefineundefineundefine-1-140
# Hot_DealsAmazonundefineundefineundefine-1-140
# a=cache.keys('*')
# print(len(a))
# print(a)
# print(Active_DailyDeals.objects.filter(SNR_Active=True, SNR_Available=str('Costco')).count())


# a=merchants.objects.all()
# for i in a:
#     print(i.name)

# a=Active_DailyDeals.objects.filter(SNR_Available='BHPHOTOVIDEO',SNR_Active=True)
# print(a.count())
# import datetime
# print(datetime.datetime.now())
# # main_data_query = 'Select * from public.products_allproducts where "SNR_CatID"=166  OFFSET ' + str(0) + ' LIMIT ' + str(40)
# main_data_query = 'Select * from public.products_allproductspartition where "SNR_CatID"=222  OFFSET ' + str(0) + ' LIMIT ' + str(40)
# main_data_query = 'Select distinct(\'SNR_Available\') from public.products_active_dailydeals where "SNR_Active"=True '
# with connection.cursor() as cursor:
#     cursor.execute(main_data_query)
#     print(cursor.fetchall())
# #
# print(datetime.datetime.now())


def remove_Dulpicate_Record(merchant):
    print('in')
    # data = Active_DailyDeals.objects.filter(SNR_Active=True,SNR_Available=str(merchants)).values('SNR_ProductURL','SNR_Title').annotate(property_l=Count('SNR_ProductURL')).filter(property_l__gt=1)
    data=Active_DailyDeals.objects.all().values('SNR_ProductURL','SNR_Title','SNR_Available').annotate(Count('id')).order_by().filter(id__count__gt=1)
    data=data.filter(SNR_Active=True,SNR_Available=str(merchant))
    print(data)
    print(len(data))
    for saidata in data:
        print(saidata)
        xyz = Active_DailyDeals.objects.filter(SNR_Title=saidata['SNR_Title'])
        umer = 1
        for data in xyz:
            if umer == 1:
                pass
            else:
                print('lll')
                data.delete()
            umer += 1

# remove_Dulpicate_Record('BHPHOTOVIDEO')

# print(Active_DailyDeals.objects.filter(SNR_Title='OTTERBOXOtterBox Defender Series Case and Holster - iPhone 7 Plus/8 Plus').count())
# print(Active_DailyDeals.objects.filter(SNR_Available='Target',SNR_Active=False).count())
'mophie 20,100mAh Encore Plus 20K Portable Power Bank with Built-In USB Type-C & Micro-USB Cables'
# main_data_query = 'Select "SNR_Title" from public.products_allproductspartition  where  public.products_allproductspartition."tsv_title" @@ plainto_tsquery(\'power bank\') limit 10'
# main_data_query = 'select * from products_active_dailydeals where "SNR_Available"=\'Beallsflorida\' order by "id" DESC limit 10'
# with connection.cursor() as cursor:
#     cursor.execute(main_data_query)
#     a=cursor.fetchall()
#     print(a)
#     if not a:
#         main_data_query = 'Select "SNR_Title" from public.products_active_dailydeals  where  "tsv_title" @@ plainto_tsquery(\'Instant Pot Duo SV 6qt Multi-Use Pressure Cooker\') limit 10'
#         with connection.cursor() as cursor:
#             cursor.execute(main_data_query)
#             a = cursor.fetchall()
#             print(a)
#         print('ok')

# cache.delete('Hot_Deals'+str('Amazon')+'undefineundefineundefine-1-140')
# cache.delete('Home_page_Backup')
# print(Active_DailyDeals.objects.filter(SNR_Available='Kay').count())
# print(Active_DailyDeals.objects.filter(SNR_Active=True).count())
# print(AllProductsCoupons.objects.all().update(SNR_Active=True))

# merchants.objects.filter(name='OldNavy').update(name='Old Navy')


# Active_DailyDeals.objects.filter(SNR_Available='Verizon').update(SNR_Available='verizon')

# cache.delete('Merchant_Logos_Home')

#
# a=AllProductsCoupons.objects.filter(SNR_Active=True).distinct('SNR_Available')
# for i in a:
#     print(i.SNR_Available)
#     if merchants.objects.filter(name=i.SNR_Available).exists():
#         n=merchants.objects.get(name=i.SNR_Available)
#         obj =merchantscoupons(name=i.SNR_Available,image20px=n.image20px,image40px=n.image40px,image60px=n.image60px,image80px=n.image80px,image100px=n.image100px,count=str(AllProductsCoupons.objects.filter(SNR_Available=i.SNR_Available,SNR_Active=True).count()),active=True)
#         obj.save()



# merchantscoupons.objects.all().delete()
# merchantscoupons.objects.filter(name='OfficeSupply').update(name='officesupply')
# a=merchantscoupons.objects.get(name='officesupply')
# a.count=str(AllProductsCoupons.objects.filter(SNR_Available='officesupply',SNR_Active=True).count())
# a.active=True
# a.save()

# print(AllProducts.objects.filter(SNR_Available='target').count())

# a=AllProductsPartition.objects.filter(SNR_Title__search='Moderna Portable Hanging Spiral Feeder Birds Parrot Pet Food Fruit Holder Climb Play Toy')
# print(a.count())
# print(Active_DailyDeals.objects.filter(SNR_Available='Walgreens',SNR_Active=True).count())
# from SNR.settings import *
# client = hazelcast.HazelcastClient(config)
# my_map = client.get_map("map-name").blocking()
# my_map.remove('Home_Page')
# def newlewi():
#     my_map.remove('Hot_DealsWalgreensundefineundefineundefine-1-1401')
#     path = 'https://backend.shopnroar.com/products/filterVendorDeals_test/Walgreens/40/'
#     st = requests.post(path, json={"cat": "undefine", "minprice": -1, "maxprice": -1, "sort": "undefine",
#                                    "search": "undefine"})
#     print(st.status_code)
#
# newlewi()

# print(AllProductsCoupons.objects.all()[:1])
# word = 'shoes'
# url = 'https://www.walmart.com/search/?query=jug'
# source = requests.get(url)
# plain_text = source.text
# soup = BeautifulSoup(plain_text, "html.parser")
#
# print(soup)

# def get_request(sitelink):
#     try:
#         page_source=requests.get(sitelink)
#         if page_source.status_code==200:
#             soup=BeautifulSoup(page_source.text,'html.parser')
#             return soup
#         else:
#             print("site not loaded")
#     except:
#         pass

def Amazon():
    word = 'shoes'
    url = 'https://www.amazon.com/s?k=' + str(word) + '&ref=nb_sb_noss_2'
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, "html.parser")
    print(soup)
    # for maindiv in soup.find_all('div',{'class':'a-section a-spacing-medium'}):
    #     print(maindiv)
        # try:
        #     tit=maindiv.find('span',{'class':'a-size-base-plus'})
        #     title=tit.text
        #     print(title)
        # except:
        #     pass
        # try:
        #     img = maindiv.find('picture', {'class': 's-aspect-ratio-flex-container'})
        #     images=img.find('img')
        #     pics=images['src']
        #     print(pics)
        #
        # except:
        #     pass
        # try:
        #     rate = maindiv.find('span', {'class': 'a-price'})
        #     price=rate.text.split('$')[1]
        #     print(price)
        #     befor=maindiv.find('span', {'class': 'a-price a-text-price'})
        #     beforprice = befor.text.split('$')[1]
        #     print(beforprice)
        # except:
        #     pass
        # # try:
        # #     ho = requests.find_element_by_css_selector("#search > div.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.s-right-column.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-result-list.s-search-results.sg-row > div:nth-child(1) > div > span > div > div > div:nth-child(2) > div:nth-child(3) > div > div.a-section.a-spacing-none.a-spacing-top-micro > div > span:nth-child(1) > span > a > i.a-icon.a-icon-popover")
        # #     hover = ActionChains(requests).move_to_element(ho)
        # #     hover.perform()
        # #     time.sleep(2)
        # #     soup2 = BeautifulSoup(requests.page_source, "html.parser")
        # #     popup = soup2.find('div', {'class': 'rating_2y4eNoU6rFkAxupboWxNzj'})
        # #     span = popup.find('span')
        # #     Review = span.text.split(' out')[0]
        # #     print(Review)
        # # except:
        # #     pass

# Amazon()


# a=User(username='Coupon',password='Admin')
# from newdb.models import *
# # print(AllProductsCoupons.objects.using('newdb').count())
# obj=AllProductsCoupons(SNR_Title='',SNR_Description='',SNR_Available='',SNR_CouponCode_url='abc101',SNR_Expire='2019-10-19')
# obj.save(using='newdb')


# print(merchants.objects.using('default').all())
# print(merchants.objects.using('default').all())
# print(Active_DailyDeals.objects.filter(SNR_Available='AEROPOSTALE',SNR_Active=False).update(SNR_Active=True))
# from django.template.loader import get_template
# from django.core.mail import EmailMessage
#
# key={
# 'fname':'Rizwan'
# }
# message = get_template('contact_us.html').render(key)
# email = EmailMessage('SHOPnROAR Contact Us Mail ', message, to=['rizwan.khan@brainplow.com'])
# email.content_subtype = 'html'
# email.send()

# print(Active_DailyDeals.objects.filter(SNR_Available='Wallgreens',SNR_Active=True).count())
# a=merchants.objects.all()
# for i in a :
#     print(i.name)


# print(AllProducts.objects.using('newdb').filter(SNR_Available='KOHL\'S').delete())

# print(Active_DailyDeals.objects.filter(SNR_Available='AMERICAN EAGLE').values())
# obj=merchants(name='Straight Talk')
# obj.save()
# obj=merchants(name='Nike')
# obj.save()
# obj=merchants(name='Jet')
# obj.save()
# obj=merchants(name='hp')
# obj.save()
# obj=merchants(name='FINISH LINE')
# obj.save()
# obj=merchants(name='chewy')
# obj.save()

# print(Active_DailyDeals.objects.count())
#
# import time
# lines = []
# count=0
# with open("/home/hamza/Downloads/UPC codes") as fp:
#     # for i in fp:
#     a=fp.readlines()
#     for i in a:
#         print(i)
#         url = 'https://api.upcitemdb.com/prod/trial/lookup?upc=' + str(i.strip())
#         re = requests.get(url)
#         print(re.status_code)
#         count=count+1
#         print('>>>>>',count)
#         time.sleep(2)


# a=Active_DailyDeals.objects.filter(SNR_Active=True,SNR_Customer_Rating=0).update(SNR_Customer_Rating=3.5)
# print(a.count())


def updatewaltmart_iamges():
    try:
        # li=[1, 8, 111, 141, 166, 222, 412, 436, 469, 536, 537, 632, 772, 783, 888, 922, 988, 1239, 2092, 5181, 5605]
        li=[1]
        temp=[]
        for ii in li:
            main_data_query = 'Select {0} from public.products_allproducts_'+str(ii)+' where "SNR_CustomerReviews"=0'
            fields = [
                  "id","SNR_CustomerReviews"
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

                data='Update public.products_allproducts_'+str(ii)+' set "SNR_CustomerReviews"=3.5 where id=\''+str(k['id'])+'\''
                with connection.cursor() as cursor:
                    cursor.execute(data)
                print('done')
    except:
        print('something went wrong')

# updatewaltmart_iamges()

# a=AllProducts.objects.filter(SNR_Available='Amazon').distinct('SNR_Category')
# for i in a:
#     print(i.SNR_Category)
#     with open("/home/hamza/Desktop/cat","w") as fp:
#         fp.write(str(i.SNR_Category)+"\n")


# Active_Vocation.objects.filter(SNR_Customer_Rating=-1.0).update(SNR_Customer_Rating=3.5)
# a=Active_Vocation.objects.distinct('SNR_Available')
# for i in a:
#     print(i.SNR_Available)

# all_objs = AllProducts.objects.filter(SNR_Description_Mobile=None).exclude(SNR_Available='ebay')[0:100000]
# for i in all_objs:
#     print(i.SNR_Description_Mobile)
#     soup = BeautifulSoup(i.SNR_Description, u'html.parser')
#     mobile_des = soup.text.strip()  # Decription clean function call return clean description
#     i.SNR_Description_Mobile = mobile_des
#     i.SNR_isShow = False
#     i.SNR_CatID = 0
#     i.SNR_MainCatID = 0
#     i.SNR_SubCatID = 0
#     i.save()
#     print('UpdataDescription')



# a=Active_DailyDeals.objects.filter(SNR_Customer_Rating=-1.00).update(SNR_Customer_Rating=3.5)
# print(a.count())
# a=AllProducts.objects.get(id=85450888)
# print(a.SNR_Description_Mobile)


# all_objs=AllProducts.objects.filter(SNR_Description_Mobile=None).exclude(SNR_Available='ebay').exclude(SNR_Description=None).values('SNR_Description','SNR_Description_Mobile','SNR_Available')[0:2]
# print(all_objs)



# que='shoes'
# # url='https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywordsResponse&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ZeeShan-Dhaar-PRD-f38876c40-7ef67ffa&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=nike%20shoes&paginationInput.entriesPerPage=2'
# url='https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ZeeShan-Dhaar-PRD-f38876c40-7ef67ffa&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords='+str(que)+'&paginationInput.entriesPerPage=2'
# re=requests.get(url)
# main=re.json()
# # print(main)
# li=[]
# count=0
# for i in main['findItemsByKeywordsResponse']:
#     # print(i['searchResult'])
#     for j in i['searchResult']:
#         print(j)
#         for k in j['item']:
#             print(k)
#             # for m in k['convertedCurrentPrice']:
#             #     price=m['__value__']
#             dic={
#                 'index':count,
#                 'SNR_Title': k['title'][0],
#                 'SNR_Available':'ebay',
#                 'SNR_ProductURL':k['viewItemURL'][0],
#                 'SNR_ImageURL':k['galleryURL'][0],
#                 'SNR_Description':'None',
#                 # 'SNR_Price':price,
#                 'SNR_PriceBefore':'0.00',
#                 'SNR_CustomerReviews':'3.50'
#             }
#             count = count + 1
#             li.append(dic)
#
# print('final>>',li)

# import matplotlib.pyplot as plt
#
# # x axis values
# x = [1, 2, 3]
# # corresponding y axis values
# y = [2, 4, 1]
#
# # plotting the points
# plt.plot(x, y)
#
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#
# # giving a title to my graph
# plt.title('My first graph!')

# # function to show the plot
# plt.show()

# from SNR import settings

# print(settings.DATABASES['old']['ENGINE']) # postgresql

# class TestModel(Model):
#     age = IntegerField(default=1)

# # Insert 10 rows
# for i in range(10):
#     TestModel().save()


# print(db_name)

# import django.conf as conf


# a=AllProducts.objects.using('default').all().values()[:2]
# print(a)


# a=AllProducts.objects.using('old').filter(SNR_Available='Amazon').values('id')[20000001:20000008]
# print(a)



# import csv
#
# with open('/home/hamza/Downloads/decision_tree/test', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped if line)
#     with open('/home/hamza/Downloads/decision_tree/log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(('title', 'intro'))
#         writer.writerows(lines)


# print(Active_DailyDeals.objects.filter(SNR_Available='Overstock').count())
keyword="Maldives:Three-Night Getawa y with 4* or 5* Hotel Accommodation, Breakfast, Airport Transfers and Option for Flights*"
type='Vocations'
try:
            page = 1#int(request.GET.get('page'))
            if page < 1:
                page = 1
except:
            page = 1
print(page)
limit = page * int(18)
offset = (page - 1) * int(10)
if type=='Coupon':

    ls = ' "SNR_Active"=\'' + str(True) + '\''
    # ls = ''
    data='select count(*) from public."products_allproductscoupons" where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'+ 'And' + str(
                        ls) + ' LIMIT ' + str(10) + ' OFFSET ' + str(offset);
    with connection.cursor() as cursor:
        cursor.execute(data)
        res = cursor.fetchall()
        print(res)
elif type=='Coupons':

    print("Similarity")
    results =AllProductsCoupons.objects.annotate(
        similarity=TrigramSimilarity('SNR_Available', keyword)+TrigramSimilarity('SNR_Title', keyword) + TrigramSimilarity('SNR_Description', keyword)).filter(similarity__gte=0.3,SNR_Active=True).order_by("-similarity")[:800]
    print(len(results))
elif type=='Vocation':
    ls = ' "SNR_Active"=\'' + str(True) + '\''
    # ls = ''
    data = 'select count(*) from public.products_active_vocation where "tsv_Search_full"@@plainto_tsquery(\'' + keyword + '\')'
    with connection.cursor() as cursor:
        cursor.execute(data)
        res = cursor.fetchall()
        print(res)
elif type == 'Vocations':

    print("Similarity")
    results = Active_Vocation.objects.annotate(
        similarity=TrigramSimilarity('SNR_Available', keyword) + TrigramSimilarity('SNR_Title',
                                                                                   keyword) + TrigramSimilarity(
            'SNR_Description', keyword)).filter(similarity__gte=0.3, SNR_Active=True).order_by("-similarity")[:800]
    print(len(results))

# a= AllProducts.objects.filter(SNR_Available='ebay')
