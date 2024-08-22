import django
import os

from django.contrib.postgres.search import TrigramSimilarity

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.models import *


data=DailyDeals.objects.filter(SNR_Active=False).update(SNR_Active=True)
print(data)