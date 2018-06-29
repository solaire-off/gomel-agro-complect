from django.contrib import admin
from .models import Service, Category, CategoryImage
from .forms import ServiceAdminForm, CategoryAdminForm

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 3

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('title','url','category','published', 'created_date')
    list_filter = ('published','category', 'created_date')
    list_editable = ["published"]
    search_fields = ['title','description']
    list_per_page = 20
    form = ServiceAdminForm



class CategoryAdmin(admin.ModelAdmin):
    models = Category
    # inlines = [CategoryImageInline,]
    list_display = ('title','url','published','created_date')
    list_filter = ('created_date',)
    list_editable = ["published"]
    search_fields = ['title','ceo_description']
    list_per_page = 20
    form = CategoryAdminForm

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)

