import os, django

import pickle

from concurrent.futures import ThreadPoolExecutor

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from django.db import connection

from products.models import CategoryTable, AllProducts

from datetime import datetime, timedelta
how_many_days = 15


try:
    with open("data.pickle","rb") as r:
        seen_data = pickle.load(r)
except:
    seen_data = []

data = AllProducts.objects.filter(
    SNR_Date__gte=datetime.now()-timedelta(days=how_many_days)
    ).exclude(SNR_SKU__in=seen_data)

offset = 0
step = limit = 20
ct = data.count()

def test_data(dt):
    url,sku = dt

while limit<ct:

    data_slice = data[offset:limit].values_list("SNR_ProductURL","SNR_SKU")
    data_slice = list(data_slice)

    offset = limit
    limit += step



    with ThreadPoolExecutor(max_workers=4) as executor:
        future = executor.map(test_data, data_slice, chunksize=100)
        executor.shutdown(wait=True)

    ct = data.count()

