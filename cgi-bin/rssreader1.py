#!C:\Python36\python.exe
# -*- coding: utf-8 -*-

import sys
import cgitb
sys.stdin = open(sys.stdin.fileno(), "r", encoding="utf-8")
sys.stdout = open(sys.stdout.fileno(), "w", encoding="utf-8")
sys.stderr = open(sys.stderr.fileno(), "w", encoding="utf-8")
cgitb.enable()
print("Content-Type: text/html; charset=utf-8\n")
from rssparser import parse_rss
from httphandler import Request, Response, get_htmltemplate
form_body = """
<form method="GET" action="rssreader1.py">
  RSSのURL:
  <input type="text" size="40" name="url" value="%s"/>
  <input type="submit" />
</form>"""
rss_parts = """
<h3><a href="%(link)s">%(title)s</a></h3>
<p>%(description)s</p>
"""
content = "URLを入力してください"
req = Request()
fo = req.form
if 'url' in fo:
    try:
        rss_list = parse_rss(req.form['url'].value)
        content = ""
        for d in rss_list:
            content += rss_parts % d
    except:
        pass
res = Response()
body = form_body % req.form.getvalue('url', '')
body += content
res.set_body(get_htmltemplate() % body)
print(res)
