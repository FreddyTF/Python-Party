import PySimpleGUI as sg
layout = [[sg.Table(values=[['',''],['one','two']],headings=['Col1','Col2'],auto_size_columns=True),
           sg.Table(values=[['',''],['one','two']],headings=['Col1','Col2'],col_widths=[30,30]),
           sg.Table(values=[['',''],['one','two']],headings=['Col1','Col2'],max_col_width=40),
           sg.Table(values=[['',''],['one','two']],headings=['Col1','Col2'],def_col_width=20)]]
window = sg.Window('Title',layout=layout,finalize=True)
event, values = window.read()
window.close()