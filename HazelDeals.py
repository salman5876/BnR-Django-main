import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from django.db import connection
import requests
from products.models import *
from django.core.cache import cache
from SNR.settings import *


my_map = client.get_map("Deal").blocking()
my_map.clear()




def scrt():
    a=merchants.objects.filter(active=True).exclude(name='Sam\'s Club').exclude(name='Lowe\'s')
    for i in a:
        try:
            # my_map.remove('Hot_Deals'+str(i.name)+'undefineundefineundefine-1-1401')
            path = 'http://127.0.0.1:8000/products/filterVendorDeals_test/'+str(i.name)+'/40/'
            print(path)
            st = requests.post(path, json={"cat": "undefine", "minprice": -1, "maxprice": -1, "sort": "undefine",
                                           "search": "undefine"})
            print(st.status_code)
        except:
            print('something wrong')

scrt()


def newsam():
    # my_map.remove('Hot_DealsSam\'s Clubundefineundefineundefine-1-1401')
    path='https://backend.shopnroar.com/products/filterVendorDeals_test/Sam\'s Club/40/'
    st=requests.post(path,json={"cat":"undefine","minprice":-1,"maxprice":-1,"sort":"undefine","search":"undefine"})
    print(st.status_code)
newsam()


def newlewi():
    # my_map.remove('Hot_DealsLowe\'sundefineundefineundefine-1-1401')
    path = 'https://backend.shopnroar.com/products/filterVendorDeals_test/Lowe\'s/40/'
    st = requests.post(path, json={"cat": "undefine", "minprice": -1, "maxprice": -1, "sort": "undefine",
                                   "search": "undefine"})
    print(st.status_code)

def newebay():
    # my_map.remove('Hot_DealsLowe\'sundefineundefineundefine-1-1401')
    path = 'http://127.0.0.1:8000/products/filterVendorDeals_test/ebay/40/'
    st = requests.post(path, json={"cat": "undefine", "minprice": -1, "maxprice": -1, "sort": "undefine",
                                   "search": "undefine"})
    print(st.status_code)


newebay()
