from controlcenter import Dashboard, widgets
from django.utils.timesince import timesince
from .models import Order
from django.template.defaultfilters import truncatechars
from django.utils.formats import localize
from django.db.models import Count
from django.db.models.functions import Trunc

from pytz import timezone
server_timezone = timezone('Europe/Moscow')

from datetime import datetime, timedelta
one_week_ago = datetime.today() - timedelta(days=7)


class OrderItemList(widgets.ItemList):
    title = "Необработанные заявки за неделю"
    changelist_url = Order
    model = Order
    width = widgets.FULL
    sortable = True
    list_display = ('#', 'name','phone','category','topic','description','ago')
    list_display_links = ['name', 'description']
    empty_message = "Заявки отсутствуют"

    def get_queryset(self):
        return Order.objects.filter(processed=False, created_date__gte=one_week_ago).order_by('-created_date')

    def ago(self, obj):
        return localize(obj.created_date.astimezone(server_timezone))

    ago.short_description = 'Дата отправки'

    def is_processed(self, obj):
        if obj.processed:
            return 'Да'
        return 'Нет'
    is_processed.short_description = 'Обработана'

    def description(self, obj):
        if obj.note:
            return truncatechars(obj.note, 50)
        return '-'

    description.short_description = 'Примечания'

class OrderSingleBarChart(widgets.SingleBarChart):
    # Строит бар-чарт по числу заказов
    title = 'Статистика по темам'
    model = Order

    width = widgets.LARGE
    class Chartist:
        options = {
            # По-умолчанию, Chartist может использовать
            'onlyInteger': True,
            # Внутренние отступы чарта -- косметика
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 25,
            }
        }

    def legend(self):
        # Выводит в легенде значения оси `y`,
        # поскольку, Chartist не рисует сами значения на графике
        return self.series

    def values(self):
        queryset = self.get_queryset()
        return (queryset.values_list('category')
                        .annotate(baked=Count('category'))
                        .order_by('-baked')
                        .filter(created_date__gte=one_week_ago))



class OrderSingleLineChart(widgets.SingleLineChart):
    # Строит бар-чарт по числу заказов
    title = 'График количества заявок за неделю'
    model = Order

    width = widgets.LARGE

    class Chartist:
        options = {
            # По-умолчанию, Chartist может использовать
            # float как промежуточные значения, это ни к чему
            'onlyInteger': True,
            'lineSmooth': False,
            # Внутренние отступы чарта -- косметика
            'chartPadding': {
                'top': 55,
                'right': 85,
                'bottom': 20,
                'left': 25,
            }
        }

    def legend(self):
        # Выводит в легенде значения оси `y`,
        # поскольку, Chartist не рисует сами значения на графике
        return self.series

    def values(self):
        queryset = self.get_queryset()
        return (queryset.annotate(date=Trunc('created_date_format', 'day'))
                        .values('date')
                        .annotate(count = Count('id'))
                        .values_list('date', 'count')
                        .order_by('-date')
                        .filter(created_date__gte=one_week_ago))


class OrderDashboard(Dashboard):
    title = "Заявки"
    widgets = (
        OrderItemList,
        OrderSingleBarChart, OrderSingleLineChart
    )

