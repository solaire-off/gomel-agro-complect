from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from catalog.models import Detail, Item, Category
from news.models import News
import xlwt

def home_page(request):
    news = News.objects.filter(published=True).order_by('-created_date')
    category = Category.objects.filter(published=True).order_by('-created_date')
    context = {
            'news' : news,
            'category' : category
            }
    return render(request, 'home.html', context)


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Пользователи')

    # First row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Имя пользователя', 'Имя', 'Фамилия', 'Электроная почта']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    max_col_width = [16,10,10,20]

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

            if len(row[col_num]) > max_col_width[col_num]:
                max_col_width[col_num] = len(row[col_num])


    for col_num in range(len(max_col_width)):
        ws.col(col_num).width = (max_col_width[col_num]+1) * 280


    wb.save(response)
    return response

def export_catalog_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="catalog.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Каталог')

    # First row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['Наименование', 'Категория','Опубликовано', 'Запчасти и комплектующие']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    alignment = xlwt.Alignment()

    alignment.horz = xlwt.Alignment.HORZ_LEFT
    alignment.vert = xlwt.Alignment.VERT_TOP

    font_style.alignment = alignment # Add Alignment to Style

    max_col_width = [35,35,20,35]

    items = Item.objects.all()
    details = Detail.objects.all()

    for item in items:
        publish = 'Нет'
        item_details = ''
        item_details_count = 0
        row_num += 1
        ws.write(row_num, 0, item.title, font_style)
        ws.write(row_num, 1, item.category.title , font_style)
        if (item.published) : publish = 'Да'
        ws.write(row_num, 2, publish, font_style)
        for detail in details:
            if item in detail.items.all():
                item_details += detail.title + '\n'
                item_details_count += 1
        if item_details_count == 0 : item_details = "Отсутствуют"
        ws.write(row_num, 3, item_details, font_style)

        if item_details_count > 1 :
            ws.row(row_num).height_mismatch = True
            ws.row(row_num).height = 255 * (item_details_count-1)


    #set width by max_col_width
    for col_num in range(len(max_col_width)):
        ws.col(col_num).width = (max_col_width[col_num]+1) * 280



    wb.save(response)
    return response
