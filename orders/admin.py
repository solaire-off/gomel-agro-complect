from django.contrib import admin
from .models import Order
from .views import export_orders_as_xls

class OrderAdmin(admin.ModelAdmin):
    models = Order
    list_display = ('name','phone','category','topic','processed','created_date')
    list_filter = ('processed', 'category', 'created_date')
    list_editable = ['processed']
    search_fields = ['name','phone','note']
    actions = [export_orders_as_xls]
    list_per_page = 20


admin.site.register(Order, OrderAdmin)
