#!/usr/bin/env python
# -*- coding:utf-8 -*-

# iOS国际化： 将excel中的内容转化成对应的.strings文件

from xlrd import open_workbook
import codecs

workbook = open_workbook('simple.xls')
for sheet in workbook.sheets():
    print
    'IpCameraClient: ', sheet.name
    # 按照sheet的name生成.strings文件
    file = codecs.open(sheet.name + '.strings', 'w+', encoding='utf-8')
    for row_index in range(sheet.nrows):
        result_placeholder = sheet.cell(row_index, 0).value
        result_content = sheet.cell(row_index, 1).value

        if sheet.name == 'InfoPlist':
            file.write(result_placeholder + '="' + result_content + '";\n')
        else:
            file.write('"' + result_placeholder + '" = "' + result_content + '";\n');
    file.close()

