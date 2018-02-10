#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()

import cgi
print("Content-Type: text/html; charset=utf-8\n")
print(cgi.print_environ())

print("以下はURLエンコードの確認<br/>")
from urllib import parse
querystr = parse.urlencode({'foo': 'bar& baz'})
print(querystr)
