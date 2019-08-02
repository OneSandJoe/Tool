#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Android ios国际化： 将xml String文件中对应的相同字符串解析到excel中，展现不同ID

import xml.dom.minidom
from xlwt import Workbook
import re,sys,os

# 新建一个workbook
book = Workbook(encoding='utf-8')
sheet = book.add_sheet('Android',cell_overwrite_ok=True)

# 打开xml
xmldoc = xml.dom.minidom.parse('strings.xml')
code = xmldoc.getElementsByTagName('string')
row = 1
sheet.write(0, 0, "android_ID")
sheet.write(0, 3, "ios_ID")
sheet.write(0, 6, "ZH")

tong = 1

dir = sys.path[0]
bookios = Workbook(encoding='utf-8')
patternios = re.compile(r'".+?"')
pattern3ios = re.compile(r'')

for file in os.listdir(dir):
    fileName = os.path.splitext(file)[0]
    fileExt = os.path.splitext(file)[1]

    if os.path.isfile(file) and fileExt == '.strings':
        sheetios = bookios.add_sheet(fileName)
        f = open(file, "r")
        row_index = 0
        for node in code:
            for item in node.childNodes:
                print(row)
                # print(node.getAttribute('name'))
                sheet.write(row, 0, node.getAttribute('name'))  # 行数 写入ID
                f = open(file, "r")
                for line in f:
                    col_index = 0
                    line = "\"" + line
                    a = line.replace('=', '"=')
                    a = a.replace(" ", "")
                    #print("a====" + a)
                    for m in patternios.finditer(a):
                        if col_index == 1:
                            valus = m.group()[1:-1].rstrip()
                            print("value====" + valus  + "item.data"+item.data + "key===》"+key)
                            if item.data == valus:
                                #print(row)
                                #print(key)
                                sheet.write(row, 3, key)
                                tong = tong + 1

                        else:
                            key = m.group()[1:-1].rstrip();

                        col_index = col_index + 1
                    row_index = row_index + 1
                    #print("key====" + key)
                    #print("value====" + valus)

                sheet.write(row, 6, item.data)  # 行数 android翻译
                print(item.data)
                f.close()
                pass
            row = row + 1

# 保存workbook
book.save('strings.xls')

print("========finish=======")
print(tong)

