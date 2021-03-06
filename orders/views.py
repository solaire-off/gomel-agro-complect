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
        topic = request.POST.get('topic')
        category = request.POST.get('category')
        if form.is_valid():
            is_valid = True
            order = form.save(commit=False)
            order.topic = topic
            order.category = category
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


    columns = ['Имя', 'Телефон','Категория','Тема','Примечание','Принята','Дата']


    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    alignment = xlwt.Alignment()

    alignment.horz = xlwt.Alignment.HORZ_LEFT
    alignment.vert = xlwt.Alignment.VERT_TOP
    alignment.wrap = 1


    font_style.alignment = alignment

    max_col_width = [15,15,25,30,30,10,15]

    for obj in queryset:
        row_num += 1

        processed = 'Нет'
        if obj.processed : processed = 'Да'

        local_datetime = timezone.localtime(obj.created_date).strftime("%Y-%m-%d %H:%M:%S")

        note = obj.note
        if obj.note is None:
            note = '-'


        ws.write(row_num, 0, obj.name, font_style)
        ws.write(row_num, 1, obj.phone, font_style)
        ws.write(row_num, 2, obj.category, font_style)
        ws.write(row_num, 3, obj.topic, font_style)
        ws.write(row_num, 4, note, font_style)
        ws.write(row_num, 5, processed, font_style)
        ws.write(row_num, 6, local_datetime, font_style)


        len_cols = [len(obj.note), len(obj.category), len(obj.name)]
        max_len_col = max(len_cols)



        field_hight = round(max_len_col / 30)
        ws.row(row_num).height_mismatch = True
        ws.row(row_num).height = 265 * (field_hight)

    for col_num in range(len(max_col_width)):
        ws.col(col_num).width = (max_col_width[col_num]+1) * 280

    wb.save(response)
    return response

export_orders_as_xls.short_description = "Экспортировать в XLS"
