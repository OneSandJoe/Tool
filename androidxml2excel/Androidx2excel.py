#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Android国际化： 将xml文件中对应的字符串解析到excel中

import xml.dom.minidom
from xlwt import Workbook

# 新建一个workbook
book = Workbook(encoding='utf-8')
sheet = book.add_sheet('Android')

# 打开xml
xmldoc = xml.dom.minidom.parse('strings.xml')
code = xmldoc.getElementsByTagName('string')
row = 1
sheet.write(0, 0, "android_ID")
sheet.write(0, 6, "ZH")


for node in code:
    for item in node.childNodes:
        print(row)
        sheet.write(row, 0, node.getAttribute('name')) # 行数 写入ID
        sheet.write(row, 6, item.data)   # 行数 android翻译
    row = row + 1
# 保存workbook
book.save('strings.xls')
print("========finish=======")


