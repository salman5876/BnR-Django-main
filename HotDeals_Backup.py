import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from django.db import connection
import requests
from products.models import *
from django.core.cache import cache
import datetime



def scrt():
    a=merchants.objects.filter(active=True).exclude(name='Sam\'s Club').exclude(name='Lowe\'s')
    for i in a:
        try:
            cache.delete('Hot_Deals_backup'+str(i.name)+'undefineundefineundefine-1-1401')
            path = 'https://backend.shopnroar.com/products/filterVendorDeals_test_backup/'+str(i.name)+'/40/'
            print(path)
            st = requests.post(path, json={"cat": "undefine", "minprice": -1, "maxprice": -1, "sort": "undefine",
                                           "search": "undefine"})
            print(st.status_code)
        except:
            print('something wrong')

scrt()


def newsam():
        cache.delete('Hot_Deals_backupSam\'s Clubundefineundefineundefine-1-1401')
        path='https://backend.shopnroar.com/products/filterVendorDeals_test_backup/Sam\'s Club/40/'
        st=requests.post(path,json={"cat":"undefine","minprice":-1,"maxprice":-1,"sort":"undefine","search":"undefine"})
        print(st.status_code)
newsam()


def newlewi():
    cache.delete('Hot_Deals_backupLowe\'sundefineundefineundefine-1-1401')
    path = 'https://backend.shopnroar.com/products/filterVendorDeals_test_backup/Lowe\'s/40/'
    st = requests.post(path, json={"cat": "undefine", "minprice": -1, "maxprice": -1, "sort": "undefine",
                                   "search": "undefine"})
    print(st.status_code)

newlewi()
print('---------------------------------------')
print(datetime.datetime.now())
print('---------------------------------------')
