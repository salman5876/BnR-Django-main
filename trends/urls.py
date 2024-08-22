__author__ = 'Amad'
from django.urls import re_path as url,include
from . import views


urlpatterns = [
    url(r'^getTrends$',  views.getTrend, name='index'),
    url(r'^getTrendsMobile$', views.getTrendMobile, name='index'),
    url(r'^getTrendsLaptop$', views.getTrendLaptop, name='index'),
    url(r'^getTrendstv$', views.getTrendTV, name='index'),
    url(r'^getTrendsgame$', views.getTrendgame, name='index'),
    url(r'^getTrendsaudio$', views.getTrendaudio, name='index'),
    url(r'^getTrendsmovie$', views.getTrendmovies, name='index'),
    url(r'^getTrendstoys$', views.getTrendtoy, name='index'),
    url(r'^getTrendscam$', views.getTrendcam, name='index'),
    url(r'^getTrendscar$', views.getTrendcar, name='index'),
    url(r'^getTrendsAppliances$', views.getTrendappliance, name='index'),
    url(r'^getTrendsWearable$', views.getTrendWearable, name='index'),

    # url(r'^getCount$', views.CountAll, name='index'),

    url(r'^setTrends$',  views.setTrend, name='index'),
    url(r'^popular',  views.popular, name='index'),
    url(r'^delete', views.delete, name='index'),
    url(r'^setPopular', views.setPopular, name='index'),


]