import xlwt
import json


with open('city.txt', 'r') as f:
    data = json.loads(f)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('city', cell_overwrite_ok=True)
    for index, (key, value) in enumerate(data.items()):
        sheet1.write(index, 0, key)
        sheet1.write(index, 1, value)
    workbook.save('city.xls')
