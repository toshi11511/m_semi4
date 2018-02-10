#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
import os

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
<title>test3.py</title>
</head>
<body>
    {}
    <hr>
    {}
    <hr>
    {}
</body>
</html>
"""
# フォームから値を取得
name = '未入力'
email = '未入力'
errors = []

if 'name' in form:
    name = form['name'].value
else:
    errors.append('お名前の入力がありません。')

if 'email' in form:
    email = form['email'].value
else:
    errors.append('メールアドレスの入力がありません。')

result = 'お名前：{}<br/>'.format(name)
result += 'メールアドレス：{}'.format(email)

print(html_body.format(
    'リクエストは{}です。'.format(os.environ['REQUEST_METHOD']),
    result,
    '<br/>'.join(errors))
)
