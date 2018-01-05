from django.contrib import admin
from .models import Item, Category, Detail
from .forms import ItemAdminForm, CategoryAdminForm, DetailAdminForm

class ItemAdmin(admin.ModelAdmin):
    models = Item
    list_display = ('title','description','category','published','created_date')
    list_filter = ('published','category', 'created_date')
    list_editable = ["published"]
    search_fields = ['title','description']
    list_per_page = 10
    form = ItemAdminForm

class CategoryAdmin(admin.ModelAdmin):
    models = Category
    list_display = ('title','description','published','created_date')
    list_filter = ('created_date',)
    list_editable = ["published"]
    search_fields = ['title','description']
    list_per_page = 10
    form = CategoryAdminForm

class DetailAdmin(admin.ModelAdmin):
    models = Detail
    list_display = ('title','description','published','created_date')
    list_filter = ('created_date',)
    list_editable = ["published"]
    search_fields = ['title','description','items']
    filter_horizontal = ('items',)
    list_per_pag = 10
    form = DetailAdminForm

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Detail,DetailAdmin)

admin.site.site_header = 'ОАО "Гомельагрокомплект"'
admin.site.index_title = 'Панель администрации'
admin.site.site_title = 'ОАО Гомельагрокомлект'

