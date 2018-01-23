from controlcenter import Dashboard, widgets
from django.utils.timesince import timesince
from .models import Item

class ModelItemList(widgets.ItemList):
    title = "Тестовая доска"
    changelist_url = Item
    limit_to = 20
    model = Item
    sortable = True
    width = '500'
    list_display = ('pk', 'title','url','category','published','created_date','ago')
    list_display_links = ['title']

    def ago(self, obj):
        return timesince(obj.created_date)
    ago.short_description = 'Отправлено'


class ItemDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )
