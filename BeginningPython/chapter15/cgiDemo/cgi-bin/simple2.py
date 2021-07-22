#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name', 'world')
print('Content-type:text/html\n')

print('Hello, {}!'.format(name))
