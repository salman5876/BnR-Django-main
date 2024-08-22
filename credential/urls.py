__author__ = 'Amad'
from django.urls import re_path as url,include
#from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    url(r'^social_login/$', views.customer_social_register_login, name='social login'),
    # url(r'^social_login_test/$', views.customer_social_register_login_testing, name='social login'),
    # path('', views.social_settings, name='user_list'),
    path('delete_user/<int:pk>', views.DeleteUser.as_view()),
    path('del_usr/<str:email>', views.DeleteUserByEmail.as_view()),
    url(r'^error$', views.social_oauth_error, name='user_list'),
    url(r'^logout$', views.logout_view, name='user_list'),
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^email/$', views.emailToFriend, name='email'),
    url(r'^subscribers/$', views.AllSubscribers, name='Subscribers'),
    url(r'^subscribers/add$', views.Subscribe, name='ADD Subscribers'),
    url(r'^friendsemail/$', views.friendmailList, name='email'),
    url(r'^checkreset/$', views.CheckResetPassword, name='Reset'),
    url(r'^getresetemailCode/$', views.CheckResetCodemail, name='Reset'),
    url(r'^checkresetcode/$', views.CheckResetCode, name='Reset'),
    url(r'^reset/$', views.ResetPassword, name='Reset'),
    url(r'^ForgetPssword/$', views.ForgetPssword, name='Reset'),
    url(r'^reset_password_verification/$', views.reset_password_verification, name='Reset'),
    url(r'^reset_password/$', views.reset_password, name='Reset'),
    url(r'^updatepassword/$', views.updatePassword, name='email'),
    url(r'^updatepasswordmanually/$', views.updatePasswordManually, name='email'),
    url(r'^updatelink/(?P<email>[\w.@+-]+)$', views.UpdateLink, name='email'),
    #path("ForgetPssword/", ForgetPssword.as_view(), name="ForgetPssword"),
    url(r'^usersDetails/$', views.userDetaillist, name='userDetailslist'),
    # path('user-token-auth/', obtain_jwt_token),
    path('user-token-auth/', views.get_user_credentials),
    # login-api, OK-check by me
    # url(r'^api-token-refresh/', refresh_jwt_token),
    # url(r'^api-token-verify/', verify_jwt_token),
    url(r'^getID/(?P<query>.+)/$', views.getID, name="Filter"),
    url(r'^getprofile/(?P<query>.+)/$', views.getProfile, name="Filter"),
    url(r'^updateprofile/$', views.updateProfile, name="Filter"),
    url(r'^verifyusername/(?P<username>[\w.@+-]+)$', views.verify_username),

    url(r'^verifyAccount/$', views.verify_account),
    path('isvarified/', views.verify_user_authenticated),
    url(r'^resendAuthentication/$', views.resend_authentication),

    url(r'^verifypassword/$', views.check_password),

    url(r'^intrst/$', views.intrst),
    url(r'^isvarified/(?P<mer>.+)/$', views.get_count_merchant),
    url(r'^email_verify/(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$' , views.email_verify)


]
urlpatterns = format_suffix_patterns(urlpatterns)