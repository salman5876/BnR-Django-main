"""SNR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import re_path as url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from SNR import view

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('mobile/', include('mobile.urls')),
    path('laptop/', include('laptop.urls')),
    path('recommendation/', view.review_Recommendation),
    path('trend/', include('trends.urls')),
    path('wearable/', include('wearables.urls')),
    path('user/', include('credential.urls')),
    path('products/', include('products.urls')),
    path('feedback/', include('feedback.urls')),
    path('review/', include('userReviews.urls')),
    # url(r'^soc/', include('django.contrib.auth.urlsurls', namespace='auth')),
    # path('oauth/', include('social_django.urls', namespace='social')),  # <--
    # url("^soc/", include("social_django.urls", namespace="social")),
    path('search/', include('Search.urls')),
    path('settings/', include('credential.urls')),
    path('social/', include('social.urls')),
    path('tube/', include('tube.urls')),
    path('cat/', include('categories.urls')),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)