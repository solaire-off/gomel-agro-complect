from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^service/$', views.service_list, name="service_list"),
    url(r'^service/(?P<service_url>[-\w]+)/$',views.service_by_category, name="service_by_category"),
    url(r'^service/(?P<category_url>[-\w]+)/(?P<service_url>[-\w]+)/$',views.service_detail, name="service_detail")
]


