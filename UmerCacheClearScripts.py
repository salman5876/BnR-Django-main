
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

Deal_map2 = client.get_map("Deal_all").blocking()
Deal_map2.clear()






Coupons_map = client.get_map("map-name").blocking()
Coupons_map.clear()

Category_map = client.get_map("MainCat").blocking()
Category_map.clear()

logo_map = client.get_map("Logo").blocking()
logo_map.clear()

Home_map = client.get_map("Home").blocking()
Home_map.clear()
Home_map = client.get_map("Home_old").blocking()
Home_map.clear()
Vocation_map = client.get_map('Vocation').blocking()
Vocation_map.clear()
Deal_map = client.get_map("Deal").blocking()
Deal_map.clear()

print("all Clear")
