import math

from scrapetools import *
from django.db import connection

category_map = {
"%shoes%": "Shoes",
"Other Snowsports%": "Uncategorized",
"Movies, music & books": "Movies, Music & Books",
"Network & Connectivity": "Computer Hardware & Software",
"%Cloth%": "Clothing & Apparel",

}

from contextlib import closing
#
# def updatecat(cat):
#     key, val = cat[1]
#     c = int(cat[0] / items_num)
#     c = c + (1 if cat[0] % items_num > 0 else 0)
#
#     with closing(connection.cursor()) as cursor:
#         print "Mapping {0} to {1}".format(key, val)
#         for i in range(c):
#             q = a.format(val, key)
#             cursor.execute(q)
#
#
# def countc(cat):
#     key, val = cat
#
#
#     q = 'Select count(*) from products_allproducts Where "SNR_Category" ILIKE \'{0}\''.format(key)
#     with closing(connection.cursor()) as cursor:
#         cursor.execute(q)
#         try:
#
#             temp = cursor.fetchone()[0]
#         except:
#             return (0,cat)
#
#     return (int(temp), cat)
#
#
# items = [(i[0].capitalize(), i[1]) for i in category_map.iteritems()]
# cap_dict = dict(items)


items = [(i[0].capitalize(), i[1]) for i in category_map.iteritems()]
cap_dict = dict(items)

import time
if __name__ == '__main__':

    # a = """update products_allproducts SET "SNR_Category" = '{0}' Where id in (Select id from products_allproducts Where "SNR_Category" ILIKE '{1}' limit %s)""" % (
    #     str(items_num))
    all_cats = []

    with connection.cursor() as cursor:
        for key in cap_dict:
            print key + " : " + cap_dict[key]

            print "Mapping {0} to {1}".format(key, cap_dict[key])
            a = """update products_allproducts SET "SNR_Category" = '{0}' Where "SNR_Category" ilike '{1}' """
            q=a.format(cap_dict[key],key)
            print q
            time.sleep(1)
            cursor.execute(q)
            # row = cursor.fetchone()[0]
            # print row

