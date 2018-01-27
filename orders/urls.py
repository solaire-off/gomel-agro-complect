from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^send_order$', views.get_order_form, name="get_order_form")
]
