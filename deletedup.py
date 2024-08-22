import os, django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
from django.db import transaction, connection
django.setup()
from contextlib import closing
a = 'Select "SNR_SKU" from products_allproducts Group BY "SNR_SKU" Having count("SNR_SKU")>1 limit 10000'
ids_query = """Select id from products_allproducts Where "SNR_SKU" IN ({0}) AND id NOT IN (Select max(id) from products_allproducts Where "SNR_SKU" IN ({0}) Group BY "SNR_SKU")""".format(a)
delete_rev = 'Delete from products_product_reviews Where "Product_id" IN ({0})'.format(ids_query)
delete_post = 'Delete from products_allproducts Where id IN ({0})'.format(ids_query)

with closing(connection.cursor()) as cursor:
    print "Finding  And Deleting Duplicates"
    for i in range(40):
        try:
            cursor.execute(delete_rev)
            cursor.execute(delete_post)
        except Exception as e:
            pass