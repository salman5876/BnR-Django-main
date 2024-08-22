import sys, os
import traceback
from datetime import datetime
from django.db.models import Sum
from elasticsearch import NotFoundError
from gatherproxy import count

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
# PROJECT_ROOT = BASE_DIR.split('MudassirCode')[0]
# # PROJECT_ROOT PROJECT_ROOT= Path(__file__).parent.parent
# print('PROJECT_ROOT:  ',PROJECT_ROOT)
# sys.path.append(PROJECT_ROOT)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import *
from django.db.models import Q
from categories.models import CategoriesBrandNames
from django.db.models import Count

def query_testing():
    try:
        id = 49286171
        data = AllProducts.objects.using('newdb').get(id=id)
        # data = Active_DailyDeals.objects.get(id=id)
        print(data)
        print(data.values())
    except AllProducts.DoesNotExist as e:
        print(e)


def allProductsQuery():
    start_index = 847300
    end_index = 9075000
    all_products = AllProducts.objects.using("newdb").exclude(
        SNR_Title__isnull=True,
        SNR_Title="00",
        SNR_Category__isnull=True,
        SNR_Category="00",
        SNR_ImageURL__isnull=True,
        SNR_ImageURL="00",
        SNR_isShow=True,
    # ).order_by('id')[start_index:end_index]
    ).order_by('id')
    print('Prod Count: ', all_products.count())


def insertBrandsNameFromAllproductstable():
    # brand_names = AllProducts.objects.using('newdb').exclude(SNR_Brand__in = exclude_list).values_list('SNR_Brand', flat=True).distinct()
    # brand_names = AllProducts.objects.using('newdb').values_list('SNR_Brand', flat=True).distinct()

    # brand_names = AllProducts.objects.values('SNR_Brand').annotate(count=Count('SNR_Brand')).distinct()

    exclude_list = ['Total','00', 'No Brand', 'Does not apply', 'Not Available', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=ACCUFLEX+TANTRUM','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Unknown', 's/ref=w_bl_sl_s_ap_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=ONSQLIDFLR', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=LUXMO+PREMIUM',
                    's/ref=w_bl_sl_s_sh_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=Pollyhb%27s+Backpack','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=PHYSN','',]
    # brand_names = AllProducts.objects.values('SNR_Brand').exclude(
    #         Q(SNR_Brand__in=exclude_list) | Q(SNR_Brand__isnull= True) | Q(SNR_Brand=None)
    # ).annotate(count=Count('SNR_Brand')).order_by('-count')
    brand_names = AllProducts.objects.using('newdb').values('SNR_Brand').annotate(count=Count('SNR_Brand')).order_by('-count')
    # brand_names = AllProducts.objects.values('SNR_Brand').distinct()
    print(brand_names)
    print(brand_names.count())
    c = 1
    for brand in brand_names[1000:5000]:
        brand_name = brand['SNR_Brand']
        if brand_name in brand_names:
            print('pass')
        bcount = brand['count']
        obj = CategoriesBrandNames.objects.create(brand_name=brand_name, products_count=bcount)
        print(obj)
        print("Insert: ", c)
        print('--------------------------------')

def getBrandNames():
    exclude_list = ['','Total','00', 'NO BRAND','No Brand','Does Not Apply', 'Does not apply', 'Not Available','Unbranded','Unknown','Unknown','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Unknown','0.0','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=EbuyChX','PackagingSuppliesByMail','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Aexit','NA','na','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=eDealMax','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Sukvas','N/A','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=CUSHY','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=NA','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=The+Art+of+Service', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Baosity','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=GRAPHICS+%26+MORE','s/ref=w_bl_sl_s_je_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=BRK+Studio','Ship Now Supply', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Exam+Edge%2C+LLC', 's/ref=w_bl_sl_s_je_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=GRAPHICS+%26+MORE', 's/ref=w_bl_sl_s_je_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=LooPoP', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=verde+powersports', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=B+Blesiya', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Modula+Racks', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=DealMux', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=FFMMdog','s/ref=w_bl_sl_s_je_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=TG+Graphics','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Rhino+Rack+Roof+Racks','s/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Ochoos', 's/ref=w_bl_sl_s_ap_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=TCK+Socks', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=YIXKC', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Flameer', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Ambesonne', 's/ref=w_bl_sl_s_ap_web_7141123011?ie=UTF8&node=7141123011&field-brandtextbin=Kidhome', 's/ref=bl_dp_s_web_0?ie=UTF8&search-alias=aps&field-keywords=Kasuki', ]
    exclude_list = [name.strip() for name in exclude_list]
    # specific_letters = ['s/ref',]
    res = CategoriesBrandNames.objects.exclude(
        Q(brand_name__in=exclude_list) |
        Q(brand_name__isnull= True) |
        Q(brand_name=None) |
        Q(brand_name__startswith='s/ref') |
        Q(brand_name__exact='')
    # ).values('brand_name').annotate(count=Count('brand_name')).order_by('-count')
    # ).values_list('brand_name', flat=True).annotate(count=Count('brand_name')).order_by('-count')
    ).values('id','brand_name') #.order_by('-products_count')
    # x = CategoriesBrandNames.objects.all()
    print(res.count())
    print(res)

def getBesetBuydata():
    all_products = AllProducts.objects.using("newdb").exclude(
        Q(SNR_Title__isnull=True) |
        Q(SNR_Title="00") |
        Q(SNR_Category__isnull=True) |
        Q(SNR_Category="00") |
        Q(SNR_ImageURL__isnull=True) |
        Q(SNR_ImageURL="00") |
        Q(SNR_isShow=False) |
        Q(Q(SNR_Available='BestBuy') | Q(SNR_Available='BEST BUY'))
    # ).order_by('id')
    ).values_list('SNR_Available',flat=True).distinct()
    print(all_products.count())
    for product in all_products:
        print(product)
    # print(all_products)



if __name__ == '__main__':
    import time
    s = time.time()
    # allProductsQuery()
    # allProductsQuery()
    # query_testing()
    # insertBrandsNameFromAllproductstable()
    # getBrandNames()
    # x = CategoriesBrandNames.objects.all()
    # for i in x:
    #     print(i.)
    # print(count)
    # obj = CategoriesBrandNames.objects.create(brand_name='nike', products_count=10)
    # print(obj)

    getBesetBuydata()

    # brand_names = AllProducts.objects.using('newdb').values_list('SNR_Brand',flat=True).distinct()
    # brand_names = AllProducts.objects.using('newdb').values_list('SNR_Available',flat=True).distinct()
    # print(brand_names)
    e = time.time()
    print(e-s)
