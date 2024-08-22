from django.urls import path

from . import views


urlpatterns = [
    path('post_short/', views.post_short),
    path('get_shorts/', views.get_shorts),
]
