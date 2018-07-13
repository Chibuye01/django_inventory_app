"""firstdjangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from inventory import views 

urlpatterns = [
    #url(r'^$', views.index, name="index"),
    url(r'^grn/$', views.grn, name="grn"),
    url(r'^grnz$', views.grnz, name="grnz"),
    url(r'^grn/(?P<id>\d+)/', views.grn_detail, name="grn_detail"),
    url(r'^supply_voucher/$', views.supply_voucher, name="supply_voucher"),
    url(r'^supply_voucherz$', views.supply_voucherz, name="supply_voucher"),
    url(r'^supply_voucher/(?P<id>\d+)/', views.supply_voucher_detail, name="supply_voucher_detail"),
    url(r'^admin/', admin.site.urls),
]
