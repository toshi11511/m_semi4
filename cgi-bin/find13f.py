#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
from datetime import datetime

sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()

import cgi
form = cgi.FieldStorage()

html_body = """
<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
</head>
<body>
%s
</body>
</html>
"""

content = ''

year_str = form.getvalue('year', '')  # yearに代入された中身を取り出す
if not year_str.isdigit():
    content = "西暦を入力してください"
else:
    year = int(year_str)
    friday13 = 0
    for month in range(1, 13):
        date = datetime(year, month, 13)
        if date.weekday() == 4:
            friday13 += 1
            content += "%d年%d月13日は金曜日です" % (year, date.month)
            content += "<br/>"

if friday13:
    content += "%d年には合計%d個の13日の金曜日があります" % (year, friday13)
else:
    content += "%d年には13日の金曜日がありません"

print("Content-Type: text/html; charset=utf-8\n")
print(html_body % content)
