
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from products.models import Active_DailyDeals

results = Active_DailyDeals.objects.all()
print(results.count())
# print(results.count())


