def hello(**c):
    print(c)


hello(c=3, b =2, a=1)


d = {'auth': "aaa", 'name': "bbb", 'address': "hahaha"}
hello(**d)