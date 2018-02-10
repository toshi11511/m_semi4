#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb

sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()
print("Content-Type: text/html; charset=utf-8\n")

import cgi
form = cgi.FieldStorage()

html_body = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8"/>
<title>test2.py</title>
</head>
<body>
<form method="POST">
<input type="text" name="ptest"/>
<input type="submit"/>
</form>
<div>%s</div>
</body>
</html>
"""

print(html_body % form.getvalue('ptest'))

