#!/usr/bin/python

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tempfile import TemporaryFile
from xlwt import Workbook
import re,sys,os
 
dir = sys.path[0]
book = Workbook(encoding='utf-8')
pattern = re.compile(r'".+?"') 
pattern3 = re.compile(r'') 
 
for file in os.listdir(dir):
	fileName = os.path.splitext(file)[0]
	fileExt = os.path.splitext(file)[1]
 
	if os.path.isfile(file) and fileExt == '.strings':
		sheet = book.add_sheet(fileName)
		f = open(file, "r")

		row_index = 0
		for line in f:
			col_index = 0
			line = "\""+line
			a = line.replace('=','"=')
			a  = a.replace(" ","")
			#print("a===="+a)
			for m in pattern.finditer(a):
				sheet.write(row_index, col_index, m.group()[1:-1].rstrip())
				col_index = col_index + 1
			row_index = row_index + 1

		pass
		f.close()
 
book.save('simple.xls')
book.save(TemporaryFile())

