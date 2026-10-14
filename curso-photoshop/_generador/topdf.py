# -*- coding: utf-8 -*-
import sys, os, win32com.client
rutas = sys.argv[1:]
word = win32com.client.Dispatch("Word.Application")
word.Visible = False
try:
    for r in rutas:
        r = os.path.abspath(r)
        pdf = os.path.splitext(r)[0] + ".pdf"
        d = word.Documents.Open(r, ReadOnly=True)
        d.ExportAsFixedFormat(pdf, 17)   # 17 = wdExportFormatPDF
        d.Close(False)
        print("PDF:", pdf)
finally:
    word.Quit()
