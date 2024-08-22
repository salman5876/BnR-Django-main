from django.urls import re_path as url,include
from . import views


urlpatterns = [
    url(r'^$',  views.Allunreadfeedback, name='unread Feedback'),
    # url(r'^delete/$',  views.delete, name='unread Feedback'),
    url(r'^wishlist$',  views.WishlistALL, name='unread Feedback'),
    # url(r'^add$',  views.addwishlistback, name='Add Feedback'),
    url(r'^add$',  views.feedback, name='Add Feedback'),
    url(r'^addblog/$',  views.blogAddition, name='Add Feedback'),
    url(r'^getBlog/$',  views.blogAddition, name='Add Feedback'),
    url(r'^addwishlist$',  views.ADDwishlist, name='Add Feedback'),
    url(r'^addwishlist/(?P<pk>.+)$',views.ADDwishlist_pro),
    url(r'^deletefromwishlist/$',views.deletefromwihslist,name='delteebyurl'),
    url(r'^checkwishlist$',  views.checkwishlist, name='Add Feedback'),
    url(r'^wishlistbyuser/(?P<query>.+)/$', views.Wishlistbyuser, name="Filter"),
    url(r'^Wishlistby_user/$', views.Wishlistby_user, name="Filter"),
    url(r'^deletewishlistbyuser/(?P<query>.+)/(?P<product>.+)/$', views.deletefromWishlist, name="Filter"),
    url(r'^deletewishlistbyuserweb/$', views.deletefromWishlistbyURL, name="Filter"),
    # url(r'^wishlistbyuser/(?P<query>.+)/$', views.Wishlistbyuser, name="Filter"),

]
