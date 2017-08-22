import json, xlwt


with open('numbers.txt') as f:
    data = json.loads(f.read())
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('numbers', cell_overwrite_ok=True)
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet1.write(i, j, data[i][j])
    workbook.save('number.xls')
