#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
import datetime
import cgi

sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()

html_body = """
<html><body>
{0.year:d}/{0.month:d}/{0.day:d} {0.hour:d}:{0.minute:d}:{0.second:d}
</body></html>"""

now = datetime.datetime.now()
print("Content-Type: text/html; charset=utf-8\n")
print(html_body.format(now))
