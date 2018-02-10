#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")
from httphandler import Request, Response, get_htmltemplate
import sqlite3

form_body = """
<form method="GET" action="dbpole.py">
好きな軽量言語は？<br/>
%s
<input type="submit">
</form>
"""
radio_parts = """
<input type="radio" name="language" value="%s"/>%s
<div style="border-left: solid %sem red;">%s</div>
"""
def incrementvalue(cur, lang_name):
    cue.execute(""""SELECT value FROM language_pole 
    WHERE name='%s';""" % lang_name)
    item = None
    for item in cur.fetchall():
        cur.execute("""UPDATE language_pole 
        SET value=%d WHERE name='%s';"""
                    % (item[0] + 1, lang_name))
    if not item:
        cur.execute("""INSERT INTO language_pole(name, value) 
        VALUE('%s', 1);""" % lang_name)
con = sqlite3.connect('db_file.dat')
cur = con.cursor()

try:
    cur.execute("""CREATE TABLE language_pole 
    (name text, value int);""")
except:
    pass

content = ""
req = Request()
if 'language' in req.form:
    incrementvalue(cur, req.form['language'].value)

lang_dic = {}
cur.execute("""SELECT name, value FROM language_pole;""")
for res in cur.fetchall():
    lang_dic[res[0]] = res[1]

for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
    num = lang_dic.get(lang, 0)
    content += radio_parts % (lang, lang, num, num)
con.commit()
res = Response()
body = form_body % content
res.set_body(get_htmltemplate() % body)
print(res)
