#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()

import sqlite3
from string import Template
from os import path
from httphandler import Request, Response, get_htmltemplate
print("Content-Type: text/html; charset=utf-8\n")
con = sqlite3.connect('bookmark.dat')
cur = con.cursor()
try:
    cur.execute("""CREATE TABLE bookmark(title text, url text);""")
except:
    pass
req = Request()
f = req.form
value_dic = {'message': '', 'title': '', 'url': '', 'bookmarks': ''}

if 'post' in f:
    if not f.getvalue('title', ) or not f.getvalue('url', ''):
        value_dic['message'] = 'タイトルとURLは必須項目です'
        value_dic['title'] = str(f.getvalue('title', ''))
        value_dic['url'] = f.getvalue('url', '')
    else:
        cur.execute("""INSERT INTO bookmark(title, url) VALUES(?, ?);""",
                    (f.getvalue('title', ''), f.getvalue('url', '')))
        con.commit()

listbody = ''
cur.execute("SELECT title, url FROM bookmark")
for item in cur.fetchall():
    listbody += """<dt>%s</dt><dd>%s</dd>\n""" % item
listbody = """<ul>\n%s</ul>""" % listbody
value_dic['bookmarks'] = listbody
res = Response()
f = open(path.join(path.dirname(__file__), 'bookmarkform.html'), encoding='utf-8')
t = Template(str(f.read()))

body = t.substitute(value_dic)
res.set_body(body)
print(res)

# cur.execute("SELECT * from bookmark")
# for row in cur:
#     print(row[0], row[1])
