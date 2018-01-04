from django.contrib import admin
from .models import Item, Category

admin.site.register(Item)
admin.site.register(Category)



admin.site.site_header = 'ОАО "Гомельагрокомплект"'
admin.site.index_title = 'Панель администрации'
admin.site.site_title = 'ОАО Гомельагрокомлект'

