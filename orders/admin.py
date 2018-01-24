from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    models = Order
    list_display = ('name','phone','item','processed','created_date')
    list_filter = ('processed', 'created_date')
    list_editable = ['processed']
    search_fields = ['name','phone','note']
    list_per_page = 10

admin.site.register(Order, OrderAdmin)
