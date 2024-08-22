import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from django.db import connection

from products.models import CategoryTable, AllProducts

def delete_and_set_cats():
    delete_query = "Delete from products_categorytable"
    print("Deleting all categories from category table")
    #CategoryTable.objects.all().delete()
    category_query = 'Select distinct "SNR_Category" from products_allproducts'

    with connection.cursor() as cursor:
        cursor.execute(category_query)
        data = cursor.fetchall()
        cursor.execute(delete_query)

    #data = [i[0].title() for i in AllProducts.objects.all().values_list("SNR_Category").distinct()]
    data = [i[0] for i in data]
    data = set([i for i in data if i])
    print("Refresh And Create Categories")
    data = [CategoryTable(SNR_Category=i) for i in data]

    CategoryTable.objects.bulk_create(data)

delete_and_set_cats()

from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['00:00', '12:00']
    DJANGO_CRON_CACHE = 'cron_cache'
    MIN_NUM_FAILURES = 3

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'refresh_cat.my_cron_job'  # a unique code

    def do(self):
        print "refreshing..."
        delete_and_set_cats()

        pass  # do your thing here

    do(0)


