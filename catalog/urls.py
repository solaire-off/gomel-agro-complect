from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^catalog/$', views.items_list, name="items_list"),
    url(r'^catalog/(?P<category_url>[-\w]+)/$',views.items_by_category, name="items_by_category"),
    url(r'^catalog/(?P<category_url>[-\w]+)/(?P<item_url>[-\w]+)/$',views.single_item, name="single_item")
]


