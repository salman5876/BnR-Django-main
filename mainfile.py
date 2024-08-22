from multiprocessing.dummy import Pool as ThreadPool
import os
from os import listdir

import multiprocessing



# directoryPath='scrapingScripts'
# files = listdir(directoryPath)

files=['walmartdata.py','appoutdoorsData.py','AttData.py','beallsfloridadata.py','bestbuydata.py'
    ,'bestbuyreview_waryam.py','bhphotodata.py','bjsdata.py','buydigdata.py',
       'costcodata.py','ebaydata.py', 'frysdata.py', 'fanaticsdata.py', 'gapdata.py']


def run(file):
    print(file)


    os.system('python '+file)


pool = ThreadPool(multiprocessing.cpu_count()*4)

results = pool.map(run, files)

pool.close()
pool.join()




from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10080  # every hours
    DJANGO_CRON_CACHE = 'cron_cache'
    MIN_NUM_FAILURES = 3

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'mainfile.my_cron_job'    # a unique code

    def do(self):
        print "amad ud din"

        files = []

        def run(file):
            print(file)
            os.system('python ' + file)

        pool = ThreadPool(multiprocessing.cpu_count() * 4)

        results = pool.map(run, files)

        pool.close()
        pool.join()

        pass    # do your thing here
    do(0)