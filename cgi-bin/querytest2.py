#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
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
for cnt, item in enumerate(form.getlist('language')):  # getvalue() →getlist()
    content += "%d：%s<br/>" % (cnt + 1, item)
print("Content-Type: text/html; charset=utf-8\n")
print(html_body % content)
