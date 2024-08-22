from datetime import time

from scrapetools import *

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from products.serializers import DailyDeals_Serializer
from products.models import DailyDeals
from data import  bestbuy

u"""
gr : Groupon Deals Data from https://www.groupon.com/occasion/deals-of-the-day
bestbuy : BestBut Deal from https://www.bestbuy.com/site/clp/sale-page/pcmcat185700050011.c?id=pcmcat185700050011
EbayDeals: Ebay Deals from https://www.ebay.com/deals
walmart: Walmart Deals from https://www.walmart.com/browse/daily-deals/0/0/ (First Two Pages)
"""
commitdata = commitdeal


class dealyData():

    def getallDeals(self, request):
        print ("calling")

        allDealsFunc = [bestbuy.getDeals(),
                        ]

        temp = True

        data = []

        while temp:
            temp = []
            for i in range(len(allDealsFunc)):
                try:
                    c_item = next(allDealsFunc[i])
                    temp.append(c_item)
                except Exception as e:
                    pass

            if temp:

                for it in temp:
                    commitdata(it)

        from data.delldeals import DellDealsSpider
        from data.hpdeals import HpDeals
        from data.bestbuy import getDeals
        from data.neweggdeals import NewEggDeals
        from scrapy.crawler import CrawlerProcess
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(DellDealsSpider)
        process.crawl(NewEggDeals)
        # process.crawl(getDeals())
        process.crawl(HpDeals)

        process.start()

        proceses = [
            "python ./data/adorama.py"
        ]

        for i in proceses:
            try:
                run_sub(i)
            except:
                pass



import time
while(True):

    print ('calling....')
    dealyData().getallDeals({})
    time.sleep(43200)