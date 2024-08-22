from django.contrib import admin

# from .models import VendorReviewsScore,VendorReviews
from .models import *
# Register your models here.

admin.site.register(VendorReviewsScore)
admin.site.register(VendorReviews)
admin.site.register(VendorNamesandImages)
