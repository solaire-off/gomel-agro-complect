from django.contrib import admin
from .forms import NewsAdminForm
from .models import News, Tag

class NewsAdmin(admin.ModelAdmin):
    models = News
    list_display = ('title','published','created_date')
    list_filter = ('published','tags', 'created_date')
    list_editable = ["published"]
    search_fields = ['title','content']
    list_per_page = 20
    form = NewsAdminForm

class TagAdmin(admin.ModelAdmin):
    models = Tag
    list_display = ('title','url','created_date')
    list_filter = ('created_date',)
    search_fields = ['title','ceo_description']
    list_per_page = 20

admin.site.register(News,NewsAdmin)
admin.site.register(Tag,TagAdmin)




