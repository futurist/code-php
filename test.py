#!/usr/bin/python
print "Content-type: text/html\n\n"

print """<h1>
lksdfjlajsldfj
aweogijoawej
"""

import cgi
form = cgi.FieldStorage()
print form['id']

