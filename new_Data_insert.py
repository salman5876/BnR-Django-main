import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from bs4 import BeautifulSoup
from selenium import webdriver
from userReviews.models import *

data = VendorNamesandImages.objects.filter(vendor_type='Deals')
deals = []
for value in data:
    data={
        "name":value.vendor_name,
        "image":value.vendor_image
    }
    deals.append(data)

data = VendorNamesandImages.objects.filter(vendor_type='Coupons')
Coupons = []
for value in data:
    data={
        "name":value.vendor_name,
        "image":value.vendor_image
    }
    Coupons.append(data)

data = VendorNamesandImages.objects.filter(vendor_type='Vacations')
Vactions = []
for value in data:
    data={
        "name":value.vendor_name,
        "image":value.vendor_image
    }
    Vactions.append(data)




# driver=webdriver.Chrome('./chromedriver')
# driver.get('https://devdeals.shopnroar.com/')
# soup = BeautifulSoup(driver.page_source,'html.parser')
# ul=soup.find('ul',{'class':'vacations'})
# for lis in ul.find_all('li'):
#     logo=lis.find('img')['src']
#     name = lis.text.strip()
#     print(logo)
#     print(name)
#     VendorNamesandImages.objects.create(
#         vendor_image=logo,
#         vendor_type='Vacations',
#         vendor_name=name
#     )
#     print('///////')
# # print(ul)
# driver.close()
