from django.urls import re_path as url
from django.urls import path
from categories import views

urlpatterns = [
    path("brands/", views.GetBrandsNames.as_view(), name='get_brands_names'),
]