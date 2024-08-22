import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
import requests
from products.models import *
from SNR.settings import *
print("before")
data=AllProductsPartition.objects.filter(SNR_Brand__iexact='walmart').count()
print("hre")
print(data)
input()


my_map = client.get_map("Logo").blocking()


def updatelogo():
    print('in')
    a=Active_DailyDeals.objects.filter(SNR_Active=True).distinct('SNR_Available')
    print(a)
    merchants.objects.filter(active=True).update(active=False)
    print('ok')
    for i in a:
        print(i.SNR_Available)
        if merchants.objects.filter(name=str(i.SNR_Available)).exists():
            res=merchants.objects.get(name=str(i.SNR_Available))
            res.active=True
            res.save()
            print('Done')
        else:
            print('Not IN Merchant Table :',i.SNR_Available)

updatelogo()

#
def cac():
    my_map.clear()
    # my_map.remove('Merchant_Logos_Home')
    date = requests.get('https://backend.shopnroar.com/products/merchantlogos/')
    print(date.status_code)
    print('Done')

# cac()

# print(Active_DailyDeals.objects.filter(SNR_Active=True).distinct('SNR_Available').order_by('SNR_Available','-SNR_PriceAfter')[:10])

def updatelogocoupon():
    a=AllProductsCoupons.objects.filter(SNR_Active=True).distinct('SNR_Available')
    merchantscoupons.objects.filter(active=True).update(active=False)
    for i in a:
        print(i.SNR_Available)
        if merchantscoupons.objects.filter(name=str(i.SNR_Available)).exists():
            res=merchantscoupons.objects.get(name=str(i.SNR_Available))
            res.active=True
            res.count=str(AllProductsCoupons.objects.filter(SNR_Available=i.SNR_Available,SNR_Active=True).count())
            res.save()
            print('Done')
        else:
            print('Not IN Merchant Table :',i.SNR_Available)

# updatelogocoupon()
