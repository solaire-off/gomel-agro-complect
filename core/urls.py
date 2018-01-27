"""core URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from . import views
from controlcenter.views import controlcenter

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'admin/dashboard/', controlcenter.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^export/users/xls/$', views.export_users_xls, name='export_users_xls'),
    url(r'^export/catalog/xls/$', views.export_catalog_xls, name='export_catalog_xls'),
    url(r'', include('catalog.urls')),
    url(r'', include('orders.urls'))
]


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
