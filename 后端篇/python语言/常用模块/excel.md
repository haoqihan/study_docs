#### openpyxl的使用

##### 下载

```python
pip install openpyxl
```

##### 基本模板

```python
# -*- coding: utf-8 -*-

import os
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side


class Excel:
    def __init__(self, path):
        self.path = path
        self.flag = 0
        self.run()

    # 设置字体大小和样式
    def font(self, name="微软雅黑", size=14, bold=False, color="000000"):
        return Font(name=name, size=size, bold=bold, color=color)

    # 设置背景颜色
    def fill(self, fgColor="DDDDDD"):
        return PatternFill("solid", fgColor=fgColor)

    # 设置对其格式
    def alignment(self, format="center"):
        return Alignment(horizontal=format, vertical=format)

    # 设置边框线
    def border(self, style="thin", color="000000"):
        side = Side(style=style, color=color)
        return Border(left=side, right=side, top=side, bottom=side)

    # 添加workbook
    def create_workbook(self):
        isE = os.path.exists(self.path)
        if isE:
            self.workbook = load_workbook(self.path)
        else:
            self.workbook = Workbook()
            self.flag = 1
    # 添加sheet
    def create_sheet(self):
        if self.flag:
            sheet = self.workbook.active
        else:
            sheet = self.workbook.create_sheet("sheet")
        return sheet

    # 运行
    def run(self):
        self.create_workbook()
        sheet = self.create_sheet()
        self.create_demo(sheet)

    # 设置样式
    def set_style(self, cell_obj):
        cell_obj.fill = self.fill()
        cell_obj.font = self.font()
        cell_obj.alignment = self.alignment()
        cell_obj.border = self.border()

    # 向excel表添加内容
    def create_demo(self, sheet):
        for i in "ABCDEFG":
            sheet.column_dimensions[i].width = 20
        row = ["运营商", "ismi", "手机型号", "mcc", "mnc", "采集日期"]
        for index, i in enumerate(row):
            xx = sheet.cell(1,index+1,index)
            self.set_style(xx)
        self.workbook.save(self.path)


Excel("666.xlsx")
```

