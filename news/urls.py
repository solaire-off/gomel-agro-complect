from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news/$', views.news_list, name="news_list"),
]

