import os

import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool


print multiprocessing.cpu_count()


files=['ebayreview_waryam.py', 'walmartrev_waryam.py', 'bestbuyreview_waryam.py']


def run(file):
    os.system('python '+file)


pool = ThreadPool(multiprocessing.cpu_count()*3)

results = pool.map(run, files)

pool.close()
pool.join()

