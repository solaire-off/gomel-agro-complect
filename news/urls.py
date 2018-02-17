from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news/$', views.news_list, name="news_list"),
    url(r'^news/(?P<tag_url>[-\w]+)/$',views.news_by_tag, name="news_by_tag")
]

