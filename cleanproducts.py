import os, django
import json
from contextlib import closing



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
from django.db import transaction, connection
from rest_framework.renderers import JSONRenderer
django.setup()

from products.models import AllProducts, CentralTableProducts

from datetime import datetime, timedelta
how_many_days = 60

data = AllProducts.objects.filter(SNR_Date__lt=datetime.now()-timedelta(days=how_many_days))
ar = ["id",'SNR_Available', 'SNR_Brand', 'SNR_Category', 'SNR_Condition', 'SNR_CustomerReviews', 'SNR_Date', 'SNR_Description', 'SNR_ImageURL', 'SNR_ModelNo', 'SNR_Price', 'SNR_PriceBefore', 'SNR_ProductURL', 'SNR_SKU', 'SNR_SubCategory', 'SNR_Title', 'SNR_UPC', 'SNR_isShow']


total = data.count()

jr_obj = JSONRenderer()

objects_per_batch = 100
print (total)
total = total//objects_per_batch
art = ar[1:]
q = 'INSERT INTO products_centraltableproducts (%s)' % (",".join( ['"%s"' % j for j in art]))+ 'VALUES (%s) ON CONFLICT DO NOTHING' % (("%s,"*len(art))[:-1])
for i in range(total):
    try:
        prog = "Done %d Out of %d\nProgress: %0.2f"  % (i,total,i/total)
        os.system("clear")
        print (prog)
        all_ids = []
        insert_data = []
        t = i*objects_per_batch
        data_dict = data[t:t+objects_per_batch].values_list(*ar)

        for j in data_dict:
            all_ids.append(j[0])
            insert_data.append(tuple( json.loads(jr_obj.render(j[1:])) ))


        with closing(connection.cursor()) as cursor:
            cursor.executemany(
                q,
                insert_data
            )

        AllProducts.objects.filter(id__in=all_ids).delete()



    except KeyboardInterrupt:
        # Ignore Any Error
        pass
