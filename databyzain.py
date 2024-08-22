from multiprocessing.dummy import Pool as ThreadPool
import os

#
# from zain_deals import  verizondatazain
import multiprocessing

import os

# print os.listdir("zain_deals")

folder="completedata_byzain";
files=os.listdir(folder)



def run(file):
    print(file)


    os.system('python '+folder+'/'+file)






import time
while (True):


    print 'calling schduling...'
    pool = ThreadPool(multiprocessing.cpu_count() * 4)

    results = pool.map(run, files)

    pool.close()
    pool.join()

    time.sleep(4320)
