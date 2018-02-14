from controlcenter import Dashboard, widgets
from django.utils.timesince import timesince
from .models import Order

class ModelItemList(widgets.ItemList):
    title = "Доска заявок"
    changelist_url = Order
    limit_to = 20
    model = Order
    sortable = True
    width = '500'
    list_display = ('#', 'name','phone','topic','description','is_processed','ago')
    list_display_links = ['name']
    empty_message = "Заявки отсутствуют"

    def ago(self, obj):
        return timesince(obj.created_date)
    ago.short_description = 'Прошло времени'

    def is_processed(self, obj):
        if obj.processed:
            return 'Да'
        return 'Нет'
    is_processed.short_description = 'Принята'

    def topic(self, obj):
        if obj.item:
            return obj.item.title
        return 'Индивидуальный заказ'
    topic.short_description = 'Тема'

    def description(self, obj):
        if obj.note:
            return obj.note
        return 'Отсутствует'
    description.short_description = 'Примечание'


class OrderDashboard(Dashboard):
    title = "Заявки"
    widgets = (
        ModelItemList,
    )
