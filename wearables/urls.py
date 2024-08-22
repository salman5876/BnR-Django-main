__author__ = 'Amad'
from django.urls import re_path as url

from . import views

urlpatterns = [

    url(r'^$', views.getAll_Wearables, name="getAll_Wearables"),
    url(r'^sortASC$', views.getAll_WearablesASC, name="getAll_Wearables"),
    url(r'^sortDESC$', views.getAll_WearablesDESC, name="getAll_Wearables"),

    url(r'^getModels$', views.getAllWearablesModels, name="getAll_Wearables"),
    url(r'^getModelsbestbuy$', views.getModelsBestbuy, name="getAll_Wearables"),
    url(r'^getModelsebay$', views.getModelsebay, name="getAll_Wearables"),
    url(r'^getModelswalmart$', views.getModelswalmart, name="getAll_Wearables"),

    url(r'^filterallwearable/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProducts, name="Search Result"),
    url(r'^filterallwearableASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProductsASC, name="Search Result"),
    url(r'^filterallwearableDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProductsDESC, name="Search Result"),

    url(r'^filterbybrands/(?P<query>.+)/$', views.filterWearablesbybrands, name="Filter"),
    url(r'^filterbybrandsASC/(?P<query>.+)/$', views.filterWearablesbybrandsASC, name="Filter"),
    url(r'^filterbybrandsDESC/(?P<query>.+)/$', views.filterWearablesbybrandsDESC, name="Filter"),


    url(r'^filter/(?P<query>.+)/$', views.filterWearables, name="Filter"),
    url(r'^filterASC/(?P<query>.+)/$', views.filterWearablesASC, name="Filter"),
    url(r'^filterDESC/(?P<query>.+)/$', views.filterWearablesDESC, name="Filter"),

    url(r'^filterbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.filterWearableswithprice, name="Filter"),
    url(r'^filterASCbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.filterWearablesASCwithprice, name="Filter"),
    url(r'^filterDESCbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.filterWearablesDESCwithprice, name="Filter"),

    # url(r'^delete/$', views.deleteAmazon, name="Filter"),
    url(r'^wearablebyrange/(?P<p1>.+)/(?P<p2>.+)$', views.Wearablesbyprice, name="Filter"),
    url(r'^wearablebyrangeASC/(?P<p1>.+)/(?P<p2>.+)$', views.WearablesbypriceASC, name="Filter"),
    url(r'^wearablebyrangeDESC/(?P<p1>.+)/(?P<p2>.+)$', views.WearablesbypriceDESC, name="Filter"),

    # url(r'^search/(?P<query>.+)/$', views.search, name='search_results'),

    url(r'^add/$',views.add_Wearables,name="add_Wearable"),

]