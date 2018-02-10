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

body_line = []
body = form.getvalue('body', '')
# body = unicode(body, 'utf-8', 'ignore')
for cnt in range(0, len(body), 10):
    line = body[:10]
    line += ''.join(['□' for i in range(len(line), 10)])
    body_line.append(line)
    body = body[10:]
body_line_v = [' '.join(reversed(x)) for x in zip(*body_line)]

print("Content-Type: text/html; charset=utf-8\n")
print(html_body % '<br/>'.join(body_line_v))
