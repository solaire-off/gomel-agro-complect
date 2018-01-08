from django.http import HttpResponse
from django.contrib.auth.models import User
import xlwt



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
