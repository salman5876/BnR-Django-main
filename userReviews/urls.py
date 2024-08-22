from django.urls import re_path as url

from .  import views


urlpatterns = [

    url(r'^add$',views.add_Reviews,name="reviewbyuser"),
    url(r'^$',views.getAll_Revies,name="reviewbyuser"),
    url(r'^getallscore$',views.getAll_ReviewsScore,name="reviewbyuser"),
    # url(r'^delete$',views.deleteallreviews,name="reviewbyuser"),
    url(r'^calculationScore$',views.Calculate_VendorReviewsScore,name="reviewbyuser"),
    url(r'^filterReview/(?P<query>.+)/$', views.Filter_reviews, name="Filter"),
    url(r'^filterReviewVendor/(?P<query>.+)/$', views.Filter_VendorReviews, name="Filter"),
    url(r'^filterReviewScore/(?P<query>.+)/$', views.Filter_ReviewsScores, name="Filter"),
    url(r'^bestbuyproduct/$', views.add_ReviewsBestBuy, name="Add"),
    url(r'^vendorReviews/$', views.GetVendorReviews, name="Get"),
    url(r'^delete/$', views.delete, name="delete"),
    url(r'^getallvendors/$',views.GetVendroNames),
    url(r'^emailforuser',views.EmailforUser),
    url(r'^selectedemailvendors/',views.GetActiveEmilVendors)


]
