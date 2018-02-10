#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgi
from datetime import datetime
import cgitb
sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()
html_body = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta http-equiv="content-type" content="text/html;charset=UTF-8">
    <title></title>
</head>
<body>
    <form action="f13form.py" method="get">西暦を入力してください。<br/>
        <select name="year">%s</select>
        <input type="submit" name="submit" value="送信">
    </form>
    %s
</body>
</html>
"""
options = ''
content = ''
now = datetime.now()
for y in range(now.year-10, now.year+10):
    if y != now.year:
        select = ''
    else:
        select = ' selected="selected"'
    options += "<option%s>%d</option>" % (select, y)
form = cgi.FieldStorage()
year_str = form.getvalue('year', '')
if year_str.isdigit():
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
        content += "%d年には13日の金曜日がありません" % year
print("Content-Type: text/html; charset=utf-8\n")
print(html_body % (options, content))
