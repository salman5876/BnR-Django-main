from django.urls import re_path as url
from django.urls import path
from . import views

urlpatterns = [


    url(r'^deals$', views.getAll_Deals, name=""),
    url(r'^todaydehttps://backend.shopnroar.comals$', views.getAll_TodayDeals, name=""),
    # url(r'^filtertodaydeals/(?P<query>.+)/$', views.filter_TodayDeals, name=""),
    url(r'^filtertodaydealsbybrand/(?P<query>.+)/$', views.filter_TodayDeals, name=""),
    url(r'^filterVendorDeals/(?P<query>.+)/$', views.filter_VendorDeals, name=""),


    url(r'^filterVocation/(?P<query>.+)/(?P<totalResult>.+)/$', views.filter_Vocation, name=""),
    url(r'^filterVendorDeals_test_backup/(?P<query>.+)/(?P<totalResult>.+)/$', views.filter_VendorDeals_test_backup, name=""),
    url(r'^filterVendorDeals_test_sm/(?P<query>.+)/(?P<totalResult>.+)/$', views.filter_VendorDeals_test_sm, name=""),
    url(r'^filterVendorDeals_test_sm1/$', views.filter_VendorDeals_test_sm1, name=""),
    url(r'^filter_VendorDeals_mainsearch/(?P<merchant>.+)/(?P<query>.+)/(?P<totalResult>.+)/$', views.filter_VendorDeals_mainsearch, name=""),

    url(r'^getVendorCategories/(?P<query>.+)/$', views.get_VendorCategories, name=""),
    url(r'^get_VocationCategories/(?P<query>.+)/$', views.get_VocationCategories, name=""),
    # url(r'^todayhotdeals$', views.getAll_Deals, name=""),
    url(r'^todayhotdeals$', views.getAll_HotDeals, name=""),
    url(r'^todayTop3hotdeals$', views.getop_3_HotDeals, name=""),
    # url(r'^dealsCategorsies$', views.getAll_CatsDeals, name=""),
    url(r'^dealsBrands$', views.getAll_BrandsDeals, name=""),
    url(r'^senddeals$', views.SendDeals, name=""),

    url(r'^sendData$', views.send_data, name=""),

    url(r'^countbyvendor/(?P<vendor>.+)$', views.CountProduct, name=""),


    url(r'^countreviews/$', views.CountProductReviews, name=""),


    url(r'^categoryproductScrapping/(?P<category>.+)$', views.getproductsforScrapping, name=""),


    url(r'^singleproduct/(?P<id>.+)$', views.get_singleproduct, name=""),
    url(r'^singleproduct_deal/(?P<id>.+)$', views.get_singleproductdeal, name=""),
    url(r'^singleproduct1/(?P<id>.+)$', views.get_singleproduct1, name=""),
    url(r'^GetAllCategories$', views.testingRawData, name=""),


    url(r'^category/(?P<category>.+)$', views.categoryall_explain, name=""),
    url(r'^categoryByID/(?P<category>.+)$', views.categoryall_explainByID, name=""),

    ############################################################

    url(r'^getVendorsCategories/', views.GetVendorsCategories.as_view(), name=""),
    url(r'^categoryByName/(?P<category_name>.+)/(?P<products_per_page>.+)$', views.GetCategoriesDataByName.as_view(), name=""),
    url(r'^categoryByName_Post/(?P<category_name>.+)/(?P<products_per_page>.+)$', views.GetCategoriesDataByName_PostTest.as_view(), name=""),

    url(r'^homepageCategoriesData/', views.HomePageCategoriesData.as_view(), name=""),
    url(r'^CategoryNamesFromCache/', views.CategoryNamesFromCache.as_view(), name=""),

    url(r'^categoryByID_test/(?P<category>.+)$', views.categoryall_explainByID_test, name=""),
    url(r'^filterVendorDeals_test/(?P<query>.+)/(?P<totalResult>.+)/$', views.filter_VendorDeals_test, name=""),
    # url(r'^filterVendorDeals_test_test/(?P<query>.+)/(?P<totalResult>.+)/$', views.filter_VendorDeals_test_test, name=""),

    url(r'^merchantlogos/$', views.merchantlogos, name=""),
    # url(r'^getallvendors/',views.VendorNamesandImages,name=''),


    # Sharding
    path('sharding/', views.sharding_view, name='sharding'),
    ###############################################################

    url(r'^category_Home/(?P<category>.+)$', views.category_Home, name=""),
    url(r'^categoryByID_test/(?P<category>.+)/(?P<totalResult>.+)$', views.categoryall_explainByID_test, name=""),
    url(r'^categoryByID1/(?P<category>.+)$', views.categoryall_explainByID1, name=""),
    url(r'^categoryByID2/(?P<category>.+)$', views.categoryall_explainByID2, name=""),
    url(r'^subCategoryByID/(?P<category>.+)/(?P<subcategory>.+)$', views.subCategoryall_explainByID, name=""),
    url(r'^categoryCount/(?P<category>.+)$', views.CategoryAll_explainCount, name=""),
    # url(r'^category_explain/(?P<category>.+)$', views.CategoryAll, name=""),
    url(r'^category_ASC/(?P<category>.+)$', views.CategoryAll_explain_ASC, name=""),
    url(r'^category_DESC/(?P<category>.+)$', views.CategoryAll_explain_DESC, name=""),

    #category filters
    url(r'^GetMerchantsofCategory/(?P<category>.+)$', views.GetMerchantsCategories, name=""),
    url(r'^GetBrandsofCategory/(?P<category>.+)$', views.GetBrandsCategories, name=""),
    url(r'^GetSubCategoryofCategory/(?P<category>.+)$', views.GetSubCatsCategories, name=""),

    url(r'^$', views.getAll_Products, name=""),

    url(r'^shops/(?P<store>.+)$', views.StoreAll, name=""),


    url(r'^filterReview/(?P<query>.+)/$',
        views.FilterProductsRevs, name="Search Review"),
    # url(r'^filterReviewebay/(?P<query>.+)/$',
    #     views.FilterProductsRevsebay, name="Search Review"),

    url(r'^filterReviewAI/(?P<query>.+)/$',
        views.FilterProducts_RevAI, name="Search Review"),

    url(r'^addreview/?$',
        views.AddSnrRev, name="Search Review"),


    url(r'^Product_Rec/(?P<query>.+)/$',
        views.Products_Rec, name="Search Review"),

    url(r'^InsertProduct/$',
        views.InsertData, name="Search Review"),

    url(r'^InsertProductReviews/$',
        views.InsertProductReviews, name="Search Review"),
url(r'^filter1/(?P<id>.+)/(?P<item>.+)$',
        views.filter),
url(r'^test/(?P<category>.+)$', views.categoryall_explainByID, name=""),
url(r'^recentlyitems/$', views.recentlyitem, name=""),

url(r'^Home_Test/$', views.Home_test, name=""),
url(r'^Home_Cats/$', views.Home_Cats, name=""),       ################################################
path('Home_Test_mobile/', views.Home_test_mobile, name=""),
url(r'^Home_Test1/$', views.Home_test1, name=""),

url(r'^Home_Test_new/$', views.Home_test_New, name=""),

url(r'^addwishlist/(?P<pk>.+)$',views.ADDwishlist_pro),
url(r'^AllMerchantCoupns/$', views.AllMerchantCoupns, name=""),
url(r'^AllMerchantCoupns1/$', views.AllMerchantCoupns1, name=""),
url(r'^AllCoupns/(?P<que>.+)/(?P<item>.+)$', views.AllCoupns, name=""),
url(r'^CouponsInsertion/$', views.CouponsInsertion, name=""),
url(r'^AllCouponsMerchants/$', views.AllCouponsMerchants, name=""),
url(r'^Coupons_edit_del/(?P<id>.+)/$', views.Coupons_edit_del, name=""),
url(r'^newsuggest/(?P<query>.+)$', views.newsuggest, name=""),
url(r'^upc/(?P<query>.+)$', views.upc, name=""),
url(r'^test1/(?P<query>.+)$', views.test1, name=""),
# url(r'^AllSearch/(?P<totalResult>.+)/$', views.AllSearch, name=""),
url(r'^AllSearch/(?P<totalResult>.+)/$', views.AllSearch, name=""),
url(r'^AllSearch/', views.AllSearch, name=""),

url(r'^AllSearch_/(?P<totalResult>.+)/$', views.AllSearch_, name=""),
url(r'^AllSearch_/', views.AllSearch_, name=""),

url(r'^productdetial/', views.detail_of_product, name=""),

]

