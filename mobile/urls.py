__author__ = 'Amad'
from django.urls import re_path as url
from django.urls import path
from . import views


urlpatterns = [
    path('',  views.index, name='index'),
    path('viewAll',views.getAll_Mobiles,name="getAll_Mobiles"),
    url(r'^viewAllASC$', views.getAll_MobilesASC, name="getAll_Mobiles"),
    url(r'^viewAllDESC$', views.getAll_MobilesDESC, name="getAll_Mobiles"),

    url(r'^AddMobile$',views.add_Mobiles,name="Add Mobiles"),
    url(r'^delete',views.deleteAmazon,name="Add Mobiles"),
    url(r'^mobilebyrange/(?P<p1>.+)/(?P<p2>.+)$', views.Mobilesbyrange, name="Filter"),
    url(r'^mobilebyrangeASC/(?P<p1>.+)/(?P<p2>.+)$', views.MobilesbyrangeASC, name="Filter"),
    url(r'^mobilebyrangeDESC/(?P<p1>.+)/(?P<p2>.+)$', views.MobilesbyrangeDESC, name="Filter"),

    url(r'^filterallmobile/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProducts, name="Search Result"),
    url(r'^filterallmobileASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProductsASC, name="Search Result"),
    url(r'^filterallmobileDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProductsDESC, name="Search Result"),

    url(r'^getModels$',views.getModels,name="Models"),
    url(r'^getModelsbestbuy$', views.getModelsebestbuy, name="Models"),
    url(r'^getModelsebay$', views.getModelsebay, name="Models"),
    url(r'^getModelswalmart$', views.getModelswalmart, name="Models"),

    url(r'^filtermobilebybrands/(?P<query>.+)/$', views.Filter_Mobilesbybrands,name="Filter"),
    url(r'^filtermobilebybrandsASC/(?P<query>.+)/$', views.Filter_MobilesbybrandsASC,name="Filter"),
    url(r'^filtermobilebybrandsDESC/(?P<query>.+)/$', views.Filter_MobilesbybrandsDESC,name="Filter"),



    url(r'^filtermobile/(?P<query>.+)/$', views.Filter_Mobiles,name="Filter"),
    url(r'^filtermobileASC/(?P<query>.+)/$', views.Filter_MobilesASC, name="Filter"),
    url(r'^filtermobileDESC/(?P<query>.+)/$', views.Filter_MobilesDESC, name="Filter"),
    url(r'^filtermobilebyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.Filter_Mobileswithprice,name="Filter"),
    url(r'^filtermobileASCbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.Filter_MobilesASCwithprice, name="Filter"),
    url(r'^filtermobileDESCbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.Filter_MobilesDESCwithprice, name="Filter"),

]