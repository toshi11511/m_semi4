#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")
import pickle
from httphandler import Request, Response, get_htmltemplate

form_body = """
<form method="GET" action="picklepole.py">
好きな軽量言語は？<br/>
%s
<input type="submit">
</form>
"""
radio_parts = """
<input type="radio" name="language" value="%s"/>%s
<div style="border-left: solid %sem red;">%s</div>
"""
lang_dic = {}
try:
    f = open('favorite_language.dat', 'rb')
    lang_dic = pickle.load(f)
except EOFError:
    pass

content = ""
req = Request()
if 'language' in req.form:
    lang = req.form['language'].value
    lang_dic[lang] = lang_dic.get(lang, 0) + 1
f = open('favorite_language.dat', 'wb')
pickle.dump(lang_dic, f)
for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
    num = lang_dic.get(lang, 0)
    content += radio_parts % (lang, lang, num, num)

res = Response()
body = form_body % content
res.set_body(get_htmltemplate() % body)
print(res)
