from django.http import HttpResponse
from django.utils import timezone
from .forms import OrderForm
from django.http import JsonResponse
from catalog.models import Item
import xlwt

def get_order_form(request):
    is_valid = False
    if request.POST:
        form = OrderForm(request.POST)
        item_id = request.POST.get('item')
        if form.is_valid():
            is_valid = True
            order = form.save(commit=False)
            if item_id:
                order.item = Item.objects.get(pk=int(item_id))
            order.processed = False
            order.created_date = timezone.now()
            order.save()
    context = {
        'valid': is_valid
    }
    return JsonResponse(context)

def export_orders_as_xls(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="orders.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Заказы')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Имя', 'Телефон','Примечание','Товар','Принята','Дата']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    alignment = xlwt.Alignment()

    alignment.horz = xlwt.Alignment.HORZ_LEFT
    alignment.vert = xlwt.Alignment.VERT_TOP
    alignment.wrap = 1


    font_style.alignment = alignment

    max_col_width = [15,15,30,30,10,15]

    for obj in queryset:
        row_num += 1

        processed = 'Нет'
        if obj.processed : processed = 'Да'

        local_datetime = timezone.localtime(obj.created_date).strftime("%Y-%m-%d %H:%M:%S")

        note = obj.note
        if obj.note is None:
            note = 'Отсутствует'

        ws.write(row_num, 0, obj.name, font_style)
        ws.write(row_num, 1, obj.phone, font_style)
        ws.write(row_num, 2, note, font_style)
        if obj.item:
            ws.write(row_num, 3, obj.item.title, font_style)
        else:
            ws.write(row_num, 3, 'Не выбран', font_style)
        ws.write(row_num, 4, processed, font_style)
        ws.write(row_num, 5, local_datetime, font_style)

        if len(note) > 29 :
            note_hight = round(len(note) / 30)
            ws.row(row_num).height_mismatch = True
            ws.row(row_num).height = 255 * (note_hight)

    for col_num in range(len(max_col_width)):
        ws.col(col_num).width = (max_col_width[col_num]+1) * 280

    wb.save(response)
    return response

export_orders_as_xls.short_description = "Экспортировать в XLS"
