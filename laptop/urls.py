from django.urls import re_path as url

from . import views

urlpatterns = [

    url(r'^$', views.getAll_Laptops, name="getAll_Laptops"),
    url(r'^sortASC$', views.getAllLaptopsSortASC, name="getAll_Laptops"),
    url(r'^sortDESC$', views.getAllLaptopsSortDESC, name="getAll_Laptops"),

    url(r'^add/$', views.add_Laptop, name="add_Laptop"),
    url(r'^delete/$', views.delete, name="add_Laptop"),
    url(r'^deleteAmazon/$', views.deleteAmazon, name="add_Laptop"),
    url(r'^deleteEbay/$', views.deleteEbay, name="add_Laptop"),
    url(r'^brands/$', views.getAllBrands, name="add_Laptop"),

    url(r'^getModels$', views.getModels, name="Models"),
    url(r'^getModelsebay$', views.getModelsebay, name="Models"),
    url(r'^getModelswalmart$', views.getModelswalmart, name="Models"),
    url(r'^getModelsamazon$', views.getModelsamazon, name="Models"),

    url(r'^filterlaptopbybrand/(?P<query>.+)/$', views.FilterLaptopsbybrands, name="Filter"),
    url(r'^filterlaptopbybrandASC/(?P<query>.+)/$', views.FilterLaptopsbybrandsasc, name="Filter"),
    url(r'^filterlaptopbybrandDESC/(?P<query>.+)/$', views.FilterLaptopsbybrandsdesc, name="Filter"),

    url(r'^filterlaptop/(?P<query>.+)/$', views.FilterLaptops, name="Filter"),
    url(r'^filterlaptopbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.FilterLaptopswithprice,
        name="Filter"),
    url(r'^laptopbyrange/(?P<price1>.+)/(?P<price2>.+)$', views.LaptopsRange, name="Filter"),
    url(r'^laptopbyrangeASC/(?P<price1>.+)/(?P<price2>.+)$', views.LaptopsRangeASC, name="Filter"),
    url(r'^laptopbyfetch/$', views.laptopbyfetch, name="Filter"),
    url(r'^laptopbyfetch1/$', views.laptopbyfetch1, name="Filter"),
    url(r'^laptopbyrangeDESC/(?P<price1>.+)/(?P<price2>.+)$', views.LaptopsRangeDESC, name="Filter"),

    url(r'^filteralllaptpos/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProducts, name="Search Result"),
    url(r'^filteralllaptposASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProductsASC, name="Search Result"),
    url(r'^filteralllaptposDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',views.FilterAllProductsDESC, name="Search Result"),

    url(r'^filterlaptopASC/(?P<query>.+)/$', views.FilterLaptopsAsc, name="Filter"),
    url(r'^filterlaptopDESC/(?P<query>.+)/$', views.FilterLaptopsDesc, name="Filter"),
    url(r'^filterlaptopASCbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.FilterLaptopsAscwithprice,
        name="Filter"),
    url(r'^filterlaptopDESCbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)$', views.FilterLaptopsDESCwithprice,name="Filter"),

]
