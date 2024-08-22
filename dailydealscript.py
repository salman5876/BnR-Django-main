import django,os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import *
from products.serializers import Active_DailyDeals_Serializer


def script():
    final={'SNR_SKU': 'Mch10230613', 'SNR_Title': "Level 1 Back Stapled Canvas by Artist's Loft®", 'SNR_ProductURL': 'https://www.michaels.com/artists-loft-back-stapled-canvas/M10015472.html?dwvar_M10015472_size=4%22%20x%204%22', 'SNR_ImageURL': 'https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/EF141F4E255141E08379BF64FF65BC5D/10230613_1.jpg?fit=inside|540:540,https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/5A914D2E5AB641E5A33B296C321A9B11/10230613_2.jpg?fit=inside|540:540,https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/044B79055FE54DEE864EC9F2D8425166/10230613_3.jpg?fit=inside|540:540', 'SNR_Category': 'Art Supplies', 'SNR_PriceBefore': 3.19, 'SNR_PriceAfter': 1.59, 'SNR_Available': 'Michaels'}
    final.update({"SNR_Active":False})
    serializer=Active_DailyDeals_Serializer(data=final)
    if serializer.is_valid():
        serializer.save()
script()

def new(merchant):
    try:
        Active_DailyDeals.objects.filter(SNR_Active=True,SNR_Available=str(merchant)).update(SNR_Active=None)
        Active_DailyDeals.objects.filter(SNR_Active=False,SNR_Available=str(merchant)).update(SNR_Active=True)
        old = Active_DailyDeals.objects.filter(SNR_Active=None,SNR_Available=str(merchant))
        for i in old:
            transfer = DailyDeals(SNR_SKU=i.SNR_SKU,SNR_Title=i.SNR_Title,SNR_Category=i.SNR_Category,SNR_PriceBefore=i.SNR_PriceBefore
                                  ,SNR_PriceAfter=i.SNR_PriceAfter,SNR_Available=i.SNR_Available,SNR_ProductURL=i.SNR_ProductURL
                                  ,SNR_ImageURL=i.SNR_ImageURL,SNR_Active=False)
            transfer.save()
        Active_DailyDeals.objects.filter(SNR_Active=None,SNR_Available=str(merchant)).delete()
        print('Done')
    except:
        print('something went wrong')
