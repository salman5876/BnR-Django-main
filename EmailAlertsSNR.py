import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from userReviews.models import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from products.models import *

vendorsdata = VendorNamesandImages.objects.all()
for data in vendorsdata:
    User_data=EmailAlert.objects.filter(vendor_name__iexact=data.vendor_name,alerty_type=data.vendor_type)
    print(data.vendor_image)
    print(data.vendor_type)
    print(data.vendor_name)
    if User_data.count()>0:
        Emaillist=[]
        new_data = []
        for email_data in User_data:
            Emaillist.append(email_data.user_id.email)
        title = None
        if data.vendor_type=='Deals':
            title =  "New "+data.vendor_name.title()+' Deals Arrival'
            activedata=Active_DailyDeals.objects.filter(SNR_Available__iexact=data.vendor_name,SNR_Active=True).order_by('-id')[:15]
            print("this is deal")

            for detaildata in activedata:
                try:
                    discount_percent =round(detaildata.SNR_PriceAfter / detaildata.SNR_PriceBefore*100)
                except:
                    discount_percent = None
                try:
                    image_url = detaildata.SNR_ImageURL.split(',')[0]
                except:
                    image_url =None
                dic = {

                    "image": image_url,
                    "product_title" : detaildata.SNR_Title,
                    "price_after" : detaildata.SNR_PriceAfter,
                    "price_before": detaildata.SNR_PriceBefore,
                    "brand_image": data.vendor_image.replace('../../','https://devdeals.shopnroar.com/'),
                    "snr_producturl":detaildata.SNR_ProductURL,
                    "detail_page_url" : 'https://devdeals.shopnroar.com/deals-detail?Model='+detaildata.SNR_SKU+'&Name='+detaildata.SNR_Title+'&ID='+str(detaildata.id)+'&Type='+'Deals',
                    "saving_percentage": discount_percent

                }
                print(dic['brand_image'])

                new_data.append(dic)
            key = {

                "data": new_data,
                "title": title,
                "show_more": "https://devdeals.shopnroar.com/deals/"+data.vendor_name
            }

            message = get_template('NewDealsTemplate.html').render(key)
            email = EmailMessage('ShopnRoar Email Alerts', message, to=Emaillist)
            email.content_subtype = 'html'
            email.send()
            print("email sent")
        elif data.vendor_type=='Coupons':
            title = "New " + data.vendor_name.title() + ' Coupons Arrival'

            activedata = AllProductsCoupons.objects.filter(SNR_Available__iexact=data.vendor_name,
                                                          SNR_Active=True).order_by('-id')[:15]
            for detaildata in activedata:

                dic = {
                    # "image": detaildata.SNR_ImageURL.split(',')[0],
                    "product_title" : detaildata.SNR_Title,
                    "snr_discount" : detaildata.SNR_Discount,
                    "snr_description": detaildata.SNR_Description,
                    "brand_image": data.vendor_image.replace('../../','https://devdeals.shopnroar.com/'),
                    "snr_producturl":detaildata.SNR_CouponCode_url,
                    # "detail_page_url" : 'https://devdeals.shopnroar.com/deals-detail?Model='+detaildata.SNR_SKU+'&Name='+detaildata.SNR_Title+'&ID='+str(detaildata.id)+'&Type='+'Deals',


                }
                print(dic['brand_image'])

                new_data.append(dic)
            key = {

                "data": new_data,
                "title": title,
                "show_more": "https://devdeals.shopnroar.com/coupons?name="+data.vendor_name
            }

            message = get_template('CouponsTemplate.html').render(key)
            email = EmailMessage('ShopnRoar Email Alerts', message, to=['umarzafar54@gmail.com'])
            email.content_subtype = 'html'
            email.send()
            print("email sent")
            print("coupons sned")


        elif data.vendor_type == 'Vacations':
            title = "New " + data.vendor_name.title() + ' Vacations Arrival'
            activedata = Active_Vocation.objects.filter(SNR_Available__iexact=data.vendor_name, SNR_Active=True).order_by('-id')[:15]
            for detaildata in activedata:
                try:
                    discount_percent =round(detaildata.SNR_PriceAfter / detaildata.SNR_PriceBefore*100)
                except:
                    discount_percent = None
                try:
                    image_url = detaildata.SNR_ImageURL.split(',')[0]
                except:
                    image_url =None
                dic = {
                    "image": image_url,
                    "product_title" : detaildata.SNR_Title,
                    "price_after" : detaildata.SNR_PriceAfter,
                    "price_before": detaildata.SNR_PriceBefore,
                    "brand_image": data.vendor_image.replace('../../','https://devdeals.shopnroar.com/'),
                    "snr_producturl":detaildata.SNR_ProductURL,
                    "detail_page_url" : 'https://devdeals.shopnroar.com/vacations-detail?Model='+detaildata.SNR_SKU+'&Name='+detaildata.SNR_Title+'&ID='+str(detaildata.id)+'&Type='+'Vocation',
                    "saving_percentage": discount_percent

                }
                print(dic['brand_image'])

                new_data.append(dic)
            key = {

                "data": new_data,
                "title": title,
                "show_more": "https://devdeals.shopnroar.com/vacations?name="+data.vendor_name
            }
            message = get_template('VacationsTemplate.html').render(key)
            email = EmailMessage('ShopnRoar Email Alerts', message, to=['saad.farooq@brainplow.com'])
            email.content_subtype = 'html'
            email.send()
            print("email sent")



