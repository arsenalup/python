import json
import xlwt
from collections import OrderedDict


with open('student.txt', 'r') as f:
    data = json.loads(f, object_pairs_hook=OrderedDict)
    workbook = xlwt.workbook()
    sheet1 = workbook.add_sheet('student', cell_overwrite_ok=True)
    for index,  (key, values) in enumerate(data.items()):
        sheet1.write(index, 0, key)
        for i, value in enumerate(values):
            sheet1.write(index, i+1, value)
    workbook.save('student.xls')
