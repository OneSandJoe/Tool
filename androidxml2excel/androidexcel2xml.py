#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Android国际化： 将excel中的内容转化到xml中

from xml.dom import minidom
from xlrd import open_workbook
import codecs

# 打开excel
workbook = open_workbook('strings.xls')

# 新建xml
doc = minidom.Document()
# 添加根元素
resources = doc.createElement('resources')
doc.appendChild(resources)

# 添加字符串
for sheet in workbook.sheets():
    for row_index in range(sheet.nrows):
        result_placeholder = sheet.cell(row_index, 0).value
        result_content = sheet.cell(row_index, 6).value
        # 新建一个文本元素
        text_element = doc.createElement('string')
        text_element.setAttribute('name', result_placeholder)
        text_element.appendChild(doc.createTextNode(result_content))
        resources.appendChild(text_element)

f = codecs.open('new_strings.xml', 'w', encoding='utf-8')
# doc.writexml(f)
f.write(doc.toprettyxml(indent='    '))
f.close()

