#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name', 'world')
print("""Content-type: text/html

<html> <head>
<title>Greeting Page</title> </head>
<body>
<h1>Hello, {}!</h1>
<form action='simple3.py'>
Change name <input type='text' name='name' /> <input type='submit' />
</form>
</body> </html>
""".format(name))
