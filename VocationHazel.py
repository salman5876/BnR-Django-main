import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from django.db import connection
import requests
from products.models import *
from django.core.cache import cache
from SNR.settings import *


my_map = client.get_map("Vocation").blocking()
my_map.clear()
def scrt():
    a=['GROUPON','sam\'s club','COSTCO','BJs','TRAVELZOO']
    for i in a:
        try:
            # my_map.remove('Hot_Deals'+str(i.name)+'undefineundefineundefine-1-1401')
            path = 'https://backend.shopnroar.com/products/filterVocation/'+str(i)+'/40/'
            print(path)
            st = requests.post(path, json={"cat": "undefine", "minprice": -1, "maxprice": -1, "sort": "undefine",
                                           "search": "undefine"})
            print(st.status_code)
        except:
            print('something wrong')

scrt()