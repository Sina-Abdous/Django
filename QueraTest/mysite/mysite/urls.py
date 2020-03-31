"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from mysite.views import hello , current_datetime, hour_ahead
from books import views
from contact.views import *

admin.autodiscover()
urlpatterns = [
    path(r'admin/', admin.site.urls),
    re_path(r'^hello/$', hello),
    re_path(r'^time/$', current_datetime),
    re_path(r'^time/plus/(?P<offset>[1-9]{1,2})/$', hour_ahead),
    re_path(r'^search-form/$', views.search),
    re_path(r'^search/$', views.search),
    re_path(r'^contact/$', contact)
]