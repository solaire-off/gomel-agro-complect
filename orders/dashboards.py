from controlcenter import Dashboard, widgets
from django.utils.timesince import timesince
from .models import Order
from django.template.defaultfilters import truncatechars
from django.utils.formats import localize

from pytz import timezone
server_timezone = timezone('Europe/Moscow')


class ModelItemList(widgets.ItemList):
    title = "Доска заявок"
    changelist_url = Order
    limit_to = 20
    model = Order
    sortable = True
    width = '500'
    list_display = ('#', 'name','phone','topic','description','is_processed','ago')
    list_display_links = ['name', 'description']
    empty_message = "Заявки отсутствуют"

    def get_queryset(self):
        return Order.objects.all().order_by('-created_date')

    def ago(self, obj):
        return localize(obj.created_date.astimezone(server_timezone))

    ago.short_description = 'Прошло времени'

    def is_processed(self, obj):
        if obj.processed:
            return 'Да'
        return 'Нет'
    is_processed.short_description = 'Обработана'

    def description(self, obj):
        if obj.note:
            return truncatechars(obj.note, 130)
        return '-'

    description.short_description = 'Примечания'


class OrderDashboard(Dashboard):
    title = "Заявки"
    widgets = (
        ModelItemList,
    )
