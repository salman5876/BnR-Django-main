from datetime import datetime
import traceback
from bs4 import BeautifulSoup
import  requests
import re
import math
import sys
# sys.path.append('/home/brainplow/Documents/shopnroar_amazon')
sys.path.append('/amazon/shopnroar_amazon/')
import os, django
from selenium.webdriver.common.keys import Keys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import EbayIndividualURLs, DailyDeals, AllProducts
from products.serializers import DailyDeals_Serializer, Active_DailyDeals
import time
from multiprocessing.pool import ThreadPool
from selenium import webdriver
import  json
from urllib.parse import urljoin
from selenium.webdriver.chrome.options import Options


# def tempfunc():
#
#     all_objs = Active_DailyDeals.objects.filter(SNR_Active=None, SNR_Available='BEST BUY')
#     print(all_objs.count())
#     pool = ThreadPool(50)
#     pool.map(multiproces, all_objs)
#     pool.close()
#     pool.join()
#     print('Done All Pool')
def DesciptionScript(all_objs):
    # all_objs = AllProducts.objects.filter(SNR_Description_Mobile=None).exclude(SNR_Available='ebay').exclude(
    #     SNR_Description=None)[0:100000]
    # print(all_objs)
    for i in all_objs:
        try:
            print(i.id)
            soup = BeautifulSoup(i.SNR_Description, u'html.parser')
            mobile_des = soup.text.strip()  # Decription clean function call return clean description
            i.SNR_Description_Mobile = mobile_des
            i.SNR_isShow = False
            i.SNR_CatID = 0
            i.SNR_MainCatID = 0
            i.SNR_SubCatID = 0
            i.save()
            print('UpdataDescription')
        except:
            pass

def description_tag_remove_update_all_products_table(previous,current):
    print('chunk start:',datetime.now())
    chunksList=[]
    all_objs = AllProducts.objects.filter(SNR_Description_Mobile=None).exclude(SNR_Available='ebay').exclude(SNR_Description=None)[previous:current]
    # print(all_objs)
    # for i in all_objs:
    #     try:
    #         print(i.SNR_Title)
    #         soup = BeautifulSoup(i.SNR_Description, u'html.parser')
    #         mobile_des = soup.text.strip()  # Decription clean function call return clean description
    #         i.SNR_Description_Mobile = mobile_des
    #         i.SNR_isShow = False
    #         i.SNR_CatID = 0
    #         i.SNR_MainCatID = 0
    #         i.SNR_SubCatID = 0
    #         i.save()
    #         print('UpdataDescription')
    #     except:
    #         pass
    # DesciptionScript(all_objs)
    # print('Lenght Description Tag',all_objs.count())
    for i in range(0,100000, 5000):
        chunk = all_objs[i:i + 5000]
        print('1')
        chunksList.append(chunk)
    print('Done Chunk')
    print('chunk end:',datetime.now())
    pool = ThreadPool(10)
    pool.map(DesciptionScript, chunksList)
    pool.close()
    pool.join()
    print('Done All Description')

def multiprocessWalmartImages(all_objs):

    # images=all_objs.SNR_ImageURL.split(',')
    # images_list=[]
    for img in all_objs:
        image=img.SNR_ImageURL.replace("Height=180&odnWidth=180", "Height=500&odnWidth=500")
        # image=img.replace("_100", "_800")
        # images_list.append(image)
        # print(images_list)
        img.SNR_ImageURL = image
        print(img.id)
        img.save()
        print('ImageUpdate')

def Walmart_image_update(previous,current):
    all_objs=AllProducts.objects.filter(SNR_Available='Walmart',SNR_ImageURL__icontains='Height=180&odnWidth=180')[previous:current]#Limit apply for Testing
    chunksList=[]
    # print('Lenght Walmart Images', all_objs.count())
    for i in range(0,200000, 5000):
        chunk = all_objs[i:i + 5000]
        chunksList.append(chunk)
    pool = ThreadPool(10)
    pool.map(multiprocessWalmartImages, chunksList)
    pool.close()
    pool.join()
    print('Done All Images')



def deals_scriptupdation():
    all_objs=Active_DailyDeals.objects.filter(SNR_Available='KAY')#Limit apply for Testing

    print('Lenght  Images', all_objs.count())
    pool = ThreadPool(100)
    pool.map(multiprocessWalmartImages, all_objs)
    pool.close()
    pool.join()
    print('Done All Images')
def desciption_call():
    # print('start')
    # pre = 1000000
    # chunksList=[1000000,1200000,1300000,1400000,1500000,1600000,1700000,1800000,1900000,2000000]
    # for i in chunksList:
        # cur=pre+i
    Walmart_image_update(0,200000)
        # pre=pre+100000



    # chunksList = [100000,200000]
    # # for i in range(0, len(all_links), 12):
    # #     chunk = all_links[i:i + 12]
    # #     chunksList.append(chunk)

    # all_objs = AllProducts.objects.all().exclude(SNR_Available='ebay')
    # print(all_objs.count())
    # x=math.ceil(all_objs.count()/1000000)

    # previous=0
    # for i in range(1,281):
    #     current=i*1000000
    #     yy='pre:{0},cur:{1}'.format(previous,current)
    #     print(yy)
    #     print('main start:',datetime.now())
    #                       # For Description
    #     print('Start Description Tag')
    #     description_tag_remove_update_all_products_table(previous,current)
    #     print('End Description Tag')
    #     print('main end:',datetime.now())
    #     previous=current
    #     f = open("description.txt", "a+")
    #     f.write(yy + '\n')
    # print('End')

from django.db import connection
def anc(temp):
    for k in temp:
        print('id', k['id'])
        try:
            soup = BeautifulSoup(str(k['SNR_Description']), u'html.parser')
            mobile_des = soup.text.strip()  # Decription clean function call return clean description
            SNR_Description_Mobile = mobile_des
            SNR_Description_Mobile = [re.sub(r"[^a-zA-Z0-9-]+", ' ', k) for k in SNR_Description_Mobile.split("\n")]
            print(SNR_Description_Mobile)
            data = 'Update public.products_allproducts set "SNR_Description_Mobile"=\'' + str(
                SNR_Description_Mobile[0]) + '\' where id=\'' + str(k['id']) + '\''
            with connection.cursor() as cursor:
                cursor.execute(data)
            print('done')
        except:
            print('>>>')

def updatewaltmart_iamges11():
    try:
        temp=[]
        main_data_query = 'Select {0} from public.products_allproducts where "SNR_Description_Mobile" is null and "SNR_Description" is not null and "SNR_Available" !=\'ebay\' limit 5000'
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
        for i in range(0,50000, 50):
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

    except:
        print('something went wrong')



if __name__ == '__main__':
    # all_objs = AllProducts.objects.filter(SNR_Available='Walmart')
    # print(all_objs.count())
    print('done')
    # updatewaltmart_iamges11()
                     #For Images
    desciption_call()
    # all_objs = AllProducts.objects.filter(SNR_Description_Mobile=None).exclude(SNR_Available='ebay')
    # print(all_objs.count())






    # # previous=0
    # for i in range(1,6):
    #     current=i*500000
    #     yy='pre:{0},cur:{1}'.format(previous,current)
    #     print(yy)
    #     print('main start:',datetime.now())
    #                       # For Description
    #     # print('Start W Tag')
    #
    #     print('Start walmart images')
    #     Walmart_image_update(previous,current)
    #     print('End Walmart Images')
    #     previous=current
    #
    #     f = open("walmart.txt", "a+")
    #     f.write(yy + '\n')



    # deals_scriptupdation()
