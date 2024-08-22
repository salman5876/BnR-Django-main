from datetime import datetime
s1 = '10:33:26'
s2 = '11:15:49' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print tdelta

# import re
#
# link='https://www.ebay.com/itm/Samsung-Galaxy-Note8-SM-N950U-64GB-Midnight-Black-Unlocked-Smartphone/302836056548?epid=239011926&hash=item46826f81e4%3Ag%3AULcAAOSwhXhbZnnm&_sacat=0&_nkw=samsung+note+8&_from=R40&rt=nc&_trksid=p2047675.m570.l1313.TR12.TRC2.A0.H0.Xsamsung+note+8.TRS0'
#
# # m = re.search('https://www.ebay.com/itm/(.+?)/', link)
# # if m:
# #     found = m.group(1)
# #
# # print found
#
# found=""
# m = re.search('/itm/(.+?)/?hash=', link)
# if m:
#     found = m.group(1)
#
# print found
# title= found.split("/")
# print title[0]
# id= title[1].split("?")
# print id[0]
# prodid=id[1].split("=")
# print prodid[1].split("&")[0]
# newlink='https://www.ebay.com/urw/'+title[0]+'/product-reviews/'+prodid[1].split("&")[0]+'?_itm='+str(id[0])
#
# print newlink