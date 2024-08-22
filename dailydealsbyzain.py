from multiprocessing.dummy import Pool as ThreadPool
import os

#
# from zain_deals import  verizondatazain
import multiprocessing

import os

# print os.listdir("zain_deals")

# folder="Amazon_Sraper_Files"
# files=os.listdir(folder)
# scrap_files = []
file_list = ['Fashion.py']
# for item in files:
#     if item in file_list:
#         scrap_files.append(item)



def run(file):
    print(file)


    os.system('python '+file)






import time
while (True):


    print 'calling schduling...'
    pool = ThreadPool(2)
    # multiprocessing.cpu_count() * 4
    results = pool.map(run, file_list)

    pool.close()
    pool.join()

    time.sleep(4320)
