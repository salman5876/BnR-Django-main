import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")

from products.models import AllProducts, AllProductsDuplicate

for product in AllProducts.objects.all()[0:10]:
    product_duplicate = AllProductsDuplicate(**product.__dict__)
    product_duplicate.id = None
    product_duplicate.save()
    print(('Insert.....'))
print("Completed")