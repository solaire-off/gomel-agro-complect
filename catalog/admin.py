from django.contrib import admin
from .models import Item, Category


class ItemAdmin(admin.ModelAdmin):
    models = Item
    list_display = ('title','description','category','published','created_date')
    list_filter = ('published','category', 'created_date')
    search_fields = ['title','description']
    list_per_page = 10

class CategoryAdmin(admin.ModelAdmin):
    models = Category
    list_display = ('title','description','created_date')
    list_filter = ('created_date',)
    search_fields = ['title','description']

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'ОАО "Гомельагрокомплект"'
admin.site.index_title = 'Панель администрации'
admin.site.site_title = 'ОАО Гомельагрокомлект'

