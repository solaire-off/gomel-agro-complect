from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.items_list, name="items_list"),
    url(r'^details/$', views.details_list, name="details_list"),
    url(r'^(?P<category_url>[-\w]+)/$',views.items_by_category, name="items_by_category")
]


