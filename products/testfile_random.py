cat = 'Accessible Home'

from products.models import AllProducts


# urls = AllProducts.objects.using('newdb').filter(SNR_Available="ebay", SNR_isShow=True)  #.order_by('id')
urls = AllProducts.objects.using('newdb').filter(SNR_Category=cat, SNR_isShow=True)  #.order_by('id')
print(urls.count())
