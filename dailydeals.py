# from scrapetools import *
#
# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
#
#
#
# from products.serializers import DailyDeals_Serializer
# from products.models import DailyDeals
# from data import gr, bestbuy, ebaydeals, walmart, buydigdeals, amazondeals, dailydeals_frys, bhphotovideosdeals, \
#     kmartdeals, samsclub
#
#
#
# u"""
# gr : Groupon Deals Data from https://www.groupon.com/occasion/deals-of-the-day
# bestbuy : BestBut Deal from https://www.bestbuy.com/site/clp/sale-page/pcmcat185700050011.c?id=pcmcat185700050011
# EbayDeals: Ebay Deals from https://www.ebay.com/deals
# walmart: Walmart Deals from https://www.walmart.com/browse/daily-deals/0/0/ (First Two Pages)
# """
# commitdata = commitdeal
#
# class dealyData():
#
#
#     def getallDeals(self,request):
#         print "calling"
#
#
#
#
#
#
#         allDealsFunc = [
#             # ebaydeals.getDeals(),
#             #              bestbuy.getDeals(),
#             #              gr.getDeals(),
#             #              walmart.getDeals(),
#                          # buydigdeals.getDeals(),
#                          amazondeals.getDeals(),
#                          # dailydeals_frys.get_deals(),
#                          # bhphotovideosdeals.getDeals(),
#                          # kmartdeals.get_deals(),
#                          # samsclub.getDeals()
#                          ]
#
#
#         temp = True
#
#         data = []
#
#         while temp:
#             temp = []
#             for i in range(len(allDealsFunc)):
#                 try:
#                     c_item = next(allDealsFunc[i])
#                     temp.append(c_item)
#                 except Exception as e:
#                     pass
#
#             if temp:
#
#                 for it in temp:
#                     commitdata(it)
#         #
#         # from data.delldeals import DellDealsSpider
#         # from data.hpdeals import HpDeals
#         # from data.neweggdeals import NewEggDeals
#         # from scrapy.crawler import CrawlerProcess
#         # process = CrawlerProcess({
#         #     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#         # })
#         # process.crawl(DellDealsSpider)
#         # process.crawl(NewEggDeals)
#         # process.crawl(HpDeals)
#
#
#         # process.start()
#
#
#         # proceses = [
#         #     "python ./data/adorama.py"
#         # ]
#
#         # for i in proceses:
#         #     try:
#         #         run_sub(i)
#         #     except:
#         #         pass
#
#
# import time
# while (True):
#
#     print 'calling schduling...'
#
#     dealyData().getallDeals({})
#     time.sleep(43200)



from django_cron import CronJobBase, Schedule
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AllProducts_Serializer, DailyDeals_Serializer,AmazonURLs_Serializer
from products.models import AmazonURLs, AllProducts, AmazonProxies


# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 10  # every 1 hours
#     RETRY_AFTER_FAILURE_MINS = 5
#
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'dailydeals.my_cron_job'    # a unique code
#
#     def do(self):
#         pro = AmazonURLs.objects.get(id = 7505)
#         if pro.status_range == True:
#             pro.status_range = False
#             pro.save()
#         else:
#             pro.status_range = True
#             pro.save()
#         pass    # do your thing here


pro = AmazonURLs.objects.get(id = 7505)
if pro.status_range == True:
    pro.status_range = False
    pro.save()
else:
    pro.status_range = True
    pro.save()
