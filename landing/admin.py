from django.contrib import admin
from .models import TextBlock, ImageItem
from .forms import TextBlockAdminForm, ImageItemAdminForm

class ImageItemAdmin(admin.ModelAdmin):
    models = ImageItem
    list_display = ('title','identifier','get_source_url')
    list_filter = ('created_date',)
    search_fields = ['title','identifier','description']
    list_per_page = 20
    form = ImageItemAdminForm

admin.site.register(ImageItem,ImageItemAdmin)



class TextBlockAdmin(admin.ModelAdmin):
    models = TextBlock
    list_display = ('title','identifier','is_extend')
    list_filter = ('is_extend','created_date',)
    search_fields = ['title','identifier','content','extend_content']
    list_per_page = 20
    form = TextBlockAdminForm

admin.site.register(TextBlock,TextBlockAdmin)
